# 使命：插件 Node execution grant 全链路

## 为什么
读者需要把 Super Productivity 的 `nodeExecution` 当成一条受主进程守门的安全链路来理解，而不是把 `executeNodeScript()` 当成普通 renderer API。学完后应能从插件启用、`onReady`、脚本执行一路追到 native consent、session grant、IPC 校验与脚本执行边界。

## 成功的样子
- 能区分 session grant token、renderer 本地 token 缓存、main 持久化 consent 三者的职责。
- 能说明为什么 renderer 不能自写 consent，以及 built-in 与 uploaded 插件的对话框差异。
- 能定位 grant 申请、脚本执行、revoke/clear consent 分别落在哪些文件。
- 能判断 nodeExecution 失败时应先查平台、grant、bridge ping 还是 main 进程脚本执行。

## 约束条件
- 本主题是 L2 垂直切片，只交付一节 15 分钟内的路径图短课和一份可反复查阅的参考文档。
- 教学写作使用简体中文；源码标识符、路径、API 名保留英文。
- 所有源码引用使用源项目内相对路径，不带仓库分类目录前缀。

## 不在范围内
- 不展开每个内置 node 插件的业务脚本逻辑。
- 不深入讲解 issue provider 或 OAuth 边界；只在与 grant 交接处做交叉引用。
- 不把 Electron 全量 IPC 或 preload 暴露面作为本 L2 主课内容。
