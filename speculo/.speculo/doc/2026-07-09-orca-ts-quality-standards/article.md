# TypeScript 开发质量规范

本文档定义项目的 TypeScript 开发质量规范，覆盖三个维度：**目录结构**（文件放哪里）、**代码写法**（怎么写合规）、**注释约定**（为什么这么写）。每条规则标注来源文件与自动化检查方式，可逐条核验。

## 1. 规则执行层

项目 使用 oxlint（Rust linter）+ oxfmt（Rust formatter）替代 ESLint/Prettier，速度提升 50-100 倍。所有规则通过四层机制强制执行：

| 层级 | 机制 | 触发时机 | 配置文件 |
|------|------|---------|---------|
| 编辑器 | IDE 插件 | 输入时实时提示 | `.oxlintrc.json` / `.oxfmtrc.json` |
| 提交前 | lint-staged | `git commit` | `.husky/pre-commit` |
| 类型检查 | tsgo | CI / 手动 `pnpm typecheck` | `config/tsconfig.*.json` |
| PR 门禁 | GitHub Actions | `pull_request` | `.github/workflows/pr.yml` |

核心配置入口：

| 文件 | 控制范围 |
|------|---------|
| `.oxlintrc.json` | TypeScript / React / unicorn 规则（50+ 条，插件 `typescript` `react` `react-hooks` `react-perf` `unicorn`） |
| `.oxfmtrc.json` | 单引号、无分号、100 行宽、无尾逗号 |
| `tsconfig.json` + `config/tsconfig.*.json` | 路径别名 `@/` → `src/renderer/src/`、module 解析、strict 模式 |
| `AGENTS.md` | 命名禁用词、注释 Why 约定、跨平台规则、工作区安全 |

## 2. 目录结构规范

### 2.1 src/ 顶层：七分区模型

项目 的 `src/` 按**运行环境**划分，不是按功能划分。这是理解目录结构最关键的心智模型。

```
src/
├── main/       ← Electron 主进程（Node 环境）
├── renderer/   ← Electron 渲染进程（Chromium，React UI）
├── preload/    ← contextBridge 安全桥
├── shared/     ← 纯逻辑与类型（main + renderer + CLI 共用）
├── cli/        ← 独立 CLI 工具
├── relay/      ← SSH 远端 agent 执行器
└── types/      ← 仅 ambient shim 声明
```

| 目录 | 运行环境 | 职责 | 判断信号 |
|------|---------|------|---------|
| `src/main/` | Electron 主进程 (Node) | 系统调用、IPC、daemon、PTY、Git、窗口 | 代码中有 `app`、`BrowserWindow`、`ipcMain` |
| `src/renderer/` | Chromium 渲染进程 | React UI、Zustand store、组件、样式 | 代码中有 JSX、`useAppStore`、`@/` 别名 |
| `src/preload/` | Electron preload | contextBridge API 暴露 | 代码中有 `contextBridge.exposeInMainWorld` |
| `src/shared/` | 无副作用纯逻辑 | 类型、常量、工具函数 | 被 main + renderer + cli 同时 import |
| `src/cli/` | Node 独立进程 | CLI 入口、参数解析、RuntimeClient | 代码中有 RuntimeClient、yargs |
| `src/relay/` | Node 独立进程 | SSH 远端 agent 执行 | 代码中有 Unix socket、agent exec handler |
| `src/types/` | — | 仅 ambient shim | 只有 `.d.ts` 文件，仅 `build-constants.d.ts` |

> **判断法则**：产生系统副作用的代码进 main，纯 UI 进 renderer，跨端共享的类型/工具进 shared，远端执行进 relay，脚本入口进 cli。

**来源**：`AGENTS.md`、`electron.vite.config.ts`

### 2.2 铁律一：扁平领域目录，禁止深层嵌套

`src/main/` 下有 72 个领域目录，**全部平铺在一层**，按业务概念直接命名。不使用 `src/main/services/agent/status/` 这种嵌套模块树。

