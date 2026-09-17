# 练习卡：全量微调、LoRA 与实验公平性

[返回笔记](../../notes/cs224n/10-finetuning.md)

## 任务

计算1024×1024权重与rank=8的LoRA增量参数数，并设计冻结骨干与微调的公平对照。

<details>
<summary>参考验收点</summary>

全矩阵1048576，低秩增量16384；公平对照固定基础权重、数据拆分、有效token预算和选择规则。

</details>

## 边界追问

LoRA训练参数少，为什么不能直接宣称推理快？

<details>
<summary>追问验收</summary>

推理仍包含基础模型，是否合并、量化与部署实现都会影响速度，需独立计时。

</details>
