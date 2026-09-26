# 练习卡：价值函数近似、投影与半梯度

[返回笔记](../../notes/westlake-rl/09-value-approximation.md)

## 任务

构造两个状态共享同一特征但价值不同的例子，解释近似误差与半梯度。

<details>
<summary>参考验收点</summary>

无法同时精确表示两个不同目标；半梯度不反传自举目标分支。

</details>

## 边界追问

完整Bellman残差梯度与TD半梯度相同吗？

<details>
<summary>追问验收</summary>

不相同，前者可能含下一价值分支的导数；半梯度只更新当前预测分支。

</details>
