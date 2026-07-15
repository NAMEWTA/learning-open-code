# 工具层 资源

## 知识

- [源码：`tools/registry.py`](https://github.com/NousResearch/hermes-agent/blob/main/tools/registry.py)
  工具注册中心——`ToolEntry` 数据结构、`register()` 自注册机制、`discover_builtin_tools()` 自动发现器、check_fn TTL 缓存。适用于：理解工具如何被声明和汇总。

- [源码：`tools/terminal_tool.py` (132KB)](https://github.com/NousResearch/hermes-agent/blob/main/tools/terminal_tool.py)
  终端命令执行工具——支持 local / Docker / Modal / SSH / Singularity / Daytona 六种后端。适用于：理解终端工具的多后端抽象和命令执行生命周期。

- [源码：`tools/browser_tool.py` (201KB)](https://github.com/NousResearch/hermes-agent/blob/main/tools/browser_tool.py)
  浏览器自动化工具——基于 agent-browser CLI，支持 Browser Use 云、Browserbase 云、本地 Chromium 三种模式。适用于：理解无视觉 LLM Agent 如何通过可访问性树操作网页。

- [源码：`tools/delegate_tool.py` (148KB)](https://github.com/NousResearch/hermes-agent/blob/main/tools/delegate_tool.py)
  子代理委托工具——生成独立 AIAgent 实例，支持单任务和批量并行模式。适用于：理解 Agent 层级委托的隔离模型和上下文管理。

- [源码：`tools/approval.py` (130KB)](https://github.com/NousResearch/hermes-agent/blob/main/tools/approval.py)
  命令审批系统——危险命令模式检测、交互式/异步审批、硬线阻断、智能 LLM 审批。适用于：理解 Agent 安全闸门的设计模式。

- [源码：`tools/skills_hub.py` (154KB)](https://github.com/NousResearch/hermes-agent/blob/main/tools/skills_hub.py)
  技能中心——技能发现、安装、发布、GitHub 源适配器、锁定文件溯源。适用于：理解技能的来源管理和安全扫描。

- [源码：`tools/blueprints.py`](https://github.com/NousResearch/hermes-agent/blob/main/tools/blueprints.py)
  工具蓝图——将技能元数据桥接到 cron 定时任务。适用于：理解"技能即蓝图"的设计哲学。

- [项目 README](https://github.com/NousResearch/hermes-agent#readme)
  Hermes Agent 官方项目说明，包含工具层架构的宏观描述。

## 智慧（社区）

- [Hermes Agent GitHub Discussions](https://github.com/NousResearch/hermes-agent/discussions)
  官方讨论区，可搜索工具开发、安全策略、子代理使用等主题的社区经验。

## 空白

- 暂无官方架构设计文档（RFC/ADR）专门描述工具层的分层设计决策
- 缺少工具开发的贡献指南或教程
