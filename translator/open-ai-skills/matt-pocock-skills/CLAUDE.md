技能按分类目录组织在 `skills/` 下：

- `engineering/` — 日常编码工作
- `productivity/` — 日常非编码工作流工具
- `misc/` — 保留但很少使用，不推广
- `personal/` — 与我个人设置绑定，不推广
- `in-progress/` — 尚未准备好发布的草稿
- `deprecated/` — 已不再使用

`engineering/` 或 `productivity/`（**推广**分类）中的每个技能必须在顶层 `README.md` 中有引用，并在 `.claude-plugin/plugin.json` 中有条目。`misc/`、`personal/`、`in-progress/` 和 `deprecated/` 中的技能不得出现在这两者中。

顶层 `README.md` 中的每个技能条目必须将技能名称链接到其 `SKILL.md`。

每个分类目录都有一个 `README.md`，列出该分类中的每个技能及其一行描述，技能名称链接到其 `SKILL.md`。推广分类的 `README.md` 和顶层 `README.md` 将条目分组为**用户调用**和**模型调用**；非推广分类的 `README.md`（`misc/`、`personal/`）使用扁平列表。

`engineering/` 和 `productivity/` 中的技能还在 `docs/<bucket>/<skill-name>.md` 处有面向用户的文档页面（文档树镜像 `skills/` 下的这两个分类目录）。发布 URL 为 `https://aihero.dev/skills-<skill-name>`，无论属于哪个分类——文档路径仅用于仓库组织。当您添加、重命名或更改 `engineering/` 或 `productivity/` 中技能的行为时，请按照 [.agents/writing-docs.md](./.agents/writing-docs.md) 创建或重新同步其文档页面。非推广分类（`misc/`、`personal/`、`in-progress/`、`deprecated/`）中的技能**不**创建文档页面。

每个 `SKILL.md` 要么是用户调用（`disable-model-invocation: true`，只能由用户访问），要么是模型调用（模型或用户均可访问）。参见 [.agents/invocation.md](./.agents/invocation.md)。

[`ask-matt`](./skills/engineering/ask-matt/SKILL.md) 是路由技能，映射每个用户可访问的技能及其关联方式。与文档页面重新同步的触发器相同：每当您添加、重命名、删除或更改用户可访问技能的工作流适配时，请重新阅读 `ask-matt` 的 `SKILL.md` 并更新它，使映射保持准确——一个新技能未被提及，或一个过时技能仍被路由指向，都会使路由器失效。

要（重新）将每个技能链接到本地 harness 技能目录（`~/.claude/skills`、`~/.agents/skills`），请运行 `scripts/link-skills.sh`。每个条目是指向此仓库的符号链接，因此 `git pull` 可使已安装的技能保持最新；在添加、删除或重命名技能后重新运行该脚本。
