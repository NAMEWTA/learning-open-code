# 教学笔记：多平台消息全链路

## 用户偏好
- 偏好时序图 + 表格对照形式理解链路
- 关注异常路径（投递失败、消息丢失）多于正常路径

## 教学难点预警
- gateway/run.py 文件 995KB，是网关启动和生命周期管理的巨型文件，不需要通读
- base.py 文件 239KB，包含 22+ 平台适配器实现，本课只需关注抽象基类部分
- RelayTransport 的 WebSocket 协议细节较复杂，首次学习只需了解 hello/handshake/inbound/outbound 四类帧即可

## 交叉引用
- 前置课程：L1-gateway（gateway 三层架构）、L1-agent-core（对话循环）
- 关联 L2 课程：L2-cron-scheduled-task（定时任务投递使用相同的 DeliveryRouter）
