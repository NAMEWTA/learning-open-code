# 使命：插件系统模块

## 为什么
掌握 Hermes Agent 的插件架构与扩展机制，理解如何通过插件模式为 Agent 集成浏览器自动化、记忆增强、看板管理、图像生成等外部能力。这是将 Hermes 从"单体 Agent"升级为"可组合 Agent 平台"的核心设计——所有非核心功能都以插件形式注入，核心框架保持轻量。

## 成功的样子
- 能画出 Hermes 插件的四种来源（bundled / user / project / entry-point）和五种形态（standalone / backend / exclusive / platform / model-provider）
- 能解释 `PluginManager.discover_and_load()` 从扫描目录到调用 `register(ctx)` 的完整加载链路
- 能说出 `PluginContext` 提供的 12+ 种注册方法，以及它们分别对接哪些子系统（工具注册、Hook 回调、Provider 后端、CLI 命令等）
- 能解释生命周期 Hook（`pre_tool_call`、`post_tool_call`、`on_session_end` 等 20+ 种）的触发时机与用途
- 能区分 backend 插件（如 image_gen/openai）和 exclusive 插件（如 memory/honcho）的加载策略差异

## 约束条件
- 学习方式：阅读教学课程 + 对照源码验证，非视频学习
- 先修要求：已完成 L0 项目总览，了解 Hermes Agent 整体架构

## 不在范围内
- 具体插件（browser/memory/kanban/image_gen）的 Provider 实现细节与 API 调用逻辑
- `plugins/` 下各子目录的完整代码分析（如 `platforms/` 52 个 .py 文件）
- `plugin_utils.py` 中 `lazy_singleton` / `SingletonSlot` 的线程安全细节
- `hermes plugins` CLI 子命令的安装/卸载流程
