import unittest
from study_labs.geometry import conv_output_size, receptive_field, unproject, transform


class GeometryTests(unittest.TestCase):
    def test_convolution_shapes_and_receptive_field(self):
        self.assertEqual(conv_output_size(5, 3), 3)
        self.assertEqual(conv_output_size(5, 3, stride=2), 2)
        self.assertEqual(conv_output_size(5, 3, padding=2, dilation=2), 5)
        self.assertEqual(receptive_field([(3, 2, 1), (3, 1, 1)]), {'field': 7, 'jump': 2})
        with self.assertRaises(ValueError): conv_output_size(4, 3, dilation=2)

    def test_pinhole_units_and_rigid_roundtrip(self):
        self.assertEqual(unproject(370, 240, 1, 500, 500, 320, 240), [.1, 0, 1])
        p = [.1, .2, 1]
        r = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
        t = [1, 2, 3]
        moved = transform(p, r, t)
        back = transform(moved, r, t, inverse=True)
        for a, b in zip(p, back): self.assertAlmostEqual(a, b)
        with self.assertRaises(ValueError): unproject(0, 0, 0, 500, 500, 0, 0)
        with self.assertRaises(ValueError): transform(p, [[1,0,0],[0,1,0],[0,0,-1]], t)
