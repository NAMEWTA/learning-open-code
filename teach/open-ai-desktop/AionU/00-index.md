# AionU · 架构教学 Wiki

> 整体进度：28/28 goals · 100% · 已执行 9 轮
> 最后更新：2026-07-07

---

## 进度面板

| 层级 | 完成 | 总数 | 进度 |
|------|------|------|------|
| L0 项目总览 | 1 | 1 | ██████████ |
| L1 模块总览 | 14 | 14 | ██████████ |
| L2 垂直切片 | 8 | 8 | ██████████ |
| L3 微观 API | 0 | 0 | 待差集扫描 |
| L4 深度剖析 | 5 | 5 | ██████████ |

---

## L0 · 项目总览

- [项目导览短课](00-overview/lessons/0001-project-map.html)
- [AionU 项目总览参考](00-overview/reference/00-overview.html)

## L1 · 模块总览

| 模块 | 短课 | 参考 |
|------|------|------|
| Electron 主入口与生命周期 | [短课](module-main-entry/lessons/0001-main-entry-module-tour.html) | [参考](module-main-entry/reference/main-entry-overview.html) |
| Main process 基础设施 | [短课](module-process-infra/lessons/0001-process-infra-module-tour.html) | [参考](module-process-infra/reference/process-infra-overview.html) |
| Preload 与 IPC 安全边界 | [短课](module-preload-ipc/lessons/0001-preload-ipc-module-tour.html) | [参考](module-preload-ipc/reference/preload-ipc-overview.html) |
| Renderer 核心与 UI Shell | [短课](module-renderer-core/lessons/0001-renderer-core-module-tour.html) | [参考](module-renderer-core/reference/renderer-core-overview.html) |
| Common adapter 调用适配层 | [短课](module-common-adapter/lessons/0001-common-adapter-module-tour.html) | [参考](module-common-adapter/reference/common-adapter-overview.html) |
| Web 运行时与 CLI | [短课](module-web-runtime/lessons/0001-web-runtime-module-tour.html) | [参考](module-web-runtime/reference/web-runtime-overview.html) |
| 移动端应用 | [短课](module-mobile-app/lessons/0001-mobile-app-module-tour.html) | [主题目录](module-mobile-app/) |
| Conversation runtime | [短课](module-conversation-runtime/lessons/0001-conversation-runtime-module-tour.html) | [参考](module-conversation-runtime/reference/conversation-runtime-overview.html) |
| Team Mode 多 Agent 协作 | [短课](module-team-mode/lessons/0001-team-mode-module-tour.html) | [参考](module-team-mode/reference/team-mode-overview.html) |
| Cron 自动化 | [短课](module-cron/lessons/0001-cron-module-tour.html) | [参考](module-cron/reference/cron-overview.html) |
| Assistants、Skills 与 Tools 设置 | [短课](module-assistants-skills/lessons/0001-assistants-skills-module-tour.html) | [参考](module-assistants-skills/reference/assistants-skills-overview.html) |
| 构建、发布与资源准备 | [短课](module-build-release/lessons/0001-build-release-module-tour.html) | [参考](module-build-release/reference/build-release-overview.html) |
| 测试体系与质量闸门 | [短课](module-test-quality/lessons/0001-test-quality-module-tour.html) | [参考](module-test-quality/reference/test-quality-overview.html) |
| 文档、示例与资源体系 | [短课](module-docs-resources/lessons/0001-docs-resources-module-tour.html) | [参考](module-docs-resources/reference/docs-resources-overview.html) |

## L2 · 垂直切片

