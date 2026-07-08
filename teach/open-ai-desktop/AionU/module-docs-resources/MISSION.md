# 使命：AionU docs/resources 模块总览

## 为什么
学习者需要把 AionU 的文档、示例、协作模板和静态资源看成一个模块来读，而不是把它们当成“源码之外的杂物”。掌握这个模块后，后续修改 README、WebUI 资源、扩展示例、安装器资源或 PRD 时，能先判断它会影响产品叙事、贡献者入口、扩展契约、Web 运行时还是发布包。

## 成功的样子
- 能区分 `docs/`、`examples/`、`.aionui/`、`resources/`、`public/` 的职责和边界。
- 能沿着一张 README 图片、一个 PWA 文件或一个 extension manifest 找到实际调用方。
- 能说出本模块与 `module-build-release`、`module-web-runtime`、`module-assistants-skills` 的交叉点。
- 能识别当前资料层的缺口，例如缺失的 architecture/specs/schema 目录和漂移的脚本文档。

## 约束条件
- 本主题是 teach-goal 批量生成模式，不等待额外交互；默认读者已完成 L0 项目总览。
- lesson 必须是 15 分钟短课；完整文件清单、接口表和风险表放入 reference。
- 本轮持久化产出只写入 `teach/open-ai-desktop/AionU/module-docs-resources/`。

## 不在范围内
- 不修改 `open-ai-desktop/AionU/` 源项目中的任何文档、资源或示例。
- 不重讲 WebHost/WebCLI、构建发布、助手技能的完整实现；这些分别由对应模块承接。
- 不深入 AionCore 后端内部协议，只记录 AionU 仓库中可见的资源与接口边界。
