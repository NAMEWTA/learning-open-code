# 技能机制（Skill mechanics）

[`writing-for-agents`](SKILL.md) 中 skill 特有的分支：当文档是一份 skill 时，哪些东西会改变——frontmatter、调用方式选择，以及路由技能。除此之外的撰写之道，都是 `SKILL.md` 中的通用参考。

## 调用方式

两种选择，权衡两种负载：

- **模型调用（model-invoked）** 的 skill 保留 `description`，agent 可以自主触发它——其他 skill 也能到达它。你仍然可以输入它的名字：模型调用始终*包含*用户可达性；description 只会增加 agent 的发现能力，绝不会移除人工可达性。description 是 skill 顶层的上下文指针，被迫时刻保持加载——用永久的上下文负载换取可发现性。一份内容全是参考的模型调用 skill，也是共享参考的一个归宿：其他 skill 可以调用它，于是多个 skill 需要的参考就住在一处。机制：省略 `disable-model-invocation`，并写一个面向模型、携带触发分支的 description（`SKILL.md` 中的指针撰写规则完全适用）。
- **用户调用（user-invoked）** 的 skill 把 description 从 agent 的视野中剥离：只有人类输入它的名字才能调用它，其他 skill 都不行。零上下文负载，但花的是认知负载——你就是那个必须记住它存在的索引。机制：设置 `disable-model-invocation: true`；`description` 变成面向人类的——一行摘要，触发器列表剥掉。

只有 agent 必须自己到达这份 skill、或另一份 skill 必须到达它时，才选模型调用。如果它只会通过人工触发，就做成用户调用，不付上下文负载。

两份用户调用 skill 都需要、却哪一份都放不下的共享参考——由于没有 description，两者都无法触发对方——把它推到 skill 体系之外的普通文件里：任何 skill 都可以指向的外部参考。

## 按调用方式拆分

调用方式的拆分切口（序列切口在 `SKILL.md` 中）：当你有一个独特的引导词、应该单独触发它——一个你真正在 prompts 里使用的触发词——或者另一份 skill 必须到达它时，拆出一份模型调用的 skill。你要为这条新的常驻 description 付出上下文负载，所以这种独立可达性必须值得。

## 路由技能

当用户调用 skill 多到你记不过来时，堆积起来的认知负载由**路由技能（router skill）** 治愈：一份用户调用的 skill，它点名其他 skill 以及各自该何时使用，于是人类只需要记住一份 skill，而不是很多份。它只能提示，永远不能触发它们：用户调用 skill 没有 description，所以除了人类，没有东西能到达它们。
