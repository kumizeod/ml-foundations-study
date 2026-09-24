# 练习卡：价值迭代、策略迭代与可验证基准

[返回笔记](../../notes/westlake-rl/04-dynamic-programming.md)

## 任务

手算5状态链起点最优价值，再运行价值迭代核验，并比较同步/原地更新定义。

<details>
<summary>参考验收点</summary>

gamma0.9时起点0.7019，贪心策略全向右；更新方式可影响中间轮次。

</details>

## 边界追问

全向左策略在链起点的价值是多少？

<details>
<summary>追问验收</summary>

每步−0.01、gamma0.9，价值−0.1；这是防止把策略评估错写成max的反例。

</details>
