---
name: frontend-ui-engineering
description: 构建生产级质量的用户界面。适用于构建或修改面向用户的界面，创建组件、实现布局、管理状态，或当输出需要达到生产质量而非 AI 生成感时使用。
---

# 前端 UI 工程

## 概述

构建具有可访问性、高性能且视觉精美的生产级用户界面。目标是打造看起来像是由顶级公司中具备设计意识的工程师构建的 UI —— 而不是像 AI 生成的东西。这意味着真正遵循设计系统、适当的无障碍性、深思熟虑的交互模式，以及没有任何通用的"AI 风格"。

## 适用场景

- 构建新的 UI 组件或页面
- 修改现有的面向用户界面
- 实现响应式布局
- 添加交互性或状态管理
- 修复视觉或 UX 问题

## 组件架构

### 文件结构

将与组件相关的所有内容放在一起：

```
src/components/
  TaskList/
    TaskList.tsx          # 组件实现
    TaskList.test.tsx     # 测试
    TaskList.stories.tsx  # Storybook stories（如使用）
    use-task-list.ts      # 自定义 hook（如有复杂状态）
    types.ts              # 组件专用类型（如需要）
```

### 组件模式

**优先使用组合而非配置：**

```tsx
// Good: Composable
<Card>
  <CardHeader>
    <CardTitle>Tasks</CardTitle>
  </CardHeader>
  <CardBody>
    <TaskList tasks={tasks} />
  </CardBody>
</Card>

// Avoid: Over-configured
<Card
  title="Tasks"
  headerVariant="large"
  bodyPadding="md"
  content={<TaskList tasks={tasks} />}
/>
```

**保持组件职责聚焦：**

```tsx
// Good: Does one thing
export function TaskItem({ task, onToggle, onDelete }: TaskItemProps) {
  return (
    <li className="flex items-center gap-3 p-3">
      <Checkbox checked={task.done} onChange={() => onToggle(task.id)} />
      <span className={task.done ? 'line-through text-muted' : ''}>{task.title}</span>
      <Button variant="ghost" size="sm" onClick={() => onDelete(task.id)}>
        <TrashIcon />
      </Button>
    </li>
  );
}
```

**将数据获取与展示分离：**

```tsx
// Container: handles data
export function TaskListContainer() {
  const { tasks, isLoading, error } = useTasks();

  if (isLoading) return <TaskListSkeleton />;
  if (error) return <ErrorState message="Failed to load tasks" retry={refetch} />;
  if (tasks.length === 0) return <EmptyState message="No tasks yet" />;

  return <TaskList tasks={tasks} />;
}

// Presentation: handles rendering
export function TaskList({ tasks }: { tasks: Task[] }) {
  return (
    <ul role="list" className="divide-y">
      {tasks.map(task => <TaskItem key={task.id} task={task} />)}
    </ul>
  );
}
```

## 状态管理

**选择能解决问题的最简方案：**

```
Local state (useState)           → 组件特定的 UI 状态
Lifted state                     → 2-3 个兄弟组件之间共享
Context                          → 主题、认证、语言环境（读多写少）
URL state (searchParams)         → 筛选、分页、可分享的 UI 状态
Server state (React Query, SWR)  → 带缓存的远程数据
Global store (Zustand, Redux)    → 应用全局共享的复杂客户端状态
```

**避免超过 3 层的 prop 传递。** 如果你在通过不使用的组件传递 props，应该引入 context 或重构组件树。

## 设计系统遵循

### 避免 AI 风格

AI 生成的 UI 有一些可识别的模式。应全部避免：

| AI 默认做法 | 为什么是问题 | 生产质量做法 |
|---|---|---|
| 到处使用紫色/靛蓝色 | 模型默认使用视觉上"安全"的调色板，导致每个应用看起来都一样 | 使用项目实际的调色板 |
| 过多渐变 | 渐变增加视觉噪音，与大多数设计系统冲突 | 扁平或匹配设计系统的微妙渐变 |
| 到处使用圆角（rounded-2xl） | 最大圆角传递"友好"信号，但忽略了真实设计中圆角半径的层次性 | 使用设计系统中一致的 border-radius |
| 通用 hero 区域 | 模板驱动的布局，与实际内容或用户需求无关 | 内容优先的布局 |
| Lorem ipsum 风格的文案 | 占位文本会隐藏真实内容才暴露的布局问题（长度、换行、溢出） | 真实的占位内容 |
| 到处使用过大内边距 | 均等的大内边距破坏视觉层次，浪费屏幕空间 | 一致的空间尺度 |
| 模板化的卡片网格 | 统一网格是一种忽略信息优先级和浏览模式的布局捷径 | 目的驱动的布局 |
| 大量阴影设计 | 层叠阴影增加深度感，但与内容争夺注意力，且在低端设备上渲染缓慢 | 除非设计系统指定，否则使用微妙阴影或不使用 |

### 间距与布局

使用一致的空间尺度。不要自创数值：

```css
/* 使用尺度：0.25rem 递增（或项目实际使用的尺度） */
/* Good */  padding: 1rem;      /* 16px */
/* Good */  gap: 0.75rem;       /* 12px */
/* Bad */   padding: 13px;      /* 不在任何尺度上 */
/* Bad */   margin-top: 2.3rem; /* 不在任何尺度上 */
```

### 字体排版

遵循排版层级：

```
h1 → 页面标题（每页一个）
h2 → 章节标题
h3 → 子章节标题
body → 默认文本
small → 次要/辅助文本
```

