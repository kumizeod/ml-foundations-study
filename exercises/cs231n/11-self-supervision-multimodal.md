# 练习卡：自监督、对比学习与视觉语言表示

[返回笔记](../../notes/cs231n/11-self-supervision-multimodal.md)

## 任务

为同一杯子构造正视图对，并找出可能把不同目标当成负例的情况。

<details>
<summary>参考验收点</summary>

解释误负例与标签语义；将表示质量和任务质量分开评测。

</details>

## 边界追问

去掉背景后检索下降，可能说明什么？

<details>
<summary>追问验收</summary>

可能依赖背景捷径，也可能去掉了真实上下文；需匹配控制而非直接下结论。

</details>
