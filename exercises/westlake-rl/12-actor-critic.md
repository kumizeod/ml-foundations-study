# 练习卡：Actor–Critic、优势与重要性采样

[返回笔记](../../notes/westlake-rl/12-actor-critic.md)

## 任务

行为概率0.2、目标概率0.5时计算重要性比率；再讨论十步连乘与支持条件。

<details>
<summary>参考验收点</summary>

单步2.5，十步约9536.74；行为概率为0时不能用比率补回未覆盖动作。

</details>

## 边界追问

分母加epsilon能补回行为策略从未采到的动作吗？

<details>
<summary>追问验收</summary>

不能，数值防除零不等于满足数据支持；缺失信息仍缺失。

</details>