```
src/main/
├── agent-hooks/    ← agent hook 安装与生命周期
├── browser/        ← 浏览器标签页管理
├── daemon/         ← 后台 daemon 进程
├── git/            ← Git 操作
├── ipc/            ← IPC handler 注册（180+ 文件，仍扁平）
├── keybindings/    ← 快捷键管理
├── pty/            ← 伪终端
├── runtime/        ← 运行时编排（唯一含深嵌套的例外）
│   └── rpc/methods/  ← ~40 个 RPC 方法，数量过大才拆一层
├── ssh/            ← SSH 连接
└── ...（共 72 个平铺目录 + 113 个顶层散文件）
```

> **规则**：如果你在 `main/` 下建了 `foo/bar/baz/` 三层目录，99% 的概率违反规范。嵌套仅用于 `runtime/rpc/methods` 这类"子方法数量过多必须拆分"的场景。

同样，`src/renderer/src/components/` 下 45 个领域组件目录也全部平铺。

**来源**：`AGENTS.md`、`.oxlintrc.json`（max-lines 规则驱动拆分）

### 2.3 铁律二：测试文件与源文件同居

测试文件紧挨源文件，**禁止**放入独立的 `__tests__/` 目录。整个 `src/` 树只有 1 处历史遗留的 `__tests__/`。

```
src/shared/
├── workspace-name.ts
├── workspace-name.test.ts      ← 紧挨源文件
├── agent-detection.ts
├── agent-detection.test.ts     ← 紧挨源文件

src/main/ipc/
├── pty.ts
├── pty.test.ts                 ← 紧挨源文件
```

测试文件通过后缀区分意图：

| 后缀 | 含义 | 示例 |
|------|------|------|
| `.test.ts` | 单元测试 | `agent-detection.test.ts` |
| `.integration.test.ts` | 集成测试 | `ssh-relay-session-agent-hooks.integration.test.ts` |
| `.benchmark.test.ts` | 性能基准 | `store-snapshot.benchmark.test.ts` |
| `.repro.test.ts` | Bug 复现 | `issue-4631-terminal-hover.repro.test.ts` |
| `-test-harness.ts` | 测试辅助工具（非测试） | `agent-hooks/test-harness.ts` |

### 2.4 铁律三：index.ts 只用四种场景

项目 **不**为每个目录自动建 barrel 文件。`index.ts` 仅出现在：

| 场景 | 示例 | 原因 |
|------|------|------|
| 进程入口 | `src/main/index.ts`、`src/cli/index.ts` | app 生命周期、服务装配 |
| 聚合注册 | `runtime/rpc/methods/index.ts` | 收集 ~25 个 RPC 方法到一个数组 |
| 隐藏内部结构 | `ghostty/index.ts`、`warp-themes/index.ts` | 对外暴露公共 API，隐藏内部实现文件 |
| 状态组合 | `renderer/src/store/index.ts` | Zustand `create` 合并 ~20 个 slice |

> **判断法则**：如果你准备新建 `index.ts` 只为了少写几个 import 路径——别建。直接按文件名导入即可。

### 2.5 铁律四：components/ 按业务逻辑分层

`src/renderer/src/components/` 下只有两种目录：

```
components/
├── ui/                  ← 纯 UI 原语（shadcn 风格）
│   │                     无业务逻辑、无 store 依赖、可跨项目复用
│   └── button.tsx, dialog.tsx, select.tsx, tooltip.tsx …（35 个文件）
│
├── terminal/            ← 业务领域组件
├── settings/            ← 含 store 交互、IPC 调用、持久化逻辑
├── agent/               ← 含 agent 状态展示
├── sidebar/             ← 含项目树、拖拽、右键菜单
└── ...（共 45 个平铺业务目录）
```

> **规则**：包含 `useAppStore` 或 `ipcRenderer` 调用的组件 → 放业务领域目录。纯受控的按钮/弹窗/选择器 → 放 `ui/`。

### 2.6 铁律五：shared/ 是扁平文件池

`src/shared/` 下有 542 个 `.ts` 文件平铺在一个目录下，除了 `network/`（4 个文件）外零嵌套。文件以描述性前缀自然分组，不需要子目录：

