# 练习卡：随机近似、Robbins–Monro 与 SGD

[返回笔记](../../notes/westlake-rl/06-stochastic-approximation.md)

## 任务

解释sum alpha无穷、sum alpha²有限各控制什么；比较固定步长和递减步长跟踪变化。

<details>
<summary>参考验收点</summary>

前者避免过早停止，后者控制累积噪声；仍需其他收敛假设，不能推广为任意网络保证。

</details>

## 边界追问

固定步长在变化环境中有什么优势与代价？

<details>
<summary>追问验收</summary>

持续响应新数据，但稳态噪声不消失；递减步长静态误差可降，变化后可能反应慢。

</details>
