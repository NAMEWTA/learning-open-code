# 使命：Web 仪表盘

## 为什么
Hermes Agent 提供 Web 仪表盘作为图形化管理界面，用于配置 Agent 参数、管理 API 密钥、监控会话状态、查看日志分析。理解 web/ 模块的 SPA 前端架构和与 FastAPI 后端的联动方式，是后续深入定制仪表盘、开发仪表盘插件的前置基础。

## 成功的样子
- 能画出 web/ 模块的完整目录树，说出 pages/、components/、lib/、plugins/、contexts/ 各目录职责
- 能解释 Vite 开发服务器如何通过代理与 FastAPI 后端协作（/api 代理、session token 注入）
- 能列出仪表盘提供的 18 个内置页面及其功能
- 能描述插件系统如何通过 PluginManifest 注册新页面和侧边栏导航项

## 约束条件
- 学习方式：阅读教学课程 + 对照源码验证
- 先修要求：已完成 L0 Hermes Agent 项目总览，理解整体分层架构
- 本模块聚焦 web/ 目录本身，不深入 Python 后端 web_server.py 实现

## 不在范围内
- Python 后端 hermes_cli/web_server.py 的 FastAPI 路由实现细节
- gateway/ 消息网关的平台适配逻辑（属于 gateway 模块课程）
- @nous-research/ui 设计系统的组件实现细节
- CLI、TUI、Desktop 等其他入口的实现
