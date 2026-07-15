# 教学笔记：ACP 适配器与注册中心

## 用户偏好

- 学习风格：先理解整体架构，再深入关键代码路径
- 关注重点：事件桥接机制（线程安全）、会话持久化设计

## 教学注意事项

- ACP 协议概念在 L0 已介绍，本模块只讲 Hermes 的具体实现
- 重点强调 acp_adapter 的"桥接"本质：将阻塞式 AIAgent 包装为异步 ACP Agent
- entry.py 中的日志处理细节（stderr vs stdout 分离）是理解 ACP stdio transport 的关键
