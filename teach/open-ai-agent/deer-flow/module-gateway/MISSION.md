# 使命：Gateway API 外壳

## 为什么
学习者希望从 deer-flow 的默认运行外壳入手，准确判断一个前端请求进入后会经过哪些 Gateway 边界，以及哪些逻辑应继续下钻到 agent runtime、持久化或前端工作区。掌握这个边界后，后续调试认证、router 注册、SSE run 和配置热加载时能先找到正确入口。

## 成功的样子
- 能说明 `backend/app/gateway/app.py` 在启动、middleware、router 和 runtime 接线中的职责。
- 能把 Gateway 与 nginx、前端、RunManager、lead agent、persistence 的关系放进一张请求流图里。
- 能通过一个简单 HTTP 调用验证 Gateway 是否在运行，并知道认证接口与业务接口的基本门槛。

## 约束条件
- 本主题是 L1 模块课，只建立边界和入口地图，不展开每个 router 的内部实现。
- 主课控制在 15 分钟内完成；长接口清单、源码索引和调用速查放入 reference。
- 输出使用简体中文；代码路径、函数名和 HTTP 路径保留原始英文。

## 不在范围内
- lead agent 中间件链、工具调用、subagent 执行和 sandbox 文件系统细节。
- RunManager、StreamBridge、checkpointer、store 的内部算法。
- 前端 workspace 页面如何消费流式事件。
