# 使命：Worktree 创建链路

## 为什么
用户要系统学习 Orca，需要把“新建 workspace”从一个按钮动作追到真实的 `git worktree add`、metadata 写入和终端/Agent 启动。这个 L2 主题把 renderer、store、preload、main IPC、runtime RPC 和 Git helper 串成一条可验证链路，为后续 SSH relay session flow、CLI command flow 和 reconnect 主题提供共同语境。

## 成功的样子
- 能从 New Workspace modal 追到 `WorktreeCreationRequest` 的生成，并说明为什么创建会转入后台 pending surface。
- 能解释本地桌面创建、远端 runtime RPC 创建、SSH relay 创建在 store/main/runtime 之间如何分流。
- 能说清 base ref 解析、fetch 进度、分支/路径冲突重试、`git worktree add`、metadata/lineage 写入、setup/startup terminal 的先后顺序。
- 能根据相关测试定位这条链路的关键不变量，而不是只凭 UI 行为猜测。

## 约束条件
- 短课控制在 15 分钟内，只用 3 个代表性源码文件建立主路径。
- 参考页可以展开更多源码和测试，但所有结论必须能回到 Orca 当前源码。
- 本主题是 L2 跨模块切片，必须建立在 renderer shell、main IPC、main runtime 和 shared contracts 的 L1 主题之上。

## 不在范围内
- 不逐个讲解所有 smart GitHub、GitLab、Linear、Bitbucket、Azure DevOps、Gitea 的 review 创建细节。
- 不深入 task automation 调度、source control diff、branch compare 和 reconnect 恢复逻辑。
- 不把 SSH relay 协议本身展开到 transport/session 层；那属于独立 L2 主题。