```
src/shared/
├── agent-detection.ts           ← 文件名 = 概念名
├── agent-status-types.ts
├── browser-url.ts
├── clipboard-text.ts
├── constants.ts
├── keybindings.ts
├── remote-runtime-client.ts
├── runtime-types.ts
├── telemetry-events.ts
├── terminal-custom-themes.ts
├── types.ts
├── workspace-name.ts
├── network/                     ← 唯一嵌套目录
│   ├── manual-address.ts
│   └── server-share-address.ts
└── ...（共 542 个 .ts 文件）
```

> **规则**：新增共享类型时，直接在 `shared/` 下建一个 `<概念名>.ts` 文件。不需要建子目录。

**来源**：整个第 2 节规则来自 `AGENTS.md` 与源码目录实地验证

## 3. 代码写法规范

### 3.1 格式规则（oxfmt 强制执行）

oxfmt 在保存时自动格式化，规则不可协商：

| 配置项 | 值 | 反例 |
|--------|-----|------|
| `singleQuote` | `true`（单引号） | `"hello"` → `'hello'` |
| `semi` | `false`（不加分号） | `const x = 1;` → `const x = 1` |
| `printWidth` | `100` | 超过 100 字符自动换行 |
| `trailingComma` | `"none"` | `{ a, b, }` → `{ a, b }` |

**来源**：`.oxfmtrc.json`

### 3.2 类型系统约定（oxlint TypeScript 规则）

以下 10 条规则为 **error** 级别，CI 不通过则拒绝合入：

| # | 规则 | 要求 | 反例 |
|----|------|------|------|
| 1 | `consistent-type-definitions` | 只用 `type`，禁止 `interface` | `interface Foo {}` → `type Foo = {}` |
| 2 | `no-explicit-any` | 禁止显式 `any`（rest args 除外） | `data: any` → `data: unknown` + 类型守卫 |
| 3 | `consistent-type-imports` | 类型导入必须 `import type` | `import { Foo } from './types'` → `import type { Foo } from './types'` |
| 4 | `switch-exhaustiveness-check` | switch 必须穷举所有分支 | 缺少 case → error |
| 5 | `prefer-node-protocol` | Node 内置模块加 `node:` 前缀 | `import { readFile } from 'fs'` → `from 'node:fs'` |
| 6 | `prefer-optional-chain` | 用 `?.` 替代多层判空 | `a && a.b && a.b.c` → `a?.b?.c` |
| 7 | `prefer-includes` | 用 `.includes()` 替代 `indexOf` | `arr.indexOf(x) !== -1` → `arr.includes(x)` |
| 8 | `throw-new-error` | throw 必须用 Error 对象 | `throw 'error'` → `throw new Error('error')` |
| 9 | `error-message` | Error 构造函数必须传消息 | `new Error()` → `new Error('描述')` |
| 10 | `prefer-date-now` | 用 `Date.now()` | `new Date().getTime()` → `Date.now()` |

**来源**：`.oxlintrc.json`（插件 `typescript` `unicorn`，category `correctness` = error）

### 3.3 命名规范

**禁用词黑名单**（文件/目录/模块名中不得出现）：

| 禁用词 | 原因 | 替代策略 |
|--------|------|---------|
| `helpers` | 零信息量，代码垃圾场 | 以操作的具体概念命名 |
| `utils` | 同上 | 拆分职责，每个文件一个概念 |
| `common` | 同上 | 同上 |
| `misc` | 同上 | 同上 |
| `shared-stuff` | 同上 | 同上 |

**命名格式约定**：

| 元素 | 格式 | 示例 |
|------|------|------|
| 文件 | `kebab-case` | `tab-group-state.ts`、`terminal-orphan-cleanup.ts` |
| 类 / React 组件 / 类型别名 | `PascalCase` | `KeybindingService`、`SidebarToolbar`、`AgentStatus` |
| 函数 / 变量 | `camelCase` | `getAgentLabel`、`persistedUIReady` |
| 原始常量 | `SCREAMING_SNAKE_CASE` | `AGENT_AWAKE_STATUS_STALE_AFTER_MS` |
| 布尔变量 | `is`/`has` 前缀 | `isQuitting`、`hasAgentName` |

