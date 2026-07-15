# Hermes Agent 教学索引

## 教学主题

| 主题 | 路径 | 描述 |
|------|------|------|
| 项目总览 | `./00-overview/` | Hermes Agent 架构全景、目录地图、设计哲学与源码入口导航 |
| Agent 核心引擎 | `./module-agent-core/` | 对话循环、工具执行、记忆管理、上下文压缩四层核心架构 |
| Agent 入口层 | `./module-agent-entry/` | CLI启动、主运行循环、状态持久化、日志与配置系统 |
| 消息网关 | `./module-gateway/` | 多平台消息路由、适配器三层架构与投递系统 |
| 工具层 | `./module-tools/` | 终端/浏览器/委托工具、三层安全审批、AST自注册机制 |
| 技能系统 | `./module-skills/` | SKILL.md规范、Skills Hub七源联合发现、策展器生命周期管理 |
| CLI 框架 | `./module-cli-framework/` | argparse命令树、子命令Builder插件化、三层配置优先级与Shell补全 |
| 插件系统 | `./module-plugins/` | 四源五态插件架构、PluginManager加载链路、20+Hook生命周期与Provider注册 |
| 模型提供商层 | `./module-providers/` | ProviderProfile声明式抽象、注册中心与30+提供商插件发现机制 |
| 定时任务调度 | `./module-cron/` | croniter自然语言定时、双线程池调度、lifecycle_guard安全防护 |
| 终端 UI | `./module-tui/` | React+Ink TUI 双进程架构、JSON-RPC 通信与交互系统 |
| Agent Client Protocol | `./module-acp/` | ACP协议桥接架构、会话持久化、事件流转发与权限审批 |
| Web 仪表盘 | `./module-web/` | FastAPI+SPA前后端分离、插件系统、14个API端点族 |
| Agent 对话全链路 | `./slice-agent-conversation-loop/` | CLI到LLM响应的六阶段完整请求路径、Provider故障链式切换 |
| 工具执行与审批全链路 | `./slice-tool-execution-approval/` | Tool Call→Registry→三层安全闸门→Execute的完整链路 |
| 技能生命周期全链路 | `./slice-skill-lifecycle/` | 从任务完成到技能创建、策展器状态机到归档保护的全链路 |
| 多平台消息全链路 | `./slice-multi-platform-message/` | 外部消息→Platform Adapter→Relay→Agent→Delivery全链路 |
| 定时任务全链路 | `./slice-cron-scheduled-task/` | NL解析→表达式→持久化→调度→执行→守护→投递七阶段完整追踪 |
