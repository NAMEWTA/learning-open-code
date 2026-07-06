# 贡献指南

PM Skills Marketplace 由 [Paweł Huryn](https://www.productcompass.pm)（pawel@productcompass.pm）维护。欢迎贡献——无论是 Bug 修复、拼写错误还是新的 skill 创意。

## 如何贡献

- **Bug 和小型修复**——直接提交 PR。
- **新 skill、command 或较大变更**——请先提交 Issue，以便我们讨论方案。

## 规范

- 保持 PR 专注——每个 PR 一个变更。
- 遵循现有模式：skills 是名词（领域知识），commands 是动词（工作流）。
- 每个 skill 需要包含 `name` 和 `description` 的 frontmatter。每个 command 需要 `description` 和 `argument-hint`。
- Skill 的 `name` 必须与其目录名匹配。
- Commands 中禁止跨插件引用。仅以自然语言建议后续操作。
- 每位贡献者将公开列名。
- 提交前运行验证器：`python3 validate_plugins.py`

## 许可证

贡献即表示您同意您的贡献将基于 [MIT 许可证](LICENSE) 进行许可。
