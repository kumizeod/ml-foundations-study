# 练习卡：扩展：GAE、PPO 与批次复用边界

[返回笔记](../../notes/westlake-rl/13-ppo-extension.md)

## 任务

对A=+2或−2、ratio1.5、clip[0.8,1.2]手算PPO min代理目标，并写GAE递推。

<details>
<summary>参考验收点</summary>

目标分别2.4与−3；GAE为delta+gamma lambda下一优势，终止边界需正确处理。

</details>

## 边界追问

每个PPO epoch重新计算old logprob有什么问题？

<details>
<summary>追问验收</summary>

会把比率重置到接近1，失去相对采样时策略的比较，改变算法目标。

</details>
