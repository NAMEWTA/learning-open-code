# Web 仪表盘 资源

## 知识

- [web/README.md — 项目文档](https://github.com/NousResearch/hermes-agent/blob/main/web/README.md)
  Web 仪表盘的官方说明文档，涵盖技术栈、开发流程、构建命令、排版规范。适用于快速了解项目结构和开发约定。

- [web/src/App.tsx — 主布局组件](https://github.com/NousResearch/hermes-agent/blob/main/web/src/App.tsx)
  仪表盘主布局（1357 行），包含侧边栏导航、路由表、页面布局、插件注入槽位、移动端适配。适用于理解仪表盘的整体 Shell 结构。

- [web/src/main.tsx — React 入口](https://github.com/NousResearch/hermes-agent/blob/main/web/src/main.tsx)
  React 应用入口，挂载 BrowserRouter、I18nProvider、ThemeProvider、SystemActionsProvider。适用于理解应用的 Provider 层级和初始化顺序。

- [web/src/lib/api.ts — API 客户端](https://github.com/NousResearch/hermes-agent/blob/main/web/src/lib/api.ts)
  前端 API 层，封装所有后端端点调用，含 session token 注入、management profile 范围注入、WebSocket ticket 获取。适用于理解前后端通信协议。

- [web/vite.config.ts — 构建配置](https://github.com/NousResearch/hermes-agent/blob/main/web/vite.config.ts)
  Vite 配置（103 行），含 dev token 注入插件、/api 代理、dashboard-plugins 代理、构建输出到 ../hermes_cli/web_dist。适用于理解开发与生产环境的构建流程。

- [web/src/plugins/types.ts — 插件 SDK 类型](https://github.com/NousResearch/hermes-agent/blob/main/web/src/plugins/types.ts)
  仪表盘插件系统的类型定义（PluginManifest），含 tab 位置、路由覆盖、隐藏注册、SRI 完整性校验。适用于理解插件扩展机制。

- [web/src/pages/ — 页面目录](https://github.com/NousResearch/hermes-agent/tree/main/web/src/pages)
  18 个内置页面：SessionsPage、ConfigPage、EnvPage、ModelsPage、CronPage、SkillsPage、PluginsPage、McpPage、ProfilesPage、ProfileBuilderPage、ChannelsPage、WebhooksPage、PairingPage、SystemPage、AnalyticsPage、LogsPage、FilesPage、ChatPage、DocsPage。

- [web/src/components/ — 组件目录](https://github.com/NousResearch/hermes-agent/tree/main/web/src/components)
  27 个业务组件：AuthWidget、ChatSidebar、ModelPickerDialog、SkillEditorDialog、ScheduleBuilder、ToolsetConfigDrawer 等。

- [web/src/i18n/ — 国际化](https://github.com/NousResearch/hermes-agent/tree/main/web/src/i18n)
  18 种语言翻译文件，含中文简体和繁体支持。

- [web/src/themes/ — 主题系统](https://github.com/NousResearch/hermes-agent/tree/main/web/src/themes)
  可切换的主题预设（含字体、配色），通过 CSS 变量注入。

## 智慧（社区）

- [r/nousresearch](https://reddit.com/r/nousresearch)
  Nous Research 官方 subreddit，适用于：仪表盘使用问题、功能建议。

- [Hermes Agent Discord](https://discord.gg/nousresearch)
  官方 Discord 社区，适用于：实时问答、bug 报告、插件开发讨论。

## 空白

- web/ 模块没有独立的架构设计文档，架构信息主要来自 README.md 和源码注释。
- 仪表盘插件系统的开发者指南在公开资料中缺失（仅 types.ts 和 registry.ts 中的类型定义和注释可用）。
- @nous-research/ui 设计系统（shadcn/ui 风格的手写组件库）没有独立的文档站，需阅读源码理解组件 API。
