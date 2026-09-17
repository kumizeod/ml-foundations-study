# 练习卡：Attention：查询、匹配、加权读取

[返回笔记](../../notes/cs224n/07-attention.md)

## 任务

用query=(1,0)、keys=[(1,0),(0,1)]、values=[(2,3),(100,100)]计算遮罩后attention。

<details>
<summary>参考验收点</summary>

仅允许第一个key时权重为(1,0)，输出(2,3)；改变被遮罩value不影响输出。

</details>

## 边界追问

先softmax再把未来权重清零，为什么不够？

<details>
<summary>追问验收</summary>

剩余权重通常不再和为1；应在归一化前遮罩。用修改未来value不影响前缀的测试检查。

</details>
