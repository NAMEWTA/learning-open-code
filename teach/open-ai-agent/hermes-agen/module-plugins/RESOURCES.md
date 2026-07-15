# 插件系统模块 资源

## 知识

- [hermes_cli/plugins.py — 插件系统核心 (2334 行)](https://github.com/NousResearch/hermes-agent/blob/main/hermes_cli/plugins.py)
  PluginManager、PluginContext、PluginManifest、LoadedPlugin 的完整实现。包含四种插件来源扫描、五种插件形态的路由策略、生命周期 Hook 调用、工具/Middleware 注册等全部机制。适用场景：理解插件加载全链路。

- [plugins/memory/__init__.py — 独占型插件发现 (451 行)](https://github.com/NousResearch/hermes-agent/blob/main/plugins/memory/__init__.py)
  exclusive 插件的发现和加载范本——`discover_memory_providers()` 和 `load_memory_provider()` 展示了插件自有发现系统如何与 PluginManager 共存。适用场景：理解 exclusive 插件形态的设计模式。

- [plugins/plugin_utils.py — 插件线程安全工具](https://github.com/NousResearch/hermes-agent/blob/main/plugins/plugin_utils.py)
  为插件作者提供 `lazy_singleton` 装饰器和 `SingletonSlot` 类，解决多线程环境下 TOCTOU 单例竞争问题。适用场景：理解插件开发的并发安全基础。

- [plugins/image_gen/openai/plugin.yaml — backend 插件清单示例](https://github.com/NousResearch/hermes-agent/blob/main/plugins/image_gen/openai/plugin.yaml)
  典型 backend 插件的 plugin.yaml 格式：kind、requires_env、description。适用场景：理解插件元数据格式。

- [plugins/disk-cleanup/plugin.yaml — standalone 插件清单示例](https://github.com/NousResearch/hermes-agent/blob/main/plugins/disk-cleanup/plugin.yaml)
  典型 standalone 插件的 plugin.yaml 格式：hooks 声明、作者信息。适用场景：理解 standalone 插件如何声明 Hook 依赖。

- [hermes_cli/plugins_cmd.py — 插件 CLI 管理命令](https://github.com/NousResearch/hermes-agent/blob/main/hermes_cli/plugins_cmd.py)
  `hermes plugins install/list/enable/disable/remove` 等管理命令实现。适用场景：理解插件的安装与生命周期管理。

## 智慧（社区）

- [Discord — Nous Research](https://discord.gg/NousResearch)
  Hermes Agent 官方社区，包含插件开发讨论和最佳实践分享。适用场景：插件开发问题求助和实践交流。

- [GitHub Issues — hermes-agent](https://github.com/NousResearch/hermes-agent/issues)
  搜索 "plugin" 标签查看插件系统的历史设计决策和已知限制。适用场景：理解插件系统的边界情况和设计意图。

## 空白

- 暂无针对 Hermes 插件系统的独立开发者文档或教程
- 插件 API（PluginContext 各注册方法）的独立参考文档缺失，当前仅以源码注释形式存在
