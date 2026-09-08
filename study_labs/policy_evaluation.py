"""Fixed-policy evaluation, explicitly distinct from value iteration's max."""
import math
from .rl import transition


def evaluate_policy(prob_right, gamma=.9, tolerance=1e-10, max_iterations=10000):
    if (not prob_right or any(not math.isfinite(p) or not 0 <= p <= 1 for p in prob_right)
            or not math.isfinite(gamma) or not 0 <= gamma < 1
            or not math.isfinite(tolerance) or tolerance <= 0
            or type(max_iterations) is not int or max_iterations <= 0):
        raise ValueError('invalid policy/evaluation parameters')
    size = len(prob_right)+1
    values = [0.0]*size
    def backup(s, old):
        if s == size-1: return 0.0
        total = 0.0
        for a, probability in ((0, 1-prob_right[s]), (1, prob_right[s])):
            nxt, reward, done = transition(s, a, size)
            total += probability*(reward + gamma*(not done)*old[nxt])
        return total
    for iteration in range(max_iterations):
        new = [backup(s, values) for s in range(size)]
        delta = max(abs(a-b) for a,b in zip(new,values))
        values = new
        if delta < tolerance: break
    else: raise RuntimeError('policy evaluation did not converge')
    residual = max(abs(backup(s, values)-values[s]) for s in range(size))
    return {'values': values, 'bellman_residual': residual, 'iterations': iteration+1}
