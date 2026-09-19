# 练习卡：计算图、链式法则与梯度检查

[返回笔记](../../notes/cs231n/03-backprop.md)

## 任务

为输入3维、隐藏5维、类别2、batch4的MLP标注所有权重与梯度形状。

<details>
<summary>参考验收点</summary>

W为5×3、U为2×5；梯度与相应参数形状一致，bias沿batch聚合。

</details>

## 边界追问

同一变量走两条计算路径，反传该相加还是覆盖？

<details>
<summary>追问验收</summary>

相加；例如x²+x导数2x+1。广播bias也累加所有样本贡献。

</details>
