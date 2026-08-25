# 练习卡：全量微调、LoRA 与实验公平性

[返回笔记](../../notes/cs224n/10-finetuning.md)

## 任务

计算1024×1024权重与rank=8的LoRA增量参数数，并设计冻结骨干与微调的公平对照。

<details>
<summary>参考验收点</summary>

全矩阵1048576，低秩增量16384；公平对照固定基础权重、数据拆分、有效token预算和选择规则。

</details>
