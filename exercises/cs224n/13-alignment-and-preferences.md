# 练习卡：偏好学习、奖励信号与工具使用边界

[返回笔记](../../notes/cs224n/13-alignment-and-preferences.md)

## 任务

写出一个可被删测试绕过的验收，再设计独立验证修补它。

<details>
<summary>参考验收点</summary>

验证器不能完全处于Agent可编辑工作区；检查真实产物和旧功能，不能只检查自报成功。

</details>

## 边界追问

独立验收与训练奖励分别解决什么？

<details>
<summary>追问验收</summary>

前者测量任务是否完成，后者优化行为；权限再限制可执行范围，三者不能互相替代。

</details>