> **核心原则**：文件名必须准确描述它包含的概念。`tab-group-state.ts` ✅ / `tabs-helpers.ts` ❌

**来源**：`AGENTS.md`、`.oxlintrc.json`

### 3.4 文件行数限制

oxlint 对单文件行数有硬性上限，**禁止 disable**：

| 文件类型 | 上限 |
|---------|------|
| `.ts` | 300 行 |
| `.tsx` | 400 行 |
| `.mjs` | 600 行 |
| 测试文件 | 800 行 |

超限时的处理方式：拆分文件、提取专注模块、将 fixtures/builders 移入独立文件。

**来源**：`.oxlintrc.json`（`max-lines` 规则）

### 3.5 类型声明文件禁令

项目自有类型**必须放在 `.ts` 文件中，禁止使用 `.d.ts`**。原因：TypeScript 的 `skipLibCheck: true` 会使 `.d.ts` 中的类型错误静默变成 `any`。`.d.ts` 仅保留给 ambient shim——整个项目只有 3 个：`env.d.ts`、`mermaid.d.ts`、`build-constants.d.ts`。CI 中有专门的 `.d.ts` 守卫检查 `src/preload/` 和 `src/shared/`。

**来源**：`AGENTS.md`、`.github/workflows/pr.yml`

## 4. 注释约定与代码质量

### 4.1 注释规范：只写"为什么"，不写"是什么"

项目 的注释哲学极其精简——注释只解释**非显而易见的决策原因**，绝不复述代码做了什么。

**三种合法注释：**

| 形态 | 用途 | 格式 |
|------|------|------|
| `// Why:` | 解释非显而易见的决策 | `// Why: <安全约束/兼容/trade-off 原因>` |
| `/** 一句话 */` | 导出函数的用途描述 | `/** Resolve the shell kind from a shell binary path. */` |
| `// ─── Section ───` | 长文件内部视觉分隔 | `// ─── Garbage Collection ───` |

**Why 注释示例：**

```ts
// Why: forward-slash UNC roots need win32 ops; POSIX joins collapse //Server to /Server.
const pathOps = isWindowsAbsolutePathLike(root) ? win32Path : posixPath

// Why 5 minutes: GC runs ~10s after startup. Without an age guard,
// GC would delete its freshly-created history directory (TOCTOU race).
const HISTORY_GC_MIN_AGE_MS = 5 * 60 * 1000

// Why: quitAndInstall is a side effect. React StrictMode double-invokes
// render functions — calling it inline would trigger a double-install.
const handleQuitAndInstall = useCallback(() => quitAndInstall(), [])
```

**绝对不写：**

| 禁止类型 | 反例 | 原因 |
|---------|------|------|
| 复述代码 | `// increment counter` | 代码已自解释 |
| 机制叙述 | `// first we check if x is null, then we...` | 应拆分而非注释 |
| 设计文档引用 | `// see design doc section 3.2` | 文档会过时 |

> **规则**：不超过两行。如果你发现自己写了三行解释，说明这段代码需要拆分而非加注释。lint disable 也必须加 Why：`/* eslint-disable max-lines -- Why: <原因> */`

**来源**：`AGENTS.md`

### 4.2 错误处理规范

项目 **没有集中式错误基类或 `errors/` 目录**。每个领域在需要时自行定义 Error 类，但遵循统一模板：

```ts
// 模板：所有自定义 Error 类统一写法
export class RemoteRuntimeClientError extends Error {
  readonly code: string

  constructor(code: string, message: string) {
    super(message)
    this.name = 'RemoteRuntimeClientError'
    this.code = code
  }
}
```

关键约束：
- 始终有 `readonly code: string` 字段
- 构造函数签名固定为 `(code: string, message: string)`
- 始终设置 `this.name` 为类名

每个 Error 类通常伴随一个类型守卫函数：

```ts
export function isClipboardTextTooLargeError(error: unknown): boolean {
  return error instanceof ClipboardTextTooLargeError
}
```

> **判断法则**：需要根据错误类型做不同处理 → 定义 Error 子类 + 守卫函数。不需要区分 → 直接用 `throw new Error('描述')`。

