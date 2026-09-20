# 练习卡：视觉序列、图像描述与 Vision Transformer

[返回笔记](../../notes/cs231n/08-visual-sequences-transformers.md)

## 任务

计算224分辨率下patch16与patch8的token数量和attention分数矩阵大小比。

<details>
<summary>参考验收点</summary>

不含分类token时196与784，分数元素比16；说明加分类token后不是精确16。

</details>

## 边界追问

加入分类token后，patch减半的attention元素比仍精确16吗？

<details>
<summary>追问验收</summary>

不是，224例中为785²/197²约15.88；说明特殊token与padding。

</details>
