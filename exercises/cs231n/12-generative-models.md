# 练习卡：VAE、GAN、自回归与扩散的目标区别

[返回笔记](../../notes/cs231n/12-generative-models.md)

## 任务

给出VAE重建项与KL项的功能，并说明生成好看视频为什么不能证明物理正确。

<details>
<summary>参考验收点</summary>

重建鼓励解释观测，KL约束后验与先验关系；物理行为需独立任务或动力学验证。

</details>

## 边界追问

生成视频逐帧好看，能证明接触合理吗？

<details>
<summary>追问验收</summary>

不能；需检查时间连续、物体关系、动力学与下游执行，分开报告。

</details>
