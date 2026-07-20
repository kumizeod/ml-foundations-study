"""Stable softmax, attention, cross entropy and a finite-difference check."""
import math


def softmax(logits):
    if not logits or any(not math.isfinite(x) for x in logits):
        raise ValueError("need finite nonempty logits")
    values = [math.exp(x-max(logits)) for x in logits]
    total = sum(values)
    return [x/total for x in values]


def cross_entropy(logits, target):
    if not 0 <= target < len(logits):
        raise ValueError("invalid target")
    softmax(logits)  # Validate inputs, but use log-sum-exp for numerical stability.
    m=max(logits)
    return m+math.log(sum(math.exp(x-m) for x in logits))-logits[target]


def attention(query, keys, values, allowed=None):
    if not query or not keys or len(keys)!=len(values):
        raise ValueError("invalid attention input")
    if any(len(k)!=len(query) for k in keys):
        raise ValueError("key/query dimensions differ")
    if not values[0] or any(len(v)!=len(values[0]) for v in values):
        raise ValueError("value dimensions differ")
    if any(not math.isfinite(x) for v in [query,*keys,*values] for x in v):
        raise ValueError("nonfinite attention input")
    allowed=[True]*len(keys) if allowed is None else allowed
    if len(allowed)!=len(keys) or not any(allowed):
        raise ValueError("mask must allow at least one key")
    indices=[i for i,x in enumerate(allowed) if x]
    probs=softmax([sum(x*y for x,y in zip(query,keys[i]))/math.sqrt(len(query)) for i in indices])
    weights=[0.0]*len(keys)
    for i,p in zip(indices,probs): weights[i]=p
    output=[sum(weights[i]*values[i][j] for i in range(len(keys))) for j in range(len(values[0]))]
    return output,weights


def gradient_check(logits,target,epsilon=1e-5):
    analytical=softmax(logits)
    analytical[target]-=1
    numerical=[]
    for i in range(len(logits)):
        plus,minus=list(logits),list(logits)
        plus[i]+=epsilon
        minus[i]-=epsilon
        numerical.append((cross_entropy(plus,target)-cross_entropy(minus,target))/(2*epsilon))
    return {"analytical":analytical,"numerical":numerical,
            "max_error":max(abs(a-b) for a,b in zip(analytical,numerical))}


def main():
    import json
    result={"softmax_large_logits":softmax([1000,1001,999]),
            "gradient_check":gradient_check([0.3,-0.8,1.2],2),
            "masked_attention":attention([1,0],[[1,0],[0,1]],[[2,3],[100,100]],[True,False])}
    print(json.dumps(result,indent=2))


if __name__=="__main__": main()
