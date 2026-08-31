---
name: setup-ts-deep-modules
description: 将 dependency-cruiser 接入 TypeScript 仓库，使每个包都是深层模块 —— 实现隐藏在子文件夹中，只能通过其入口文件访问。用户调用。
disable-model-invocation: true
---

# 设置 TS 深层模块

让本仓库的每个包都成为**深层模块（deep module）**：大量行为藏在一个小接口后面。包的公共表面是它的**入口点（entry points）** —— 位于包根目录的文件 —— 子文件夹中的一切都被隐藏。此技能安装 [dependency-cruiser](https://github.com/sverweij/dependency-cruiser) 和让入口点成为唯一入口的规则，然后证明这些规则确实生效。

关于词汇（deep module、interface、seam、depth），运行 `/codebase-design` 技能 —— 全程使用它的语言。

## 此配置强制出的形态

```
src/packages/
  <name>/
    index.ts        ← 一个入口点（公共）。从外部导入它。
    client.ts       ← 另一个入口点。包可以暴露多个。
    lib/            ← 实现：对外部隐藏，彼此可以自由导入。
    tests/          ← 就近放置的测试和夹具（子文件夹，因此是私有的）。
```

公共表面是包的**根文件** —— 而不是某个指定的 `index.ts`。按惯例，实现放在 `lib/`、测试放在 `tests/`，让每个包都有相同的两文件夹形态。但规则本身是通用的：*任何*子文件夹中的*任何*东西都是私有的，所以你永远不需要扩展配置来添加文件夹。

四条规则，全部 `error`：

1. **入口点边界** —— 包外的代码（应用代码或其他包）只能导入该包的入口点（它的根文件），绝不能导入它子文件夹中的任何东西。
2. **包内自由** —— 包自己的文件彼此自由导入。
3. **测试走入口点** —— `<pkg>/tests/` 下的文件可以导入任何包的入口点和自己的 `tests/` 夹具，但绝不能导入任何包的子文件夹内部（连自己的也不行）。跨包的集成测试没问题；深层导入不行。
4. **无循环** —— 不允许依赖循环。

**入口点，不是 barrel。** 因为公共表面是*每个*根文件，一个包可以暴露几个小入口点（`index.ts`、`client.ts`、`server.ts`），而不是把一切塞进一个巨大的 `index.ts`。重新导出整个子树的 barrel 文件是被劝阻的 —— 保持入口点小而精，把实现藏在子文件夹中。

分层（哪些包可以依赖哪些包）是*另一件事*，在配置中留作注释存根，由本仓库自行填充。

## 步骤

### 1. 检测环境

- **包管理器** —— `pnpm-lock.yaml` → pnpm，`yarn.lock` → yarn，`bun.lockb` → bun，否则 npm。下面每条命令都用它（`pnpm`/`yarn`/`npm run`/`bunx`）。
- **包根目录** —— 如果存在 `src/` 则用 `src/packages`，否则用 `packages`。如果仓库已有明显不同的约定，与用户确认选择。
- **现有配置** —— 检查是否有 `.dependency-cruiser.*` 文件。如果存在，**不要**覆盖它：合并四条规则和选项进去，并告诉用户你添加了什么。

**完成标准：** 包管理器、包根目录和现有配置状态都已确定。

### 2. 安装 dependency-cruiser

用检测到的包管理器将 `dependency-cruiser` 安装为 devDependency。

**完成标准：** `dependency-cruiser` 在 `devDependencies` 中。

### 3. 编写配置

将 [`dependency-cruiser.config.cjs`](./dependency-cruiser.config.cjs) 复制到仓库根目录，命名为 `.dependency-cruiser.cjs`。将 `PACKAGES_ROOT` 设置为步骤 1 中检测到的根目录。规则基于路径深度且与扩展名无关，所以其他什么都不用调整。

**完成标准：** `.dependency-cruiser.cjs` 存在、`PACKAGES_ROOT` 正确，且四条禁止规则都在。

### 4. 接入检查

- 添加 `lint:boundaries` 脚本：`depcruise <packages-root>`（或 `depcruise src`）。
- 将其并入仓库的总检查命令 —— 已经运行 typecheck 的那个（例如 `check` / `ci` / `validate` 脚本）。**不要**动 `tsconfig` 或添加路径别名。
- 如果没有总检查脚本，添加 `lint:boundaries` 并告诉用户将其纳入 CI。

**完成标准：** `lint:boundaries` 存在，并与 typecheck 在同一个命令中运行。

### 5. 搭建示例包

创建一个已提交的 `<packages-root>/example/` 作为可复制的模板：

- `index.ts` —— 一个入口点。导出一个委托给内部文件的函数（这样包明显是*深的*，不是直通）。
- `lib/impl.ts` —— 一个位于**子文件夹**中的内部文件，被 `index.ts` 导入，外部不可达。
- `tests/example.test.ts` —— 只导入 `../index`（一个入口点），并针对公共函数断言。

告诉用户这是一个可复制或删除的起始模板。

**完成标准：** 示例包存在，通过根入口点暴露行为，并把 `impl` 藏在子文件夹中。

### 6. 证明规则生效

这是整个技能的完成标准 —— 一个违反时不失败的配置毫无价值。

1. 运行 `lint:boundaries`。在干净的示例上必须**通过**。
2. 临时在 `tests/example.test.ts` 中添加一个深层导入（例如 `import { thing } from "../lib/impl"`）。再次运行 `lint:boundaries` —— 必须**失败**，报 `tests-through-entrypoints`。
3. 还原深层导入。再运行一次 —— 必须**通过**。

**完成标准：** 你观察到通过 → 深层导入失败 → 再次通过。如果步骤 2 没有失败，说明规则没有正确接线 —— 在完成前修复。

### 7. 记录约定

在**包文件夹内**（`<packages-root>/README.md`）写一份 `README.md` —— 就在它所管辖的包旁边 —— 涵盖：`src/packages/<name>/` 布局（入口点在根目录、`lib/` 放实现、`tests/` 放测试）、"只通过包的入口点（它的根文件）导入"，以及如何运行 `lint:boundaries`。**明确劝阻 barrel 文件** —— 暴露几个小入口点，而不是通过一个 index 重新导出整个子树。保持简洁：复制即用的代码片段加四条规则，每条一段。

然后从仓库的 agent 指令文件 —— 存在 `CLAUDE.md` 就用它，否则 `AGENTS.md`（两者都不存在则创建 `AGENTS.md`）—— 添加一个指向它的**上下文指针**。一行就够了，例如 `Packages are deep modules — see [src/packages/README.md](./src/packages/README.md) before adding or importing one.` 这正是让 agent 发现边界规则、而不是撞上去的方式。

**完成标准：** `<packages-root>/README.md` 存在且劝阻 barrels，仓库的 `CLAUDE.md`/`AGENTS.md` 链接到它。

## 注意事项

- 配置中的 `$1` 反向引用（dependency-cruiser 的分组匹配）让一个包能触及自己的内部，而外部不能 —— 不要把它们摊平成独立的按包规则。
- 公共与私有由**深度**决定：包的根文件是入口点；子文件夹中的任何东西都是私有的。惯用子文件夹是 `lib/`（实现）和 `tests/`，但规则没有硬编码它们 —— 任何子文件夹都是私有的，所以新文件夹永远不需要改配置。添加入口点只是添加一个根文件 —— 不需要 barrel。
- 包是**扁平**的：根下只有一层直接子级。包的内部可以任意嵌套；一个包不能包含另一个包。
- 使用 `.cjs`（而不是 `.js`），这样配置的 `module.exports` 即使在 `"type": "module"` 仓库中也能工作。
