# 练习卡：生成策略与评测：模型得分不等于任务完成

[返回笔记](../../notes/cs224n/11-decoding-and-evaluation.md)

## 任务

设n=5次生成中c=2成功，计算k=2的组合pass@k估计，并解释一次成功样本选择的成本。

<details>
<summary>参考验收点</summary>

1−C(3,2)/C(5,2)=0.7；样本选择、失败尝试与重试成本不能省略。

</details>
