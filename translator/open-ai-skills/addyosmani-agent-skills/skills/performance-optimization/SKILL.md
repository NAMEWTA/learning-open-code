---
name: performance-optimization
description: 优化应用性能。适用于存在性能需求、怀疑性能退化、或需要改善 Core Web Vitals 或加载时间的场景。适用于性能分析发现瓶颈需要修复的场景。
---

# 性能优化

## 概述

先测量再优化。不经测量的性能工作是猜测——而猜测会导致过早优化，增加复杂性却未改善真正重要的指标。先进行性能分析，识别真正的瓶颈，修复它，再次测量。仅优化那些测量数据证明确实重要的部分。

## 适用场景

- 规格中存在性能需求（加载时间预算、响应时间 SLA）
- 用户或监控系统报告行为缓慢
- Core Web Vitals 分数低于阈值
- 怀疑某个变更引入了性能退化
- 构建处理大数据量或高流量的功能

**不适用场景：** 在没有性能问题证据之前不要优化。过早优化增加的复杂性成本超过其带来的性能收益。

## Core Web Vitals 指标目标

| 指标 | 良好 | 需要改进 | 差 |
|--------|------|-------------------|------|
| **LCP**（Largest Contentful Paint） | ≤ 2.5 秒 | ≤ 4.0 秒 | > 4.0 秒 |
| **INP**（Interaction to Next Paint） | ≤ 200 毫秒 | ≤ 500 毫秒 | > 500 毫秒 |
| **CLS**（Cumulative Layout Shift） | ≤ 0.1 | ≤ 0.25 | > 0.25 |

## 优化工作流

```
1. MEASURE  → 使用真实数据建立基线
2. IDENTIFY → 找到真正的瓶颈（而非假设）
3. FIX      → 处理具体瓶颈
4. VERIFY   → 再次测量，确认改进
5. GUARD    → 添加监控或测试以防止退化
```

### 步骤 1：Measure（测量）

两种互补的方法——同时使用：

- **合成测试（Lighthouse、DevTools Performance 面板）：** 受控条件，可复现。最适合 CI 退化检测和隔离具体问题。
- **真实用户监控 RUM（web-vitals 库、CrUX）：** 真实条件下的真实用户数据。验证修复是否确实改善了用户体验所必需的。

**前端：**
```bash
# 合成测试：Chrome DevTools 中的 Lighthouse（或 CI 中）
# Chrome DevTools → Performance 选项卡 → 录制
# Chrome DevTools MCP → Performance trace

# RUM：代码中使用 Web Vitals 库
import { onLCP, onINP, onCLS } from 'web-vitals';

onLCP(console.log);
onINP(console.log);
onCLS(console.log);
```

**后端：**
```bash
# 响应时间日志记录
# 应用性能监控（APM）
# 带计时的数据库查询日志

# 简单计时
console.time('db-query');
const result = await db.query(...);
console.timeEnd('db-query');
```

### 从哪里开始测量

根据症状决定首先测量什么：

```
什么慢了？
├── 首次页面加载
│   ├── 打包体积大？ --> 测量打包体积，检查代码分割
│   ├── 服务端响应慢？ --> 在 DevTools Network 瀑布图中测量 TTFB
│   │   ├── DNS 时间长？ --> 为已知的域名添加 dns-prefetch / preconnect
│   │   ├── TCP/TLS 时间长？ --> 启用 HTTP/2，检查边缘部署，keep-alive
│   │   └── 等待（服务器）时间长？ --> 分析后端，检查查询和缓存
│   └── 渲染阻塞资源？ --> 检查网络瀑布图中的 CSS/JS 阻塞
├── 交互感觉迟钝
│   ├── 点击时 UI 冻结？ --> 分析主线程，查找长任务（> 50 毫秒）
│   ├── 表单输入延迟？ --> 检查重渲染，受控组件的开销
│   └── 动画卡顿？ --> 检查布局抖动，强制回流
├── 导航后的页面
│   ├── 数据加载？ --> 测量 API 响应时间，检查请求瀑布
│   └── 客户端渲染？ --> 分析组件渲染时间，检查 N+1 获取
└── 后端 / API
    ├── 单个端点慢？ --> 分析数据库查询，检查索引
    ├── 所有端点都慢？ --> 检查连接池、内存、CPU
    └── 间歇性变慢？ --> 检查锁竞争、GC 暂停、外部依赖
```

