---
name: documentation-and-adrs
description: 记录决策和文档。适用于制定架构决策、更改公共 API、发布功能，或者需要记录未来工程师和 agent 理解代码仓库所需的上下文。
---

# 文档与 ADR

## 概述

记录决策，而不仅仅是代码。最有价值的文档捕获了*为什么*——导致一个决策的上下文、约束和权衡。代码展示了构建了*什么*；文档解释了*为什么这样构建*以及*考虑了哪些替代方案*。这个上下文对在代码仓库中工作的未来人类和 agent 至关重要。

## 何时使用

- 做出重大架构决策
- 在竞争方案之间选择
- 添加或更改公共 API
- 发布改变面向用户行为的功能
- 让新团队成员（或 agent）了解项目
- 当你发现自己在反复解释同一件事

**何时不使用：** 不要为显而易见的代码写文档。不要添加重述代码已经表达的内容的注释。不要为一次性的原型写文档。

## 架构决策记录（ADR）

ADR 捕获重大技术决策背后的推理。它们是你能写的最有价值的文档。

### 何时编写 ADR

- 选择一个框架、库或主要依赖
- 设计数据模型或数据库模式
- 选择认证策略
- 决定 API 架构（REST vs. GraphQL vs. tRPC）
- 在构建工具、托管平台或基础设施之间选择
- 任何逆转代价高昂的决策

### ADR 模板

将 ADR 存储在 `docs/decisions/` 中，使用顺序编号：

```markdown
# ADR-001：使用 PostgreSQL 作为主数据库

## 状态
已接受 | 被 ADR-XXX 取代 | 已弃用

## 日期
2025-01-15

## 上下文
我们需要一个用于任务管理应用的主数据库。关键需求：
- 关系数据模型（具有关系的用户、任务、团队）
- 用于任务状态变更的 ACID 事务
- 支持任务内容的全文搜索
- 托管服务可用（小型团队，有限的运维能力）

## 决策
使用 PostgreSQL 配合 Prisma ORM。

## 考虑的替代方案

### MongoDB
- 优点：灵活的模式，易于上手
- 缺点：我们的数据本质上是关系型的；需要手动管理关系
- 拒绝原因：关系数据在文档存储中会导致复杂的连接或数据重复

### SQLite
- 优点：零配置，嵌入式，读取速度快
- 缺点：有限的并发写入支持，没有生产环境的托管服务
- 拒绝原因：不适合生产环境中的多用户 Web 应用

### MySQL
- 优点：成熟，广泛支持
- 缺点：PostgreSQL 有更好的 JSON 支持、全文搜索和生态系统工具
- 拒绝原因：PostgreSQL 更适合我们的功能需求

## 后果
- Prisma 提供类型安全的数据库访问和迁移管理
- 我们可以使用 PostgreSQL 的全文搜索，而无需添加 Elasticsearch
- 团队需要 PostgreSQL 知识（标准技能，低风险）
- 在托管服务上托管（Supabase、Neon 或 RDS）
```

### ADR 生命周期

```
PROPOSED → ACCEPTED → (SUPERSEDED 或 DEPRECATED)
```

- **不要删除旧的 ADR。** 它们捕获历史上下文。
- 当决策发生变化时，编写一个引用并取代旧 ADR 的新 ADR。

## 内联文档

### 何时写注释

注释*为什么*，而不是*什么*：

```typescript
// 差：重述代码
// 将计数器加 1
counter += 1;

// 好：解释非显而易见的意图
// 速率限制使用滑动窗口 —— 在窗口边界重置计数器，
// 而不是在固定时间表上，以防止窗口边缘的突发攻击
if (now - windowStart > WINDOW_SIZE_MS) {
  counter = 0;
  windowStart = now;
}
```

### 何时不写注释

```typescript
// 不要为自解释的代码写注释
function calculateTotal(items: CartItem[]): number {
  return items.reduce((sum, item) => sum + item.price * item.quantity, 0);
}

// 不要为现在就应该做的事情留 TODO 注释
// TODO: 添加错误处理  ← 直接添加

// 不要留被注释掉的代码
// const oldImplementation = () => { ... }  ← 删除它，git 有历史记录
```

### 记录已知的坑

