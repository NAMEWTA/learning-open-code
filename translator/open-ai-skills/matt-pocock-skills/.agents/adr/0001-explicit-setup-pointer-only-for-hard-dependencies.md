# 仅为硬依赖显式指向 `/setup-matt-pocock-skills`

工程 skill 依赖由 `/setup-matt-pocock-skills` 生成的按仓库配置（issue tracker、分类标签词汇、领域文档布局）。某些 skill 在没有该配置的情况下无法正常工作——它们必须发布到特定的 issue tracker 或应用特定的标签字符串。其他 skill 仅将其用于增强输出（词汇、ADR 感知），并在没有时优雅降级。

我们将这些分为**硬依赖**和**软依赖** skill：

- **硬依赖**（`to-tickets`、`to-spec`、`triage`）——包含显式的单行说明：*"… should have been provided to you — run `/setup-matt-pocock-skills` if not."* 没有映射，输出是错误的，而不仅仅是模糊的。
- **软依赖**（`diagnose`、`tdd`、`improve-codebase-architecture`）——仅在模糊的散文中引用"项目的领域词汇表"和"您所触及区域的 ADR"。如果文档不存在，skill 仍然可以工作；输出只是不够精准。

这种划分使软依赖 skill 保持轻量，并避免将 setup 指针机械地复制到不必要的地方。
