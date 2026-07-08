# Main process 基础设施资源

## 知识

- `open-ai-desktop/AionU/packages/desktop/src/process/index.ts`
  本主题主来源。用于确认 `initializeProcess` 的导入副作用、显式初始化步骤和性能标记。
- `open-ai-desktop/AionU/packages/desktop/src/index.ts`
  Electron 总入口。用于判断 `initializeProcess` 与 backend 启动、窗口创建、WebUI/resetpass 分支的先后关系。
- `open-ai-desktop/AionU/packages/desktop/src/process/utils/initStorage.ts`
  存储与迁移前置条件的核心来源。用于理解目录创建、ConfigStorage/EnvStorage 拦截、助手目录、legacy SQLite 迁移和 `getSystemDir()`。
- `open-ai-desktop/AionU/packages/desktop/src/process/utils/initBridge.ts` 与 `open-ai-desktop/AionU/packages/desktop/src/process/bridge/index.ts`
  IPC bridge 注册入口。用于追踪 main process 暴露给 preload/renderer 的原生能力。
- `open-ai-desktop/AionU/packages/desktop/src/process/services/i18n/index.ts`
  main process i18n 初始化。用于理解为什么 i18n 被副作用导入，并在窗口/托盘语言刷新时复用。
- `open-ai-desktop/AionU/packages/desktop/src/process/backend/binaryResolver.ts`
  aioncore 二进制解析来源。用于判断 packaged 资源、系统 PATH 与诊断信息如何进入启动失败分类。
- `open-ai-desktop/AionU/tests/unit/bootstrap/` 与 `open-ai-desktop/AionU/tests/unit/process/`
  行为佐证。用于验证 backend 启动失败、数据库迁移、退出清理、日志、更新服务等边界。
- `teach/open-ai-desktop/AionU/00-overview/reference/00-overview.html`
  L0 总览锚点。用于保持本 L1 模块与 AionU 三进程、aioncore backend、WebHost 架构位置一致。

## 智慧（社区）

- [AionUi GitHub Issues](https://github.com/iOfficeAI/AionUi/issues)
  上游 issue 区适合验证启动失败、安装完整性、WebUI、自动更新等真实用户问题是否与本模块判断一致。

## 空白

- 当前仓库内未发现专门讲解 `process/` 基础设施设计决策的独立架构文档；本主题以源码、测试和 L0 总览为一手事实来源。
- 暂未收录外部 Electron 社区讨论作为本主题依据，避免把通用 Electron 经验误当成 AionU 的具体实现。
