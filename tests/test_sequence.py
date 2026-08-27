import unittest
from study_labs.sequence import causal_attention, masked_cross_entropy


class SequenceTests(unittest.TestCase):
    def test_future_changes_cannot_affect_prefix(self):
        q = [[1, 0], [0, 1], [1, 1]]
        k = [[1, 0], [0, 1], [2, 1]]
        v = [[2, 3], [4, 5], [6, 7]]
        out, w = causal_attention(q, k, v)
        changed, _ = causal_attention(q, k[:2] + [[10000, -10000]],
                                     v[:2] + [[1e9, -1e9]])
        self.assertEqual(out[:2], changed[:2])
        for t, row in enumerate(w):
            self.assertAlmostEqual(sum(row), 1)
            self.assertTrue(all(x == 0 for x in row[t+1:]))

    def test_padding_does_not_change_effective_mean(self):
        logits = [[2, 0], [0, 2]]
        base = masked_cross_entropy(logits, [0, 1], [True, True])
        padded = masked_cross_entropy(logits + [[0, 1000]], [0, 1, -100],
                                      [True, True, False])
        self.assertEqual(base, padded)
        with self.assertRaises(ValueError):
            masked_cross_entropy([[1, 2]], [-100], [False])
