# 练习卡：三维表示、相机坐标与几何一致性

[返回笔记](../../notes/cs231n/13-3d-geometry.md)

## 任务

取fx=500、cx=320、u=370、深度1米，计算相机X；再讨论毫米与米混淆。

<details>
<summary>参考验收点</summary>

X=0.1米；单位错误可造成1000倍误差；还需外参才能到机器人基座坐标。

</details>

## 边界追问

p_b=Rp_c+t的逆，为什么不是随意写−t？

<details>
<summary>追问验收</summary>

应先减t再乘Rᵀ：p_c=Rᵀ(p_b−t)，坐标系与乘法顺序必须一致。

</details>
