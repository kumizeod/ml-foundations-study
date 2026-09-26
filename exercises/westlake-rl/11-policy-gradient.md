# 练习卡：策略梯度与 REINFORCE 的推导

[返回笔记](../../notes/westlake-rl/11-policy-gradient.md)

## 任务

推导两个动作softmax下−logπ(a)A的更新方向，分别使用正/负优势。

<details>
<summary>参考验收点</summary>

正优势提高所采动作概率，负优势降低；基线独立于动作时相应期望项为0。

</details>

## 边界追问

基线依赖动作时，还能直接减去而不改期望吗？

<details>
<summary>追问验收</summary>

不能直接保证；动作无关基线的零期望推导不再适用，需额外修正。

</details>
