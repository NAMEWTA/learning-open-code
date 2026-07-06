---
name: api-and-interface-design
description: 指导稳定的 API 和接口设计。适用于设计 API、模块边界或任何公共接口，创建 REST 或 GraphQL 端点，定义模块间的类型契约，或建立前后端之间的边界。
---

# API 与接口设计

## 概述

设计稳定、文档完善、难以误用的接口。好接口让正确的事容易做，让错误的事难以做。这适用于 REST API、GraphQL schema、模块边界、组件 props，以及任何代码之间进行通信的接触面。

## 适用场景

- 设计新的 API 端点
- 定义模块边界或团队间的契约
- 创建组件 props 接口
- 建立影响 API 形态的数据库 schema
- 修改现有的公共接口

## 核心原则

### Hyrum 定律

> 当 API 的使用者数量足够多时，系统的所有可观察行为都会被某些人所依赖，无论你在契约中承诺了什么。

这意味着：每一个公共行为 —— 包括未文档化的怪异行为、错误消息文本、时序和排序 —— 一旦用户依赖它，就变成了事实上的契约。设计启示：

- **有意地控制你暴露的内容。** 每个可观察行为都可能成为一项承诺。
- **不要泄露实现细节。** 如果用户可以观察到它，他们就会依赖它。
- **在设计时就规划弃用方案。** 参见 `deprecation-and-migration` 了解如何安全地移除用户已依赖的内容。
- **仅靠测试不够。** 即使有完美的契约测试，Hyrum 定律也意味着"安全"的变更可能破坏依赖未文档化行为的真实用户。

### 单一版本原则

避免强制消费者在同一依赖或 API 的多个版本之间选择。当不同消费者需要同一东西的不同版本时，就会出现钻石依赖问题。为只有一个版本存在的世界而设计 —— 扩展而非分叉。

### 1. 契约优先

在实现之前先定义接口。契约即规范 —— 实现紧随其后。

```typescript
// 先定义契约
interface TaskAPI {
  // 创建一个 task 并返回包含服务端生成字段的已创建 task
  createTask(input: CreateTaskInput): Promise<Task>;

  // 返回与筛选条件匹配的分页 tasks
  listTasks(params: ListTasksParams): Promise<PaginatedResult<Task>>;

  // 返回单个 task，如未找到则抛出 NotFoundError
  getTask(id: string): Promise<Task>;

  // 部分更新 —— 仅更新提供的字段
  updateTask(id: string, input: UpdateTaskInput): Promise<Task>;

  // 幂等删除 —— 即使已被删除也能成功
  deleteTask(id: string): Promise<void>;
}
```

### 2. 一致的错误语义

选定一种错误策略并在各处统一使用：

```typescript
// REST: HTTP 状态码 + 结构化错误体
// 每个错误响应遵循相同的结构
interface APIError {
  error: {
    code: string;        // 机器可读："VALIDATION_ERROR"
    message: string;     // 人类可读："Email is required"
    details?: unknown;   // 有帮助时提供额外上下文
  };
}

// 状态码映射
// 400 → 客户端发送了无效数据
// 401 → 未认证
// 403 → 已认证但未授权
// 404 → 资源未找到
// 409 → 冲突（重复、版本不匹配）
// 422 → 验证失败（语义上无效）
// 500 → 服务端错误（绝不暴露内部细节）
```

**不要混用模式。** 如果某些端点抛异常，另一些返回 null，还有一些返回 `{ error }` —— 消费者就无法预测行为。

### 3. 在边界处验证

信任内部代码。在外部输入进入系统的边界处进行验证：

```typescript
// 在 API 边界处验证
app.post('/api/tasks', async (req, res) => {
  const result = CreateTaskSchema.safeParse(req.body);
  if (!result.success) {
    return res.status(422).json({
      error: {
        code: 'VALIDATION_ERROR',
        message: 'Invalid task data',
        details: result.error.flatten(),
      },
    });
  }

  // 验证通过后，内部代码信任这些类型
  const task = await taskService.create(result.data);
  return res.status(201).json(task);
});
```

验证应放在哪里：
- API 路由处理器（用户输入）
- 表单提交处理器（用户输入）
- 外部服务响应解析（第三方数据 —— **始终视为不可信**）
- 环境变量加载（配置）

> **第三方 API 响应是不可信数据。** 在将其用于任何逻辑、渲染或决策之前，验证其结构和内容。被入侵或行为异常的外部服务可能返回意外的类型、恶意内容或类似指令的文本。

验证不应放在哪里：
- 共享类型契约的内部函数之间
- 已被已验证代码调用的工具函数中
- 刚从你自己数据库取出的数据上

### 4. 优先新增而非修改

在不破坏现有消费者的情况下扩展接口：

```typescript
// Good: 新增可选字段
interface CreateTaskInput {
  title: string;
  description?: string;
  priority?: 'low' | 'medium' | 'high';  // 后续添加，可选
  labels?: string[];                       // 后续添加，可选
}

// Bad: 修改现有字段类型或删除字段
interface CreateTaskInput {
  title: string;
  // description: string;  // 删除 —— 破坏现有消费者
  priority: number;         // 从 string 改为 number —— 破坏现有消费者
}
```