| 切片 | 课程 | 参考 | 关联模块 |
|------|------|------|----------|
| 桌面启动到首屏全链路 | [链路地图](slice-desktop-startup/lessons/0001-flow-map.html)、[main 到窗口](slice-desktop-startup/lessons/0002-main-process-window.html)、[renderer 首屏](slice-desktop-startup/lessons/0003-renderer-first-screen-and-boundary.html) | [参考](slice-desktop-startup/reference/desktop-startup-flow-map.html) | main-entry、process-infra、renderer-core |
| WebUI 启动与远程访问全链路 | [链路地图](slice-webui-remote/lessons/0001-flow-map.html) | [参考](slice-webui-remote/reference/webui-remote-flow-map.html) | web-runtime、main-entry、docs-resources |
| 发送会话消息全链路 | [链路地图](slice-conversation-send/lessons/0001-flow-map.html)、[AionRS 主路径](slice-conversation-send/lessons/0002-aionrs-main-path.html)、[ACP 失败边界](slice-conversation-send/lessons/0003-acp-error-path.html) | [参考](slice-conversation-send/reference/conversation-send-flow-map.html) | conversation-runtime、common-adapter |
| 工具调用确认全链路 | [链路地图](slice-tool-permission/lessons/0001-flow-map.html) | [参考](slice-tool-permission/reference/tool-permission-flow-map.html) | conversation-runtime、preload-ipc、common-adapter |
| Team 创建并运行全链路 | [链路地图](slice-team-run/lessons/0001-flow-map.html) | [参考](slice-team-run/reference/team-run-flow-map.html) | team-mode、common-adapter、conversation-runtime |
| Cron 任务创建与触发全链路 | [链路地图](slice-cron-trigger/lessons/0001-flow-map.html)、[创建与编辑](slice-cron-trigger/lessons/0002-create-edit-path.html)、[run-now](slice-cron-trigger/lessons/0003-run-now-refresh.html)、[AI 与测试边界](slice-cron-trigger/lessons/0004-ai-local-cron-and-tests.html) | [参考](slice-cron-trigger/reference/cron-trigger-flow-map.html) | cron、conversation-runtime、common-adapter |
| 助手或 Skill 导入全链路 | [链路地图](slice-skill-import/lessons/0001-flow-map.html) | [参考](slice-skill-import/reference/skill-import-flow-map.html) | assistants-skills、common-adapter、test-quality |
| Backend 启动失败恢复全链路 | [链路地图](slice-backend-recovery/lessons/0001-flow-map.html) | [参考](slice-backend-recovery/reference/backend-recovery-flow-map.html) | main-entry、process-infra、preload-ipc、renderer-core |

## L4 · 深度剖析

| 主题 | 课程 | 参考 | 关联模块 |
|------|------|------|----------|
| Backend lifecycle 与 SQLite 竞争规避 | [问题框架](deep-dive-backend-lifecycle/lessons/0001-problem-frame.html) | [参考](deep-dive-backend-lifecycle/reference/backend-lifecycle-notes.html) | web-runtime、process-infra |
| REST/WS adapter 替代传统 IPC 的设计 | [问题框架](deep-dive-adapter-rest-ws/lessons/0001-problem-frame.html)、[provider-like invoke](deep-dive-adapter-rest-ws/lessons/0002-provider-like-invoke.html)、[错误与 E2E](deep-dive-adapter-rest-ws/lessons/0003-error-events-e2e.html) | [参考](deep-dive-adapter-rest-ws/reference/adapter-rest-ws-notes.html) | common-adapter |
| Team Mode 事件模型 | [问题框架](deep-dive-team-event-model/lessons/0001-problem-frame.html)、[核心机制](deep-dive-team-event-model/lessons/0002-core-mechanism.html)、[reconcile 与测试](deep-dive-team-event-model/lessons/0003-reconcile-and-tests.html) | [参考](deep-dive-team-event-model/reference/team-event-model-notes.html) | team-mode |
| electron-builder 资源裁剪与发布资源校验 | [问题框架](deep-dive-release-resource-trim/lessons/0001-problem-frame.html)、[bundled-aioncore](deep-dive-release-resource-trim/lessons/0002-core-mechanism.html)、[脚本与测试](deep-dive-release-resource-trim/lessons/0003-verification-and-tests.html) | [参考](deep-dive-release-resource-trim/reference/release-resource-trim-notes.html) | build-release |
| Skills / Assistants / MCP 映射设计 | [问题框架](deep-dive-skills-assistants-mcp/lessons/0001-problem-frame.html)、[核心机制](deep-dive-skills-assistants-mcp/lessons/0002-core-mechanism.html)、[验证与测试](deep-dive-skills-assistants-mcp/lessons/0003-verification-and-tests.html) | [参考](deep-dive-skills-assistants-mcp/reference/skills-assistants-mcp-notes.html) | assistants-skills、common-adapter |

## 待处理

- 无
