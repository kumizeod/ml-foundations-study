# 练习卡：Transformer：残差、归一化、多头与位置

[返回笔记](../../notes/cs224n/08-transformer.md)

## 任务

对B=2、T=8、d=16、4头attention列出Q、分头Q、分数矩阵和拼接输出形状。

<details>
<summary>参考验收点</summary>

常见Q为2×8×16，分头为2×4×8×4，分数为2×4×8×8，拼接恢复2×8×16。

</details>

## 边界追问

参数数量没变，序列变长为何显存变大？

<details>
<summary>追问验收</summary>

激活与attention矩阵、KV cache都随序列变化；参数内存只是总内存的一部分。

</details>
