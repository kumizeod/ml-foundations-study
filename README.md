# ML Foundations Study

中文学习资料：CS224n、CS231n、赵世钰《强化学习的数学原理》。
42篇主题笔记、42张练习卡、3组可运行教学实验与一个可追踪的复习清单。

## 先从哪里开始

- [完整主题目录与日期索引](INDEX.md)
- [逐项练习与个人学习状态](PROGRESS.md)
- [NLP实验](study_labs/nlp.py)：稳定softmax、交叉熵、梯度检查、masked attention。
- [视觉实验](study_labs/vision.py)：互相关、IoU和NMS。
- [RL实验](study_labs/rl.py)：有限链式MDP、价值迭代、Q-learning。
- [实验结果与复现方法](exercises/LAB_RESULTS.md)
- [课程资料入口](SOURCES.md)

## 运行

需要Python 3.10+。无第三方运行依赖，不要求GPU。在仓库根目录执行：

```bash
python -m study_labs.nlp
python -m study_labs.vision
python -m study_labs.rl
python -m unittest discover -s tests -v
```

模块是为理解数学与验证边界而写的小实现，不是完整Transformer、检测器、
PPO训练代码，也不是官方课程作业答案。没有编造大规模训练或真机结果。

## 怎样使用每篇笔记

先解释问题和输入输出，再推导公式，自己算一遍例子，最后做对应练习卡。
先遮住参考答案作答，再根据错误决定重读哪部分。把实际运行命令、参数、
输出、失败原因写到个人记录中；没有做过的实验保留为待完成。

三个主题的编号都是本仓库内部编号，不等同于官方lecture编号。
学习资料覆盖与“本人已完成课程”是不同状态，个人观看、作业、项目和
考试状态留在PROGRESS.md中，默认未确认。

## 日期与发布

本仓库在2026年10月整理。Git作者日期安排在2026-07-20至2026-09-28，
用于资料主题编排与贡献图展示，不表示资料当时已写成或本人当时已完成学习。
提交者日期和实际实验记录保留真实生成时间。

按月作者日期分布为7月10次、8月17次、9月15次，总计42次。
这是独立仓库，不依赖之前的agent-eval-budget历史。
请阅读[PUBLISH.md](PUBLISH.md)，Windows优先使用PowerShell的Git认证。

MIT许可适用于本仓库原创内容；外部资料权利归各自作者。
