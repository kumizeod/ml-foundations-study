# Attention：查询、匹配、加权读取

[总目录](../../INDEX.md) · [上一主题](../cs224n/06-seq2seq.md) · [下一主题](../cs224n/08-transformer.md)

主题编排日期：2026-07-27；不是实际学习完成日期。

## 核心问题
把 attention 看成可微检索：query 表示当前需要什么，key 表示候选内容的索引，value 表示真正读取的内容。key 与 value 的职责不同，输出是 value 的加权组合，不是 key 的平均。

## 数学与形状
Q∈R^(T_q×d_k)、K∈R^(T_k×d_k)、V∈R^(T_k×d_v)，输出 softmax(QKᵀ/√d_k+M)V。分数矩阵为 T_q×T_k，softmax 沿候选 key 的维度归一化。缩放缓解维度增大导致分数方差增大、概率过度尖锐的问题；不是一个随意的装饰常数。

## 手算与验证
若两个 value 是 (2,0)、(0,4)，权重为 (0.75,0.25)，输出是 (1.5,1)。屏蔽第二个 key 后，权重必须成为 (1,0)，不能只是把输出中的第二维清零。运行 `python -m study_labs.nlp`，修改被屏蔽 value 为极大数，确认输出不变。

## 常见错误
所有 key 都被屏蔽时，softmax 没有合法分布，应该显式处理而不是让 NaN 传播。padding mask 与 causal mask 的广播形状要核对。attention 权重大不等于因果解释：value 投影、残差和后续层都参与最终输出。

## 与代码检索的连接
可把 query 理解为当前修复问题，key 是文件片段索引，value 是代码内容。但检索命中仍需验证版本、文件路径与调用上下文，不能把“相似”当成“正确”。

## 自测与参考答案
问：query 数量必须等于 key 数量吗？答：不必，cross-attention 常不同。问：key 与 value 维度必须相同吗？答：不必，Q/K 的匹配维度必须一致，V 可以有自己的特征维度。

[对应练习卡](../../exercises/cs224n/07-attention.md) · [统一资料入口](../../SOURCES.md)
