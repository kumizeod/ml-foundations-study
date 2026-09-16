# 练习卡：Skip-gram、负采样与训练目标的区别

[返回笔记](../../notes/cs224n/03-word2vec-and-objectives.md)

## 任务

正词对分数从0提高到1，计算−logσ(s)的变化；再把它当成负词对计算对应损失。

<details>
<summary>参考验收点</summary>

正词对损失从log2约0.693降到约0.313；负词对损失从0.693升至约1.313。梯度方向相反。

</details>

## 边界追问

数值梯度两次采样不同负例，会发生什么？

<details>
<summary>追问验收</summary>

差分混入采样噪声，不再比较同一个目标函数。先固定负例再检查求导。

</details>
