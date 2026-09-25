# 练习卡：蒙特卡洛评估、探索与回报方差

[返回笔记](../../notes/westlake-rl/05-monte-carlo.md)

## 任务

对回报[1,0,1]分别用1/n与固定alpha0.5更新；再区分first/every-visit。

<details>
<summary>参考验收点</summary>

均值依次1、0.5、2/3；若初值0且alpha0.5，结果依次0.5、0.25、0.625。

</details>

## 边界追问

只统计成功回合能估计原策略价值吗？

<details>
<summary>追问验收</summary>

会改变采样分布，造成选择偏差；过滤后要重新说明目标，不能沿用原名称。

</details>
