## 功能说明

`wait-what` 是当一条消息没讲明白时你输入的东西。[Agent](https://www.aihero.dev/ai-coding-dictionary/agent) 随后会重新表述它刚说的话：补上你缺失的上下文，用平实的英语写，并使用你项目 `CONTEXT.md` 里的词汇。

这个技能只有三行长。这是设计,不是未完成的草稿。跟啰嗦作斗争的技能,失败方式是越长越糟:一份四百行的「简洁」技能照样让[模型](https://www.aihero.dev/ai-coding-dictionary/model)啰嗦,因为模型读的是篇幅,不是恳求。这个技能只带一个精准的引导词,别的什么也没有。

## 何时使用

你输入 `/wait-what` 来调用它。Agent 不会自己使用它,也不该。只有你知道自己什么时候跟丢了。

一旦发现自己在略读,立刻用。Agent 漂进了它自己发明的术语,叠了五个缩写,或者解释一个你从没见过前提的决策。它修复的是你正在进行的对话。要想让术语压根不来,用 [grill-with-docs](https://aihero.dev/skills-grill-with-docs),它在一开始就建立共同语言。

## 名字就是机制

引导词是 **wait**。「要简洁」是关于 Agent 输出的指令,模型服从它的方式是删词,把你丢得更远。**wait** 是关于*你*的状态。它在说:这里没理解。一个听到「说短点」的 Agent 写电报。一个听到「等等,你把我丢了」的 Agent 会退回去解释。

这个区别就是整个技能。每个流行的治啰嗦方案都在命名*输出*:`/tldr`、`/no-fluff`、`/talk-normal`。模型过度纠正,进入一种更短但一样不清楚的原始人语气。命名*听众*则一次性要两半:更少的词**和**你缺失的上下文。

技能说的是重新表述**那个**,不是「那条上一条消息」。让你跟丢的通常比一个段落大,所以由 Agent 决定要退多远。

## 它接上你已经有的语言

正文复用你全局 `CLAUDE.md` 和项目 `CONTEXT.md` 里已有的引导词。ASD-STE100 简化技术英语规定语域。共通语言提供名词。技能、`CLAUDE.md` 和 `CONTEXT.md` 伸手拿的是同一个 [token](https://www.aihero.dev/ai-coding-dictionary/token),所以调用它不是一个新指令。它是提醒一条 Agent 已经答应的指令。

如果没有 `CONTEXT.md`,技能照样工作。你只是损失领域词汇那一半。

## 效果如何判断

- 重新表述**更短更清楚**,而不是更短更生硬。
- 它补上你缺失的前提,而不只是删词。
- 项目的名词替换掉发明的词。你 `CONTEXT.md` 里的术语回来了。
- 你可以连着用两次,它不会退化成惜字如金。

## 在系统中的位置

`wait-what` 可以在任何时刻、任何对话里、任何其他技能内部使用。它在事后修复一条消息。真正的解药是一开始就约定好的共同语言,那就是 [grill-with-docs](https://aihero.dev/skills-grill-with-docs):一场[问询](https://www.aihero.dev/ai-coding-dictionary/grilling)会话,一边进行一边跑 [domain-modeling](https://aihero.dev/skills-domain-modeling),于是你们俩共同使用的词落进你的 `CONTEXT.md`。不确定哪个技能适合当下时,[ask-matt](https://aihero.dev/skills-ask-matt) 会为你导航。
