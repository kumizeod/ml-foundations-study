# 机器学习基础：阅读与复习入口

根目录只保留四个功能目录：notes放解释与推导，exercises放题目与验收，
study_labs放可运行小实验，tests放独立检查。三门课各14篇主题笔记，编号是
本仓库的主题编号，不是官方逐讲编号。

## 使用顺序

1. 阅读主题的问题定义、推导和手算例子。
2. 做对应练习卡，先作答再看验收。
3. 运行相关小实验，并用tests核验边界。
4. 对失败记录输入、预期、实际与修复，不只写“已掌握”。

从仓库根目录执行：

```bash
python -m study_labs.nlp
python -m study_labs.vision
python -m study_labs.rl
python -m unittest discover -s tests -v
```

无第三方运行依赖，需要Python3.10+。扩展算子见sequence.py、geometry.py
和policy_evaluation.py，测试验证mask、加权损失、几何变换与固定策略评估。
这些教学实验不是完整LLM、检测器或PPO训练。

## 资料与日期

[课程入口与内容边界](REFERENCES.md) · [原创内容许可](LICENSE) ·
[练习说明](../exercises/README.md) · [实际小实验输出](../exercises/LAB_RESULTS.md)

材料在2026年10月整理。历史Git作者日期用于主题编排与贡献图展示，
不代表当时已经开发或本人已经完成课程。原有42次提交保留，新增整理
与扩展提交集中在8月25日至9月28日；未虚构官方作业、考试或真机成绩。

## 主题目录

