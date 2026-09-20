# 练习卡：迁移学习、冻结策略与分布变化

[返回笔记](../../notes/cs231n/07-transfer-learning.md)

## 任务

设计按采集场景划分的迁移实验；列出预训练输入规范检查表。

<details>
<summary>参考验收点</summary>

包含RGB/BGR、分辨率、归一化、插值、统计状态与场景划分，不能随机混相邻帧。

</details>

## 边界追问

训练部署标签编号反了，会出现什么表现？

<details>
<summary>追问验收</summary>

网络概率可正确但显示结果相反；保存id-label映射与固定样本回归。

</details>
