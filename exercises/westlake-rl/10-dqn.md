# 练习卡：DQN：经验回放、目标网络与独立评测

[返回笔记](../../notes/westlake-rl/10-dqn.md)

## 任务

画出DQN在线网络与目标网络的梯度路径，指出reset观测误存会造成什么目标错误。

<details>
<summary>参考验收点</summary>

target停止梯度，只有online被该loss更新；错next_obs会学习不存在的转移。

</details>
