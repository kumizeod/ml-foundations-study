import unittest
from study_labs.policy_evaluation import evaluate_policy
from study_labs.rl import value_iteration


class PolicyEvaluationTests(unittest.TestCase):
    def test_optimal_policy_matches_dynamic_programming(self):
        got = evaluate_policy([1,1,1,1])
        for x,y in zip(got['values'],value_iteration()['values']):
            self.assertAlmostEqual(x,y)

    def test_nonoptimal_policy_is_not_accidentally_maximized(self):
        got = evaluate_policy([0,0,0,0])
        self.assertAlmostEqual(got['values'][0],-.1,places=8)
        self.assertLess(got['bellman_residual'],1e-9)
        mixed = evaluate_policy([.5]*4)
        self.assertLess(mixed['values'][0],value_iteration()['values'][0])
        self.assertGreater(mixed['values'][0],-.1)
        with self.assertRaises(ValueError): evaluate_policy([1.1])