```typescript
/**
 * 重要：此函数必须在第一次渲染之前调用。
 * 如果在水合之后调用，会导致无样式内容的闪烁，
 * 因为主题上下文在 SSR 期间不可用。
 *
 * 完整的设计原理请参见 ADR-003。
 */
export function initializeTheme(theme: Theme): void {
  // ...
}
```

## API 文档

对于公共 API（REST、GraphQL、库接口）：

### 内联类型（TypeScript 首选）

```typescript
/**
 * 创建一个新任务。
 *
 * @param input - 任务创建数据（标题必需，描述可选）
 * @returns 创建的任务，带有服务器生成的 ID 和时间戳
 * @throws {ValidationError} 如果标题为空或超过 200 个字符
 * @throws {AuthenticationError} 如果用户未认证
 *
 * @example
 * const task = await createTask({ title: '购买日用品' });
 * console.log(task.id); // "task_abc123"
 */
export async function createTask(input: CreateTaskInput): Promise<Task> {
  // ...
}
```

### REST API 的 OpenAPI / Swagger

```yaml
paths:
  /api/tasks:
    post:
      summary: 创建一个任务
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateTaskInput'
      responses:
        '201':
          description: 任务已创建
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Task'
        '422':
          description: 验证错误
```

## README 结构

每个项目应该有一个覆盖以下内容的 README：

```markdown
# 项目名称

一段话描述这个项目做什么。

## 快速开始
1. 克隆仓库
2. 安装依赖：`npm install`
3. 设置环境：`cp .env.example .env`
4. 运行开发服务器：`npm run dev`

## 命令
| 命令 | 描述 |
|---------|-------------|
| `npm run dev` | 启动开发服务器 |
| `npm test` | 运行测试 |
| `npm run build` | 生产构建 |
| `npm run lint` | 运行代码检查器 |

## 架构
项目结构和关键设计决策的简要概述。
链接到 ADR 获取详细信息。

## 贡献
如何贡献、编码标准、PR 流程。
```

## 更新日志维护

对于已发布的功能：

```markdown
# 更新日志

## [1.2.0] - 2025-01-20
### 新增
- 任务分享：用户可以与团队成员分享任务 (#123)
- 任务分配的邮件通知 (#124)

### 修复
- 快速点击创建按钮时出现重复任务 (#125)

### 变更
- 任务列表现在每页加载 50 项（原为 20），以改善用户体验 (#126)
```

## 为 Agent 编写文档

为 AI agent 上下文的特殊考虑：

- **CLAUDE.md / rules 文件** —— 记录项目约定，以便 agent 遵循它们
- **Spec 文件** —— 保持规格更新，以便 agent 构建正确的东西
- **ADR** —— 帮助 agent 理解过去做出决策的原因（防止重新决策）
- **内联坑点** —— 防止 agent 落入已知的陷阱

## 常见合理化借口

| 合理化借口 | 现实 |
|---|---|
| "代码是自文档化的" | 代码展示"什么"。它不展示"为什么"、拒绝了什么替代方案或适用什么约束。 |
| "等 API 稳定后我们再写文档" | 当你写文档时，API 稳定得更快。文档是设计的第一个测试。 |
| "没人读文档" | Agent 读。未来的工程师读。3 个月后的你读。 |
| "ADR 是额外开销" | 一个 10 分钟的 ADR 防止了 6 个月后关于同一决策的 2 小时争论。 |
| "注释会过时" | 关于*为什么*的注释是稳定的。关于*什么*的注释会过时——这就是为什么你只写前者。 |

## 红旗信号

- 没有书面推理的架构决策
- 没有文档或类型的公共 API
- README 没有说明如何运行项目
- 被注释掉的代码而不是删除
- 已经存在数周的 TODO 注释
- 有重大架构选择的项目中没有 ADR
- 重述代码而不是解释意图的文档

## 验证

文档编写后：

- [ ] 所有重大架构决策都存在 ADR
- [ ] README 涵盖了快速开始、命令和架构概述
- [ ] API 函数有参数和返回类型文档
- [ ] 已知的坑在其关键位置内联记录
- [ ] 没有被注释掉的代码残留
- [ ] Rules 文件（CLAUDE.md 等）是最新且准确的
