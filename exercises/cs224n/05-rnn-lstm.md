# 练习卡：RNN 与 LSTM：信息如何沿时间传播

[返回笔记](../../notes/cs224n/05-rnn-lstm.md)

## 任务

写出h_t=tanh(W_h h_(t−1)+W_x x_t+b)中各矩阵形状，并画出三步参数共享。

<details>
<summary>参考验收点</summary>

同一W_h在三步使用，反传要累加三个使用点的贡献；区分数值状态与计算图是否跨片段延续。

</details>

## 边界追问

detach后的状态能否仍携带前文信息？

<details>
<summary>追问验收</summary>

能保留数值，但梯度不再越过detach回到更早片段。二者不要混淆。

</details>
