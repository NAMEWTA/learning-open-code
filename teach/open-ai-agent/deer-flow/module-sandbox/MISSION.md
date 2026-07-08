# 使命：Sandbox 与文件系统

## 为什么
学习者希望看懂 DeerFlow 里 agent 执行命令、读取上传文件、写出 artifact 时真正经过哪些边界。掌握这部分后，他们能判断一个文件访问问题应该查 Gateway、ThreadState、sandbox provider，还是 bash/file tool 的安全校验。

## 成功的样子
- 能解释 `/mnt/user-data/workspace`、`/mnt/user-data/uploads`、`/mnt/user-data/outputs` 分别对应什么线程级 host 目录。
- 能说清 `ThreadDataMiddleware`、`SandboxMiddleware`、`SandboxProvider` 与 `Sandbox` 抽象的分工。
- 能从一次 `write_file("/mnt/user-data/outputs/...")` 推导到 Gateway artifact 路由如何读回文件。
- 能区分 Local、AIO 和 E2B provider 的隔离强度、文件同步方式与主要配置项。

## 约束条件
- 本主题是 L1 模块总览，短课限定在 15 分钟内完成。
- 输出使用简体中文，源码标识符保留英文。
- 长 provider 表、测试线索和配置速查放入 reference，lesson 只保留主线。

## 不在范围内
- 不逐行讲解 AIO/E2B provider 的所有生命周期分支。
- 不展开 Gateway uploads/artifacts 的完整垂直切片。
- 不讲前端 artifact 面板的渲染实现。
