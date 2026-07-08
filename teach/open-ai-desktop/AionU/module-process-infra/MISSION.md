# 使命：Main process 基础设施

## 为什么
用户需要能快速判断 AionU 启动问题、迁移问题、窗口/托盘/WebUI 问题分别落在 main process 的哪一层。掌握本主题后，用户可以从 `initializeProcess` 出发读懂主进程基础设施如何先铺好存储、IPC、i18n、诊断与 backend 启动前置条件，而不是在整个 `process/` 目录里迷路。

## 成功的样子
- 能解释 `initializeProcess` 在 Electron 总启动链中的位置，以及它为什么只显式等待 `initStorage()`。
- 能列出 `process/utils`、`process/services`、`process/backend` 与相邻 `process/startup` 的职责边界。
- 能从一个启动或迁移现象反推应先阅读的源码文件和测试文件。

## 约束条件
- 本 goal 是 L1 模块总览，只生成一节 15 分钟短课和一份完整参考清单。
- lesson 聚焦 `initializeProcess` 如何串起基础设施；长表格、完整入口清单和测试索引放入 reference。
- 所有持久化产物只写入 `teach/open-ai-desktop/AionU/module-process-infra/`。

## 不在范围内
- 不展开 renderer 业务状态、React Provider 栈或 conversation/team 业务流。
- 不把 preload 与 IPC 安全边界写成完整课程；该内容属于 `module-preload-ipc`。
- 不深挖 aioncore 内部 Rust 实现，只讲 main process 如何解析、启动与诊断 backend。
