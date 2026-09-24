# 练习卡：最优价值、贪心策略与压缩映射

[返回笔记](../../notes/westlake-rl/03-bellman-optimality.md)

## 任务

比较立刻得0.5与先走一步再得1：gamma分别0.9和0.1，哪种更好？

<details>
<summary>参考验收点</summary>

若先走一步奖励0，则后者折扣回报分别0.9和0.1；最优动作会改变。

</details>

## 边界追问

最优价值唯一，最优策略也一定唯一吗？

<details>
<summary>追问验收</summary>

不一定，并列最优动作可形成不同策略；比较价值而非只看动作编号。

</details>
