# 使命：CLI 与远端 Relay 模块

## 为什么
学习者需要理解 Orca 如何把桌面能力开放给命令行和远端 SSH 主机。掌握这个模块后，阅读 `orca` 命令、agent team shim、远端 PTY、文件/Git 操作和断线重连时，可以先定位到正确的进程边界。

## 成功的样子
- 能说清 `src/cli` 和 `src/relay` 分别运行在哪里、解决什么问题。
- 能从一个 CLI 命令追到 handler、RuntimeClient、main/runtime 或 relay handler。
- 能解释 relay frame、handshake、keepalive 和 dispatcher 的基本职责。

## 约束条件
- 本主题只做 L1 模块总览，不展开所有命令和 handler 的 L3 API。
- 课程保持 15 分钟内完成，长命令表和源码索引放入参考文档。
- 以 commit `61bd98db6faacb8baffa0de369b187c0e40d662a` 为准。

## 不在范围内
- 不逐个讲解 `src/cli/handlers/*` 的全部命令。
- 不深入 relay grace reconnect 的算法细节，后续由 L4 主题覆盖。