项目中至少有 20+ 个按此模板定义的 Error 类：`BrowserError`、`DaemonProtocolError`、`SessionNotFoundError`、`CredentialDecryptionError`、`JiraApiError`、`StreamProtocolError`、`RelayVersionMismatchError` 等。

### 4.3 跨平台开发规范

项目 同时支持 macOS、Linux、Windows，**禁止 `.mac.ts` / `.win.ts` / `.linux.ts` 文件后缀分裂**。所有平台逻辑通过三种策略管理：

| 策略 | 适用场景 | 示例 |
|------|---------|------|
| 领域文件分离 | 整个功能仅在某平台存在 | `win32-utils.ts`、`macos-system-sleep-assertion.ts`、`linux-lid-sleep-assertion.ts` |
| 运行时 `process.platform` | 同功能不同平台有分支 | `if (process.platform === 'win32') { ... }` |
| 依赖注入 platform | 需要测试不同平台分支 | `this.platform = options.platform ?? process.platform`（测试可传 `'darwin'`） |

**路径处理特别规则**：涉及跨平台路径时，同时导入 `posix` 和 `win32`，按**路径形状**（而非 `process.platform`）选择操作：

```ts
import * as posixPath from 'node:path/posix'
import * as win32Path from 'node:path/win32'

function getPathOps(p: string): typeof posixPath {
  return isWindowsAbsolutePathLike(p) ? win32Path : posixPath
}
```

**快捷键规则**：

| 场景 | 规则 |
|------|------|
| 键盘事件 | `navigator.userAgent.includes('Mac')` 判断 `metaKey` vs `ctrlKey` |
| Electron 菜单 | 统一使用 `CmdOrCtrl` |
| UI 快捷键标签 | Mac 显示 `⌘` / `⇧`，其他平台显示 `Ctrl+` / `Shift+` |

> **禁止**：硬编码 `e.metaKey`、路径写死 `/` 或 `\`、文件后缀分裂。

**来源**：`AGENTS.md`

## 5. 质量保障

### 5.1 CI 门禁清单

每条 PR 在合入前必须通过以下 10 道检查（来源：`.github/workflows/pr.yml`）：

| # | 检查项 | 工具 | 说明 |
|---|--------|------|------|
| 1 | lint | oxlint | 格式化 GitHub annotation，包含 50+ 规则 |
| 2 | react-doctor | oxlint | React 反模式检测（派生状态、初始化 state） |
| 3 | styled-scrollbars | 自定义脚本 | 滚动条样式约定检查 |
| 4 | reliability-gates | 自定义脚本 | 可靠性门禁 |
| 5 | macOS entitlements | 自定义脚本 | 权限声明完整性验证 |
| 6 | `.d.ts` 守卫 | 自定义脚本 | `src/preload/` 和 `src/shared/` 禁止项目自有 `.d.ts` |
| 7 | typecheck | tsgo | 3 个 tsconfig 并行类型检查 |
| 8 | test | vitest | 单元测试（`src/**/*.test.ts`） |
| 9 | build:unpack | electron-vite | 构建解包验证 |
| 10 | CLI smoke | 自定义脚本 | 打包后 CLI 可用性校验 |

### 5.2 提交前检查

`git commit` 时，`.husky/pre-commit` 通过 lint-staged 对暂存文件自动执行：

```
*.{ts,tsx,js,jsx,mjs}  → oxlint → oxlint-react-doctor → oxfmt --write
*.{json,css}            → oxfmt --write
```

### 5.3 PR 提交规范

| 规则 | 说明 |
|------|------|
| 分支命名 | `fix/`、`feat/`、`chore/` + kebab-case（如 `fix/ctrl-backspace-delete-word`） |
| 提交前自检 | 必须本地通过 `pnpm lint`、`pnpm typecheck`、`pnpm test`、`pnpm build` |
| PR 描述 | 必须包含摘要、截图/录屏、AI review report（跨平台/SSH/agent 兼容性）、security audit |
| 禁止 | 提交截图到仓库、在 PR 中 bump 版本号 |

**来源**：`.github/CONTRIBUTING.md`、`.github/pull_request_template.md`、`.husky/pre-commit`
