## 功能说明

`improve-codebase-architecture` 普查代码库，寻找**深化机会**——浅层模块（接口几乎和它所隐藏的东西一样复杂）可能变成深层模块的地方——把它们写成一份自包含的 HTML 报告，然后 [质询](https://www.aihero.dev/ai-coding-dictionary/grilling) 你走完你选中的任何一个。

它从不改动代码。整个运行只产生一个在你操作系统临时目录里的 HTML 文件和一场对话；重构本身稍后在另一场 [会话](https://www.aihero.dev/ai-coding-dictionary/session) 里、通过正常的构建流程发生。这正是它成为普查工具而非重构工具的原因，也是它值得在一个你还没准备动它的代码库上运行的原因。

两道过滤器防止报告退化成泛泛的清理建议。每个候选都必须通过**删除测试**——移除这个模块会把复杂度集中到更小的接口后面，还是只是把它摊到调用者身上？只有"集中"的情况挣到一张卡片。而除非你把它指向特定区域，它会先读最近的提交历史，把扫描偏向正在活跃变化的路径，理由是：没人碰的代码里的深化，是一次你永远兑现不了的重构。

## 何时使用

输入 `/improve-codebase-architecture` 来调用它——[Agent](https://www.aihero.dev/ai-coding-dictionary/agent) 不会自行调用。

它站在构建循环之外——它不是主循环的一步，而是你定期运行、为改进代码库排队更多工作的东西。它被使用的四种情况：

| 情况 | 怎么用 |
| --- | --- |
| 例行维护 | 每隔几天跑一次，或一有空档就跑，防止结构在功能之间腐烂。 |
| 大构建之前 | 把它指向 [规格](https://www.aihero.dev/ai-coding-dictionary/spec)："我们怎么让这个变更变容易？"这是对它最有效的提示词。 |
| 棕地普查 | 在一个大型、无结构或 [vibe-coded](https://www.aihero.dev/ai-coding-dictionary/vibe-coding) 的仓库上运行它，搞清楚它实际处于什么形状。 |
| 遗留测试工作 | 在对着不可测试的代码写测试之前，先用它找出缺失的接缝。 |

它与兄弟 skill 容易混淆的地方：

- 设计一个你已经选定的模块，用 [codebase-design](https://aihero.dev/skills-codebase-design)——那是工作台，这是找出放什么上工作台的普查。
- 一项大得装不进单次会话的整体工作，用 [wayfinder](https://aihero.dev/skills-wayfinder)。
- "这个具体的东西坏了"，用 [diagnosing-bugs](https://aihero.dev/skills-diagnosing-bugs)。当真正的发现是没有好接缝可以锁死 bug 时，它会交接回这里。

## 前置条件

运行它不需要前置条件。它会读 `CONTEXT.md` 和 `docs/adr/` 里存在的任何 ADR，并在它们存在时用你领域的原生名词说话——一个候选读起来是"深化 Order 接收模块"，而不是"重构 FooBarHandler"。

它写在两个地方。报告进入 `<tmpdir>/architecture-review-<timestamp>.html`，在仓库之外。质询循环期间它会往 `CONTEXT.md` 里添加或打磨术语——文件不存在就创建它——并提供把被拒绝的候选记录为 ADR，这样未来的运行不会再次推荐它。

## 深度，和寻找它的报告

skill 围绕一个理念展开：**深度**。深层模块把大量行为放在小而稳定的接口后面。浅层模块通过几乎和底下代码一样宽的接口泄漏实现。报告是对浅薄的猎捕——仅为可测试性抽取的纯函数，而真正的 bug 住在它们被调用的方式里（没有**局部性**）、跨**接缝**泄漏的模块、不打开五个文件就无法理解的概念——以及修复它的深化方案。

每个候选是一张卡片：涉及的文件、摩擦点、平白英语的解决方案、以**局部性**和**杠杆率**表述的收益、前后对比图，和一个强度徽章。

| 徽章 | 对你的意义 |
| --- | --- |
| `Strong` | 删除测试明确通过，摩擦是真实的。认真对待这些。 |
| `Worth exploring` | 说得通的深化，但回报取决于代码接下来往哪走。 |
| `Speculative` | 为完整性而浮出。大多数可以安全忽略。 |

报告以一条**首要推荐**收尾——它建议最先处理的那一个——然后 skill 停下，问你想探索哪个候选。到那时什么都没有决定，也没有任何代码动过。

## 你选了一个之后会发生什么

选中一个候选会开启一场关于它的 [质询](https://aihero.dev/skills-grilling) 会话：约束、接缝后面有什么、哪些测试会存活、加深后的接口应该长什么样。那场会话的产出是一个决策，不是一份 diff。之后走正常流程——把决策带进 [to-spec](https://aihero.dev/skills-to-spec)，再 [to-tickets](https://aihero.dev/skills-to-tickets)，再 [implement](https://aihero.dev/skills-implement)。

## 常见问题

**它为了一个想法质询了我一个小时，而不是给我看选项。我能关掉吗？**

能——调用时说出来（"别质询我，只给我看报告"）。这是本 skill 最响亮的抱怨。一位用户说得很直白：他喜欢它作为"获得详尽改进分析的一个方便途径"，而加了质询循环之后觉得它"几乎不可用"，报告过它会提议单一方案然后问"几十或几百个问题"的会话。设计意图是报告在先，质询只在你自己选中的候选上开始，但较弱的 [模型](https://www.aihero.dev/ai-coding-dictionary/model) 直接跳到盘问它们的第一个想法。那条讨论串里的报告因模型而异差别巨大，这是一个开放 issue——skill 还没有有据可查的无质询模式。

**报告打开是没样式的裸 HTML，没有图表。发生了什么？**

报告从 CDN 加载 Tailwind 和 Mermaid，所以打开时需要网络访问，而当有东西屏蔽那些脚本时它会悄悄坏掉。已归档的案例是一个要求 SRI 哈希的安全钩子：Agent 加上了，CDN 给浏览器提供的字节与计算哈希用的 `curl` 不同，浏览器就屏蔽了脚本。离线环境和锁死环境会撞同一堵墙。Agent 看不到这一点，因为它从不渲染页面。变通办法是要求内联 CSS 和手写 SVG 图表，而不是 CDN 脚手架。这是一个开放 issue，也是真实的粗糙边缘。

**它给了我十二个候选。我在同一场会话里处理它们，还是开新会话？**

一个会话一个候选。在一场对话里处理好几个，会把报告、质询、领域模型编辑和代码改动一下子全灌进 [上下文窗口](https://www.aihero.dev/ai-coding-dictionary/context-window)。报告只活在一个临时文件里，所以带走候选本身而不是文件：选一个、质询它、把决策带进 `/to-spec`，把其余的变成你之后可以独立拾起的 [ticket](https://www.aihero.dev/ai-coding-dictionary/ticket)。把选中的改进放进一份规格，而不是直奔实现。这是一个反复出现的问题，skill 自己里面没有有据可查的工作流。

**我该怎么提示它？**

脑子里装着下一件要建的东西。当一个大构建即将到来时，把它指向规格并问"我们怎么让这个变更变容易？"。无提示运行会自己扫描热点，对例行维护可以，但点明方向才是让报告可执行的东西。

**它在一个大型遗留代码库上有效吗？**

部分有效。它对缺乏一致结构的大型现有代码库很强，也是一次性结构搭建之后推荐的维护机制。诚实的另一面：项目真正失控的用户报告它"帮了一点，但好像还是不够"，一位有着八年遗留代码库的开发者报告模型在原地打转，而同样的 skill 在一个整洁的仓库上能产出干净图谱。那种情况还没有专门的 `/refactor` skill。如果代码库完全没有任何共享词汇，先用 [grill-with-docs](https://aihero.dev/skills-grill-with-docs) 建立一套，往往会让本 skill 的输出好得多。

**这和 `/codebase-design` 有什么不同？**

`/codebase-design` 是参考，不是会话驱动器。它提供词汇——module、interface、depth、seam、adapter、leverage、locality——而本 skill 借用它。把一个全新 Agent 指向 `/codebase-design` 让它"做"它，是一个已知的失败：没有自己的流程可循，Agent 会发明一个，重新探索代码，跑很久才问你任何东西。用本 skill 驱动；消费那一个。

**它会告诉我代码库没问题吗？**

很少，而且你该在进去之前就知道。skill 是为产出发现而构建的，所以框架推动它产出候选，而不是得出结论说没毛病。强度徽章是防线——一份全是 `Speculative` 的报告，就是 skill 用它唯一会的方式告诉你它没找到东西。

**它在 Codex 或其他工具链里有效吗？**

部分有效。探索步骤直接点名 Claude Code 的 `Agent` 工具和 `subagent_type=Explore`，所以没有那个工具的 [工具链](https://www.aihero.dev/ai-coding-dictionary/harness) 可能跳过并行探索，而不是用自己的替代。skill 照跑；只是扫描没那么彻底。一份工具链中立的改写有人提议过，但尚未合并。

**我到底怎么在 TypeScript 里实现深层模块？**

skill 没带什么好答案。反复出现的请求是要一份给出原则的具体文件和模块布局的 `TYPESCRIPT.md`，它不存在。skill 会告诉你深化该落在哪里、接缝后面该放什么；把它翻译成包或目录结构，目前靠你自己。

## 有效的标志

- 候选点名的你领域的概念，不是编造的类名——"Order 接收模块"，不是"FooBarHandler"。
- 候选聚集在你最近编辑过的文件里，不在仓库沉睡的角落。
- 运行期间没有代码变化。唯一的新文件是你临时目录里的 HTML 报告。
- 它在报告之后停下，问你想要哪个候选，而不是自己继续。
- 每张卡片把回报解释为局部性或杠杆率，并说出哪些测试会变简单——不只是"这样更干净"。
- 因为持久理由拒绝一个候选，你会收到记录 ADR 的提议，让下次运行不再推荐它。

## 在系统中的位置

`improve-codebase-architecture` 是**定期维护**——每隔几天跑一次，在任何链条之外，为工作排队而不是做工作。它的邻居是 [codebase-design](https://aihero.dev/skills-codebase-design)——拥有每个候选所书写的深度与接缝词汇；[grilling](https://aihero.dev/skills-grilling)——你选中候选后它遍历决策树；以及 [domain-modeling](https://aihero.dev/skills-domain-modeling)——在决策落定时保持 `CONTEXT.md` 和 ADR 最新。它产出的是一个想法，从 [grill-with-docs](https://aihero.dev/skills-grill-with-docs) 或 [to-spec](https://aihero.dev/skills-to-spec) 处重新进入主构建流程。哪种情况用哪个 skill，[ask-matt](https://aihero.dev/skills-ask-matt) 是覆盖整个集合的路由器。
