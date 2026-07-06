# Issue 跟踪器：GitHub

此仓库的 Issues 和 PRD 以 GitHub issues 的形式存在。所有操作使用 `gh` CLI。

## 约定

- **创建 issue**：`gh issue create --title "..." --body "..."`。多行正文使用 heredoc。
- **读取 issue**：`gh issue view <number> --comments`，通过 `jq` 过滤评论并同时获取标签。
- **列出 issues**：`gh issue list --state open --json number,title,body,labels,comments --jq '[.[] | {number, title, body, labels: [.labels[].name], comments: [.comments[].body]}]'`，配合适当的 `--label` 和 `--state` 过滤器。
- **评论 issue**：`gh issue comment <number> --body "..."`
- **添加/移除标签**：`gh issue edit <number> --add-label "..."` / `--remove-label "..."`
- **关闭**：`gh issue close <number> --comment "..."`

从 `git remote -v` 推断仓库——`gh` 在 clone 内运行时自动执行此操作。

## Pull requests 作为分类界面

**PRs as a request surface: no.** _（如果此仓库将外部 PR 视为功能请求，则设为 `yes`；`/triage` 读取此标志。）_

当设为 `yes` 时，PR 与 issues 使用相同的标签和状态流程，使用 `gh pr` 等效命令：

- **读取 PR**：`gh pr view <number> --comments` 和 `gh pr diff <number>` 获取 diff。
- **列出待分类的外部 PR**：`gh pr list --state open --json number,title,body,labels,author,authorAssociation,comments`，然后仅保留 `authorAssociation` 为 `CONTRIBUTOR`、`FIRST_TIME_CONTRIBUTOR` 或 `NONE` 的（排除 `OWNER`/`MEMBER`/`COLLABORATOR`）。
- **评论 / 标签 / 关闭**：`gh pr comment`、`gh pr edit --add-label`/`--remove-label`、`gh pr close`。

GitHub 的 issues 和 PR 共享同一编号空间，因此一个裸的 `#42` 可能是其中任意一个——通过 `gh pr view 42` 解析，若失败则回退到 `gh issue view 42`。

## 当 skill 说"发布到 issue 跟踪器"时

创建一个 GitHub issue。

## 当 skill 说"获取相关工单"时

运行 `gh issue view <number> --comments`。
