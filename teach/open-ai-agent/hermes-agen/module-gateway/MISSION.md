# 使命：消息网关模块

## 为什么
掌握 Hermes Agent 的多平台消息网关架构，理解一条消息从用户发送到 Agent 响应、再到投递回平台的完整链路。这是将 Agent 接入真实工作场景的关键——无论用户通过 Telegram、Discord、Slack 还是微信交互，核心处理逻辑不变，变化仅发生在 gateway 层。

## 成功的样子
- 能画出 gateway 的三层架构图：平台适配层 → 中继路由层 → 投递层
- 能解释 Platform 枚举中 22+ 平台如何通过统一接口对接，以及 RelayAdapter 如何统一前端
- 能说出平台适配器（BasePlatformAdapter）的四个抽象方法及各自职责
- 能解释消息投递路由的显式靶点 → home channel → 来源回投 → 本地文件三级回退策略

## 约束条件
- 学习方式：阅读教学课程 + 对照源码验证，非视频学习
- 先修要求：已完成 L0 项目总览，了解 Hermes Agent 整体架构

## 不在范围内
- 各平台适配器的完整实现细节（Telegram/Discord/Slack 的 API 差异）
- gateway/run.py（972KB）的全量代码分析
- session 管理、authz_mixin、slash_commands 的深入解析
- 定时任务（cron/）与 gateway 的集成细节
