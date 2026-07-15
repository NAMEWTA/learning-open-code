# 使命：Orca 开发规范、目录规范与命名规范

## 为什么
学习者在阅读 Orca 源码时，需要先掌握项目的编码规范体系，否则会因风格不一致而产生认知负担。理解 Orca 的 lint 规则、TypeScript 约定、目录组织方式和命名习惯后，阅读任何模块都能快速定位文件、理解类型声明、判断代码意图。

## 成功的样子
- 能说出 Orca 使用的 linter/formatter 工具链及其核心规则。
- 能根据目录规范快速判断一个功能应该放在 `src/main/`、`src/renderer/`、`src/shared/` 还是 `src/relay/`。
- 能识别不合规范的命名（如 `helpers.ts`、`interface` 关键字、缺少 `import type`）并知道正确写法。
- 能在自己的 Orca 贡献中遵循这些规范。

## 约束条件
- 单节课在 15 分钟内完成，细节规则分流到参考文档。
- 以当前子模块 commit `61bd98db6faacb8baffa0de369b187c0e40d662a` 为准。
- 规范来源于 `AGENTS.md`、`.oxlintrc.json`、`.oxfmtrc.json`、`tsconfig.json`、`CONTRIBUTING.md`、`STYLEGUIDE.md` 等权威文件。

## 不在范围内
- 不讲具体业务逻辑或功能实现。
- 不讲 CI/CD 流程细节（仅提及与规范相关的检查门禁）。
- 不讲 STYLEGUIDE.md 中的视觉设计规范（那是另一个主题）。
