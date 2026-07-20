import unittest
from study_labs.nlp import softmax,cross_entropy,attention,gradient_check
from study_labs.vision import conv2d_valid,iou,nms
from study_labs.rl import transition,value_iteration,q_learning


class Labs(unittest.TestCase):
    def test_softmax_shift_and_large_logits(self):
        self.assertEqual(softmax([1000,1001]),softmax([0,1]))
        self.assertAlmostEqual(sum(softmax([2,4,6])),1)
        self.assertAlmostEqual(cross_entropy([1000,1001],0),1.3132616875)

    def test_gradient(self):
        self.assertLess(gradient_check([.3,-.8,1.2],2)['max_error'],1e-8)

    def test_mask_blocks_future(self):
        out,w=attention([1,0],[[1,0],[0,1]],[[2,3],[1e6,1e6]],[True,False])
        self.assertEqual(out,[2,3])
        self.assertEqual(w,[1,0])
        with self.assertRaises(ValueError): attention([1],[[1]],[[1]],[False])

    def test_cross_correlation(self):
        self.assertEqual(conv2d_valid([[1,2,3],[4,5,6],[7,8,9]],[[1,0],[0,-1]]),[[-4,-4],[-4,-4]])
        self.assertEqual(conv2d_valid([[1,2],[3,4]],[[1]],2),[[1]])

    def test_detection_geometry(self):
        self.assertAlmostEqual(iou([0,0,2,2],[1,1,3,3]),1/7)
        self.assertEqual(iou([0,0,1,1],[2,2,3,3]),0)
        self.assertEqual(nms([[0,0,2,2],[0,0,2,2],[3,3,4,4]],[.9,.8,.7]),[0,2])

    def test_terminal_and_exact_values(self):
        self.assertEqual(transition(4,0),(4,0,True))
        v=value_iteration()
        self.assertEqual(v['policy'],[1,1,1,1])
        self.assertAlmostEqual(v['values'][0],-.01-.009-.0081+.729)
        self.assertLess(v['bellman_residual'],1e-9)

    def test_q_learning_reproducibility_and_oracle(self):
        a=q_learning(seed=7)
        self.assertEqual(a,q_learning(seed=7))
        self.assertEqual(a['policy'],value_iteration()['policy'])
        self.assertAlmostEqual(a['q'][0][1],value_iteration()['values'][0],places=6)

    def test_invalid_shapes_and_boxes(self):
        with self.assertRaises(ValueError): conv2d_valid([[1],[2,3]],[[1]])
        with self.assertRaises(ValueError): iou([2,0,1,1],[0,0,1,1])
        with self.assertRaises(ValueError): softmax([])


if __name__=='__main__': unittest.main()
