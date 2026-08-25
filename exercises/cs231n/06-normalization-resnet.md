# 练习卡：归一化与残差网络

[返回笔记](../../notes/cs231n/06-normalization-resnet.md)

## 任务

比较冻结参数、model.eval、no_grad的作用，写一个将三者混淆的失败例子。

<details>
<summary>参考验收点</summary>

冻结参数与关闭梯度记录不同；eval影响dropout/BN行为，不自动禁止梯度。

</details>
