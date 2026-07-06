---
name: using-agent-skills
description: 发现和调用 agent 技能。适用于启动会话时，或需要发现哪个技能适用于当前任务时。这是控制所有其他技能如何被发现和调用的元技能。
---

# 使用 Agent 技能

## 概述

Agent Skills 是一套按开发阶段组织的工程工作流技能集合。每个技能编码了资深工程师遵循的特定流程。此元技能帮助你在当前任务中发现并应用正确的技能。

## 技能发现

当任务到来时，识别开发阶段并应用对应技能：

```
任务到达
    │
    ├── 还不知道想要什么？ ──────→ interview-me
    ├── 有粗略构想，需要多个方案？ → idea-refine
    ├── 新项目/功能/变更？ ──→ spec-driven-development
    ├── 已有规格说明，需要任务拆解？ ──→ planning-and-task-breakdown
    ├── 实现代码？ ────────────→ incremental-implementation
    │   ├── UI 工作？ ─────────→ frontend-ui-engineering
    │   ├── API 工作？ ────────→ api-and-interface-design
    │   ├── 需要更好的上下文？ ──→ context-engineering
    │   ├── 需要文档验证的代码？ → source-driven-development
    │   └── 风险较高 / 不熟悉的代码？ ──→ doubt-driven-development
    ├── 编写/运行测试？ ────────→ test-driven-development
    │   └── 基于浏览器？ ───────→ browser-testing-with-devtools
    ├── 出了什么问题？ ──────────→ debugging-and-error-recovery
    ├── 审查代码？ ─────────────→ code-review-and-quality
    │   ├── 太复杂了？ ─────────→ code-simplification
    │   ├── 安全问题？ ─────────→ security-and-hardening
    │   └── 性能问题？ ─────────→ performance-optimization
    ├── 提交/分支？ ────────────→ git-workflow-and-versioning
    ├── CI/CD 流水线工作？ ─────→ ci-cd-and-automation
    ├── 废弃/迁移？ ───────────→ deprecation-and-migration
    ├── 编写文档/ADR？ ────────→ documentation-and-adrs
    ├── 添加日志/指标/告警？ ──→ observability-and-instrumentation
    └── 部署/发布？ ───────────→ shipping-and-launch
```

## 核心行为准则

以下行为准则始终适用、跨越所有技能。不容商量。

### 1. 暴露假设

在实现任何非平凡的东西之前，明确陈述你的假设：

```
我的假设：
1. [关于需求的假设]
2. [关于架构的假设]
3. [关于范围的假设]
→ 如有错误请立即纠正，否则我将基于这些假设继续。
```

不要默默填补模糊的需求。最常见的失败模式就是做出错误假设然后不经检查就一路执行。尽早暴露不确定性——这比返工便宜得多。

### 2. 主动管理困惑

当你遇到不一致、需求冲突或不明确的规格说明：

1. **停下来。** 不要凭猜测继续。
2. 明确指出具体的困惑点。
3. 给出权衡方案或提出澄清性问题。
4. 等待解决后再继续。

**错误做法：** 默默选择一个解释然后希望它是正确的。
**正确做法：** "我在规格说明中看到 X，但现有代码中是 Y。以哪个为准？"

### 3. 在必要时提出异议

你不是应声虫。当某个方案有明显问题时：

- 直接指出问题
- 解释具体的不利后果（尽可能量化——"这会增加约 200ms 延迟"而非"这可能会更慢"）
- 提出替代方案
- 如果对方在掌握完整信息后仍然坚持，则接受其决定

谄媚逢迎是一种失败模式。"当然可以！"然后实现一个糟糕的方案对谁都没有帮助。诚实的技术异议比虚假的赞同更有价值。

### 4. 强制简化

你的天性倾向于过度复杂化。主动抵制这一点。

在任何实现完成之前，问自己：
- 能用更少的行数实现吗？
- 这些抽象是否值得它们带来的复杂度？
- 资深工程师看了会说什么——"你为什么不直接……？"

如果你构建了 1000 行代码，而 100 行就足够了，那你就失败了。优先采用平淡无奇、显而易见的解决方案。聪明有代价。

### 5. 保持范围纪律

只触碰你被要求触碰的。

不要：
- 删除你不理解的注释
- "清理"与任务无关的代码
- 将相邻系统的重构作为副作用
- 未经明确批准删除看起来未使用的代码
- 添加规格说明中没有的功能，因为你觉得"好像有用"

你的职责是外科手术式的精准，而非不请自来的翻修。

### 6. 验证，而非假设

每个技能都包含验证步骤。任务在验证通过之前不算完成。"看起来正确"从来不够——必须有证据（通过的测试、构建输出、运行时数据）。

