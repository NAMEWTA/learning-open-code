# mattpocock-skills

## 1.1.0

### 次要变更

- [#406](https://github.com/mattpocock/skills/pull/406) [`930a450`](https://github.com/mattpocock/skills/commit/930a450089f77a49af09001d955db8452a4b867d) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 将 **`ask-matt`** 路由器更新至与完整 skill 集合同步。现在它映射了之前缺失的五个 skill：**`tdd`**（作为 `implement` 驱动的红-绿引擎融入主流程）、**`diagnosing-bugs`**（一个新的"出了点问题"入口——此前没有针对 bug 的路由）、**`domain-modeling`** 和 **`codebase-design`**（一个新的"底层词汇"部分），以及 **`grilling`**（共享的访谈原语）。`prototype` 被充实为独立 skill，其描述也从"用户调用的 skill"扩展为"这些 skill"。在 `CLAUDE.md` 中添加了一条维护规则，确保未来任何 skill 的新增/重命名/删除或流程变更都会触发 `ask-matt` 的重新检查，与已有的文档页重新同步规则并列。

- [#464](https://github.com/mattpocock/skills/pull/464) [`639df6e`](https://github.com/mattpocock/skills/commit/639df6e7386dfddc739b2aecdeff37a876f2483b) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 提升并强化 **`code-review`**。正在开发中的 **`review`** skill 重命名为 **`code-review`**，并从 `in-progress/` 移至 `engineering/`：现在随插件一起发布，在顶级 README 和 Engineering README 中列出（模型调用），并在 `docs/engineering/code-review.md` 拥有文档页。`/implement` skill 和文档指向 `/code-review`。

  此外，它在 Standards 轴上获得了始终启用的 **Fowler 坏味道基线**——精选约 12 个高信号的"代码坏味道"（神秘命名、重复代码、依恋情结、数据泥团、基本类型偏执、重复的 switch、霰弹式修改、发散式变化、夸夸其谈未来性、消息链、中间人、被拒绝的遗赠），内联到 `SKILL.md` 中，作为与仓库自身文档并列的固定基线，而非新增的第三个轴。两条约束规则保证其安全性：文档化的仓库标准覆盖基线，且每个坏味道以判断性意见报告，从不当成硬性违规。

- [#464](https://github.com/mattpocock/skills/pull/464) [`639df6e`](https://github.com/mattpocock/skills/commit/639df6e7386dfddc739b2aecdeff37a876f2483b) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 在两个方面打磨 **`grilling`**。

  **确认关卡。** Agent 在确认与用户达成共同理解之前不会执行计划——将 skill 现有的"共同理解"完成标准转变为显式的停止关卡。`description` 也利用预训练的 **`grill`** 引导词（"无情地盘问用户"）来增强调用精准度，文档页已重新同步。

  **事实 vs. 决策。** Grilling 现在区分 _事实_（自行查找——探索代码库）和 _决策_（逐条提交给人类并等待其回答）。旧有的笼统说法——"如果某个问题可以通过探索代码库来回答，那就探索代码库"——是为真人场景编写的，但一旦另一个 skill 在解决问题工单的框架内运行 grilling，它就可能被解读为也允许自主回答 _决策_ 类问题。将两者分开可以防止 grilling agent 抢跑并自问自答。

- [#463](https://github.com/mattpocock/skills/pull/463) [`af6d692`](https://github.com/mattpocock/skills/commit/af6d6922c3e2b5288eef155346cbe319e4ed3bd0) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 为 **`writing-great-skills`** 添加两个相邻的 Steering 失败模式，两者都关于你认为是"无关"的语言仍然会引导 agent。**否定（Negation）**——_大象效应_——是通过禁止来引导：命名 _不要做什么_ 会将禁止的行为拖入上下文，使其 _更_ 容易被触发，而非更少（_不要想大象_），因此解决方法是提示 **正面** 行为。**负空间（Negative Space）**——虚空——是对你 _遗漏_ 的内容所产生引导作用的盲区：skill 放弃的每一个决定都被委托给 agent 的先验知识，而非保持中性，因此解决方法是用心阅读草稿中的沉默之处，并有意地处理每一个遗漏（填补它，或将其保留为真正的 **分支**）。保持两条独立条目而非合二为一——因为它们有不同的诊断方法和不同的解决之道——每条都是一个完整的 `GLOSSARY.md` 条目加上一个 `SKILL.md` 失败模式要点，与其他所有失败模式的承载方式一致。

- [`850873c`](https://github.com/mattpocock/skills/commit/850873cd73d5f81826ebf512ad35d2b1e113001f) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 将 **`prototype`** skill 设为模型可调用，这样 agent 可以自主调用它（其他 skill 也可以）。其描述围绕引导词 _prototype_ 重写——用于回答设计问题的一次性代码——每个分支对应一个触发条件（状态/逻辑健全性检查，或 UI 探索）。

- [#409](https://github.com/mattpocock/skills/pull/409) [`0d74d01`](https://github.com/mattpocock/skills/commit/0d74d01cbc64ca27778a49b38599f70c534e76a0) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 新增 **`research`** skill——一个小型、模型可调用的 skill，启动一个 **后台 agent** 针对 **一手来源**（官方文档、源代码、规范、第一方 API）调查某个问题，然后将一份带有引用的 Markdown 文件留在仓库存放此类笔记的位置。这是一种可委托的阅读跑腿工作：你继续工作而它在阅读，最后拿回一份可供 grilling、规划或设计的文档。在顶级 README 和 Engineering README 中列出（模型调用），添加到 `.claude-plugin/plugin.json`，在 `docs/engineering/research.md` 拥有文档页，并在 `ask-matt` 中作为独立 skill 路由。

- [#469](https://github.com/mattpocock/skills/pull/469) [`a0329ba`](https://github.com/mattpocock/skills/commit/a0329ba95751f58566ed7ab484475917a68f1629) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 将 **`to-issues`** skill 拆分为精简的 **Process** 和 **Reference** 两部分，并教会它处理 **大规模重构**——一个单一的机械性变更（如重命名一个列），其 **爆炸半径** 遍及整个代码库，一次性破坏数千个调用点，导致没有任何垂直切片能绿色通过。起草步骤现在指向两个并列的参考块：**垂直切片规则** 用于普通的示踪子弹，以及 **大规模重构**，它通过 **扩展-收缩**（在旧形式旁边扩展新形式，按爆炸半径分批迁移调用点，然后收缩移除旧形式）来切片变更，使 CI 在每个批次之间保持绿色——或者当无法保持时，仅在最后的集成验证工单中才变红。工单正文模板也移入了 Reference。

- [#464](https://github.com/mattpocock/skills/pull/464) [`386d4ff`](https://github.com/mattpocock/skills/commit/386d4ff719a7c420ad1454232d0436b01f1b8c17) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 统一规划类 skill。**`to-prd` 重命名为 `to-spec`**——"spec" 现在是贯穿始终的单一术语（为了可发现性，它仍然以"你可能将这份文档称为 PRD"开头）。**`to-plan` 和 `to-issues` 合并为一个 `to-tickets` skill，`to-issues` 已删除。**

  `to-tickets` 将计划、spec 或对话分解为一组 **工单（tickets）**——示踪子弹式的垂直切片，每个声明其 **阻塞边（blocking edges）**。同一产物根据 `/setup-matt-pocock-skills` 配置的追踪器有两种解读方式：**本地文件**（`tickets.md`）将边写为文本，你按顺序从上到下手工推进；**真正的追踪器**将其写为原生阻塞链接，因此任何阻塞项已完成的工单都处于前沿，多个 agent 可以同时运行。边的信息无论哪种方式都存放在工单中——媒介只决定是否有东西能并行执行它们。

  发布时优先使用追踪器的 **原生子工单** 来表示父工单 → 切片，优先使用 **原生阻塞边** 来表示 `Blocked by`（在追踪器支持的情况下），将 `## Parent` / `## Blocked by` 正文部分作为回退方案。"What to build" 模板指向 `/prototype` 代码所在位置，而非内联其代码片段。

  `ask-matt` 的主流程现在路由为 `idea → /to-spec → /to-tickets → /implement`，并在 `docs/engineering/to-spec.md` 和 `docs/engineering/to-tickets.md` 提供了面向用户的文档页。

- [#464](https://github.com/mattpocock/skills/pull/464) [`0557d57`](https://github.com/mattpocock/skills/commit/0557d57579d9b3d39839fdaf8d4a6542b17539ce) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 将 wayfinder 在文档中的定位确定为 **情境入口**，而非新的主入口流程——以 grilling 为主导的 _idea → ship_ 链路仍然是正门（将 wayfinder 加冕为默认主干是 v2 级别的大动作，而非 1.1 的范畴）。**`ask-matt`** 路由器现在明确了 wayfinder 的具体触发条件——绿地项目或大型功能构建，规模超出单次会话——而两个 grilling 正门（**`grill-me`**、**`grill-with-docs`**）会向上指引到 wayfinder，用于那些超出单次会话处理能力的任务，确保入口从读者实际开始的地方可被发现。

- [#464](https://github.com/mattpocock/skills/pull/464) [`639df6e`](https://github.com/mattpocock/skills/commit/639df6e7386dfddc739b2aecdeff37a876f2483b) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 毕业并重塑 **`wayfinder`**——用于规划超大规模工作（超出单次 agent 会话承载能力）的 skill。它从 `in-progress/` 移至 `engineering/`（插件条目、顶级 + Engineering README 中归类为 **用户调用**、在 `docs/engineering/wayfinder.md` 拥有文档页、并在 `ask-matt` 中有路由），作为一个成熟的 skill 落地。使其达成的重命名与重塑如下：

  - **`decision-mapping` 重命名为 `wayfinder`**，以 `/wayfinder` 调用。"决策地图"既晦涩又不准确——只有一种工单类型是真正的决策。重塑后改为在迷雾般的问题中绘制路线，提供一个连贯的引导词框架——**战争迷雾（fog of war）**、**前沿（frontier）**、**地图（the map）**——而非在其上叠加一个生造术语。
  - **目的地作为引导词。** Wayfinding 找到的是通往目的地的 _路径_；它不负责建造。命名目的地是绘图的第一个动作——它固定范围并塑造每个工单——因此地图获得了一个 `## Destination` 字段，每次会话都围绕它展开，且分类定级在创建任何工单之前就将其确定。
  - **规划，而非执行。** 地图产出的是 **决策，而非交付物**；当在有人动手建造之前不再有任何待决事项时，地图即告完成。某项工作可以在其 Notes 中覆盖此规则。
  - **地图是索引，而非存储。** 一个决策只存在一个地方——其工单中——因此地图只做摘要和链接，从不重述；将迷雾中的条目毕业为工单后，已毕业的区域会被清除，不留任何内容在两个地方。
  - **默认协作。** 地图从本地 Markdown 文件迁移到仓库的工单追踪器：一个单一的 `wayfinder:map` 工单，其工单作为其子工单——一个团队可以共同关注的共享 URL。会话以低分辨率加载地图，按需放大到具体工单。Wayfinder 保持追踪器无关性（GitHub、GitLab、local-markdown），通过 `docs/agents/issue-tracker.md` 中的指针实现，`setup-matt-pocock-skills` 会 seed "Wayfinding operations" 部分。
  - **通过分配认领，而非标签。** 会话通过将工单分配给负责的开发者来认领——分配者 _就是_ 认领——释放标签词汇空间，仅供 `wayfinder:<type>` 使用。
  - **原生阻塞。** 阻塞优先使用追踪器的原生依赖关系，在追踪器自身的 UI 中可视化呈现前沿，使人类无需打开地图就能看到哪些可以接取。GitHub 和 GitLab 模板详细说明了原生方案，并提供正文约定的回退方案。
  - **迷雾 vs. 超出范围，分开。** 两个命名清晰的地图部分——`## Not yet specified`（范围内的迷雾，随着前沿推进而毕业）和 `## Out of scope`（被判定为超出目的地的工作，已关闭，永不毕业）——使超出目的地的工作不再被误读为可接取的前沿。
  - **第四种 `task` 工单类型。** 用于阻塞决策的字面意义上的人工操作（配置访问权限、迁移数据、注册服务）——唯一一种 _去做_ 而非决策的类型，其存在价值在于解除决策的阻塞。
  - **HITL / AFK 工单分类。** 每种工单类型要么是 **HITL**（human in the loop——grilling、prototype），要么是 **AFK**（agent alone——research；task 可以是两者之一）。HITL 工单只能通过实时交互来完成，因此"等待人类"这个信息自然从标签中浮现——一个自问自答的 grilling agent 从定义上就违反了 HITL。（这修复了学员报告的 `/wayfinder` 对自己进行 grilling 而非对人类进行 grilling 的问题。）
  - **无迷雾提前退出恢复。** 如果开场的广度优先 grilling 没有浮现任何迷雾，意味着这次旅程足够小，可以在单次会话中完成——因此它会停止并询问你希望如何继续，而非构建一张没人需要的地图。

### 补丁变更

- [#464](https://github.com/mattpocock/skills/pull/464) [`639df6e`](https://github.com/mattpocock/skills/commit/639df6e7386dfddc739b2aecdeff37a876f2483b) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 将 **`tdd`** 重塑为纯参考 skill，并补充一个缺失的反模式。

  **纯参考。** 红 → 绿 → 重构循环由模型已掌握的引导词锚定，因此逐步的 Workflow 大部分是在重述循环。删除了 Workflow 和每次循环的检查清单；将其中唯一持久的思想——垂直切片 / 示踪子弹——融入反模式部分和一个简短的循环规则列表。引入 **seam** 作为测试位置的引导词：仅在预先约定的 seam 处测试，在编写任何测试之前与用户确认。同时删除了重构阶段——TDD 现在是红 → 绿；重构属于 review 阶段，因此重构规则和 `refactoring.md` 已移出（其归属地是 `code-review`）。

  **同义反复测试。** 添加了同义反复测试（tautological-test）反模式：一个以与代码相同计算方式重新计算断言值的测试，在构造上就必然通过，提供零信心——这与已覆盖的实现耦合反模式有所区别。在相同位置作为并列项添加：一条 Philosophy 原则（期望值必须来自独立的真实来源）、一个检查清单关卡，以及 `tests.md` 中的一对 BAD/GOOD 示例。

- [`e00eadb`](https://github.com/mattpocock/skills/commit/e00eadb4bb32c3d5a631ead1a5ed5d6a7c5f74e2) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 扩展 **`triage`** skill 以支持外部 pull request 的分类定级，将 PR 视为附带代码的工单，走相同的角色和状态机流程。PR 与工单并列内联处理（由每个仓库的设置开关控制），发现机制仅展示外部 PR，仅限 bug 的"复现"步骤被泛化为单一的"验证声明"步骤，冗余性检查将已实现的请求决议为 `wontfix`，避免污染超出范围的知识库。`setup-matt-pocock-skills` 获得了面向 GitHub/GitLab 的 PR 作为请求来源的开关。

- [#472](https://github.com/mattpocock/skills/pull/472) [`d869d45`](https://github.com/mattpocock/skills/commit/d869d45afc32beab1c2d1350f8de5e81589512cd) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 修复 **`wayfinder`** 硬编码工单追踪器文档路径的问题，这破坏了套件中其他部分依赖的间接引用机制。

  `to-issues`、`to-prd` 和 `triage` 从不直接命名路径——它们通过 `setup-matt-pocock-skills` 写入 `CLAUDE.md` / `AGENTS.md` 的 `### Issue tracker` 块来解析追踪器，该块指向追踪器文档的实际位置。而 Wayfinder 却固定写死为字面路径 `docs/agents/issue-tracker.md`，因此在将 agent 文档放在其他位置的仓库中，它会静默回退到本地 Markdown 追踪器——即便该仓库的 `CLAUDE.md` 明确声明使用 GitHub issues。现在它通过相同的指针解析文档，并按名称读取其 "Wayfinding operations" 部分，保持套件内间接引用的一致性。

## 1.0.1

### 补丁变更

- [`d20ee26`](https://github.com/mattpocock/skills/commit/d20ee2684e2a9442698ac3c1e0f2c5b68c4cf296) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 将 **`teach`** skill 改为复用优先。课程现在使用 `./assets/` 中的可复用 **组件** 构建——样式表、测验小部件、模拟器、图表辅助工具。复用是默认行为：agent 在编写课程之前先读取 `./assets/`，根据已有的内容构建，并将任何新的可复用内容提取为组件，而非内联其中。

## 1.0.0

### 重大变更

- [`47bde84`](https://github.com/mattpocock/skills/commit/47bde84da032afb2e5058f997f3bbca47d321dbd) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 新增 **`ask-matt`** skill——一个用户调用的路由器，根据你的情况指向正确的 skill 或流程。

  **破坏性变更：** `ask-matt` 路由覆盖本仓库中的其他用户调用 skill，因此它期望这些 skill 都已安装。

- [`47bde84`](https://github.com/mattpocock/skills/commit/47bde84da032afb2e5058f997f3bbca47d321dbd) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 新增共享设计 skill 并将现有 skill 重新连接到其上。

  - 新增 **`codebase-design`** skill——深层模块词汇（模块、接口、深度、seam、适配器）以及将大量行为置于小型接口背后的原则。之前存放在 `improve-codebase-architecture/LANGUAGE.md` 中的语言现在移至此 skill，泛化为可跨 skill 复用。
  - 新增 **`domain-modeling`** skill——主动构建和打磨项目的领域模型，用词汇表对术语进行压力测试，并保持 `CONTEXT.md` 和 ADR 的更新。
  - `improve-codebase-architecture` 现在从 `/codebase-design` 获取其架构词汇，从 `/domain-modeling` 获取其领域模型。
  - `tdd` 现在依赖 `/codebase-design` 获取接口设计指导——其内联的 `deep-modules.md` / `interface-design.md` 笔记已被移除，改为使用共享 skill。
  - `grill-with-docs` 现在通过 `/domain-modeling` 内联构建领域模型。

  **破坏性变更：** 这些 skill 现在依赖新的 `codebase-design` / `domain-modeling` skill，因此你必须同时安装它们。

- [`47bde84`](https://github.com/mattpocock/skills/commit/47bde84da032afb2e5058f997f3bbca47d321dbd) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 移除 **`caveman`** 和 **`zoom-out`** skill。

  - `caveman` 是我正在测试的另一个 skill 的重复项，从未打算公开。
  - `zoom-out` 在实践中未被使用，因此已从仓库中移除。

  **破坏性变更：** 两个 skill 均已移除。

- [`47bde84`](https://github.com/mattpocock/skills/commit/47bde84da032afb2e5058f997f3bbca47d321dbd) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 将 **`diagnose`** skill 重命名为 **`diagnosing-bugs`**。

  **破坏性变更：** 以 `/diagnosing-bugs` 调用——旧的 `/diagnose` 名称不再存在。

- [`47bde84`](https://github.com/mattpocock/skills/commit/47bde84da032afb2e5058f997f3bbca47d321dbd) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 用 **`writing-great-skills`** 替换 **`write-a-skill`**。

  - 移除 `write-a-skill`。
  - 新增 `writing-great-skills`（及其 `GLOSSARY.md`）——编写和编辑 skill 的参考指南：使 skill 可预测的词汇和原则，将无操作指令追踪到句子级别。
  - 将 `grilling` 暴露为模型可调用 skill——`grill-me` 和 `grill-with-docs` 背后的可复用访谈循环。

  **破坏性变更：** `write-a-skill` 已移除；请改用 `writing-great-skills`。

### 次要变更

- [`47bde84`](https://github.com/mattpocock/skills/commit/47bde84da032afb2e5058f997f3bbca47d321dbd) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 新增 **`resolving-merge-conflicts`** skill——一个用于解决正在进行中的 git merge 或 rebase 冲突的循环。独立 skill，不依赖其他 skill。

- [`47bde84`](https://github.com/mattpocock/skills/commit/47bde84da032afb2e5058f997f3bbca47d321dbd) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 在文档中将 skill 分类法从 **Commands / Skills** 重命名为 **User-invoked / Model-invoked**，并添加 `docs/invocation.md` 定义该划分：用户调用的 skill 仅在你手动输入时可达，其存在目的是编排；模型调用的 skill 也可以在任务匹配时自动触发。用户调用的 skill 可以调用模型调用的 skill，但绝不能调用另一个用户调用的 skill。

### 补丁变更

- [`47bde84`](https://github.com/mattpocock/skills/commit/47bde84da032afb2e5058f997f3bbca47d321dbd) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 收紧 **`review`** skill：快速失败的分支引用检查、单一来源的规则和无操作指令的精简。
