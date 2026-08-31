# 规范安装块

一个安装故事，一套措辞。`README.md`、`.changeset/*` 和 `docs/` 下的每个页面都必须说**这一套**，不说别的。先在这里改，然后传播。

`mattpocock-skills` 已列入 **Claude Code 官方市场**——配置名为 `claude-plugins-official`，来源仓库 `anthropics/claude-plugins-official`——每个 Claude Code 安装开箱即用。不需要预先添加任何市场。官方 Anthropic 市场默认启用自动更新（[discover-plugins](https://code.claude.com/docs/en/discover-plugins)），所以"更新会自动到达"是真实的声明，而不是一个愿望。

## Claude Code —— 插件

<canonical-block name="claude-code">

```bash
claude plugins install mattpocock-skills
```

或者，在会话内部：

```
/plugin install mattpocock-skills
```

它在 Claude Code 的官方市场中，所以不需要预先添加任何东西，更新会自动到达。

</canonical-block>

## Codex 及其他 agent —— skills.sh

插件只属于 Claude Code。其他地方，[skills.sh](https://skills.sh/mattpocock/skills) 把可编辑的 skill 文件复制进项目。在 `README.md` 上使用整套形式：

<canonical-block name="skills-sh-whole-set">

```bash
npx skills@latest add mattpocock/skills
```

选择你想要的 skill，以及想将它们安装到哪些编码 agent 上。**安装器让你选择要带走哪些 skill —— 确保 `setup-matt-pocock-skills` 是其中之一。**

</canonical-block>

……以及凡是单独命名一个 skill 的地方使用单技能形式。注意 **`docs/` 页面不是这个块的消费者**：ai-hero 在正文上方渲染安装组件，所以把命令写出来的页面就是重复它。参见 [writing-docs.md](./writing-docs.md)。

<canonical-block name="skills-sh-one-skill">

```bash
npx skills@latest add mattpocock/skills --skill=<name>
```

```bash
npx skills@latest update <name>
```

</canonical-block>

`skills@latest` 是全部三处的固定拼写。`docs/` 下的页面过去各自携带这些命令的副本；现在这些块被删除而不是修正，因为站点自己渲染安装命令。

## 两条路线互斥

插件是一个你订阅的、受管理的只读捆绑包。skills.sh 写入你拥有并编辑的文件。两个都装会让用户每个技能都有两份——永远说"选一个"。

## 不属于安装故事

`.claude-plugin/marketplace.json` 让本仓库成为自己的单插件市场（`/plugin marketplace add mattpocock/skills`，然后 `/plugin install mattpocock-skills@mattpocock`）。官方列表取代了它。它保留为直接安装仓库时的回退——一个未发布的 commit，或一个 fork——并且**不**对用户文档化。
