# 练习卡：TD、自举与终止边界

[返回笔记](../../notes/westlake-rl/07-temporal-difference.md)

## 任务

V(s)=0.4、V(s′)=0.6、r=0、gamma0.9、alpha0.1时分别算普通一步与终止更新。

<details>
<summary>参考验收点</summary>

非终止更新到0.414；真终止更新到0.36。时间上限是否自举按任务语义判断。

</details>

## 边界追问

自动reset环境把新起点当next_obs有什么后果？

<details>
<summary>追问验收</summary>

将两回合错误连接，污染TD、回放与GAE；保存真正final observation。

</details>