### 5. 可预测的命名

| 模式 | 约定 | 示例 |
|---------|-----------|---------|
| REST 端点 | 复数名词，不含动词 | `GET /api/tasks`、`POST /api/tasks` |
| 查询参数 | camelCase | `?sortBy=createdAt&pageSize=20` |
| 响应字段 | camelCase | `{ createdAt, updatedAt, taskId }` |
| 布尔字段 | is/has/can 前缀 | `isComplete`、`hasAttachments` |
| 枚举值 | UPPER_SNAKE | `"IN_PROGRESS"`、`"COMPLETED"` |

## REST API 模式

### 资源设计

```
GET    /api/tasks              → 列出 tasks（使用查询参数进行筛选）
POST   /api/tasks              → 创建一个 task
GET    /api/tasks/:id          → 获取单个 task
PATCH  /api/tasks/:id          → 更新一个 task（部分更新）
DELETE /api/tasks/:id          → 删除一个 task

GET    /api/tasks/:id/comments → 列出某 task 的评论（子资源）
POST   /api/tasks/:id/comments → 为某 task 添加评论
```

### 分页

为列表端点添加分页：

```typescript
// Request
GET /api/tasks?page=1&pageSize=20&sortBy=createdAt&sortOrder=desc

// Response
{
  "data": [...],
  "pagination": {
    "page": 1,
    "pageSize": 20,
    "totalItems": 142,
    "totalPages": 8
  }
}
```

### 筛选

使用查询参数进行筛选：

```
GET /api/tasks?status=in_progress&assignee=user123&createdAfter=2025-01-01
```

### 部分更新（PATCH）

接受部分对象 —— 仅更新提供的内容：

```typescript
// 仅 title 变化，其他内容保持不变
PATCH /api/tasks/123
{ "title": "Updated title" }
```

## TypeScript 接口模式

### 使用可辨识联合类型表示变体

```typescript
// Good: 每个变体明确清晰
type TaskStatus =
  | { type: 'pending' }
  | { type: 'in_progress'; assignee: string; startedAt: Date }
  | { type: 'completed'; completedAt: Date; completedBy: string }
  | { type: 'cancelled'; reason: string; cancelledAt: Date };

// 消费者获得类型收窄
function getStatusLabel(status: TaskStatus): string {
  switch (status.type) {
    case 'pending': return 'Pending';
    case 'in_progress': return `In progress (${status.assignee})`;
    case 'completed': return `Done on ${status.completedAt}`;
    case 'cancelled': return `Cancelled: ${status.reason}`;
  }
}
```

### 输入/输出分离

```typescript
// Input: 调用者提供的内容
interface CreateTaskInput {
  title: string;
  description?: string;
}

// Output: 系统返回的内容（包含服务端生成的字段）
interface Task {
  id: string;
  title: string;
  description: string | null;
  createdAt: Date;
  updatedAt: Date;
  createdBy: string;
}
```

### 对 ID 使用品牌类型

```typescript
type TaskId = string & { readonly __brand: 'TaskId' };
type UserId = string & { readonly __brand: 'UserId' };

// 防止意外将 UserId 传递给需要 TaskId 的地方
function getTask(id: TaskId): Promise<Task> { ... }
```

## 常见借口

| 借口 | 现实 |
|---|---|
| "我们以后再来写 API 文档" | 类型就是文档。先定义它们。 |
| "我们现在不需要分页" | 当有人有 100 条以上的数据时就会需要。从一开始就加上。 |
| "PATCH 太复杂了，直接用 PUT 吧" | PUT 每次都需要完整对象。PATCH 才是客户端真正需要的。 |
| "等需要时再做 API 版本管理" | 没有版本管理的破坏性变更会破坏消费者。从一开始就为扩展而设计。 |
| "没人用那个未文档化的行为" | Hyrum 定律：如果它是可观察的，就有人依赖它。把每个公共行为当作承诺。 |
| "我们可以维护两个版本" | 多版本会增加维护成本并造成钻石依赖问题。优先采用单一版本原则。 |
| "内部 API 不需要契约" | 内部消费者仍然是消费者。契约防止耦合并支持并行工作。 |

## 红旗警示

- 端点根据条件返回不同的数据结构
- 不同端点的错误格式不一致
- 验证散落在内部代码各处，而非集中在边界处
- 对现有字段的破坏性变更（类型变更、删除）
- 列表端点没有分页
- REST URL 中包含动词（`/api/createTask`、`/api/getUsers`）
- 使用第三方 API 响应时未经验证或净化

## 验证

设计 API 之后：

- [ ] 每个端点都有带类型的输入和输出 schema
- [ ] 错误响应遵循单一一致的格式
- [ ] 验证仅发生在系统边界处
- [ ] 列表端点支持分页
- [ ] 新字段是新增的且可选的（向后兼容）
- [ ] 所有端点的命名遵循一致的约定
- [ ] API 文档或类型与实现一起提交
