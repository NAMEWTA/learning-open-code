# 编写文档页面

`engineering/` 和 `productivity/` 中的每个 skill 在 `docs/<bucket>/<skill-name>.md` 处有一个面向用户的**文档页面**——文档树镜像 `skills/` 下的这两个分类目录。发布地址为 `https://aihero.dev/skills-<skill-name>`；URL 始终为 `skills-<skill-name>`，无论属于哪个分类，因此文档路径仅用于仓库组织。页面不是 skill，也不是 `SKILL.md` 的副本。只有这两个分类是推广的；其余分类（`misc/`、`personal/`、`in-progress/`、`deprecated/`）不提供文档页面。

这些 skill 大多为**用户调用**：agent 永远不会为您触发它们，因此*您*是必须记住它们存在以及何时使用它们的索引。这种记忆是**认知负担**。文档页面的工作就是减轻它——围绕一个 skill 引导一位读者，使其能够理解、知道何时使用它，并了解它在系统中的位置。这些页面共同构成一个分布式路由器；每个页面是一个节点。

当推广 skill 被添加、重命名或行为变更时采取行动：创建或重新同步其文档页面。重命名也会移动文件（`docs/<bucket>/<old>.md` → `docs/<bucket>/<new>.md`），因为发布的 URL 跟踪名称；在 `engineering/` 和 `productivity/` 之间移动的 skill 将其文档文件移动到匹配的文件夹。`misc/`、`personal/`、`in-progress/` 和 `deprecated/` 中的 skill 没有页面——这些分类都不推广。从这些分类*移入* `engineering/` 或 `productivity/` 的 skill 获得页面；反向移动则失去页面。

由于这些页面发布在 `aihero.dev` 上，**每个链接都是绝对链接**——永远不要使用仓库相对路径。指向另一个 skill 的链接指向 `https://aihero.dev/skills-<name>`；指向仓库的链接指向其完整的 `https://github.com/mattpocock/skills/...` URL。在仓库中有效的相对链接一旦发布就会失效。

没有 H1——发布的页面从 slug 获取标题。

## 页面结构

填写以下模板。**固定框架**（Quickstart 块、源链接、`## What it does`、`## When to reach for it`、`## Where it fits`）出现在每个页面上。**可适应的中间部分**——`## Prerequisites` 和自由形式的内容章节——仅承载该特定 skill 所需的内容；删除其余部分。

<page-template>

Quickstart:

```bash
npx skills add mattpocock/skills --skill=<name>
```

```bash
npx skills update <name>
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/<bucket>/<name>)

## 功能说明

一到两段通俗语言。以 skill 的一句话职责开头，然后陈述**定义性约束**——使此 skill 行为不同于明显默认值的单一事实（对于 `to-spec`：它不会再次访谈用户，而是综合已知内容）。将其写为平实的陈述句——绝不要使用标记式的旁白，如"定义性约束："或"关键点："；公式读起来像填充词。这句话是页面上最有价值的内容；永远不要省略。

## 何时使用

如何以及何时使用此 skill——两个要点，两者基本上始终存在：

- **调用模式。** 说明是您输入还是 agent 触发。用户调用 skill："您通过输入 `/<name>` 来调用此 skill——agent 不会自行使用它。" 模型调用 skill："输入 `/<name>`，或当任务匹配时 agent 自动使用它。"
- **触发边界。** 索引条目："在以下情况使用此 skill……" 当 skill 容易与同类混淆时，添加另一半——"对于 <X>，请改用 [<sibling>](https://aihero.dev/skills-<sibling>)。"

## 前置条件

可选——仅当 skill 需要某些已就位的东西才能正常工作时包含；否则完全省略此标题。涵盖：**它写入的工作区**（有状态的 skill，如 `grill-with-docs` 写入 `CONTEXT.md` 和 ADR；`teach` 构建整个目录——说明写什么以及写在哪里）、**前置设置**（`triage`/`to-spec`/`to-tickets` 需要 `setup-matt-pocock-skills` 已配置 issue tracker）或**仓库特定工具**。无状态、可在任何地方运行的 skill 没有前置条件——删除此节。

## <自由形式的中间部分>

一到三个短节，使用 skill *自己的词汇*，使其易于理解——选择适合该 skill 的任何标题：它运行的循环、它生成的产物、它做出的分叉、它消除的反模式。没有规定的标题；skill 太异构了，无法统一。

唯一的硬性要求：**展示 skill 的主导词/定义性理念**——`tight` 反馈循环、`deep module`、一次性代码回答问题、红-绿。这有双重回报：读者了解 skill *是什么*，并学到他们以后*思考使用*时需要的关键词。

## 有效的标志

可选。一份简短、可检查的列表，包含告诉读者 skill 确实在正常工作的可观察信号——当它触发时应看到什么，以及缺少时表明未触发。当 skill 有清晰的指示时包含（例如，`to-spec` 写入而不重新访谈您；主导词在追踪中重新出现）；当信号模糊时省略标题。几条要点，仅此而已。

## 在系统中的位置

始终存在。用一两句话将 skill 置于系统中：

- **角色。** 命名它：**链式步骤**（`grill-with-docs → to-spec → to-tickets → implement → code-review`）、**一次性设置**（`setup-matt-pocock-skills`）、**定期维护**（`improve-codebase-architecture`，"每隔几天"）或**随时使用型独立 skill**（`diagnosing-bugs`、`prototype`、`handoff`）。独立 skill 的映射是一句诚实的话——远好于省略此节。
- **邻居。** 重要的一两个同类 skill，每个附带原因从句，使用绝对链接。
- **地图。** 指向 [ask-matt](https://aihero.dev/skills-ask-matt)，即整个集合的路由器，使此页面保持为节点而不必重新绘制整个图。

</page-template>

## 约定

- 解释**为什么**，而非过程。页面引导和定位 skill；从不复现 `SKILL.md` 的步骤或模板转储——选择工具的人不需要操作手册。
- 使用 skill 的**主导词**（*seam*、*deep module*、*tracer bullet*），使页面和 skill 使用同一语言。
- 保持页面本身低负担。它是关于*低认知负担 skill* 的文档；装饰性内容（多余的标题、重复的链接）正是它所反对的东西。

## 完成标准

- 页面存在于 `docs/<bucket>/<name>.md`，并且没有因重命名或分类移动而残留的过时页面。
- Quickstart 块和源链接命名了正确的分类和 skill；更新行命名了 skill。
- `## 功能说明` 以平实散文陈述定义性约束，而非标记式旁白。
- `## 何时使用` 陈述了调用模式和触发边界。
- `## 在系统中的位置` 命名了角色并链接到 `ask-matt`。
- 前置条件（工作区、前置设置、工具）在存在时被声明，不存在时该节被省略。
- 中间部分展示了主导词。
- 每个链接都是绝对链接，且每个链接都能解析。
