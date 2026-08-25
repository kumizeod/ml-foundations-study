# 练习卡：Seq2seq、teacher forcing 与训练推理差异

[返回笔记](../../notes/cs224n/06-seq2seq.md)

## 任务

为三词输出构造teacher-forcing输入和标签，随后手动执行两步自由解码。

<details>
<summary>参考验收点</summary>

训练可以使用真实前缀；自由解码只能使用已生成前缀。EOS和PAD语义不同。

</details>
