# 使命：Relay 断线重连与 Grace Socket 机制

## 为什么

用户要完整学习 Orca，需要能解释远端 SSH 终端为什么可以活过应用重启、网络闪断和系统睡眠。本主题专门下钻 L2 会话保活里最容易误判的部分：旧 relay daemon 如何被重新接上，grace socket 如何保护 PTY，旧 client 的迟到请求如何被隔离。

## 成功的样子

- 能根据一段 relay/SSH 日志判断当前是复用旧 daemon、fresh launch 新 daemon，还是进入 terminal version mismatch。
- 能解释 `relay.js --connect`、socket identity、handshake sentinel、dispatcher generation 和 `graceTimeSeconds = 0` 各自保护的边界。
- 能说明为什么 socket 重连不会让旧 SSH channel 的残留 bytes 或旧 client 的迟到 response 污染新会话。
- 能用测试文件定位这些不变量的回归护栏。

## 约束条件

- 短课控制在 15 分钟内，只训练一个判断技能：重连链路失败时先判定守住了哪一个不变量。
- 详细源码矩阵、平台差异和测试护栏放入参考页，不把 lesson 写成源码百科。
- 本主题建立在 `module-cli-relay` 与 `slice-ssh-relay-session-flow` 已完成的基础上。

## 不在范围内

- 不逐行讲解所有 relay handler，例如 Git、filesystem、port scan、agent hook。
- 不展开远端 `orca` CLI 命令的完整调用链路；那属于 `slice-orca-cli-command-flow`。
- 不介绍通用 SSH 原理，只解释 Orca 当前源码里的实现选择。
