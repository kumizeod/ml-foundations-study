# 练习卡：交叉熵梯度、数值稳定与优化检查

[返回笔记](../../notes/cs224n/04-backprop-and-optimization.md)

## 任务

运行nlp模块，并独立用中心差分检验三个logit的梯度；把全部logit加1000再算。

<details>
<summary>参考验收点</summary>

概率在浮点精度内不变；解析梯度与数值梯度接近。不要用同一解析函数同时生成两边答案。

</details>
