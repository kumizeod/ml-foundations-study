# 练习卡：视频理解、时间采样与训练工程

[返回笔记](../../notes/cs231n/10-video-and-training-systems.md)

## 任务

为10秒30fps视频设计均匀采样与接触事件附近密集采样的对照。

<details>
<summary>参考验收点</summary>

样本总量或成本应匹配；按原视频划分，记录时间戳而不是只记帧号。

</details>

## 边界追问

16帧均匀采样能保证覆盖0.1秒事件吗？

<details>
<summary>追问验收</summary>

不能；间隔可能远大于事件时长。采样策略是输入信息选择的一部分。

</details>
