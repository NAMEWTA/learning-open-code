# Issue 跟踪器：GitLab

此仓库的 Issues 和 PRD 以 GitLab issues 的形式存在。所有操作使用 [`glab`](https://gitlab.com/gitlab-org/cli) CLI。

## 约定

- **创建 issue**：`glab issue create --title "..." --description "..."`。多行描述使用 heredoc。传入 `--description -` 以打开编辑器。
- **读取 issue**：`glab issue view <number> --comments`。使用 `-F json` 获取机器可读输出。
- **列出 issues**：`glab issue list -F json`，配合适当的 `--label` 过滤器。
- **评论 issue**：`glab issue note <number> --message "..."`。GitLab 将评论称为"notes"。
- **添加/移除标签**：`glab issue update <number> --label "..."` / `--unlabel "..."`。多个标签可用逗号分隔或重复标志。
- **关闭**：`glab issue close <number>`。`glab issue close` 不接受关闭评论，因此先通过 `glab issue note <number> --message "..."` 发布解释，然后关闭。
- **合并请求**：GitLab 将 PR 称为"merge requests"。使用 `glab mr create`、`glab mr view`、`glab mr note` 等——与 `gh pr ...` 相同的形式，用 `mr` 替代 `pr`，用 `note`/`--message` 替代 `comment`/`--body`。

从 `git remote -v` 推断仓库——`glab` 在 clone 内运行时自动执行此操作。

## Merge requests 作为分类界面

**MRs as a request surface: no.** _（如果此仓库将外部 merge requests 视为功能请求，则设为 `yes`；`/triage` 读取此标志。）_

当设为 `yes` 时，MR 与 issues 使用相同的标签和状态流程，使用 `glab mr` 等效命令：

- **读取 MR**：`glab mr view <number> --comments` 和 `glab mr diff <number>` 获取 diff。
- **列出待分类的外部 MR**：`glab mr list -F json`，然后仅保留作者不是项目成员/所有者的 MR（贡献者的 MR，而非维护者进行中的工作）。
- **评论 / 标签 / 关闭**：`glab mr note`、`glab mr update --label`/`--unlabel`、`glab mr close`。

与 GitHub 不同，GitLab 对 issues 和 MR 分别编号，因此一旦你知道维护者指的是哪个界面，`#42` 就是明确的。

## 当 skill 说"发布到 issue 跟踪器"时

创建一个 GitLab issue。

## 当 skill 说"获取相关工单"时

运行 `glab issue view <number> --comments`。
