# 练习卡：状态价值、动作价值与贝尔曼期望方程

[返回笔记](../../notes/westlake-rl/02-bellman-expectation.md)

## 任务

手算A一步得1终止，B以一半概率到A且本步奖励0，gamma=0.9时的V。

<details>
<summary>参考验收点</summary>

V(A)=1，V(B)=0.45；清楚区分转移期望与策略动作期望。

</details>

## 边界追问

省略终止状态后转移矩阵行和小于1，必然错吗？

<details>
<summary>追问验收</summary>

不必然，可能是次随机表示；需要明确丢失的概率质量和零后续价值。

</details>
