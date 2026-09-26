# 练习卡：Sarsa、Expected Sarsa 与 Q-learning

[返回笔记](../../notes/westlake-rl/08-sarsa-qlearning.md)

## 任务

下一状态两动作Q为1、0，选择高值动作概率0.9，比较Sarsa、Expected Sarsa与Q-learning目标。

<details>
<summary>参考验收点</summary>

Expected下一值0.9，Q-learning为1，Sarsa取实际动作值；再加各自r与gamma。

</details>

## 边界追问

epsilon随机所有动作与只随机非贪心动作一样吗？

<details>
<summary>追问验收</summary>

不是，最优动作概率不同；Expected Sarsa期望需匹配实际行为分布。

</details>
