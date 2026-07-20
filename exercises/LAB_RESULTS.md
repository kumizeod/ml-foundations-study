# 可复现的小实验结果

这些是整理仓库时实际运行的教学程序输出，不是使用者的课程成绩、官方作业结果或历史学习证明。
原始结果与运行时间保存在[results/](results/)。本机Python：3.12.14。

| 实验 | 本次输出 | 说明 |
|---|---|---|
| 交叉熵数值梯度 | 最大绝对误差 1.15e-11 | 中心差分核对解析梯度 |
| attention mask | 输出[2,3]，权重[1,0] | 被屏蔽value不进入加权读取 |
| 二维互相关 | [[-4,-4],[-4,-4]] | 单通道valid小算子 |
| IoU | 1/7 | 连续xyxy坐标定义 |
| NMS | 保留索引[0,2] | 重合低分框被抑制 |
| 价值迭代 | 起点约0.7019，策略全向右 | 有限链式MDP |
| Q-learning | 种子7、1000回合，贪心策略全向右 | 与动态规划基准比较 |

复现命令：

```bash
python -m study_labs.nlp
python -m study_labs.vision
python -m study_labs.rl
python -m unittest discover -s tests -v
```

这些小例子没有使用公开大数据集，不含训练完整LLM、CNN、DQN或PPO的成绩。
自行修改实验后，请新增自己的真实记录，并注明参数与失败情况。
