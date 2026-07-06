---
name: code-simplification
description: 简化代码以提高清晰度。适用于在不改变行为的前提下重构代码以提高可读性时。当代码可以运行、但阅读、维护或扩展起来比应有的难度更高时使用。当审查已积累不必要复杂度的代码时使用。
---

# 代码简化

> 灵感来源于 [Claude Code Simplifier 插件](https://github.com/anthropics/claude-plugins-official/blob/main/plugins/code-simplifier/agents/code-simplifier.md)。在此适配为适用于任何 AI 编程 agent 的模型无关、流程驱动的技能。

## 概述

通过降低复杂度来简化代码，同时精确保持原有行为。目标不是更少的行数——而是让代码更易于阅读、理解、修改和调试。每次简化都必须通过一个简单的检验："新团队成员是否能比原始版本更快地理解这段代码？"

## 适用场景

- 功能已经可以工作且测试通过，但实现给人感觉比实际需要的要重
- 代码审查中发现可读性或复杂度问题
- 遇到深层嵌套逻辑、过长的函数或不清晰的命名
- 重构赶时间写出来的代码
- 整合分散在多个文件中的相关逻辑
- 合并引入了重复或不一致的变更之后

**不适用场景：**

- 代码已经干净且可读 —— 不要为了简化而简化
- 你还不理解代码的功能 —— 先理解再简化
- 代码对性能敏感，"更简单"的版本在性能上会明显变慢
- 你即将完全重写整个模块 —— 在即将抛弃的代码上简化是浪费精力

## 五大原则

### 1. 精确保持行为

不要改变代码的功能——只改变它的表达方式。所有输入、输出、副作用、错误行为和边界情况必须保持不变。如果不确定某个简化是否保持了行为，就不要做。

```
每次变更前自问：
→ 对于每个输入，是否产生相同的输出？
→ 是否保持相同的错误行为？
→ 是否保持相同的副作用和执行顺序？
→ 所有现有测试是否在不修改的情况下仍然通过？
```

### 2. 遵循项目约定

简化意味着让代码与代码库更加一致，而不是强加外部偏好。在简化之前：

```
1. 阅读 CLAUDE.md / 项目约定
2. 研究邻近代码如何处理类似模式
3. 匹配项目的以下风格：
   - import 顺序和模块系统
   - 函数声明风格
   - 命名约定
   - 错误处理模式
   - 类型注解深度
```

破坏项目一致性的简化不是简化——是折腾。

### 3. 清晰优于聪明

当紧凑版本需要思考才能解析时，显式的代码优于紧凑的代码。

```typescript
// UNCLEAR: Dense ternary chain
const label = isNew ? 'New' : isUpdated ? 'Updated' : isArchived ? 'Archived' : 'Active';

// CLEAR: Readable mapping
function getStatusLabel(item: Item): string {
  if (item.isNew) return 'New';
  if (item.isUpdated) return 'Updated';
  if (item.isArchived) return 'Archived';
  return 'Active';
}
```

```typescript
// UNCLEAR: Chained reduces with inline logic
const result = items.reduce((acc, item) => ({
  ...acc,
  [item.id]: { ...acc[item.id], count: (acc[item.id]?.count ?? 0) + 1 }
}), {});

// CLEAR: Named intermediate step
const countById = new Map<string, number>();
for (const item of items) {
  countById.set(item.id, (countById.get(item.id) ?? 0) + 1);
}
```

### 4. 保持平衡

简化有一个失败模式：过度简化。注意以下陷阱：

- **过度内联**——移除了为概念命名的辅助函数，让调用点更难以阅读
- **合并不相关的逻辑**——将两个简单函数合并成一个复杂函数，并没有变简单
- **移除"不必要"的抽象**——某些抽象是为可扩展性或可测试性而存在，而非因为复杂度
- **以行数为优化目标**——更少的行数不是目标；更容易理解才是

### 5. 作用域限定在变更内容

默认只简化最近修改的代码。避免对无关代码进行顺手重构，除非明确要求扩大范围。无限定范围的简化会在 diff 中产生噪音，并带来意外的回归风险。

## 简化流程

### 第 1 步：触碰之前先理解（切斯特顿之栏，Chesterton's Fence）

在变更或移除任何东西之前，先理解它为什么存在。这就是切斯特顿之栏：如果你在路中间看到一道围栏却不理解它为什么在那里，不要拆掉它。先理解原因，然后判断原因是否仍然成立。

```
简化之前先回答：
- 这段代码的职责是什么？
- 什么调用了它？它调用了什么？
- 边界情况和错误路径有哪些？
- 是否有定义其预期行为的测试？
- 它为什么会写成这样？（性能？平台约束？历史原因？）
- 检查 git blame：这段代码的原始上下文是什么？
```

如果你无法回答这些问题，说明还没准备好进行简化。先去阅读更多上下文。

### 第 2 步：识别简化机会

扫描以下模式——每个都是具体信号，而非模糊的坏味道：

**结构复杂度：**

| 模式 | 信号 | 简化方式 |
|---------|--------|----------------|
| 深层嵌套（3+ 层） | 控制流难以跟踪 | 将条件提取为卫语句或辅助函数 |
| 长函数（50+ 行） | 承担了多个职责 | 拆分为具有描述性名称的聚焦函数 |
| 嵌套三元表达式 | 需要心理解析栈 | 替换为 if/else 链、switch 或查表对象 |
| 布尔参数标志 | `doThing(true, false, true)` | 替换为选项对象或独立函数 |
| 重复的条件判断 | 多处出现相同的 `if` 检查 | 提取为命名良好的谓词函数 |

**命名与可读性：**

| 模式 | 信号 | 简化方式 |
|---------|--------|----------------|
| 泛型名称 | `data`、`result`、`temp`、`val`、`item` | 重命名为描述内容的名称：`userProfile`、`validationErrors` |
| 缩写名称 | `usr`、`cfg`、`btn`、`evt` | 使用完整单词，除非缩写是通用的（`id`、`url`、`api`） |
| 误导性名称 | 名为 `get` 的函数却修改了状态 | 重命名以反映实际行为 |
| 解释"是什么"的注释 | `// increment counter` 在 `count++` 上方 | 删除注释——代码已经足够清晰 |
| 解释"为什么"的注释 | `// Retry because the API is flaky under load` | 保留——这些承载了代码无法表达的意图 |

**冗余：**

| 模式 | 信号 | 简化方式 |
|---------|--------|----------------|
| 重复逻辑 | 相同的 5+ 行代码出现在多处 | 提取为共享函数 |
| 死代码 | 不可达分支、未使用的变量、被注释掉的代码块 | 移除（确认确实已死后） |
| 不必要的抽象 | 未增加任何价值的包装器 | 内联包装器，直接调用底层函数 |
| 过度设计的模式 | 工厂的工厂、只有一种策略的策略模式 | 替换为简单直接的方式 |
| 冗余的类型断言 | 强制转换为已经被推断出的类型 | 移除断言 |

### 第 3 步：逐步应用变更

一次只做一项简化。每次变更后运行测试。**将重构变更与功能或 bug 修复变更分开提交。** 一个既重构又添加功能的 PR 应该是两个 PR——将它们拆分。

```
每次简化：
1. 进行变更
2. 运行测试套件
3. 如果测试通过 → 提交（或继续下一个简化）
4. 如果测试失败 → 回退并重新评估
```

避免将多个简化批量合并成一次未测试的变更。如果出了问题，你需要知道是哪个简化引起的。

**500 行规则：** 如果某次重构需要触及超过 500 行代码，请投入自动化（codemod、sed 脚本、AST 转换）而非手工修改。这种规模的手工编辑容易出错，审查起来也令人疲倦。

### 第 4 步：验证结果

所有简化完成后，退后一步整体评估：

```
对比前后：
- 简化后的版本是否真正更容易理解？
- 是否引入与代码库不一致的新模式？
- diff 是否干净且适合审查？
- 团队成员是否会同意这次变更？
```

如果"简化后"的版本更难理解或审查，请回退。并非每次简化尝试都能成功。

## 各语言具体指南

### TypeScript / JavaScript

```typescript
// SIMPLIFY: Unnecessary async wrapper
// Before
async function getUser(id: string): Promise<User> {
  return await userService.findById(id);
}
// After
function getUser(id: string): Promise<User> {
  return userService.findById(id);
}

// SIMPLIFY: Verbose conditional assignment
// Before
let displayName: string;
if (user.nickname) {
  displayName = user.nickname;
} else {
  displayName = user.fullName;
}
// After
const displayName = user.nickname || user.fullName;

// SIMPLIFY: Manual array building
// Before
const activeUsers: User[] = [];
for (const user of users) {
  if (user.isActive) {
    activeUsers.push(user);
  }
}
// After
const activeUsers = users.filter((user) => user.isActive);

// SIMPLIFY: Redundant boolean return
// Before
function isValid(input: string): boolean {
  if (input.length > 0 && input.length < 100) {
    return true;
  }
  return false;
}
// After
function isValid(input: string): boolean {
  return input.length > 0 && input.length < 100;
}
```

### Python

```python
# SIMPLIFY: Verbose dictionary building
# Before
result = {}
for item in items:
    result[item.id] = item.name
# After
result = {item.id: item.name for item in items}

# SIMPLIFY: Nested conditionals with early return
# Before
def process(data):
    if data is not None:
        if data.is_valid():
            if data.has_permission():
                return do_work(data)
            else:
                raise PermissionError("No permission")
        else:
            raise ValueError("Invalid data")
    else:
        raise TypeError("Data is None")
# After
def process(data):
    if data is None:
        raise TypeError("Data is None")
    if not data.is_valid():
        raise ValueError("Invalid data")
    if not data.has_permission():
        raise PermissionError("No permission")
    return do_work(data)
```

### React / JSX

```tsx
// SIMPLIFY: Verbose conditional rendering
// Before
function UserBadge({ user }: Props) {
  if (user.isAdmin) {
    return <Badge variant="admin">Admin</Badge>;
  } else {
    return <Badge variant="default">User</Badge>;
  }
}
// After
function UserBadge({ user }: Props) {
  const variant = user.isAdmin ? 'admin' : 'default';
  const label = user.isAdmin ? 'Admin' : 'User';
  return <Badge variant={variant}>{label}</Badge>;
}

// SIMPLIFY: Prop drilling through intermediate components
// Before — consider whether context or composition solves this better.
// This is a judgment call — flag it, don't auto-refactor.
```

## 常见借口

| 借口 | 事实 |
|---|---|
| "已经能用了，不需要改" | 难以阅读但能工作的代码，在出问题时也难以修复。现在简化可以为你将来的每次变更节省时间。 |
| "行数越少越简单" | 1 行的嵌套三元表达式并不比 5 行的 if/else 更简单。简单关乎理解速度，而非行数。 |
| "我顺便把这段无关的代码也简化一下" | 未限定范围的简化在 diff 中产生噪音，并在你没打算改的代码中引入回归风险。保持专注。 |
| "类型定义已经足够文档化了" | 类型记录的是结构，不是意图。命名良好的函数比类型签名更好地解释了"为什么"。 |
| "这个抽象以后可能会用到" | 不要保留推测性的抽象。如果现在没用到，它只是没有价值的复杂度。移除它，需要时再加回来。 |
| "原作者肯定有原因" | 也许有。检查 git blame —— 应用切斯特顿之栏。但累积的复杂度常常没有原因，只是赶时间迭代的残留。 |
| "我顺便在加这个功能时重构一下" | 把重构和功能开发分开。混合的变更更难审查、更难回退、更难以在历史中理解。 |

## 危险信号

- 需要修改测试才能通过的简化（你可能改变了行为）
- "简化后"的代码比原始代码更长且更难理解
- 按照你的个人偏好而非项目约定来重命名
- 移除错误处理因为"这让代码更简洁"
- 简化你尚未完全理解的代码
- 将许多简化批量合并成一次大型的、难以审查的提交
- 未经要求就重构当前任务范围之外的代码

## 验证

完成一轮简化后：

- [ ] 所有现有测试在不修改的情况下通过
- [ ] 构建成功，无新增警告
- [ ] Linter/格式化工具通过（无风格回归）
- [ ] 每次简化都是一次可审查的、渐进的变更
- [ ] Diff 干净——无无关变更混入
- [ ] 简化后的代码遵循项目约定（对照 CLAUDE.md 或等效文件检查）
- [ ] 没有移除或削弱任何错误处理
- [ ] 没有遗留死代码（未使用的 import、不可达分支）
- [ ] 团队成员或审查 agent 会认可这次变更为净改进
