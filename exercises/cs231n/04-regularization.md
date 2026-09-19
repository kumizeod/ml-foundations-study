# 练习卡：正则化、数据增强与泛化诊断

[返回笔记](../../notes/cs231n/04-regularization.md)

## 任务

为“判断烧杯是否被夹住”提出三个合理增强与三个可能破坏标签的增强。

<details>
<summary>参考验收点</summary>

答案需解释接触区域、左右关系、遮挡与光照；不能只列增强名称。

</details>

## 边界追问

水平翻转检测图片，还需要改什么？

<details>
<summary>追问验收</summary>

框和mask等空间标注需同步变换，分割标签的插值不能随意产生小数类别。

</details>
