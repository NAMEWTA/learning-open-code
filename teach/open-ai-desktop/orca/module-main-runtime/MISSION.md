# 使命：主进程 Runtime 与 Daemon 模块

## 为什么
学习者需要理解 Orca 主进程中谁持有运行时状态、谁负责跨进程控制面、谁负责长期存活的终端会话。掌握这个模块后，阅读 worktree 创建、移动端配对、CLI runtime RPC、daemon 重启和终端恢复时，可以先判断代码属于状态层、传输层还是 PTY 宿主层。

## 成功的样子
- 能说清 `OrcaRuntimeService`、`OrcaRuntimeRpcServer` 和 daemon provider 的职责边界。
- 能从主进程启动流程追到 runtime 构造、RPC server 启动和 daemon PTY provider 安装。
- 能解释为什么 PTY provider 要延迟解析、为什么 metadata/配对文件必须写到 canonical userData。

## 约束条件
- 本主题只做 L1 模块总览，不展开 `OrcaRuntimeService` 内所有工作区、Git、terminal、mobile API。
- 课程保持 15 分钟内完成；长接口清单、测试佐证和调用示例放入参考文档。
- 以 commit `61bd98db6faacb8baffa0de369b187c0e40d662a` 为准。

## 不在范围内
- 不逐个讲解 `src/main/runtime/rpc/methods/*` 的所有 method。
- 不深入创建 worktree、mobile pairing、SSH relay 这些 L2 链路，它们会在后续主题单独覆盖。
