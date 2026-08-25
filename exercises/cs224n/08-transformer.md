# 练习卡：Transformer：残差、归一化、多头与位置

[返回笔记](../../notes/cs224n/08-transformer.md)

## 任务

对B=2、T=8、d=16、4头attention列出Q、分头Q、分数矩阵和拼接输出形状。

<details>
<summary>参考验收点</summary>

常见Q为2×8×16，分头为2×4×8×4，分数为2×4×8×8，拼接恢复2×8×16。

</details>
