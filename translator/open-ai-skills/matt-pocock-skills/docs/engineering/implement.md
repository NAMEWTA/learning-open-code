快速开始：

```bash
npx skills add mattpocock/skills --skill=implement
```

```bash
npx skills update implement
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/implement)

## 功能说明

`implement` 会构建 spec 或一组 ticket 中描述的工作 —— 通过测试驱动开发、类型检查以及完整的测试套件来推进，最后交给 review 并提交到当前分支。

它**不**决定要构建什么。spec 已经确定，切面也已达成共识；`implement` 负责执行这个计划，而不是重新讨论它。它是"手"而不是"脑"—— 思考在上游已经完成了。

## 何时使用

通过输入 `/implement` 来调用 —— Agent 不会自行触发它。

当工作已经写成了 spec 或拆成了 ticket，且你准备好将其转化为代码时，使用它。如果 spec 还不存在，先写 spec —— 可以使用 [to-spec](https://aihero.dev/skills-to-spec) ，或使用 [to-tickets](https://aihero.dev/skills-to-tickets) 将 spec 拆成 ticket。如果你只想以测试优先的方式构建某个功能，而不需要完整的 spec，直接使用 [tdd](https://aihero.dev/skills-tdd)。

## 预先约定的切面

`implement` 运行的核心思想是**切面（seam）**—— 在对功能进行测试时使用的稳定接口，在任何代码编写之前就已经选定。它不会在构建过程中随意发明切面；而是使用已经在 [to-spec](https://aihero.dev/skills-to-spec) 阶段选定的切面，并通过 [tdd](https://aihero.dev/skills-tdd) 针对这些切面编写测试。在预先约定的切面上工作，是保持实现诚实的关键：测试瞄准的是持久的东西，这样底层代码可以变动而测试无需改变。

围绕这个核心，它保持紧凑的循环 —— 频繁进行类型检查，在推进过程中运行单个测试文件，最后运行一次完整的测试套件 —— 然后以一轮 review 收尾并提交到当前分支。

## 在系统中的位置

`implement` 是主链末尾附近的构建步骤，位于 review 之前：

```txt
grill-with-docs → to-spec → to-tickets → implement → code-review
```

在工作已经被 spec 化并排好顺序之后再使用它，而不是在此之前。它的关键相邻 skill 是 [to-tickets](https://aihero.dev/skills-to-tickets) ，它生成 ticket —— 每个 ticket 声明了其阻塞边 —— 供 `implement` 逐步推进；以及 [tdd](https://aihero.dev/skills-tdd) ，`implement` 在内部驱动它来在每个切面上编写测试，然后运行自己的 [code-review](https://aihero.dev/skills-code-review) 并提交。当你拿不准哪个 skill 或流程合适时，[ask-matt](https://aihero.dev/skills-ask-matt) 会为你导航。
