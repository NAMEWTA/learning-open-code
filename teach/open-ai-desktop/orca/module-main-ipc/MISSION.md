# 使命：主进程 IPC 边界模块

## 为什么
学习者需要理解 Orca renderer 不能直接访问 Node/Electron 主进程能力，而是通过 preload 暴露的 API 与 main IPC handlers 协作。掌握这个模块后，阅读 worktree 创建、terminal spawn、Git 操作、mobile pairing 和设置更新时，可以先定位请求穿过了哪个 channel、在哪一层做权限和路径校验。

## 成功的样子
- 能说清 `src/preload/index.ts`、`registerCoreHandlers()` 和各 `register*Handlers()` 的职责边界。
- 能从 renderer API 名称追到 `ipcRenderer.invoke/send`，再追到 main 侧 `ipcMain.handle/on`。
- 能解释 PTY、Git、mobile pairing 三类 IPC 为什么分别有不同的路由和校验策略。

## 约束条件
- 本主题只做 L1 模块总览，不逐个展开所有 `src/main/ipc/*.ts` 文件。
- 课程保持 15 分钟内完成；长 channel 表、测试佐证和调用示例放入参考文档。
- 以 commit `61bd98db6faacb8baffa0de369b187c0e40d662a` 为准。

## 不在范围内
- 不深入 worktree 创建链路；后续 `slice-worktree-create-flow` 单独覆盖。
- 不展开每个 Git/GitHub/Linear/Jira handler 的业务实现。