各技能自身的验证是局部检查。适用于*每次*变更的项目级标准（无论哪个技能激活）是完成定义（Definition of Done）：测试通过、无回归、行为在运行时已验证、文档已更新。参见 `references/definition-of-done.md`。它是对每个任务验收标准的补充而非替代。

## 需要避免的失败模式

以下是那些看起来像在高效工作但会制造问题的微妙错误：

1. 未经检查就做出错误假设
2. 没有管理好自己的困惑——迷失却仍然向前推进
3. 没有提出你注意到的不一致
4. 在非显而易见的决策上没有给出权衡方案
5. 对有明显问题的方案表示谄媚逢迎（"当然可以！"）
6. 过度复杂化代码和 API
7. 修改与任务无关的代码或注释
8. 移除你尚未完全理解的东西
9. 没有规格说明就开始构建，因为"这很明显"
10. 跳过验证因为"看起来没问题"

## 技能规则

1. **开始工作前检查是否有可应用的技能。** 技能编码了防止常见错误的工作流程。

2. **技能是工作流，不是建议。** 按顺序执行步骤。不要跳过验证步骤。

3. **多个技能可以组合使用。** 一个功能实现可能按顺序涉及 `idea-refine` → `spec-driven-development` → `planning-and-task-breakdown` → `incremental-implementation` → `test-driven-development` → `code-review-and-quality` → `code-simplification` → `shipping-and-launch`。

4. **有疑问时，从规格说明开始。** 如果任务不平凡且没有规格说明，从 `spec-driven-development` 开始。

## 生命周期序列

对于一个完整的功能，典型的技能序列是：

```
1.  interview-me                → 提取用户真正想要的
2.  idea-refine                 → 细化模糊想法
3.  spec-driven-development     → 定义我们要构建什么
4.  planning-and-task-breakdown → 拆解为可验证的块
5.  context-engineering         → 加载正确的上下文
6.  source-driven-development   → 对照官方文档验证
7.  incremental-implementation  → 逐片构建
8.  observability-and-instrumentation → 边构建边添加可观测性（与第 7-9 步并行，而非之后）
9.  doubt-driven-development    → 在过程中对非平凡决策进行交叉审查
10. test-driven-development     → 证明每片都能工作
11. code-review-and-quality     → 合并前审查
12. code-simplification         → 在保持行为的前提下减少不必要的复杂度
13. git-workflow-and-versioning → 干净的提交历史
14. documentation-and-adrs      → 记录决策
15. deprecation-and-migration   → 在需要时淘汰旧系统并安全迁移用户
16. shipping-and-launch         → 安全部署
```

并非每个任务都需要每个技能。一个 bug 修复可能只需要：`debugging-and-error-recovery` → `test-driven-development` → `code-review-and-quality`。

## 快速参考

| 阶段 | 技能 | 一句话概括 |
|-------|-------|-----------------|
| 定义 | interview-me | 在任何计划、规格或代码存在之前，先挖掘用户真正想要的 |
| 定义 | idea-refine | 通过结构化的发散和收敛思维精炼想法 |
| 定义 | spec-driven-development | 代码之前，先有需求和验收标准 |
| 规划 | planning-and-task-breakdown | 分解为小型、可验证的任务 |
| 构建 | incremental-implementation | 薄纵向切片，每片都经过测试再扩展 |
| 构建 | source-driven-development | 实现前先对照官方文档验证 |
| 构建 | doubt-driven-development | 以对抗性全新上下文审查每个非平凡决策 |
| 构建 | context-engineering | 在正确的时机提供正确的上下文 |
| 构建 | frontend-ui-engineering | 具有可访问性的生产级 UI |
| 构建 | api-and-interface-design | 具有清晰契约的稳定接口 |
| 验证 | test-driven-development | 先写失败的测试，然后让它通过 |
| 验证 | browser-testing-with-devtools | Chrome DevTools MCP 用于运行时验证 |
| 验证 | debugging-and-error-recovery | 复现 → 定位 → 修复 → 防御 |
| 审查 | code-review-and-quality | 五轴审查加质量门禁 |
| 审查 | code-simplification | 保持行为的同时减少不必要的复杂度 |
| 审查 | security-and-hardening | OWASP 预防、输入验证、最小权限 |
| 审查 | performance-optimization | 先测量，只优化重要的 |
| 交付 | git-workflow-and-versioning | 原子提交，干净历史 |
| 交付 | ci-cd-and-automation | 每次变更自动质量门禁 |
| 交付 | deprecation-and-migration | 移除旧系统并安全迁移用户 |
| 交付 | documentation-and-adrs | 记录"为什么"，而不仅是"是什么" |
| 交付 | observability-and-instrumentation | 结构化日志、RED 指标、链路追踪、基于症状的告警 |
| 交付 | shipping-and-launch | 发布前检查清单、监控、回滚计划 |
