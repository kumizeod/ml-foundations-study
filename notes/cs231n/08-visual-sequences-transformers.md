# 视觉序列、图像描述与 Vision Transformer

[总目录](../README.md) · [上一主题](../cs231n/07-transfer-learning.md) · [下一主题](../cs231n/09-detection-segmentation.md)

## 核心问题
图像可以被编码成局部特征序列，再由 RNN 或 Transformer 处理。图像描述把视觉信息与语言生成连接起来；ViT 则把图像切成 patch，并把 patch 表示作为序列输入。

## 形状推导
224×224 图像使用 16×16 patch 时得到 14×14=196 个 patch。若加入一个分类 token，序列长为197。每个 patch 的原始展开维度为16×16×3=768，再投影到模型隐藏维。patch 变小通常提高空间分辨率，也会显著增加标准 attention 的序列成本。

## 位置与归纳偏置
卷积内置局部连接与共享结构，ViT 对局部性与位置的处理不同。不能简单说“Transformer 永远比 CNN 好”，要结合数据规模、预训练、计算预算和目标任务。改变输入分辨率时，位置表示如何插值或外推也需要记录。

## 多模态连接
图像描述可以用视觉 encoder 与文本 decoder；cross-attention 的 query 来自解码状态，key/value 来自视觉表示。语言流畅不保证图像内容真实，应检查物体、关系和动作是否得到视觉证据支持。

## 练习
比较 patch=16 与 patch=8 的 token 数，并计算分数矩阵元素数的比例。再解释为什么精确接触点可能需要局部高分辨率，而不是只依赖全局分类 token。

## 自测与参考答案
问：patch 减半后 token 数大致怎样变？答：面积方向约四倍，attention 分数元素约十六倍。问：分类 token 可以直接当像素分割输出吗？答：不能，需要空间输出结构与监督。

[对应练习卡](../../exercises/cs231n/08-visual-sequences-transformers.md)
