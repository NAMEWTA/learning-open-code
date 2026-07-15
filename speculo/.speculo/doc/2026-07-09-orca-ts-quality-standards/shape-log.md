# Shape Log

## 素材来源

| 路径 | 摘要 |
|------|------|
| `teach/.../dev-conventions/lessons/0001-dev-conventions.html` | 工具链（oxlint/oxfmt）、src/ 顶层分层、命名规范、禁用词黑名单 |
| `teach/.../dev-conventions/lessons/0002-directory-conventions.html` | 目录五条铁律：扁平领域、测试同居、barrel 四场景、组件两分层、shared 文件池 |
| `teach/.../dev-conventions/lessons/0003-code-quality-conventions.html` | 注释 Why 模式、Error 类模板、跨平台三策略 |
| `teach/.../dev-conventions/reference/dev-conventions-reference.html` | 17 章速查：50+ lint 规则、格式、max-lines、命名、TS 约定、React/Zustand/测试/PR 规范 |
| `teach/.../dev-conventions/reference/directory-map.html` | 72 领域目录清单、IPC handler 索引、Zustand slice 索引 |

## 候选开头

### 候选 A：「规则手册」直入式

> 本文档定义 Orca 项目的 TypeScript 开发质量规范，覆盖三个维度：**目录结构**（文件放哪里）、**代码写法**（怎么写合规）、**注释约定**（为什么这么写）。每条规则标注来源文件与自动化检查方式，可逐条核验。

**承诺的论点**：这是一本可查阅、可执行的规范手册。读者按目录→代码→注释的路径速查，每条有据可查。

### 候选 B：「反例驱动」破立式

> 下面这段代码在 Orca 项目中至少违反 6 条规范——你能找出几条？
> ```ts
> // file: src/main/agent-helpers.ts
> import { readFile } from 'fs'
> interface AgentInfo { name: string; status: any }
> export function check(info: AgentInfo): boolean { ... }
> ```
> 从命名到类型，从导入到注释，Orca 通过 oxlint + oxfmt 工具链将数十条规则固化为自动检查。本文逐条拆解这些规则及其背后的设计理由。

**承诺的论点**：先制造认知冲突（反例→正例），再按"这条规则为什么存在→怎么自动检查→怎么写才对"的三段式展开。记忆点强，适合学习而非速查。

### 候选 C：「心智模型」纵深式

> Orca 是一个 6000+ 源文件的 Electron+React 多进程系统，同时支持 macOS/Linux/Windows，通过 SSH 延伸到远端主机。在这样规模的项目中，规范不是装饰——它是开发者在不熟悉模块中定位代码的唯一导航系统。本文从 Orca 的三层规范心智模型出发，展开目录、代码、注释三类具体约定。

**承诺的论点**：先建立"为什么需要规范"的语境，再逐层展开。适合想理解规范背后 trade-off 的读者。篇幅会略长于纯手册型。

## 已选开头

**选择**：候选 A「规则手册」直入式
**开头承诺**：本文是一本可查阅、可执行的规范手册，按目录→代码→注释的路径组织，每条规则标注来源与自动化检查方式。读者可逐条核验。

### 开头文本（已确认）

> 本文档定义 Orca 项目的 TypeScript 开发质量规范，覆盖三个维度：**目录结构**（文件放哪里）、**代码写法**（怎么写合规）、**注释约定**（为什么这么写）。每条规则标注来源文件与自动化检查方式，可逐条核验。

## 格式决策

| Block | 内容 | 格式选择 | 理由 |
|-------|------|---------|------|
| 1 | 规则执行层 | 散文 + 表格 | 四层执行机制清单一目了然 |
| 2 | 目录结构规范 | 文件树 + 表格 + callout | 目录可视化必须用 ASCII tree；铁律用表格对照 |
| 3 | 代码写法规范 | 表格为主 + 代码块 | 规则条款性质量强，表格比散文更可查 |
| 4 | 注释约定 | 代码块 + 表格 + callout | Why 模式必须用正例代码展示；禁止列表用表格 |
| 5 | 质量保障 | 表格 + 代码块 | CI 清单和 lint-staged 流程适合表格化 |

## 缺口

无。素材堆覆盖了用户要求的所有维度（目录、代码、注释），额外补充了错误处理、跨平台、CI 门禁作为质量保障收尾。

## 最终文章结构

1. 规则执行层 — 四层强制执行机制
2. 目录结构规范 — 七分区 + 五条铁律
3. 代码写法规范 — 格式 / 类型 / 命名 / 行数 / .d.ts
4. 注释约定与代码质量 — 注释 / 错误处理 / 跨平台
5. 质量保障 — CI 门禁 / pre-commit / PR 规范

**文章路径**：`speculo/.speculo/doc/2026-07-09-orca-ts-quality-standards/article.md`
**行数**：393 行
**TODO 残留**：0
