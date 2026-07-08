# 使命：插件生命周期全链路

## 为什么
读者需要把 Super Productivity 的插件系统当成一条可追踪的运行链路来理解，而不是只记住几个分散的服务名。学完后应能从 manifest、社区插件列表或上传插件一路追到发现、启用、Bridge/API 调用、OAuth、Node executor 和 issue provider 接入边界。

## 成功的样子
- 能区分“社区列表展示”“manifest 发现”“插件代码执行”“issue sync adapter 注册”这四个不同阶段。
- 能说明 web iframe/plugin bridge、Electron OAuth、Node executor 三条边界分别由哪些文件守住。
- 能定位一个 issue provider 插件从 `registerIssueProvider()` 到 `searchIssues()` 或 `getById()` 被调用的路径。
- 能判断插件启动失败时应优先检查 manifest、启用状态、OAuth token、Node 授权还是 provider 注册。

## 约束条件
- 本主题是 L2 垂直切片，只交付一节 15 分钟内的路径图短课和一份可反复查阅的参考文档。
- 教学写作使用简体中文；源码标识符、路径、API 名保留英文。
- 所有源码引用使用源项目内相对路径，不带仓库分类目录前缀。

## 不在范围内
- 不展开每个插件 UI 组件的样式和管理页交互细节。
- 不深入讲解各个第三方平台的业务 API，例如 GitHub、Google Calendar 或 CalDAV 的完整协议。
- 不把 issue provider 的远端同步算法作为本 L2 的主课内容；只讲注册、调用和 sync adapter 接入边界。
