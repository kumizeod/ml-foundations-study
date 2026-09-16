# 练习卡：Seq2seq、teacher forcing 与训练推理差异

[返回笔记](../../notes/cs224n/06-seq2seq.md)

## 任务

为三词输出构造teacher-forcing输入和标签，随后手动执行两步自由解码。

<details>
<summary>参考验收点</summary>

训练可以使用真实前缀；自由解码只能使用已生成前缀。EOS和PAD语义不同。

</details>

## 边界追问

A首步0.6、最佳后续0.51；B首步0.4、后续0.99，贪心错在哪里？

<details>
<summary>追问验收</summary>

完整概率分别0.306和0.396；局部最高不等于序列最高。有限beam仍无全局保证。

</details>
