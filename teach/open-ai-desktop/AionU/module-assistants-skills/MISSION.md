# 使命：Assistants、Skills 与 Tools 配置模块

## 为什么
学习者需要能快速判断 AionU 中“助手预设、技能导入、MCP 工具配置”分别在哪里落地，以及它们怎样通过 renderer 和 common adapter 接到 backend。掌握这条边界后，后续修改助手编辑器、技能市场、工具页或会话默认能力时，可以先定位正确层级，再决定应该改 UI 状态、adapter 接口还是 backend 契约。

## 成功的样子
- 能画出 `/assistants`、`/settings/skills`、`/settings/tools` 三条入口到 `ipcBridge` 的调用路径。
- 能区分 assistant profile、rules、defaults、skills、mcps 分别由哪些请求保存。
- 能从 reference 表中找到 assistants、skills、mcp 三组接口及典型调用示例。
- 能识别当前测试覆盖集中在 Skills Hub，助手编辑器与 Tools MCP 页仍需要补充更直接的 E2E 证据。

## 约束条件
- 本轮是 L1 模块总览，只生成一节 15 分钟短课；长表格、接口清单和测试证据放入 reference。
- 只写入 `teach/open-ai-desktop/AionU/module-assistants-skills/`，不更新项目进度台账或源项目。
- 内容以当前源码快照为准；`docs/prds/assistants/README.md` 当前为空，不能作为事实依据。

## 不在范围内
- 不深入讲 aioncore backend 如何实现 `/api/assistants`、`/api/skills`、`/api/mcp`。
- 不覆盖会话运行时如何消费已启用的 skills 或 MCP 工具。
- 不重写 UI 组件或补测试，只做 L1 教学文档。
