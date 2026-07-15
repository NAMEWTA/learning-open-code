快速开始：

```bash
npx skills add mattpocock/skills --skill=code-review
```

```bash
npx skills update code-review
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/code-review)

## 功能说明

`code-review` 审查 `HEAD` 与你提供的一个固定参照点（commit、分支、tag 或 merge-base）之间的 diff，沿两个独立维度展开：**标准**（Standards——代码是否遵循此仓库文档化的约定？）和**规格**（Spec——代码是否实现了原始 issue 或规格说明所要求的内容？）。每个维度以独立的并行子 Agent 运行，并排呈现报告。它从不合并或重新排序两套发现——保持它们分离正是核心要点，因为一个变更可能在一方通过而在另一方失败，单一的混合裁决会让其中一方掩盖另一方。

## 何时使用

输入 `/code-review`，或者当你要求审查某个分支、PR、进行中的变更或"自 X 以来的任何内容"时，Agent 会自动调用它。

当存在一个 diff 需要对照已知良好参照点来评判，并且你希望两个问题——*代码写得对不对？*和*做的是不是该做的事？*——获得独立回答时使用此 skill。它在构建循环的末尾运行；对于实际以测试驱动方式编写代码，使用 [tdd](https://aihero.dev/skills-tdd)；对于将完整规格说明转化为代码，使用 [implement](https://aihero.dev/skills-implement)，它会在提交前运行自己的 `/code-review` 检查。

## 前置条件

**Spec** 维度需要找到原始规格说明——commit message 中对 issue 的引用、你传入的路径，或 `docs/`/`specs/` 下的规格说明文件。与 issue 追踪器的连接配置来自 [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills)；没有规格说明时，Spec 维度会直接跳过并说明情况。**Standards** 维度无需任何设置——即使在一个没有文档化约定的仓库中，它始终带有内置的 Fowler 代码坏味道基线。

## 两个维度，永不合一

核心理念是**两个维度**。**Standards** 询问 diff 是否符合此仓库的编码方式——其 `CODING_STANDARDS.md` 或 `CONTRIBUTING.md`，外加约 12 种 Fowler 代码坏味道的固定基线（神秘命名、重复代码、依恋情结、数据泥团等）。两条规则保护基线的安全性：文档化的仓库标准始终优先于基线，且每个坏味道都是判断性评估，绝非硬性违规。**Spec** 询问正交的问题——代码是否真正做了 issue 或规格说明所要求的事，既没有遗漏需求，也没有夹带范围蔓延？

它们以并行子 Agent 运行，互不污染对方的上下文，最终报告在独立的 `## Standards` 和 `## Spec` 标题下呈现，附带每个维度的摘要。刻意设计为不存在跨维度的单一赢家。

## 有效的标志

- 它首先定位并确认固定参照点（`git rev-parse`），在引用无效或 diff 为空时快速失败，而非在子 Agent 内部才报错。
- Standards 和 Spec 的发现结果以两个不同的区块呈现，每块引用其来源——仓库标准或基线坏味道适用于前者，引用的规格说明行适用于后者。
- 当找不到规格说明时，Spec 维度报告"无可用规格说明"，而非凭空捏造需求。

## 在系统中的位置

`code-review` 是主构建链末端的审查步骤：

```txt
grill-with-docs → to-spec → to-tickets → implement → code-review
```

它的最近邻是 [implement](https://aihero.dev/skills-implement)，后者驱动构建过程并在提交前调用此 skill 作为自己的审查环节；上游方面，它所对照的规格说明由 [to-spec](https://aihero.dev/skills-to-spec) 和 [to-tickets](https://aihero.dev/skills-to-tickets) 产出。当你不确定该用哪个 skill 或流程时，[ask-matt](https://aihero.dev/skills-ask-matt) 为你导航。
