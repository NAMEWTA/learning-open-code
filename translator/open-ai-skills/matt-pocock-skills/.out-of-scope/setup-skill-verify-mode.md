# `setup-matt-pocock-skills` 的验证/检查模式

本项目不会为 `setup-matt-pocock-skills` 添加专用的验证/检查模式（或单独的验证 skill）。

## 为什么不在范围内

第二个 skill——或 `--verify` 标志——用于检查 `docs/agents/*.md` 产物是否仍与种子模板模式匹配，会重复现有 setup skill 已在对话中处理的工作。

预期的工作流是：**运行 `/setup-matt-pocock-skills` 并告诉它验证您当前的设置。** 该 skill 是提示词驱动的，因此维护者可以将其范围限定为验证检查（"不要重写任何内容，只需根据当前种子模板检查我的现有文件并报告偏差"），而无需单独的代码路径。添加标志或同级 skill 会拆分一个已可通过自然语言入口点表达的功能的表面积。

将配置管理保持为单一 skill 也避免了当种子模板演进时两个 skill 相互偏差的维护成本。

## 先前的请求

- #106 — 功能请求：setup-matt-pocock-skills 的验证/检查模式
