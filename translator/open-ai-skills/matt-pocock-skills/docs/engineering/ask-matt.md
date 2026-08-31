## 功能说明

`ask-matt` 是本仓库所有 skill 的路由器。你描述自己面临的情况——一个无从下手的想法、一堆涌进来的 bug 报告、一场拖得太长的 [会话](https://www.aihero.dev/ai-coding-dictionary/session)——它会告诉你哪个 skill 或哪组 skill 组合适合，以及这组组合中人类决策点在哪里。

它只做推荐，然后停下。它不会质询、不会写 [规格](https://www.aihero.dev/ai-coding-dictionary/spec)、不会打开文件，也不会替你执行它刚点名的 skill；你拿到的是"下一步该输入什么"，然后由你自己输入。它还是一张手写的本仓库 skill 地图，而不是对你已安装内容的扫描，所以它不会把你导向你自己写的 skill 或其他作者的 skill。

## 何时使用

输入 `/ask-matt` 来调用它——Agent 不会自行调用此 skill。

| 你的情况 | 路由器给出的答案 |
| --- | --- |
| 有一个想法，但不知道从哪里开始 | 主流程的起点，以及这次构建是否小到可以跳过规格 |
| 来自他人的 bug 和需求 | [triage](https://aihero.dev/skills-triage) 入口通道，以及为什么你自己生成的 [ticket](https://www.aihero.dev/ai-coding-dictionary/ticket) 不属于它 |
| 两个 skill 看起来可以互换 | 它们之间的分界线，而这通常是一个具体的检验标准，而非口味问题。[grill-me](https://aihero.dev/skills-grill-me) 与 [grill-with-docs](https://aihero.dev/skills-grill-with-docs) 的分界在于你是否处于工作目录中；[grill-with-docs](https://aihero.dev/skills-grill-with-docs) 与 [wayfinder](https://aihero.dev/skills-wayfinder) 的分界在于这项工作的规模是否适合单次会话 |
| 一场长会话，需要就 [上下文](https://www.aihero.dev/ai-coding-dictionary/context) 做出决定 | 阶段边界上五个选项的有序决策树 |
| 你已经选好了 skill | 没有有用的答案。直接调用那个 skill 吧。 |

## 前置条件

路由器只点名 skill，不负责安装它们。它指向的每个 skill 都必须已安装，推荐才有意义；而且它只认识本仓库中推广的 skill。

依赖追踪器的路由——triage、`to-spec`、`to-tickets`、`implement`——假设 [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) 已经在仓库中配置好了问题追踪器。在这之前，路由器照样会推荐它们，不会拦着。

## 流程，而非 skill

这个 skill 给你的思考词是**流程**：一条*穿过*各 skill 的路径，而不是单个 skill。描述你的情况，你就会被放置在流程的某一步上——这不同于"这是匹配你关键词的 skill"这种答案。路由一共分四种，skill 本身完整地承载着它们：

- **主流程**，从想法到交付。质询、规格、ticket、实现、审查，内部还有两个分支：当某个问题需要可运行的代码才能定论时的原型绕行；以及规格与 ticket 的分拆——只有当构建横跨多次会话时，这次分拆才值得它的成本。
- **入口通道**，面向那些先产生工作、随后汇入主流程的情况：涌进来的 bug 报告、某个东西坏了、或者一项太模糊又太大、无法装进单次会话的工作。
- **独立工具**，不在任何流程上，按自身条件取用——原型、问卷、你已经身处其中的合并冲突。
- **底层词汇层**，两个参考 skill，当问题出在措辞而非流程上时，其他 skill 会把它们拉进来。

## 阶段边界

它交给你的另一个概念是**阶段边界**。阶段是会话内部的一块工作——[质询](https://www.aihero.dev/ai-coding-dictionary/grilling)、实现、QA——而"我拿这些上下文怎么办？"这个问题只属于两个阶段之间的边界。阶段进行中没有需要决定的事：要么继续，要么把剩余工作拆给 [子代理](https://www.aihero.dev/ai-coding-dictionary/subagent)。

| 选项 | 何时选择 |
| --- | --- |
| **继续** | 下一阶段要原样使用本阶段的内容，或者你的 [smart zone](https://www.aihero.dev/ai-coding-dictionary/smart-zone) 还有余量。它是唯一能让会话保持为 [一手来源](https://www.aihero.dev/ai-coding-dictionary/primary-source) 的做法，所以先把它排除掉再考虑别的 |
| **`/clear`** | 身后的一切都可丢弃。棋盘上最便宜的一步，但如果判断错了，它无法回头 |
| **[handoff](https://aihero.dev/skills-handoff)** | 有东西需要转移：换 [工具链](https://www.aihero.dev/ai-coding-dictionary/harness)、换目录、交给同事、或一个阶段中途岔出去的支线任务 |
| **子代理** | 任务边界足够清晰，可以 [离开键盘](https://www.aihero.dev/ai-coding-dictionary/afk) 交给它跑 |
| **`/compact`** | 以上都不合适。它是默认项，而且经常落到这一步 |

其中有两个选项经常被用错，这正是路由器携带顺序而非清单的原因。`/handoff` 读起来像是窗口之间通用的桥梁，但它不是：可移植性是它买到的全部。`/compact` 是决策树的底部而非首选，因为它上面的四个问题每一个都更便宜或更精确。

## 常见问题

**不就是一张按正确顺序排列的 skill 清单吗？**

一直有人要求在 README 里放这么一张表。这个 skill 就是那张表——这正是它存在的意义。一张静态表格会写成 `wayfinder → to-spec → to-tickets → implement → code-review`，而这对大多数情况都是错的，因为有趣的部分在于分支——有没有代码库、构建是否横跨多次会话、这个问题能否靠谈话定论。诚实的代价是：路由器靠手工维护，会落后于仓库。`/grilling` 和 `/resolving-merge-conflicts` 都上线很久之后，路由器才提到它们。

**它告诉我一半的 skill 没有安装。**

一个已知 bug，尚未修复。路由器带你经过的大多数 skill 都设置了 `disable-model-invocation: true`，这意味着工具链会把它们排除在注入 Agent 上下文的 skill 清单之外。Agent 把那份清单当成全集，于是报告它们缺失。有一份报告记录到：它宣布整个规格与 ticket 流程不存在，转而路由到光秃秃的 `/grilling` 和 `/tdd`。插件 22 个 skill 中有 13 个带有这个标志，所以这是常见情况而非边缘案例。它们确实装好了。照常输入斜杠命令即可，或者查一下 `.claude-plugin/plugin.json`——那才是判断有什么在册的权威。

**它描述了一个 skill 的行为，而那个 skill 并不这样做。**

这也是真的，同样未修复。路由器依据自己对每个 skill 的一行摘要作答，而不是去读 skill 本身。一份详细报告在同一场会话里记下了三处这样的例子，其中包括仅凭"把对话变成规格"这句注释就建议跳过 [to-spec](https://aihero.dev/skills-to-spec)——`to-spec/SKILL.md` 从未被打开过。每次都是用户提出质疑后它才去核实，从不主动为之。那次跳过 `to-spec` 确实漏掉了一次接缝检查，产出的 ticket 也低估了工作量。当路由器对其他 skill 做出关键断言时，先让它打开那个 `SKILL.md`。地图完全没有覆盖的问题也同样适用，比如是否要使用 [plan mode](https://www.aihero.dev/ai-coding-dictionary/agent-mode)：那个答案来自 [模型](https://www.aihero.dev/ai-coding-dictionary/model) 的推断，不是写在这里的东西。

**为什么用散文而不是编号清单？**

这是合理的抱怨，有人开了 issue 说：大部分路由是确定性的，叙述式写法让人难以扫读。没人拦着你索要压缩形式——"直接给我顺序"就会得到顺序。散文承载的是条件那一半：分支、哪里需要人类做决定、步骤之间在哪里 clear 或 compact。一张扁平清单丢掉的正是这些。

**它能路由到我自己的 skill 或其他作者的 skill 吗？**

不能。有三份提案都要求做一个读取本地 `skills/` 目录、从已安装内容中推荐的路由器。`ask-matt` 不是那种东西。它是一组 skill 的地图，手工维护，对你自己写的或从别处安装的 skill 一无所知。

**它让我编辑一个 SKILL.md。**

这个建议常常正确，但很少持久。有人问它怎么让 [implement](https://aihero.dev/skills-implement) 自动关闭 ticket，被告知往 skill 里加一行，然后立刻发现了问题：`npx skills update` 会覆盖这个文件，而且插件安装是只读的。把长期行为写进你自己的 `CLAUDE.md` 或 `AGENTS.md`，或者在使用时当场说明。提示层面的适配能扛过更新——把流程指向 Linear 而不是 GitHub，或者问它哪些未关闭的 ticket 可以并行跑，都是人们这样做的例子。

**它提到了我没有的 skill，或者漏掉了我有的 skill。**

在断定它消失之前，先去变更日志里查改名。`writing-great-skills` 变成了 [writing-for-agents](https://aihero.dev/skills-writing-for-agents)，没有别名；`to-prd` 变成了 [to-spec](https://aihero.dev/skills-to-spec)；`pathfinder` 变成了 [wayfinder](https://aihero.dev/skills-wayfinder)。有四个 skill 被整体退役，并入吸收它们的 skill：`ubiquitous-language`、`design-an-interface`、`qa` 和 `request-refactor-plan`。反过来那种情况——路由器自身的滞后——见上文。

## 有效的标志

- 它以说出"该输入什么"收尾并就此打住，而不是自己动手开始干活。
- 它给出的路线提到了在哪里 clear 或 compact 上下文、在哪里需要你审查，而不只是一串 skill 名。
- 当两个 skill 相近时，它说出选哪一个、以及为什么另一个不适合你。
- 它关于其他 skill 行为的任何断言，都能在轨迹中看到它确实读了那个 skill 的 `SKILL.md`。
- 它在回应中认出了你的具体情况，而不是套用最接近的通用场景。

## 在系统中的位置

`ask-matt` 是覆盖整个 skill 集合的**独立路由器**。它从不处于链条中的某一步；它指向每一条链条，也是其他文档页面反向链接的节点，这样它们谁都不用重画这张图。从这里出发，你最常落到 [grill-with-docs](https://aihero.dev/skills-grill-with-docs)——主流程的起点——或 [triage](https://aihero.dev/skills-triage)——处理"送上门的工作"而非"你自己开启的工作"的入口通道。

就它所描述的 skill 而言，它是 [二手来源](https://www.aihero.dev/ai-coding-dictionary/secondary-source)。当路由器与某个 `SKILL.md` 说法冲突时，以 `SKILL.md` 为准。