### 步骤 2：Identify（识别瓶颈）

按类别列出常见瓶颈：

**前端：**

| 症状 | 可能原因 | 调查方式 |
|---------|-------------|---------------|
| LCP 慢 | 大图片、渲染阻塞资源、服务器慢 | 检查网络瀑布图、图片大小 |
| CLS 高 | 图片无尺寸、延迟加载内容、字体偏移 | 检查布局偏移归因 |
| INP 差 | 主线程 JavaScript 过重、大 DOM 更新 | 检查 Performance trace 中的长任务 |
| 初始加载慢 | 打包体积大、网络请求多 | 检查打包体积、代码分割 |

**后端：**

| 症状 | 可能原因 | 调查方式 |
|---------|-------------|---------------|
| API 响应慢 | N+1 查询、缺少索引、未优化查询 | 检查数据库查询日志 |
| 内存增长 | 引用泄漏、无界缓存、大负载 | 堆快照分析 |
| CPU 峰值 | 同步重计算、正则回溯 | CPU 性能分析 |
| 高延迟 | 缺少缓存、冗余计算、网络跳转 | 在请求全链路中追踪 |

### 步骤 3：Fix（修复常见反模式）

#### N+1 查询（后端）

```typescript
// BAD：N+1 — 每个任务都单独查询一次 owner
const tasks = await db.tasks.findMany();
for (const task of tasks) {
  task.owner = await db.users.findUnique({ where: { id: task.ownerId } });
}

// GOOD：使用 join/include 单次查询
const tasks = await db.tasks.findMany({
  include: { owner: true },
});
```

#### 无界数据获取

```typescript
// BAD：获取全部记录
const allTasks = await db.tasks.findMany();

// GOOD：带限制的分页查询
const tasks = await db.tasks.findMany({
  take: 20,
  skip: (page - 1) * 20,
  orderBy: { createdAt: 'desc' },
});
```

#### 缺少图片优化（前端）

```html
<!-- BAD：无尺寸、无格式优化 -->
<img src="/hero.jpg" />

<!-- GOOD：首屏 / LCP 图片 — 艺术方向 + 分辨率切换，高优先级 -->
<!--
  结合两种技术：
  - 艺术方向（media）：每个断点使用不同的裁剪 / 构图
  - 分辨率切换（srcset + sizes）：根据屏幕密度加载合适的文件大小
-->
<picture>
  <!-- 移动端：竖版裁剪（8:10） -->
  <source
    media="(max-width: 767px)"
    srcset="/hero-mobile-400.avif 400w, /hero-mobile-800.avif 800w"
    sizes="100vw"
    width="800"
    height="1000"
    type="image/avif"
  />
  <source
    media="(max-width: 767px)"
    srcset="/hero-mobile-400.webp 400w, /hero-mobile-800.webp 800w"
    sizes="100vw"
    width="800"
    height="1000"
    type="image/webp"
  />
  <!-- 桌面端：横版裁剪（2:1） -->
  <source
    srcset="/hero-800.avif 800w, /hero-1200.avif 1200w, /hero-1600.avif 1600w"
    sizes="(max-width: 1200px) 100vw, 1200px"
    width="1200"
    height="600"
    type="image/avif"
  />
  <source
    srcset="/hero-800.webp 800w, /hero-1200.webp 1200w, /hero-1600.webp 1600w"
    sizes="(max-width: 1200px) 100vw, 1200px"
    width="1200"
    height="600"
    type="image/webp"
  />
  <img
    src="/hero-desktop.jpg"
    width="1200"
    height="600"
    fetchpriority="high"
    alt="主视觉图片描述"
  />
</picture>

<!-- GOOD：首屏之外的图片 — 懒加载 + 异步解码 -->
<img
  src="/content.webp"
  width="800"
  height="400"
  loading="lazy"
  decoding="async"
  alt="内容图片描述"
/>
```

#### 不必要的重渲染（React）

