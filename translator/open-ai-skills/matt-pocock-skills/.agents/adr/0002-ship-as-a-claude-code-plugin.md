# 以原生 Claude Code 插件形式发布技能集；推迟原生 Codex 插件

这些技能一直可以通过 [skills.sh](https://skills.sh/mattpocock/skills)（`npx skills add mattpocock/skills`）安装，它把可编辑的 skill 文件复制到用户的项目中，覆盖 Claude Code、Codex 和其他遵循 Agent-Skills 标准的 harness。一个反复出现的请求是**即插即用**的分发方式：把整套技能订阅为只读、始终最新的捆绑包，而不是一份你拥有的 fork。这正是原生插件系统提供的东西。

我们发布一个原生 **Claude Code 插件**，而暂时**推迟**原生 **Codex 插件**。这种分裂是由每个生态系统的插件清单选择技能的方式与本仓库的分类布局之间的冲突所决定的。

## 约束：分类技能 vs 单路径选择

技能位于 `skills/` 下的分类文件夹中——`engineering/` 和 `productivity/` 是**推广**的（随插件发布）；`misc/`、`personal/`、`in-progress/` 和 `deprecated/` **不**推广。插件必须只暴露推广集，而它横跨其中两个分类文件夹。

- **Claude Code** — `.claude-plugin/plugin.json` 接受 `skills` 作为**显式技能目录路径的数组**。我们逐个列出推广技能，零歧义地排除其他一切，并添加 `.claude-plugin/marketplace.json`，让本仓库成为自己的单插件市场。已端到端验证：`claude plugin validate . --strict` 通过，`marketplace add` → `install` 解析全部推广技能。

- **Codex** — `.codex-plugin/plugin.json` 只接受 `skills` 作为**单个路径字符串**（数组会被以 `missing or invalid plugin.json` 拒绝），并且 Codex 在其下递归发现 `SKILL.md` 文件。没有任何方法从一个路径命名两个分类文件夹，或精选一个子集。两个逃生口都已测试并拒绝：
  - 指向 `./skills/` 也会发布 `deprecated/`、`in-progress/`、`personal/` 和 `misc/`——我们刻意不推广的退役、草稿和个人技能。
  - 一个指向分类文件夹的精选**符号链接**扁平目录无法在安装后存活：Codex 把插件树复制进它的缓存并**丢弃符号链接**，所以技能到达时是空的。

给 Codex 一个仅推广的单一路径的唯一稳健方式是 (a) **重构**，让 `skills/` 只包含推广技能（把非推广分类移出去——波及 `CLAUDE.md`、`scripts/link-skills.sh`、分类 README 以及依赖 `in-progress/` 和 `personal/` 的本地开发工作流，冲击面很大），或 (b) 把推广技能的**重复副本**提交进一个扁平目录（同步负担和第二个事实来源）。两者都是结构性决策，不是该随发布 Claude 插件捆绑的东西。这很可能就是最初没有更早发布插件的、模糊记着的那个原因：清单格式无法干净地表达一个分类仓库的精选子集。

## 决策

- 现在发布 **Claude Code 插件**（`.claude-plugin/plugin.json` + `.claude-plugin/marketplace.json`），精选到推广集，作为 v1.2 的头条交付物。
- 保留 **skills.sh** 作为通用安装器——它今天已经服务于 Codex 和其他 harness，所以没有 Codex 用户会失去安装路径。
- **推迟**原生 Codex 插件，直到我们决定是在把 `skills/` 重构为仅推广，还是提交一份生成的扁平副本之间做选择。当 Codex 支持 `skills` 数组 / 包含列表，或在安装时保留符号链接时，重新考虑。

## 这创造的恒常约束

- 每个推广技能在 `.claude-plugin/plugin.json` 的 `skills` 数组中都有条目（这本来已经是 `CLAUDE.md` 的规则；现在它同时把关插件的内容）。
- `.claude-plugin/plugin.json` 的 `version` 跟踪 `package.json` 的 version——发布时两者一起升级。Claude 用插件 `version` 决定已安装用户何时看到更新。

## 更新，2026-08-05

`mattpocock-skills` 已被 **Claude Code 官方市场**接纳——配置名为 `claude-plugins-official`，来源仓库 `anthropics/claude-plugins-official`——每个 Claude Code 安装都默认拥有它。`claude plugins install mattpocock-skills` 现在是文档化路线，上面的 `marketplace add` → `install` 路径已被取代。安装措辞存在于 [.agents/install-block.md](../install-block.md)。

官方列表指向本仓库的 git URL，直接读取 `.claude-plugin/plugin.json`，所以它不依赖 `.claude-plugin/marketplace.json`。该文件仅保留为直接安装仓库时的回退（一个未发布的 commit，或一个 fork）。

2026-08-05 在 Claude Code 2.1.222 上对照线上列表验证：

- `claude plugins install mattpocock-skills` 无需预先添加市场即可解析，并报告 `mattpocock-skills@claude-plugins-official`。
- `claude plugin details mattpocock-skills` 随后报告版本 1.2.0 并加载推广技能。
- 列表的 `source` 是 `{"source": "url", "url": "https://github.com/mattpocock/skills.git", "sha": …}`——**sha 被钉住**，所以一个发布要等到那个钉移动时才到达已安装用户，而不是我们打 tag 的那一刻。写本文时钉落后于 `main` 两个 commit，这就是为什么它列出 22 个技能而不是 `plugin.json` 中的 24 个。
- 会话内的 `/plugin install mattpocock-skills` **未**被实测——`/plugin` 在无头（`claude -p`）会话中不可用。它运行与 CLI 相同的解析器，文档化的示例形式是 `/plugin install <name>@claude-plugins-official`。
