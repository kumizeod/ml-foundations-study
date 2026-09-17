# 练习卡：分词、预训练目标与数据泄漏

[返回笔记](../../notes/cs224n/09-tokenization-and-pretraining.md)

## 任务

给同一段代码设计按字符和按子词两种分词，讨论困惑度为何不能直接比较。

<details>
<summary>参考验收点</summary>

指出预测单位与序列长度不同，必须固定tokenizer；列出截断、EOS和去重规则。

</details>

## 边界追问

评测下载最新main有什么风险？

<details>
<summary>追问验收</summary>

新版本可能包含答案或改变任务环境；固定仓库commit、tokenizer与截断规则。

</details>