```tsx
// BAD：每次渲染创建新对象，导致子组件重渲染
function TaskList() {
  return <TaskFilters options={{ sortBy: 'date', order: 'desc' }} />;
}

// GOOD：稳定引用
const DEFAULT_OPTIONS = { sortBy: 'date', order: 'desc' } as const;
function TaskList() {
  return <TaskFilters options={DEFAULT_OPTIONS} />;
}

// 对高成本的组件使用 React.memo
const TaskItem = React.memo(function TaskItem({ task }: Props) {
  return <div>{/* 高成本渲染 */}</div>;
});

// 对高成本计算使用 useMemo
function TaskStats({ tasks }: Props) {
  const stats = useMemo(() => calculateStats(tasks), [tasks]);
  return <div>{stats.completed} / {stats.total}</div>;
}
```

#### 打包体积过大

```typescript
// 现代打包器（Vite、webpack 5+）通过 tree-shaking 自动处理具名导入，
// 前提是该依赖提供 ESM 并在 package.json 中标记为 `sideEffects: false`。
// 在更改导入方式之前先进行性能分析——真正的收益来自代码分割和懒加载。

// GOOD：对沉重的、使用率低的功能使用动态导入
const ChartLibrary = lazy(() => import('./ChartLibrary'));

// GOOD：被 Suspense 包裹的路由级代码分割
const SettingsPage = lazy(() => import('./pages/Settings'));

function App() {
  return (
    <Suspense fallback={<Spinner />}>
      <SettingsPage />
    </Suspense>
  );
}
```

#### 缺少缓存（后端）

```typescript
// 缓存高频读取、低频变更的数据
const CACHE_TTL = 5 * 60 * 1000; // 5 分钟
let cachedConfig: AppConfig | null = null;
let cacheExpiry = 0;

async function getAppConfig(): Promise<AppConfig> {
  if (cachedConfig && Date.now() < cacheExpiry) {
    return cachedConfig;
  }
  cachedConfig = await db.config.findFirst();
  cacheExpiry = Date.now() + CACHE_TTL;
  return cachedConfig;
}

// 为静态资源设置 HTTP 缓存头
app.use('/static', express.static('public', {
  maxAge: '1y',           // 缓存 1 年
  immutable: true,        // 永不重新验证（文件名使用内容哈希）
}));

// API 响应的 Cache-Control
res.set('Cache-Control', 'public, max-age=300'); // 5 分钟
```

## 性能预算

设定预算并强制执行：

```
JavaScript 打包体积：< 200KB gzip（初始加载）
CSS：< 50KB gzip
图片：每张首屏图片 < 200KB
字体：总计 < 100KB
API 响应时间：< 200 毫秒（p95）
可交互时间：4G 网络下 < 3.5 秒
Lighthouse Performance 分数：≥ 90
```

**在 CI 中强制执行：**
```bash
# 打包体积检查
npx bundlesize --config bundlesize.config.json

# Lighthouse CI
npx lhci autorun
```

## 参见

详细的性能检查清单、优化命令和反模式参考，参见 `references/performance-checklist.md`。


## 常见借口

| 借口 | 现实 |
|---|---|
| "以后再优化" | 性能债务会复利。现在修复明显的反模式，推迟微优化。 |
| "在我机器上很快" | 你的机器不是用户的。在有代表性的硬件和网络上进行分析。 |
| "这个优化是显而易见的" | 如果你没有测量，你就不知道。先做性能分析。 |
| "用户不会注意到 100 毫秒的差异" | 研究表明 100 毫秒的延迟会影响转化率。用户比你想象中更敏感。 |
| "框架会处理性能问题" | 框架能预防一些但无法修复 N+1 查询或过大的打包体积。 |

## 红旗信号

- 没有性能分析数据支持的情况下进行优化
- 数据获取中的 N+1 查询模式
- 列表端点无分页
- 图片无尺寸、无懒加载、无响应式尺寸
- 打包体积在未经评审的情况下增长
- 生产环境无性能监控
- 到处都是 `React.memo` 和 `useMemo`（过度使用和未使用一样糟糕）

## 验证

任何性能相关的变更之后：

- [ ] 存在前后测量数据（具体数字）
- [ ] 具体瓶颈已被识别和处理
- [ ] Core Web Vitals 在"良好"阈值内
- [ ] 打包体积未显著增加
- [ ] 新增的数据获取代码中无 N+1 查询
- [ ] 性能预算在 CI 中通过（如已配置）
- [ ] 现有测试仍然通过（优化未破坏行为）