不要跳过标题层级。不要将标题样式用于非标题内容。

### 颜色

- 使用语义化颜色 token：`text-primary`、`bg-surface`、`border-default` —— 不使用原始十六进制值
- 确保足够的对比度（普通文本 4.5:1，大文本 3:1）
- 不要仅依赖颜色传达信息（同时使用图标、文本或图案）

## 无障碍性（WCAG 2.1 AA）

每个组件必须满足以下标准：

### 键盘导航

```tsx
// 每个可交互元素必须可通过键盘访问
<button onClick={handleClick}>Click me</button>        // ✓ 默认可聚焦
<div onClick={handleClick}>Click me</div>               // ✗ 不可聚焦
<div role="button" tabIndex={0} onClick={handleClick}    // ✓ 但推荐使用 <button>
     onKeyDown={e => {
       if (e.key === 'Enter') handleClick();
       if (e.key === ' ') e.preventDefault();
     }}
     onKeyUp={e => {
       if (e.key === ' ') handleClick();
     }}>
  Click me
</div>
```

### ARIA 标签

```tsx
// 为缺少可见文本的交互元素添加标签
<button aria-label="Close dialog"><XIcon /></button>

// 为表单输入添加标签
<label htmlFor="email">Email</label>
<input id="email" type="email" />

// 或当没有可见标签时使用 aria-label
<input aria-label="Search tasks" type="search" />
```

### 焦点管理

```tsx
// 内容变化时移动焦点
function Dialog({ isOpen, onClose }: DialogProps) {
  const closeRef = useRef<HTMLButtonElement>(null);

  useEffect(() => {
    if (isOpen) closeRef.current?.focus();
  }, [isOpen]);

  // 打开时将焦点困在 dialog 内部
  return (
    <dialog open={isOpen}>
      <button ref={closeRef} onClick={onClose}>Close</button>
      {/* dialog content */}
    </dialog>
  );
}
```

### 有意义的空状态和错误状态

```tsx
// 不要显示空白屏幕
function TaskList({ tasks }: { tasks: Task[] }) {
  if (tasks.length === 0) {
    return (
      <div role="status" className="text-center py-12">
        <TasksEmptyIcon className="mx-auto h-12 w-12 text-muted" />
        <h3 className="mt-2 text-sm font-medium">No tasks</h3>
        <p className="mt-1 text-sm text-muted">Get started by creating a new task.</p>
        <Button className="mt-4" onClick={onCreateTask}>Create Task</Button>
      </div>
    );
  }

  return <ul role="list">...</ul>;
}
```

## 响应式设计

优先为移动端设计，然后扩展：

```tsx
// Tailwind: 移动优先的响应式设计
<div className="
  grid grid-cols-1      /* Mobile: single column */
  sm:grid-cols-2        /* Small: 2 columns */
  lg:grid-cols-3        /* Large: 3 columns */
  gap-4
">
```

在以下断点进行测试：320px、768px、1024px、1440px。

## 加载与过渡

```tsx
// 骨架屏加载（内容不使用 spinner）
function TaskListSkeleton() {
  return (
    <div className="space-y-3" aria-busy="true" aria-label="Loading tasks">
      {Array.from({ length: 3 }).map((_, i) => (
        <div key={i} className="h-12 bg-muted animate-pulse rounded" />
      ))}
    </div>
  );
}

// 乐观更新以提升感知速度
function useToggleTask() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: toggleTask,
    onMutate: async (taskId) => {
      await queryClient.cancelQueries({ queryKey: ['tasks'] });
      const previous = queryClient.getQueryData(['tasks']);

      queryClient.setQueryData(['tasks'], (old: Task[]) =>
        old.map(t => t.id === taskId ? { ...t, done: !t.done } : t)
      );

      return { previous };
    },
    onError: (_err, _taskId, context) => {
      queryClient.setQueryData(['tasks'], context?.previous);
    },
  });
}
```

## 参见

详细的无障碍性要求和测试工具，参见 `references/accessibility-checklist.md`。

## 常见借口

| 借口 | 现实 |
|---|---|
| "无障碍性是锦上添花" | 在许多司法管辖区这是法律要求，也是工程质量标准。 |
| "我们以后再做响应式" | 后期改造响应式设计比从一开始就构建要难 3 倍。 |
| "设计还没定稿，所以先跳过样式" | 使用设计系统默认值。未加样式的 UI 会给审核者留下糟糕的第一印象。 |
| "这只是一个原型" | 原型会变成生产代码。从一开始就把基础打好。 |
| "AI 风格暂时没问题" | 它传递出低质量的信号。从一开始就使用项目实际的设计系统。 |

## 红旗警示

- 组件超过 200 行（需要拆分）
- 内联样式或随意的像素值
- 缺少错误状态、加载状态或空状态
- 未进行键盘导航测试
- 仅使用颜色作为状态指示（红色/绿色，没有文本或图标）
- 通用的"AI 外观"（紫色渐变、过大卡片、模板化布局）

## 验证

构建 UI 之后：

- [ ] 组件渲染无控制台错误
- [ ] 所有可交互元素均可通过键盘访问（用 Tab 键遍历页面）
- [ ] 屏幕阅读器能传达页面的内容和结构
- [ ] 响应式：在 320px、768px、1024px、1440px 下均能正常工作
- [ ] 加载、错误和空状态均已处理
- [ ] 遵循项目的设计系统（间距、颜色、字体排版）
- [ ] 开发工具或 axe-core 中无无障碍性警告
