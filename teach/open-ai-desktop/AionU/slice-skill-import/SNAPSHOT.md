# 课程快照：助手或 Skill 导入全链路

## 源项目信息
- **源仓库**：`open-ai-desktop/AionU`
  - **Git Commit**：`0ea13fd0136294ab7ff30215b580b0fc028c6f56`
  - **短 Commit**：`0ea13fd01`
  - **分支**：`main`
- **快照时间**：2026-07-07T19:32:29+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `packages/desktop/src/renderer/pages/settings/SkillsHubSettings.tsx` | Skills Hub 手动导入、导入结果提示、导入后刷新主链路 | 核心 |
| `packages/desktop/src/renderer/pages/settings/skillImportMessages.ts` | Skill 导入错误码、部分成功、全失败与大小限制文案 | 核心 |
| `packages/desktop/src/renderer/components/base/TalkToButlerButton.tsx` | Add Skill 下拉入口和手动导入回调触发点 | 核心 |
| `packages/desktop/src/renderer/pages/settings/AssistantSettings/index.tsx` | AssistantSettings 入口、hooks 装配和编辑器 view model | 核心 |
| `packages/desktop/src/renderer/pages/settings/AssistantSettings/AssistantEditorPage.tsx` | assistant 编辑页保存按钮到 actions.save 的 UI 入口 | 辅助 |
| `packages/desktop/src/renderer/pages/settings/AssistantSettings/AssistantEditorSections.tsx` | 默认 skill 选项派生、自动注入 skill 合并与选择变更 | 核心 |
| `packages/desktop/src/renderer/pages/settings/AssistantSettings/editor/DefaultsSection.tsx` | Default Skills 多选控件与跳转 Skills Hub 的按钮 | 核心 |
| `packages/desktop/src/renderer/pages/settings/AssistantSettings/SkillConfirmModals.tsx` | pending skill 删除和 assistant 内移除 custom skill 的边界弹窗 | 辅助 |
| `packages/desktop/src/renderer/pages/settings/AssistantSettings/types.ts` | SkillInfo、PendingSkill、AssistantEditorViewModel 契约 | 辅助 |
| `packages/desktop/src/renderer/hooks/assistant/useAssistantList.ts` | assistant catalog 加载与排序状态刷新 | 辅助 |
| `packages/desktop/src/renderer/hooks/assistant/useAssistantEditor.ts` | assistant 编辑状态机、pending skill 导入、create/update 和 cache 刷新 | 核心 |
| `packages/desktop/src/common/adapter/ipcBridge.ts` | `/api/skills/*` 与 `/api/assistants/*` 的 renderer adapter 映射 | 核心 |
| `packages/desktop/src/common/adapter/httpBridge.ts` | HTTP base URL、provider-like invoke 和结构化后端错误 | 辅助 |
| `tests/e2e/features/settings/skills/manual-import.e2e.ts` | mock dialog 后导入 skill，并断言 success message 与 custom source | 核心 |
| `tests/e2e/features/settings/skills/refresh-empty-tabs.e2e.ts` | 通过后端状态刷新验证 My Skills 列表变化 | 辅助 |
| `tests/e2e/features/settings/skills/edge-cases.e2e.ts` | highlight 不存在、无外部源等页面不崩溃边界 | 辅助 |
| `tests/e2e/features/settings/skills/special-cases.e2e.ts` | 特殊字符 skill 名和较大数量渲染边界 | 辅助 |
| `tests/e2e/specs/assistant-settings-skills.e2e.ts` | assistant 默认 skill 控件、只读态和保存后重开验证 | 核心 |
| `tests/e2e/helpers/skillsHub.ts` | Skills Hub E2E 的 HTTP helper、fixture 和后端状态断言 | 辅助 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| 01 | `lessons/0001-flow-map.html` | 从 Skills Hub 导入和 AssistantSettings 绑定默认 skill 的垂直切片短课 |

## 已生成参考文档

| 编号 | 参考文件 | 描述 |
|------|---------|------|
| 01 | `reference/skill-import-flow-map.html` | 源文件定位、分层图谱、Mermaid 时序、异常路径和 E2E 证据速查 |

## 快照摘要
- 课程数：1
- 参考文档数：1
- 引用源文件数：19
- 学习记录数：0
