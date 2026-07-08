# AionU 项目总览资源

## 知识

- [AionU root README](../../../../open-ai-desktop/AionU/readme.md)
  产品定位、一句话卖点、用户可感知功能、社区入口与安装方式。适用于判断“这个项目想解决什么问题”。
- [AionU 中文 README](../../../../open-ai-desktop/AionU/docs/readme/readme_ch.md)
  中文版本的产品说明。适用于校对中文术语和用户侧功能名称。
- [Root package.json](../../../../open-ai-desktop/AionU/package.json)
  monorepo workspace、脚本、依赖、Node 版本、aioncore 版本和构建命令。适用于技术栈与部署方式分析。
- [Desktop package.json](../../../../open-ai-desktop/AionU/packages/desktop/package.json)
  Electron 桌面包的工作区依赖与入口声明。适用于确认桌面包边界。
- [Electron main entry](../../../../open-ai-desktop/AionU/packages/desktop/src/index.ts)
  桌面启动、单实例锁、backend 生命周期、窗口创建、WebUI/resetpass 分支和退出清理的总入口。
- [Main process bootstrap](../../../../open-ai-desktop/AionU/packages/desktop/src/process/index.ts)
  主进程初始化边界，覆盖存储初始化、bridge 初始化和主进程 i18n。
- [Preload bridge](../../../../open-ai-desktop/AionU/packages/desktop/src/preload/main.ts)
  renderer 可见 API、同步启动状态读取和托盘事件转发。适用于解释 IPC 安全边界。
- [Renderer entry](../../../../open-ai-desktop/AionU/packages/desktop/src/renderer/main.tsx)
  React provider 栈、配置引导、运行时失败弹窗和根组件挂载。适用于解释 UI 启动链路。
- [WebHost package entry](../../../../open-ai-desktop/AionU/packages/web-host/src/index.ts)
  backend-launcher 与 static-server 的组合入口。适用于解释无 Electron 的 WebUI 运行形态。
- [WebCLI entry](../../../../open-ai-desktop/AionU/packages/web-cli/src/index.ts)
  `aionui-web` 命令、参数解析、独立 backend 启动、前端-only 降级和 resetpass 流程。
- [Docs README](../../../../open-ai-desktop/AionU/docs/README.md)
  文档导航与文档归档意图。适用于理解 docs 的读者分层。
- [AionU AGENTS.md](../../../../open-ai-desktop/AionU/AGENTS.md)
  架构边界、代码规范、UI/i18n/testing 约束和贡献流程。适用于解释设计约束。
- [File structure guide](../../../../open-ai-desktop/AionU/docs/contributing/file-structure.md)
  目录职责、三进程边界和命名规则。适用于 L0 顶层目录与后续 L1 模块拆分。
- [Development guide](../../../../open-ai-desktop/AionU/docs/contributing/development.md)
  本地开发、aioncore 前置条件、脚本、构建系统与技术栈说明。

## 智慧（社区）

- [AionUi GitHub repository](https://github.com/iOfficeAI/AionUi)
  适用于提交 issue、对照 release、追踪项目演进和验证本课程与上游代码是否一致。
- [AionUi Discord](https://discord.gg/2QAwJn7Egx)
  README 推荐的英文社区。适用于询问使用体验、部署问题和功能设计背景。
- [AionUi Twitter / X](https://twitter.com/AionUI)
  README 推荐的信息入口。适用于观察发布节奏和用户场景。

## 空白

- `docs/README.md` 和 `AGENTS.md` 都指向 `docs/architecture/overview.md`，但当前检出未包含该文件；L0 参考文档只能基于源码入口、贡献文档和 README 重建架构地图。
- 本次未读取独立 AionCore Rust 仓库；涉及 backend 内部数据模型、调度器和 Agent runtime 的结论仅能从 AionU 调用边界推断，后续深挖需要补充 AionCore 源码。
