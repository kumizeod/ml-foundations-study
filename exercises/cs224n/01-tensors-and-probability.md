# 练习卡：张量、条件概率与语言建模的输入输出

[返回笔记](../../notes/cs224n/01-tensors-and-probability.md)

## 任务

给序列[BOS,机器人,抓杯,EOS]写出三组输入和下一token标签，加入两个PAD后列出有效位。

<details>
<summary>参考验收点</summary>

输入BOS/机器人/抓杯，对应机器人/抓杯/EOS；PAD位置不参加平均损失。说明按句平均与按token平均的差别。

</details>

## 边界追问

额外追加100个PAD，loss为何可能变化？

<details>
<summary>追问验收</summary>

若除以填充后长度，分母错误；只对有效位求平均应不变。全mask时平均未定义。

</details>