| 日期 | 课程 | 笔记 | 练习 |
|---|---|---|---|
| 2026-07-20 | cs224n | [张量、条件概率与语言建模的输入输出](cs224n/01-tensors-and-probability.md) | [练习卡](../exercises/cs224n/01-tensors-and-probability.md) |
| 2026-07-21 | cs224n | [词向量：相似性来自任务，而不是编号](cs224n/02-word-vectors.md) | [练习卡](../exercises/cs224n/02-word-vectors.md) |
| 2026-07-22 | cs224n | [Skip-gram、负采样与训练目标的区别](cs224n/03-word2vec-and-objectives.md) | [练习卡](../exercises/cs224n/03-word2vec-and-objectives.md) |
| 2026-07-23 | cs224n | [交叉熵梯度、数值稳定与优化检查](cs224n/04-backprop-and-optimization.md) | [练习卡](../exercises/cs224n/04-backprop-and-optimization.md) |
| 2026-07-24 | cs224n | [RNN 与 LSTM：信息如何沿时间传播](cs224n/05-rnn-lstm.md) | [练习卡](../exercises/cs224n/05-rnn-lstm.md) |
| 2026-07-26 | cs224n | [Seq2seq、teacher forcing 与训练推理差异](cs224n/06-seq2seq.md) | [练习卡](../exercises/cs224n/06-seq2seq.md) |
| 2026-07-27 | cs224n | [Attention：查询、匹配、加权读取](cs224n/07-attention.md) | [练习卡](../exercises/cs224n/07-attention.md) |
| 2026-07-28 | cs224n | [Transformer：残差、归一化、多头与位置](cs224n/08-transformer.md) | [练习卡](../exercises/cs224n/08-transformer.md) |
| 2026-07-30 | cs224n | [分词、预训练目标与数据泄漏](cs224n/09-tokenization-and-pretraining.md) | [练习卡](../exercises/cs224n/09-tokenization-and-pretraining.md) |
| 2026-07-31 | cs224n | [全量微调、LoRA 与实验公平性](cs224n/10-finetuning.md) | [练习卡](../exercises/cs224n/10-finetuning.md) |
| 2026-08-01 | cs224n | [生成策略与评测：模型得分不等于任务完成](cs224n/11-decoding-and-evaluation.md) | [练习卡](../exercises/cs224n/11-decoding-and-evaluation.md) |
| 2026-08-03 | cs224n | [检索增强、上下文选择与幻觉排查](cs224n/12-retrieval-and-factuality.md) | [练习卡](../exercises/cs224n/12-retrieval-and-factuality.md) |
| 2026-08-05 | cs224n | [偏好学习、奖励信号与工具使用边界](cs224n/13-alignment-and-preferences.md) | [练习卡](../exercises/cs224n/13-alignment-and-preferences.md) |
| 2026-08-07 | cs224n | [NLP 综合复习与小型实验设计](cs224n/14-nlp-capstone.md) | [练习卡](../exercises/cs224n/14-nlp-capstone.md) |
| 2026-08-09 | cs231n | [图像分类、线性分类器与基线](cs231n/01-classification.md) | [练习卡](../exercises/cs231n/01-classification.md) |
| 2026-08-11 | cs231n | [SGD、动量、Adam 与学习率](cs231n/02-optimization.md) | [练习卡](../exercises/cs231n/02-optimization.md) |
| 2026-08-13 | cs231n | [计算图、链式法则与梯度检查](cs231n/03-backprop.md) | [练习卡](../exercises/cs231n/03-backprop.md) |
| 2026-08-15 | cs231n | [正则化、数据增强与泛化诊断](cs231n/04-regularization.md) | [练习卡](../exercises/cs231n/04-regularization.md) |
| 2026-08-17 | cs231n | [卷积、步长、填充与感受野](cs231n/05-convolution.md) | [练习卡](../exercises/cs231n/05-convolution.md) |
| 2026-08-19 | cs231n | [归一化与残差网络](cs231n/06-normalization-resnet.md) | [练习卡](../exercises/cs231n/06-normalization-resnet.md) |
| 2026-08-21 | cs231n | [迁移学习、冻结策略与分布变化](cs231n/07-transfer-learning.md) | [练习卡](../exercises/cs231n/07-transfer-learning.md) |
| 2026-08-23 | cs231n | [视觉序列、图像描述与 Vision Transformer](cs231n/08-visual-sequences-transformers.md) | [练习卡](../exercises/cs231n/08-visual-sequences-transformers.md) |
| 2026-08-25 | cs231n | [检测、分割、IoU 与 NMS](cs231n/09-detection-segmentation.md) | [练习卡](../exercises/cs231n/09-detection-segmentation.md) |
| 2026-08-27 | cs231n | [视频理解、时间采样与训练工程](cs231n/10-video-and-training-systems.md) | [练习卡](../exercises/cs231n/10-video-and-training-systems.md) |
| 2026-08-28 | cs231n | [自监督、对比学习与视觉语言表示](cs231n/11-self-supervision-multimodal.md) | [练习卡](../exercises/cs231n/11-self-supervision-multimodal.md) |
| 2026-08-30 | cs231n | [VAE、GAN、自回归与扩散的目标区别](cs231n/12-generative-models.md) | [练习卡](../exercises/cs231n/12-generative-models.md) |
| 2026-08-31 | cs231n | [三维表示、相机坐标与几何一致性](cs231n/13-3d-geometry.md) | [练习卡](../exercises/cs231n/13-3d-geometry.md) |
| 2026-09-01 | cs231n | [视觉到机器人执行：综合复习与项目边界](cs231n/14-robot-learning-review.md) | [练习卡](../exercises/cs231n/14-robot-learning-review.md) |
| 2026-09-03 | westlake-rl | [状态、动作、奖励与马尔可夫决策过程](westlake-rl/01-mdp.md) | [练习卡](../exercises/westlake-rl/01-mdp.md) |
| 2026-09-05 | westlake-rl | [状态价值、动作价值与贝尔曼期望方程](westlake-rl/02-bellman-expectation.md) | [练习卡](../exercises/westlake-rl/02-bellman-expectation.md) |
| 2026-09-07 | westlake-rl | [最优价值、贪心策略与压缩映射](westlake-rl/03-bellman-optimality.md) | [练习卡](../exercises/westlake-rl/03-bellman-optimality.md) |
| 2026-09-09 | westlake-rl | [价值迭代、策略迭代与可验证基准](westlake-rl/04-dynamic-programming.md) | [练习卡](../exercises/westlake-rl/04-dynamic-programming.md) |
| 2026-09-11 | westlake-rl | [蒙特卡洛评估、探索与回报方差](westlake-rl/05-monte-carlo.md) | [练习卡](../exercises/westlake-rl/05-monte-carlo.md) |
| 2026-09-13 | westlake-rl | [随机近似、Robbins–Monro 与 SGD](westlake-rl/06-stochastic-approximation.md) | [练习卡](../exercises/westlake-rl/06-stochastic-approximation.md) |
| 2026-09-15 | westlake-rl | [TD、自举与终止边界](westlake-rl/07-temporal-difference.md) | [练习卡](../exercises/westlake-rl/07-temporal-difference.md) |
| 2026-09-17 | westlake-rl | [Sarsa、Expected Sarsa 与 Q-learning](westlake-rl/08-sarsa-qlearning.md) | [练习卡](../exercises/westlake-rl/08-sarsa-qlearning.md) |
| 2026-09-19 | westlake-rl | [价值函数近似、投影与半梯度](westlake-rl/09-value-approximation.md) | [练习卡](../exercises/westlake-rl/09-value-approximation.md) |
| 2026-09-21 | westlake-rl | [DQN：经验回放、目标网络与独立评测](westlake-rl/10-dqn.md) | [练习卡](../exercises/westlake-rl/10-dqn.md) |
| 2026-09-23 | westlake-rl | [策略梯度与 REINFORCE 的推导](westlake-rl/11-policy-gradient.md) | [练习卡](../exercises/westlake-rl/11-policy-gradient.md) |
| 2026-09-25 | westlake-rl | [Actor–Critic、优势与重要性采样](westlake-rl/12-actor-critic.md) | [练习卡](../exercises/westlake-rl/12-actor-critic.md) |
| 2026-09-27 | westlake-rl | [扩展：GAE、PPO 与批次复用边界](westlake-rl/13-ppo-extension.md) | [练习卡](../exercises/westlake-rl/13-ppo-extension.md) |
| 2026-09-28 | westlake-rl | [强化学习综合练习、复现与失败分析](westlake-rl/14-rl-capstone.md) | [练习卡](../exercises/westlake-rl/14-rl-capstone.md) |
