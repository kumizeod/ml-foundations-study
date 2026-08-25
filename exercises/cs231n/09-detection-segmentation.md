# 练习卡：检测、分割、IoU 与 NMS

[返回笔记](../../notes/cs231n/09-detection-segmentation.md)

## 任务

手算两个2×2相交框的IoU，并对三个框执行NMS；加入完全重合与零面积测试。

<details>
<summary>参考验收点</summary>

交叠一格时IoU=1/7；相同框高分保留；坐标连续定义不额外加1。

</details>
