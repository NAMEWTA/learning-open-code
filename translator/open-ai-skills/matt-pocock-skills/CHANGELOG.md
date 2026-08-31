# mattpocock-skills

## 1.2.2

### 补丁变更

- [#766](https://github.com/mattpocock/skills/pull/766) [`4aaccb5`](https://github.com/mattpocock/skills/commit/4aaccb58d40559d7e3c59a029b2290ae5ba538de) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 让 `writing-for-agents` 在 Codex 中恢复模型可调用。

  - 从 `agents/openai.yaml` 中移除 `policy.allow_implicit_invocation: false`。Codex 将该技能从模型可见的技能列表中过滤掉了，所以它的 description 无法触发它——只有显式提及 `$writing-for-agents` 才有效。
  - 更新过时的 `interface.display_name` 和 `interface.short_description`，它们仍指向旧的 `writing-great-skills` 技能。
  - 将该技能从 `README.md` 和 `skills/productivity/README.md` 的**用户调用**列表移至**模型调用**列表。

## 1.2.0

### 次要变更

- [#551](https://github.com/mattpocock/skills/pull/551) [`697d4ce`](https://github.com/mattpocock/skills/commit/697d4ce9742da558fd1ba6697c8e9775e2e302dd) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 在每个技能的 Claude Code frontmatter 旁边添加 Codex 元数据，使整套技能无需生成副本即可在两个 harness 中工作。

  - 在每个 `SKILL.md` 旁添加一个 `agents/openai.yaml`，包含 Codex UI 元数据（`interface.display_name`、`interface.short_description`）。
  - 用 `policy.allow_implicit_invocation: false` 标记每个用户调用的技能——这是 `disable-model-invocation: true` 的 Codex 对应物——让 Codex 将其排除在隐式调用之外，同时显式 `$skill` 调用仍然有效。
  - 在 `.agents/invocation.md`、`CLAUDE.md` 和推广分类的 README 中记录双 harness 调用模型。
  - 添加 `AGENTS.md` 作为 `CLAUDE.md` 的符号链接，让 Codex 读取相同的仓库指令。

- [#593](https://github.com/mattpocock/skills/pull/593) [`0f2bdbd`](https://github.com/mattpocock/skills/commit/0f2bdbdb06220d2df3718b8f0483157c6c8a8600) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 将 **`to-questionnaire`** 从 `in-progress/` 毕业到 **Productivity** 分类，随插件发布。它把一个你无法独立回答的决策，转化为一份交给唯一能回答之人的 Markdown 问卷——异步填写，或在会议中一起完成。

  它的标志性动作是盘问"**发送**"而非主题：常规的 grilling 会话盘问主题，而这恰恰是你无法回答的部分，所以访谈只问问卷发给谁、你需要回什么，然后把每个问题对准两者之间的差距。

  现已接入为推广技能——插件条目、顶层 + Productivity README 的**用户调用**列表、`docs/productivity/to-questionnaire.md` 文档页，以及 `ask-matt` 中把它定位为 `/grill-me` 之反面的独立路由（挖掘别人，而不是自己）。

- [#680](https://github.com/mattpocock/skills/pull/680) [`b3376f8`](https://github.com/mattpocock/skills/commit/b3376f8d39848dd08572ec2667da4739a67c8c04) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 将 **`wizard`** 从 `in-progress/` 毕业到 **Engineering** 分类，随插件发布——并使其成为模型调用。它生成一个交互式 bash 脚本，引导人工用户完成手动流程——第三方设置、一次性迁移、A→B 状态转换——打开每个 URL、说明要点击什么、捕获这些值，并写入 `.env` 文件和 GitHub Actions secrets。

  令人愉悦的用户体验已由附带的 `template.sh` 预解决（剩余时间估算的进度显示、确认关卡、包括 WSL 在内的跨平台 URL 打开、隐藏的密钥输入、幂等的 `.env` 追加更新、优雅降级的 `gh secret`/`gh variable` 写入、收尾的跳过摘要）。`STAGES` 标记上方的所有内容都是一个从不手工编辑的固定库——技能的工作只在于界定流程范围并编写其**阶段**。

  属于 Engineering 而非 Productivity：它读取 `.env*`、`docker-compose*`、框架配置以及 `.github/workflows/` 中的每个 `secrets.*`/`vars.*` 引用来界定自身范围，写入 CI secrets，并用 `bash -n` 和 `shellcheck` 验证其输出。

  因为它是模型调用的，agent 一碰到只有人类能执行的步骤就能去取用它，而不是把编号指令倾倒进聊天里指望你照着做。输入 `/wizard` 与以前完全一样——模型调用只会*增加* agent 的触达。description 被写成决定它何时触发的指针：它产出什么、四个触发分支（配置基础设施、设置凭据或 CI secrets、操作陌生的第三方后台、一次性迁移或切换），以及一个明确的非触发条件——不要为 agent 自己能完成的步骤调用它。agent 能做的活，就该 agent 做；向导是为那些你不会交给 agent 的点击、审批和后台操作准备的。写任何一行之前的阶段列表确认，现在同时充当 agent 在构建中途触发它时的提案。

  现已接入为推广技能——插件条目、顶层 + Engineering README 的**模型调用**列表、`docs/engineering/wizard.md` 文档页，以及 `ask-matt` 中"只有人类能执行的步骤"的独立路由。模型调用也使它脱离了 [#693](https://github.com/mattpocock/skills/issues/693) 的影响范围——该 issue 将用户调用的技能从 Claude 桌面和网页界面的列表中剔除。

- [#763](https://github.com/mattpocock/skills/pull/763) [`77d207e`](https://github.com/mattpocock/skills/commit/77d207ef03219cc603e2832e1159cbdd1c91818e) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 围绕两个理念重塑 **`prototype`** 技能：演示是**一个可共享的 HTML 文件**，原型是**一手资料**。

  逻辑分支现在产出一个自包含的文件（纯 HTML/CSS/JS，无构建、无服务器），而不是终端应用——非开发者可以双击打开它，用自己的领域语言驱动它：一个带标签的状态面板、始终可用的自由点击按钮，以及一组带标签的**引导式演练**，每个都是一个场景，下方列出按顺序要按的按钮。可移植的纯逻辑模块仍然会提升进真实代码；HTML 外壳才是一次性的。

  一次性不再意味着删除。原型在回答完问题后不再被移除，而是作为可运行证据捕获在 main 之外的一条临时分支（`prototype/<name>`）上，并在实现 issue 上留下指向它的上下文指针——这样 main 分支只保留已验证的决策，而探索仍然可寻。答案（结论 + 问题）仍然持久地记录在 issue/ADR/commit 中。

- [#536](https://github.com/mattpocock/skills/pull/536) [`42a5b70`](https://github.com/mattpocock/skills/commit/42a5b70fcacc7baff1977b13f3919fb2f63af14e) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 将整套技能作为原生 **Claude Code 插件**发布，收录于 Claude Code 的官方市场。你现在可以把推广技能订阅为受管理的、只读的捆绑包，而不是复制可编辑的文件：

  ```bash
  claude plugins install mattpocock-skills
  ```

  或者，在会话内部：

  ```
  /plugin install mattpocock-skills
  ```

  不需要预先添加任何市场——官方市场默认配置。

  `.claude-plugin/plugin.json` 携带完整的插件元数据（version、description、author、license、keywords）和推广技能的明确列表。`skills.sh` 仍然是通用安装器（也是 Codex 和其他 harness 当前的路）；原生 Codex 插件推迟——原因见 `.agents/adr/0002-ship-as-a-claude-code-plugin.md`。

- [#751](https://github.com/mattpocock/skills/pull/751) [`355fa74`](https://github.com/mattpocock/skills/commit/355fa7420b418af838998f7ec4365ceda1c8dfcc) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 添加 **`wait-what`** —— 一个针对模型啰嗦的单字纠正。消息没说到点的那一刻输入它，agent 就会重新阐述：一点背景、ASD-STE100 简化技术英语，以及你 `CONTEXT.md` 中的通用语言。用户调用，三行长。

  机制就是名字本身。精简类技能因膨胀而失败——一份 400 行的技能仍然让模型啰嗦——所以这个技能是一个精确的引导词，仅此而已。描述*输出*的名字（`/tldr`、`/no-fluff`）会让模型裁剪词语、让你更迷惑；命名*听者*的状态则同时索要两半——更少的词**和**你缺失的背景。它还复用你全局 `CLAUDE.md` 中已有的引导词，所以技能、`CLAUDE.md` 和每个 `CONTEXT.md` 伸手够向相同的 token。

  它修复一条消息；它不预防下一条。行话的解药是用 `/grill-with-docs` 预先建立的共享语言；这是你在还没有共享语言时的求助对象。

- [#763](https://github.com/mattpocock/skills/pull/763) [`77d207e`](https://github.com/mattpocock/skills/commit/77d207ef03219cc603e2832e1159cbdd1c91818e) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 把 `/wayfinder` 的工作单元命名为**决策票据（decision ticket）**，并用子 agent 烧掉 research 票据。

  人们一直把 wayfinder 票据读成普通的*实现*票据——要执行的一个构建切片——而 wayfinder 把它们用作**决策票据**：解决结果是一个决策的问题。技能描述和它的开篇现在引入该术语（并说明什么使它成为决策票据），`ask-matt` / engineering README 的介绍和文档页也同步——而一旦术语确立，"ticket" 仍是日常用词。`CONTEXT.md` 把 **Decision ticket** 记录为领域术语，因此"避免：ticket"的指引不再与 wayfinder 对这个词的刻意使用相矛盾。

  Research 票据不再停放在单独启动的会话中。Research 仍然是真正的票据类型——它是下游决策所依赖的真正的共享阻塞项，而这个依赖正是前沿的阻塞边要呈现的东西。变化的是它的解决方式：因为 research 是 AFK 的，绘制地图不会停下来读它。创建票据后，绘图会话为每个 research 票据派一个 `/research` 子 agent 并行烧掉它，把发现捕获到一条一次性的 `research/<name>` 分支上并留下上下文指针。Research 票据是"每个会话一个票据"的唯一例外。

- [#763](https://github.com/mattpocock/skills/pull/763) [`77d207e`](https://github.com/mattpocock/skills/commit/77d207ef03219cc603e2832e1159cbdd1c91818e) 感谢 [@mattpocock](https://github.com/mattpocock)！ - **破坏性变更：** 将 **`writing-great-skills`** 重命名为 **`writing-for-agents`**，重构它，并添加一个新引导词。

  该参考现在覆盖 agent 消费的任何文档——skills、`AGENTS.md` / `CLAUDE.md`、通过指针到达的文档——而不只是技能。`GLOSSARY.md` 并入 `SKILL.md`（每个术语一个权威论述；`_Avoid_` 同义词列表和独立的 Predictability 定义已移除）；仅技能相关的机制（frontmatter、模型调用 vs 用户调用、路由技能、按调用方式拆分）披露到新的 `SKILL-MECHANICS.md`。该技能现在是**模型调用**：在创建或编辑技能、修改 `AGENTS.md`/`CLAUDE.md` 时触发。`ask-matt` 的指针已更新。请以新名字重新安装；旧名字已消失（无别名）。

  精简章节增加了**缓存（cache）**。单一事实来源现在延伸到文档之外、进入环境——`package.json` 脚本、配置文件、目录布局、`--help` 输出本身就是权威的，所以重述它们的文档就是一次查询的缓存，只有当查询昂贵时才值得负担。正面目标：缓存 agent 无法通过查找得到的东西（不成文的约定、选择背后的原因、任何配置都不会招认的坑），把"一个文件一条命令"式的查找留给环境，在那里它们不会过期。

- [#533](https://github.com/mattpocock/skills/pull/533) [`45afd80`](https://github.com/mattpocock/skills/commit/45afd8074a8b7de5fe073845d080fa9dd6c429fa) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 给 **`improve-codebase-architecture`** 技能的探索步骤添加 YAGNI 范围过滤器。它不再均匀扫描整个仓库，而是把范围限定到变更实际落地的地方：如果你指明方向就采用它，否则读取最近约 20 条 commit 消息，把探索偏向积极开发的路径。没人碰的代码中的深化机会，是一次你永远不会兑现的重构——杠杆只在你还持续编辑的地方才有回报——所以报告不再整理仓库的休眠角落。

### 补丁变更

- [#763](https://github.com/mattpocock/skills/pull/763) [`77d207e`](https://github.com/mattpocock/skills/commit/77d207ef03219cc603e2832e1159cbdd1c91818e) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 打磨 `/ask-matt` —— 路由器现在覆盖阶段边界、两个 wayfinder 常见错误，以及两个它从未提及的技能。

  **阶段边界。** **阶段（phase）** 是会话内的一块工作——访谈、实现、QA——而两者之间的边界就是你决定如何处理已构建上下文的地方。两行的 `Crossing sessions` 部分被一棵携带全部五个选项的决策树取代（**continue**、`/clear`、`/handoff`、**subagent**、`/compact`），推理披露在新的 `PHASE-BOUNDARIES.md` 中。随之而来三个修复：

  - **`/handoff` 被过度推销了。** 它读起来像上下文窗口之间的通用桥梁。它其实很窄：只有当有东西必须*移动*时你才需要它——新的 harness、新的目录、同事，或阶段中途分叉的旁路任务。它买到的是可移植性。
  - **`/compact` 是默认，不是第一伸手可及处。** 它在树的底部，排在它上面四个更廉价或更精确的问题之后。从那里开始，会产生一个对摘要压平了什么自信地搞错的会话。
  - **两个分支完全缺失。** **Continue** 是最先要排除的选项——它是唯一让对话保持为一手资料、而非其摘要的选项——而 **subagent** 处理任何范围足够紧、可以 AFK 运行的东西。

  上下文卫生的逃生口现在说 `/compact` 而不是 `/handoff`（同一 harness、同一目录、在边界处——handoff 条款不适用），智能区间数字从约 120k 更新为约 150k token。

  **Wayfinder 路由。** 人们对这个最重、认知负担最大的流程最常犯的两个错误：

  - **过度伸手。** 它比一次单独的 grill 更慢更密集，所以被标记为最重的流程，专为真正装不进一个会话的想法保留——范围明确的功能属于 `/grill-with-docs`，而不是这里。
  - **在交接处迷失方向。** 当地图清晰时，wayfinder 是交接，不是构建：在 `/to-spec` 处汇入主流程（它把地图上相互关联的决策折叠成可构建的计划），而不是把地图直接绕进 `/implement`。直接进 `/implement` 只用于结果真的很小的工作。

  **缺失的路由。** `/grilling` 和 `/resolving-merge-conflicts` 完全不在路由器中，现在它们在里面了，而 `grill-me` 与 `grill-with-docs` 的分界是你是否在某个工作目录中。

- [#502](https://github.com/mattpocock/skills/pull/502) [`44eed54`](https://github.com/mattpocock/skills/commit/44eed545186ffd0263e8004867750b80cfddd215) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 让 `/setup-matt-pocock-skills` 更友好，并使本地 markdown tracker 与当前规范对齐。

  - **Triage 标签**现在只在 `triage` 技能已安装时才询问，且是单个推荐"是"的问题（"保留默认的 triage 标签？"），而不是覆盖式盘问。当 `triage` 未安装时，该节——以及 `docs/agents/triage-labels.md`——都被跳过。
  - **外部 PR 作为请求渠道**不再是设置问题。GitHub/GitLab 模板仍然携带该标志，默认关闭；用户之后可以在 `docs/agents/issue-tracker.md` 中翻转它。
  - **领域文档**默认单上下文，无需询问；只有当仓库显示 monorepo 信号时才提供多上下文。
  - **本地 markdown 票据**现在是 `.scratch/<feature>/issues/<NN>-<slug>.md` 下每个票据一个文件——绝不是合并的单一 `tickets.md`。`/to-tickets` 和本地 issue-tracker 模板现在一致，spec 文件是 `spec.md`（不是 `PRD.md`），与 `/to-spec` 匹配。

  `setup-matt-pocock-skills` 和 `to-tickets` 的文档页已重新同步。

- [#532](https://github.com/mattpocock/skills/pull/532) [`170ad48`](https://github.com/mattpocock/skills/commit/170ad48655825783d0193e850e31a9aac957bb95) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 为通用用途改写 **`grilling`**。它的 description 和正文不再把访谈限定在软件计划上："this plan" → "this"、"enact the plan" → "act on it"、"exploring the codebase" → "exploring the environment"。技巧不变；现在它读起来是对任何计划、决策或想法的压力测试。

- [#593](https://github.com/mattpocock/skills/pull/593) [`a4b2009`](https://github.com/mattpocock/skills/commit/a4b2009a1a3ac9575506c10b4c84f08f9bba7a38) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 将 **`grilling`** 从一次一个问题重构为逐轮进行。它现在映射决策树，并在单个编号轮次中问完整条**前沿**——每个前置条件已确定的问题——然后根据用户的回答重新计算前沿，再问下一轮。同样的 13 个问题在约 3 轮内完成，而不是 13 轮。环境能回答的事实被派发给后台子 agent，因此研究从不阻塞轮次：只有正在进行的探索下游的问题才等它。当前沿为空时会话结束。

  一轮中的每个问题都以一个固定形态发出——`❓ **Q1** - **<标题>**`，然后是正文（散文或多个选项），再在独立的 `➡️` 行给出推荐。一轮读起来像一份可扫描的编号列表，每个推荐与问题视觉分离，所以你可以按编号回答，而不是把问题复述回去。

  `grill-me`、`grill-with-docs` 和 `triage` 也逐轮运行前沿——`triage` 的 grill 步骤和 `grilling` 的 Codex `short_description` 现在如此表述，而不是描述旧的节奏。一次一个问题的退出开关（全局 `CLAUDE.md` 中的一行）不变。

- [#752](https://github.com/mattpocock/skills/pull/752) [`c66bdee`](https://github.com/mattpocock/skills/commit/c66bdeeee002d81e3f8b21403c07f9a0d7bea6da) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 从仓库中移除六个技能。它们都不在 Claude Code 插件中，但六个都能通过 [skills.sh](https://skills.sh/mattpocock/skills) 安装——它服务于仓库中的每个技能——所以这就是离开该列表的内容，以及每一个的去向。

  四个退役技能，每一个都已被做得更好的技能吸收：

  - **`ubiquitous-language`** → **`/domain-modeling`**，它构建并维护整个领域模型，而不是从一次对话中倾倒一份词汇表。
  - **`design-an-interface`** → **`/codebase-design`**。没有任何损失："设计两次"技巧——并行子 agent 生成截然不同的设计，源自 Ousterhout——作为 `DESIGN-IT-TWICE.md` 随该技能发布。
  - **`qa`** → **`/triage`** 和 **`/to-tickets`**。
  - **`request-refactor-plan`** → **`/to-spec`** 和 **`/improve-codebase-architecture`**。

  还有两个从来只属于我——绑定在我自己的机器上，从不是为别人准备的。`personal/` 分类随它们一起消失：

  - **`edit-article`**
  - **`obsidian-vault`**，它硬编码了一条指向我自己 Obsidian 库的路径。

  `skills/deprecated/` 作为一个分类保留，现在为空。`skills/in-progress/` 不变，现在被如实描述：一个 beta 频道，有意公开，通过 skills.sh 一次安装一个技能。

- [#734](https://github.com/mattpocock/skills/pull/734) [`a2f9333`](https://github.com/mattpocock/skills/commit/a2f9333669ff53db762c87ecda5a15442060a3be) 感谢 [@mattpocock](https://github.com/mattpocock)！ - 完成 `to-prd` → `to-spec` 重命名："spec" 现在是发布文本中的唯一术语。

  - **`to-spec`** 不再以"你可能知道这份文档叫 PRD"开头——该括注已从技能及其文档页中移除。本地 markdown tracker 模板也删除了同样的措辞保留。
  - **`code-review`** 在其 frontmatter description、双轴摘要和 spec 来源搜索顺序中，谈论的是原始 issue/spec 而不是 issue/PRD。两个 README 已重新同步。
  - **GitHub 和 GitLab tracker 模板**现在写着"此仓库的 Issues 和 specs 以 GitHub/GitLab issues 的形式存在"——本地模板更新时它们还停留在"PRDs"，于是过时术语传播到了写入它们的每个仓库。
  - **`docs/engineering/research.md`** 指向 `https://aihero.dev/skills-to-prd`，这是重命名后技能的死链；现在像其他 19 个文档页一样链接 `to-spec`。

  CHANGELOG 和现有 changesets 在记录重命名本身的地方仍然使用 PRD 一词，这是正确的。

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
