# 教学笔记：Skills / Assistants / MCP 映射设计

- 用户要求生成 AionU 最后一个 L4 深度剖析主题，写入范围严格限定在 `teach/open-ai-desktop/AionU/deep-dive-skills-assistants-mcp/`。
- 不修改源项目 `open-ai-desktop/AionU/`，不修改 `_progress.json`、`_progress.md`、`00-index.md`、`index.md`。
- 文档语言使用简体中文；代码标识符、源码路径和 API 名称保留英文。
- 关键教学边界：Assistant 是角色和默认能力定义；Skill 是可注入提示/能力单元；MCP 是工具服务器配置和连接状态；会话创建时会把选择解析成 snapshot。
- `docs/prds/assistants/README.md` 为空，不能作为设计论据，只能作为“PRD 空白”记录。
