# Issue tracker 集成仅限于主流工具

`setup-matt-pocock-skills` 仅为**主流** issue tracker 提供一流支持。添加对小众、新型或单供应商实验性 tracker 的支持请求不在范围内。

## 为什么不在范围内

每个 issue-tracker 后端都会将 CLI 形态硬编码到 skill 中（命令、标志、输出解析）。每个新后端都是永久的维护负担——它必须随着工具的 CLI 演进继续工作，并且必须持续接受 `/to-spec`、`/to-tickets`、`/triage` 等的测试。只有对相当比例用户实际使用的 tracker 才值得付出这一成本。

"主流"是一个判断标准，而非数字门槛：

- GitHub、GitLab 和 Backlog.md 是我们认为的主流工具——广为人知、广泛使用、早已过了实验阶段。
- 一个只有几百个 GitHub star 的全新 agent 聚焦工具则不是，无论其设计多有趣。

Star 数、年龄和下载量在做出判断时是有用的信号，但它们都不是规则。规则是：一个典型的工程师是否能认出这个工具，并且可能已经为他们的团队选择了它？

对于非主流 tracker，已经存在逃生通道：

- `local markdown` 用于轻量级仓库内追踪。
- `other/custom` 用于想要自己接线的用户。

两者都不需要核心 skill 了解特定工具。

## 先前的请求

- #99 — "添加 dex 作为 issue tracker 后端"（dex 在请求时约 3 个月大、约 300 star）
