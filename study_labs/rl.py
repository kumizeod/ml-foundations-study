"""Tabular finite-chain MDP, dynamic programming and seeded Q-learning."""
import random


def transition(state,action,size=5):
    if size<2 or not 0<=state<size or action not in (0,1):
        raise ValueError("invalid state/action/size")
    if state==size-1: return state,0.0,True
    nxt=max(0,min(size-1,state+(1 if action else -1)))
    done=nxt==size-1
    return nxt,(1.0 if done else -0.01),done


def value_iteration(size=5,gamma=0.9,tolerance=1e-10):
    if size<2 or not 0<=gamma<1 or tolerance<=0: raise ValueError("invalid parameters")
    v=[0.0]*size
    for _ in range(10000):
        new=[]
        for s in range(size):
            qs=[]
            for a in (0,1):
                nxt,reward,done=transition(s,a,size)
                qs.append(reward+gamma*(not done)*v[nxt])
            new.append(max(qs))
        residual=max(abs(x-y) for x,y in zip(v,new))
        v=new
        if residual<tolerance: break
    else: raise RuntimeError("did not converge")
    policy=[]
    for s in range(size-1):
        qs=[]
        for a in (0,1):
            nxt,r,done=transition(s,a,size)
            qs.append(r+gamma*(not done)*v[nxt])
        policy.append(max((0,1),key=lambda a:qs[a]))
    return {"values":v,"policy":policy,"bellman_residual":residual}


def q_learning(seed=7,episodes=1000,size=5,gamma=0.9,alpha=0.2,epsilon=0.2):
    if episodes<=0 or size<2 or not 0<=gamma<1 or not 0<alpha<=1 or not 0<=epsilon<=1:
        raise ValueError("invalid parameters")
    rng=random.Random(seed)
    q=[[0.0,0.0] for _ in range(size)]
    for _ in range(episodes):
        s=0
        for step in range(100):
            a=rng.randrange(2) if rng.random()<epsilon else max((0,1),key=lambda a:q[s][a])
            nxt,r,done=transition(s,a,size)
            # The loop's 100-step time limit is truncation, not an MDP terminal.
            target=r+gamma*(not done)*max(q[nxt])
            q[s][a]+=alpha*(target-q[s][a])
            s=nxt
            if done: break
    return {"q":q,"policy":[max((0,1),key=lambda a:q[s][a]) for s in range(size-1)],
            "seed":seed,"episodes":episodes}


def main():
    import json
    print(json.dumps({"dynamic_programming":value_iteration(),"q_learning":q_learning()},indent=2))


if __name__=="__main__": main()
