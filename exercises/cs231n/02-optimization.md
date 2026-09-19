# 练习卡：SGD、动量、Adam 与学习率

[返回笔记](../../notes/cs231n/02-optimization.md)

## 任务

对f(x)=x²、x=2、学习率0.1做三次SGD更新，并讨论损失sum/mean切换。

<details>
<summary>参考验收点</summary>

x依次为1.6、1.28、1.024；梯度来自2x。batch求和可能放大更新，不能不调整约定直接比较。

</details>

## 边界追问

同epoch比较batch10和batch100，优化预算相同吗？

<details>
<summary>追问验收</summary>

样本量可相同，step数不同；分别报告有效batch、step和总时间。

</details>
