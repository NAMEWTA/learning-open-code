# OpenHanako / HanaAgent 源码学习计划

## 一、文档目标

本计划用于系统学习 OpenHanako（HanaAgent）源码，目标不是逐文件浏览，而是建立以下能力：

1. 能完整解释 HanaAgent 的系统架构和模块边界。
2. 能独立启动桌面端、Server 和 CLI，并定位启动问题。
3. 能追踪一条聊天消息从 UI 到模型、工具执行，再返回 UI 的完整链路。
4. 能理解 Agent、Session、Model、Skill、Channel、Bridge 和 Plugin 的生命周期。
5. 能理解文件、记忆、自动化和多 Agent 协作系统。
6. 能判断一个新功能应放在 `desktop`、`server`、`core`、`hub`、`lib` 还是插件中。
7. 能完成至少一个小型功能修改或插件开发。
8. 能输出一份完整的架构文档和关键链路时序图。


# 第一阶段：环境准备与仓库全景

## 第 1 周：建立项目地图

### 本周目标

- 成功运行项目。
- 理解仓库各顶层目录的定位。
- 明确主要运行进程。
- 理解构建、测试和代码规范。
- 建立第一版架构图。

---

## 第 1 天：阅读项目入口文档

### 阅读内容

```text
README.md
CONTRIBUTING.md
SECURITY.md
PLUGINS.md
PLUGIN_SDK.md
package.json

```

### 重点问题

1. HanaAgent 的产品定位是什么？
2. 它与普通 Electron 聊天客户端有什么区别？
3. 项目有哪些客户端入口？
4. Server 是否能独立于 Electron 运行？
5. Agent 的数据保存在哪里？
6. 插件可以扩展哪些能力？
7. 项目当前接受什么类型的贡献？
8. 支持哪些外部 Bridge？
9. 主要 npm scripts 分别做什么？
10. Node.js 版本和原生依赖要求是什么？

### 实践任务

执行并记录结果：

```bash
npm install
npm run typecheck
npm run lint
npm test

```

再根据仓库脚本启动开发环境。

### 当日输出

创建 `docs-learning/[01-repository-overview.md](http://01-repository-overview.md)`，至少包含：

- 项目定位
- 主要功能
- 主要运行方式
- 环境要求
- 开发命令
- 初步疑问清单

---

## 第 2 天：分析构建体系

### 阅读内容

```text
package.json
vite.config*.js
vite.config*.ts
vitest.config.js
tsconfig.base.json
tsconfig.json
tsconfig.node.json
tsconfig.test.json
scripts/

```

### 重点问题

1. Renderer、Server、Main、Preload 是否分别构建？
2. Electron 主进程为什么使用 `.cjs`？
3. Server 如何收集生产依赖？
4. `better-sqlite3` 和 `node-pty` 如何参与构建？
5. Open 和 Full Server 构建有什么差异？
6. 哪些代码由 TypeScript 检查，哪些由 Vite 输出？
7. 打包时如何处理 Native Module？
8. Windows、macOS、Linux 的打包差异是什么？

### 实践任务

为主要构建脚本建立映射表：


| 命令  | 输入  | 输出  | 运行环境 | 用途  |
| --- | --- | --- | ---- | --- |


### 当日输出

绘制一张构建产物关系图：

```text
TypeScript Source
├── Renderer Bundle
├── Server Bundle
├── Electron Main
├── Preload
├── Plugin Packages
└── Native Helpers

```

---

## 第 3 天：理解目录边界

### 阅读目录

```text
core/
lib/
server/
hub/
desktop/
shared/
packages/
plugins/
cli/
tests/

```

本日不深入具体实现，只阅读每个目录的文件名和入口文件。

### 重点问题

1. `core` 与 `lib` 的边界是什么？
2. `server` 是否包含业务逻辑？
3. `hub` 与普通聊天会话是什么关系？
4. `shared` 中哪些内容属于跨层契约？
5. `packages` 与 `plugins` 有什么区别？
6. `desktop` 中 Electron Shell 和 React Renderer 如何分离？
7. 哪些模块可以被插件扩展？
8. 哪些模块是内部实现，不应直接依赖？

### 实践任务

制作模块职责表：


| 目录        | 核心职责       | 允许依赖              | 不应承担的职责    |
| --------- | ---------- | ----------------- | ---------- |
| `desktop` | UI 和桌面壳    | Server API、shared | Agent 核心编排 |
| `server`  | HTTP/WS 接口 | Engine、shared     | 底层工具实现     |
| `core`    | 业务编排       | lib、shared        | React UI   |
| `lib`     | 基础能力       | shared            | 页面状态       |
| `hub`     | 后台任务和路由    | core、lib          | 桌面组件       |


### 当日输出

完成第一版“仓库目录架构图”。

---

## 第 4 天：代码规范和架构约束

### 阅读内容

```text
eslint.config.js
tsconfig.base.json
相关 lint:boundary 脚本
现有测试文件命名

```

### 重点问题

1. 为什么 Server Route 不能访问 `engine._xxx`？
2. 为什么后端不能直接导入底层 Pi SDK？
3. React 中为什么限制 `document.createElement`？
4. `any`、未使用变量和空代码块为什么只是 warning？
5. `.js` 扩展名导入与 TypeScript 源文件如何配合？
6. Manager、Coordinator、Registry、Store、Router 的命名区别是什么？

### 实践任务

整理一份“新增代码检查清单”：

- 是否跨越了架构边界？
- 是否直接访问私有 Engine 成员？
- 是否直接导入底层 Pi SDK？
- 是否存在不必要的 `any`？
- 是否有资源清理？
- 是否有错误处理？
- 是否有测试？
- 是否会暴露本地路径或秘密信息？

### 当日输出

创建 [`02-coding-rules.md`](http://02-coding-rules.md)。

---

## 第 5 天：建立运行时进程模型

### 阅读内容

```text
desktop/bootstrap.cjs
desktop/main.cjs
desktop/preload.cjs
cli/
server/main-open.ts
server/main-full.ts
server/bootstrap.ts
server/index.ts

```

### 重点问题

1. Electron 启动后首先执行哪个文件？
2. Electron 如何启动 Server？
3. Electron 如何知道 Server 已经就绪？
4. Server 端口和鉴权信息从哪里获得？
5. Renderer 如何访问 Server？
6. Preload 暴露了哪些桌面能力？
7. CLI 如何发现或启动 Server？
8. Server 独立运行时与 Electron 模式有什么差异？

### 实践任务

在关键入口添加临时日志或使用调试器记录启动顺序。

### 本周里程碑

能够不看源码口述以下链路：

```text
Electron Bootstrap
→ Electron Main
→ Spawn HanaAgent Server
→ Server Bootstrap
→ 创建 HanaEngine
→ 注册 HTTP/WS
→ Renderer 加载
→ Renderer 连接 Server

```

---

# 第二阶段：核心 Engine 与领域对象

## 第 2 周：HanaEngine、Agent 和 Session

### 本周目标

- 理解 `HanaEngine` 的组合根角色。
- 理解 Manager 的初始化和依赖关系。
- 理解 Agent 与 Session 的区别。
- 能追踪 Session 创建和恢复流程。

---

## 第 6 天：阅读 HanaEngine 结构

### 阅读内容

```text
core/engine.ts

```

不要一开始逐行阅读，先按以下方式分段：

1. import 区域
2. 类型和接口
3. 内部字段
4. constructor
5. initialize/start
6. shutdown/dispose
7. Agent 公开方法
8. Session 公开方法
9. Model、Skill、Plugin 等代理方法
10. Event 和 Resource 方法

### 重点问题

1. Engine 拥有哪些 Manager？
2. 哪些组件在构造时创建？
3. 哪些组件延迟初始化？
4. 初始化顺序为什么重要？
5. Engine 是 Facade、Service Locator，还是两者兼有？
6. 哪些方法是供 Server Route 调用的公开 API？
7. 哪些下划线成员属于内部实现？

### 实践任务

建立 Engine 依赖表：


| Engine 成员 | 类型  | 初始化时机 | 依赖项 | 对外职责 |
| --------- | --- | ----- | --- | ---- |


---

## 第 7 天：AgentManager

### 阅读内容

```text
core/agent-manager.ts
core/agent.ts
shared/agent-id.ts
相关 Agent 配置和资源模块

```

### 重点问题

1. Agent 的唯一标识如何生成和验证？
2. Agent 配置如何加载？
3. Agent Runtime 何时创建？
4. 活动 Agent 如何切换？
5. Agent 删除后是否可以恢复？
6. Agent 数据目录中包含什么？
7. 多 Agent 之间如何隔离？
8. Agent 如何获得 Model、Skill、Memory 和 Workspace？

### 实践任务

跟踪一次“创建 Agent”操作：

```text
UI
→ Agent Route
→ HanaEngine
→ AgentManager
→ 文件或数据库
→ Event
→ UI 刷新

```

### 输出

绘制 Agent 生命周期状态图：

```text
不存在
→ 创建
→ 已加载
→ Runtime 初始化
→ 活动
→ 非活动
→ 删除
→ 恢复或永久清理

```

---

## 第 8 天：SessionCoordinator 第一部分

### 阅读内容

```text
core/session-coordinator.ts

```

第一天只关注：

- Session 数据结构
- 内部 Map 和 Cache
- 构造函数
- 依赖注入
- Session 创建
- Session 列表
- Session 恢复

### 重点问题

1. Agent 与 Session 是一对多还是多对多？
2. Session 的持久化身份是什么？
3. Session Runtime 与 Session Metadata 有什么区别？
4. 为什么需要休眠 Session？
5. 当前 Session 如何保存？
6. Session 列表如何生成和缓存？
7. Session Manifest 的作用是什么？

### 实践任务

记录 Session 创建过程中所有写入的文件和状态。

---

## 第 9 天：SessionCoordinator 第二部分

继续阅读：

- Runtime 创建和释放
- AbortController
- 当前 Turn Context
- 权限模式
- Session Compaction
- 压力和健康管理
- 清理逻辑

### 重点问题

1. 用户停止生成时，信号如何传递？
2. 一个 Session 可以同时执行多个 Turn 吗？
3. 工具运行时如何绑定到 Session？
4. Session 什么时候进入休眠？
5. 内存压力出现时会发生什么？
6. Session 压缩和长期记忆有什么区别？
7. 会话删除时需要清理哪些资源？

### 实践任务

在 Session 创建、休眠、恢复、删除处设置断点，并记录调用栈。

---

## 第 10 天：Model、Preferences 和 Config

### 阅读内容

```text
core/model-manager.ts
core/preferences-manager.ts
core/config-coordinator.ts
core/provider-registry.ts
shared/config*
shared/model*

```

### 重点问题

1. 模型配置分为哪些槽位？
2. Provider 凭据保存在什么位置？
3. 模型引用如何规范化？
4. Provider 如何注册？
5. Preferences 和 Config 的边界是什么？
6. Agent 级、全局级、Session 级配置如何合并？
7. 模型切换如何影响已有 Session？

### 本周里程碑

可以解释：

```text
HanaEngine
├── AgentManager
├── SessionCoordinator
├── ModelManager
├── PreferencesManager
├── SkillManager
├── ChannelManager
├── BridgeSessionManager
└── PluginManager

```

并能说明每个组件的生命周期和主要依赖。

---

# 第三阶段：聊天主链路

## 第 3 周：追踪一条完整聊天消息

### 本周目标

完整跟踪：

```text
React 输入
→ HTTP/WS
→ Chat Route
→ HanaEngine
→ SessionCoordinator
→ Agent Runtime
→ Pi SDK
→ 模型调用
→ 工具调用
→ 流式事件
→ Store
→ UI 渲染

```

---

## 第 11 天：前端聊天入口

### 阅读内容

```text
desktop/src/main.tsx
desktop/src/react/chat/
desktop/src/react/stores/
desktop/src/react/services/

```

### 重点问题

1. 输入框状态保存在哪里？
2. 发送按钮调用哪个 Service？
3. 当前 Agent 和 Session 从哪里获得？
4. 附件如何加入请求？
5. 消息发送后如何进入本地 Store？
6. 流式回复如何更新同一条消息？
7. 错误和中断如何显示？

### 实践任务

从“发送按钮”开始，通过 IDE 的引用查找，一直跟踪到网络请求函数。

---

## 第 12 天：Server Chat 和 Session 路由

### 阅读内容

```text
server/routes/chat*
server/routes/sessions*
server/session-stream-store.ts
server/app-events.ts
server/resource-events-ws.ts

```

### 重点问题

1. HTTP 和 WebSocket 分别承担什么？
2. 消息发送接口的请求结构是什么？
3. Server 如何验证 Agent 和 Session？
4. Stream 如何与 Session 绑定？
5. 断线重连后是否可以恢复事件？
6. Server Route 通过 Engine 的哪个公开方法发起 Turn？
7. 错误如何转化为客户端可理解的结构？

### 实践任务

使用浏览器开发者工具或日志记录：

- 请求 URL
- 请求体
- 响应
- WebSocket 消息类型
- Event ID
- Session ID

---

## 第 13 天：进入 Agent Runtime

### 阅读内容

```text
core/engine.ts 中聊天相关公开方法
core/session-coordinator.ts 中 Turn 相关代码
core/agent.ts
lib/pi-sdk/

```

### 重点问题

1. Session Runtime 如何取得 Agent 配置？
2. System Prompt 如何生成？
3. 人格、记忆、Skills 在什么阶段注入？
4. 当前工作区如何传给 Runtime？
5. 模型 Provider 如何选择？
6. 工具列表如何生成？
7. Turn Context 中包含什么？

### 实践任务

记录一次模型请求前的上下文组成：

```text
System Instructions
Personality
Memory
Session History
Skills
Workspace Context
User Message
Attachments
Tool Definitions

```

---

## 第 14 天：工具执行链

### 阅读内容

```text
lib/tools/
core/execution-router.ts
core/execution-boundary.ts
core/capability-policy.ts
lib/permission/
core/confirmation*
core/approval*

```

### 重点问题

1. 工具如何注册到 Agent Runtime？
2. 模型返回 Tool Call 后由谁执行？
3. Execution Router 如何选择执行器？
4. 哪些工具需要用户确认？
5. Approval Gateway 如何阻塞和恢复执行？
6. 工具错误如何返回模型？
7. 工具结果如何进入消息流？
8. 工具取消时如何清理子进程和文件句柄？

### 实践任务

选择一个简单工具，例如文件读取或 Shell 命令，完整跟踪：

```text
模型 Tool Call
→ 工具名称解析
→ 参数校验
→ 权限判断
→ 用户确认
→ 工具执行
→ 结果规范化
→ 返回模型
→ UI 卡片展示

```

---

## 第 15 天：流式事件返回 UI

### 阅读内容

```text
server/session-stream-store.ts
WebSocket 事件处理
desktop/src/react/stores/
desktop/src/react/chat/
消息卡片相关组件

```

### 重点问题

1. 文本 Token、思考、工具调用、工具结果分别是什么事件？
2. Store 如何防止重复事件？
3. 工具卡片如何识别？
4. 历史消息重新加载时如何还原卡片？
5. Session 切换后旧 Stream 如何处理？
6. 用户中断生成后 UI 如何更新？

### 本周里程碑

输出完整聊天时序图：

```text
User
→ React Chat
→ Chat Service
→ Server Route
→ HanaEngine
→ SessionCoordinator
→ Agent Runtime
→ Model Provider
→ Tool Runtime
→ Session Stream
→ WebSocket
→ Zustand Store
→ React Message Components

```

---

# 第四阶段：文件、安全和资源系统

## 第 4 周：理解 Agent 如何操作电脑

### 本周目标

- 理解 Workspace 和 Desk。
- 理解 SessionFile。
- 理解路径权限和系统沙盒。
- 理解 Resource Ticket 和媒体访问。
- 理解终端、浏览器和 Computer Use。

---

## 第 16 天：Workspace 和 Desk

### 阅读内容

```text
lib/desk/
lib/session-files/
lib/file-ref/
server/routes/desk*
server/routes/fs*
core/resource-service.ts

```

### 重点问题

1. Desk 和 Workspace 有什么区别？
2. Agent 工作目录如何确定？
3. 文件引用为什么不能只使用绝对路径？
4. 文件如何登记为 SessionFile？
5. 文件删除和移动后引用是否仍有效？
6. Desktop 和 Mobile 如何消费同一个文件？

---

## 第 17 天：Resource 系统

### 阅读内容

```text
lib/resources/
lib/resource-io/
core/resource-service.ts
server/routes/resources*
server/routes/media*

```

### 重点问题

1. Resource 与普通文件有什么区别？
2. Resource 是否可以来自插件、会话和外部 Bridge？
3. 下载票据如何生成？
4. 资源票据是否有过期时间和次数限制？
5. MIME 类型如何识别？
6. 如何阻止任意本地路径被公开访问？

### 实践任务

跟踪一个 Agent 生成文件从本地到 Desktop 预览的完整流程。

---

## 第 18 天：PathGuard 和权限策略

### 阅读内容

```text
lib/sandbox/path-guard.ts
lib/sandbox/policy.ts
lib/sandbox/managed-config-guard.ts
lib/permission/
core/capability-policy.ts

```

### 重点问题

1. 允许读取和允许写入的目录是否相同？
2. 路径规范化如何防止 `../` 穿越？
3. 符号链接如何处理？
4. 配置文件为什么需要特殊保护？
5. Agent、Plugin 和用户操作的权限是否一致？
6. 不同安全等级如何改变策略？

### 实践任务

设计至少五个路径安全测试：

- 正常工作区文件
- `../` 路径穿越
- 符号链接逃逸
- 系统配置文件
- Agent 数据目录外写入

---

## 第 19 天：操作系统沙盒

### 阅读内容

```text
lib/sandbox/seatbelt.ts
lib/sandbox/bwrap.ts
desktop/native/
Windows sandbox helper 相关脚本

```

### 重点问题

1. macOS Seatbelt 策略如何生成？
2. Linux Bubblewrap 挂载哪些目录？
3. Windows 当前提供什么隔离？
4. 网络访问如何限制？
5. 系统沙盒不可用时是否降级？
6. 应用层 PathGuard 和 OS 沙盒为什么必须同时存在？

---

## 第 20 天：Terminal、Browser 和 Computer Use

### 阅读内容

```text
lib/terminal/
lib/shell/
lib/exec-command/
lib/browser/
core/computer-use/

```

### 重点问题

1. 一次性命令和持续终端有什么区别？
2. `node-pty` 会话如何保存和销毁？
3. Browser Tool 如何控制浏览器？
4. Computer Use 如何获取截图和执行动作？
5. 工具超时如何处理？
6. Server 退出时如何清理残留子进程？

### 本周里程碑

输出“Agent 操作本机安全边界图”：

```text
Model Request
→ Capability Policy
→ PathGuard
→ Approval Gateway
→ OS Sandbox
→ Tool Process
→ Resource Registration
→ Client Delivery

```

---

# 第五阶段：记忆、自动化和多 Agent

## 第 5 周：后台智能系统

### 本周目标

- 理解短期会话与长期记忆的区别。
- 理解记忆编译和反思。
- 理解 Hub、Cron 和后台任务。
- 理解 Agent 频道与 DM。

---

## 第 21 天：记忆目录全景

### 阅读内容

```text
lib/memory/

```

先按文件职责分类：


| 类型          | 示例职责       |
| ----------- | ---------- |
| Fact Store  | 保存结构化事实    |
| Compile     | 将原始内容编译为记忆 |
| Snapshot    | 保存编译状态     |
| Search      | 检索相关记忆     |
| Reflection  | 反思和总结      |
| Deep Memory | 深度分析       |
| Budget      | 控制模型消耗     |
| Ticker      | 定期维护       |


### 重点问题

1. 什么内容会进入长期记忆？
2. 记忆是否与 Agent 隔离？
3. 记忆搜索发生在 Turn 的哪个阶段？
4. 记忆编译是否同步执行？
5. 大工具模型在记忆系统中承担什么工作？
6. 失败的记忆任务如何恢复？

---

## 第 22 天：记忆生成链

跟踪：

```text
Session Message
→ 候选内容
→ Compile
→ Fact Store
→ Snapshot
→ Reflection
→ 后续 Session Search
→ Prompt 注入

```

### 实践任务

通过日志或测试验证：

1. 完成一段包含个人偏好的对话。
2. 结束或切换会话。
3. 找到生成的记忆数据。
4. 在新会话中观察该记忆是否被检索。
5. 记录记忆注入的位置和格式。

---

## 第 23 天：Hub 与 Event Bus

### 阅读内容

```text
hub/index.ts
hub/event-bus.ts
hub/event-bus-capabilities.ts
hub/agent-executor.ts

```

### 重点问题

1. Hub 在 Server 启动的哪个阶段初始化？
2. Event Bus 中有哪些事件？
3. 哪些组件可以发布事件？
4. 事件能力为什么需要权限控制？
5. Agent Executor 与前台 Session Runtime 有何区别？
6. 后台任务是否会创建独立 Session？

---

## 第 24 天：Scheduler 和 Cron

### 阅读内容

```text
hub/scheduler.ts
自动化相关 Route
任务持久化模块

```

### 重点问题

1. Cron 配置保存在什么位置？
2. Server 重启后任务如何恢复？
3. 触发器和任务执行为什么分离？
4. 同一任务重复触发如何处理？
5. 执行失败是否重试？
6. 后台任务如何发送通知？
7. 任务如何选择 Agent 和模型？

### 实践任务

创建一个最简单的定时任务，跟踪：

```text
Cron 配置
→ Scheduler 注册
→ 时间触发
→ Agent Executor
→ Agent Runtime
→ 工具或文本结果
→ Notification

```

---

## 第 25 天：Channel 和 DM

### 阅读内容

```text
core/channel-manager.ts
hub/channel-router.ts
hub/dm-router.ts
lib/session-collab/
server/routes/channels*
server/routes/dm*

```

### 重点问题

1. 多 Agent 频道如何表示？
2. 一个频道消息会触发几个 Agent？
3. 如何避免 Agent 无限互相回复？
4. Agent DM 与普通 Session 有何区别？
5. Guest Handler 解决什么问题？
6. 频道消息如何进入各 Agent 的记忆？

### 本周里程碑

完成三张图：

1. 记忆生命周期图
2. Cron 后台任务时序图
3. 多 Agent Channel/DM 消息路由图

---

# 第六阶段：插件体系

## 第 6 周：从宿主到插件 SDK

### 本周目标

- 理解插件发现、加载、注册和卸载。
- 理解 Plugin Protocol。
- 理解 restricted 与 full-access。
- 完成一个最小插件。

---

## 第 26 天：PluginManager

### 阅读内容

```text
core/plugin-manager.ts
plugins/

```

### 重点问题

1. 插件从哪些目录发现？
2. 插件 Manifest 包含什么？
3. 插件如何启用和禁用？
4. PluginManager 保存了哪些注册表？
5. 插件加载失败是否影响 Server？
6. 插件更新后如何重新加载？
7. 插件配置保存在哪里？

### 实践任务

建立插件注册能力表：


| 能力       | 注册位置              | 权限要求            | 生命周期          |
| -------- | ----------------- | --------------- | ------------- |
| Tool     | Tool Registry     | restricted/full | Agent Runtime |
| Route    | Route Registry    | full-access     | Server        |
| Provider | Provider Registry | full-access     | Model         |
| Page     | UI Registry       | full-access     | Renderer      |
| Skill    | Skill Paths       | restricted/full | Agent         |
| Command  | Command Registry  | restricted/full | Session       |


---

## 第 27 天：Plugin Protocol 和 Runtime

### 阅读内容

```text
packages/plugin-protocol/
packages/plugin-runtime/

```

### 重点问题

1. Protocol 中定义了哪些跨边界类型？
2. Host 和 Plugin 如何通信？
3. Runtime 如何加载插件代码？
4. 插件异常如何隔离？
5. 插件版本和宿主 Contract 如何校验？
6. 插件是否能直接访问 Engine？

---

## 第 28 天：Plugin SDK 和组件

### 阅读内容

```text
packages/plugin-sdk/
packages/plugin-components/
examples/plugins/sdk-showcase/

```

### 重点问题

1. SDK 暴露了哪些稳定 API？
2. 插件页面如何调用宿主能力？
3. 插件 Widget 如何渲染？
4. 插件设置项如何声明？
5. 插件工具如何定义参数 Schema？
6. SDK Showcase 演示了哪些能力？

---

## 第 29 天：内置插件分析

选择两个内置插件深入阅读：

```text
plugins/mcp/
plugins/office/
plugins/media/
plugins/beautify/
plugins/jimeng-cli/

```

推荐组合：

- `mcp`：学习外部工具协议接入
- `office`：学习文件和办公能力
- `media`：学习资源、UI 和工具协作

### 输出

为每个插件回答：

- 入口在哪里？
- 注册了什么？
- 使用了哪些宿主 API？
- 需要什么权限？
- 如何保存配置？
- 如何处理错误？
- 是否有前端页面？

---

## 第 30 天：开发最小插件

建议实现一个“学习日志插件”：

### 功能

- 提供 `/study-log` 命令。
- 提供一个 Agent Tool。
- 接收标题和学习总结。
- 将内容写入受控工作区文件。
- 返回一个可打开的 SessionFile。
- 可选增加设置项：默认日志目录。

### 验收标准

- 插件可安装。
- 可启用和禁用。
- 命令可以调用。
- Tool 参数有 Schema。
- 文件写入遵守 PathGuard。
- 错误不会导致 Server 崩溃。
- 有最少一个测试。

---

# 第七阶段：Bridge、CLI 与多客户端

## 第 7 周：理解同一 Agent 如何服务多个入口

### 本周目标

- 理解 Bridge Adapter。
- 理解外部用户和频道映射。
- 理解 CLI 接入。
- 理解 Mobile PWA。
- 比较不同客户端的能力差异。

---

## 第 31 天：Bridge 总体架构

### 阅读内容

```text
lib/bridge/
core/bridge-session-manager.ts
server/routes/bridge*

```

### 重点问题

1. Bridge Adapter 的统一接口是什么？
2. 外部用户如何映射到内部身份？
3. 外部私聊如何映射为 Session？
4. 外部群组如何映射为 Channel？
5. Bridge 上下文如何传入 Agent？
6. 回复如何回传原平台？

---

## 第 32 天：分析一个具体 Bridge

选择 Telegram、飞书、QQ 或微信中的一个。

### 跟踪链路

```text
外部平台 Webhook / Polling
→ Bridge Adapter
→ 身份和频道解析
→ BridgeSessionManager
→ Agent Session
→ Agent 回复
→ 媒体转换
→ 平台发送 API

```

### 重点问题

1. 文本和媒体消息如何统一？
2. 引用消息如何处理？
3. 平台文件大小限制在哪里处理？
4. Markdown 或富文本如何转换？
5. 平台 API 失败如何重试？
6. 如何防止外部用户访问本地任意文件？

---

## 第 33 天：CLI

### 阅读内容

```text
cli/
server/cli.ts

```

### 重点问题

1. `hana` 命令如何解析参数？
2. CLI 如何确定 Server 地址？
3. Server 不存在时是否自动启动？
4. CLI 如何显示流式消息和工具结果？
5. CLI 能进行哪些会话管理操作？
6. CLI 与桌面端是否共用 API？

### 实践任务

使用 CLI 完成：

- 查看 Server 状态
- 新建 Session
- 发送消息
- 查看历史
- 中断执行

---

## 第 34 天：Mobile PWA

### 阅读内容

```text
desktop/src/mobile-main.tsx
desktop/src/react/mobile/
PWA manifest
Service Worker
server/routes/mobile-static*
server/routes/mobile-workbench*

```

### 重点问题

1. Mobile 是否与桌面 Renderer 共用组件？
2. 移动端如何鉴权？
3. Service Worker 缓存什么？
4. Mobile Workbench 提供什么能力？
5. 移动端如何下载 SessionFile？
6. 移动端缺失哪些桌面原生能力？

---

## 第 35 天：统一客户端能力矩阵

制作以下表格：


| 能力         | Desktop | Mobile | CLI | Telegram | 飞书  | QQ  | 微信  |
| ---------- | ------- | ------ | --- | -------- | --- | --- | --- |
| 文本聊天       |         |        |     |          |     |     |     |
| 工具卡片       |         |        |     |          |     |     |     |
| 文件上传       |         |        |     |          |     |     |     |
| 文件下载       |         |        |     |          |     |     |     |
| 用户确认       |         |        |     |          |     |     |     |
| 媒体预览       |         |        |     |          |     |     |     |
| 多 Agent 频道 |         |        |     |          |     |     |     |


### 本周里程碑

能够解释为什么项目需要：

- SessionFile
- Resource Ticket
- Bridge Context
- Client Capability
- Server-first 架构

---

# 第八阶段：前端架构、综合验证与实战

## 第 8 周：完成全局闭环

### 本周目标

- 理解 React 状态和页面组织。
- 将前七周链路串联起来。
- 完成一个小功能。
- 输出最终架构文档。

---

## 第 36 天：React 应用入口和路由

### 阅读内容

```text
desktop/src/main.tsx
desktop/src/react/
desktop/src/react/settings/
desktop/src/react/onboarding/
desktop/src/react/quick-chat/

```

### 重点问题

1. React 根组件如何初始化？
2. 应用有哪些主要页面状态？
3. Onboarding 如何判断是否完成？
4. Settings 如何读取和更新 Server 配置？
5. Quick Chat 与主窗口是否共用 Store？
6. 错误总线如何显示全局错误？

---

## 第 37 天：Zustand Store 和 Service

### 阅读内容

```text
desktop/src/react/stores/
desktop/src/react/services/
shared/ 中相关 Contract

```

### 重点问题

1. Store 按领域如何拆分？
2. Server 数据与本地 UI 状态如何区分？
3. 是否存在乐观更新？
4. WebSocket Event 如何写入 Store？
5. Session 切换如何重置状态？
6. 网络断线如何恢复？
7. Store 是否直接访问 Electron IPC？

### 实践任务

为一个 Store 绘制数据流：

```text
Component
→ Action
→ Service/API
→ Server
→ Event
→ Store Mutation
→ Component Re-render

```

---

## 第 38 天：综合跟踪启动链路

重新完整追踪：

```text
desktop/bootstrap.cjs
→ desktop/main.cjs
→ Server Process
→ server/bootstrap.ts
→ HanaEngine
→ Manager 初始化
→ HTTP/WS 启动
→ Preload
→ React
→ Store 初始化
→ Server 连接
→ Agent/Session 加载

```

### 输出

完成最终版启动时序图，并标出：

- 进程边界
- IPC 边界
- HTTP 边界
- WebSocket 边界
- 文件系统边界

---

## 第 39 天：完成一个小型源码功能

推荐功能之一：

### 方案 A：Session 诊断信息

新增一个只读诊断接口，返回：

- Session ID
- Agent ID
- 当前模型
- 权限模式
- Runtime 状态
- 是否休眠
- 最近活动时间

要求：

- Route 不访问 Engine 私有成员。
- Engine 提供公开方法。
- SessionCoordinator 返回明确类型。
- 添加测试。
- 不暴露 Secret 和本地敏感路径。

### 方案 B：学习模式 Slash Command

新增 `/study-status`：

- 显示当前 Agent。
- 显示当前 Session。
- 显示当前模型。
- 显示工作目录。
- 显示已启用 Skills 数量。
- 返回结构化卡片。

### 方案 C：前端会话信息面板

在聊天页面增加一个可折叠诊断面板，展示通过公开 API 获得的 Session 信息。

---

## 第 40 天：总结和复盘

### 最终总结结构

```text
1. 项目定位
2. 运行时架构
3. 目录边界
4. Engine 与 Manager
5. Agent 生命周期
6. Session 生命周期
7. 聊天主链路
8. 工具执行链
9. 文件和资源链
10. 安全体系
11. 记忆系统
12. 自动化系统
13. 多 Agent 通信
14. 插件系统
15. Bridge 系统
16. 前端状态管理
17. 构建和测试
18. 当前技术债务
19. 二次开发建议
20. 个人实践成果

```

---

# 四、必须掌握的八条重点链路

## 链路一：应用启动链路

```text
Electron Bootstrap
→ Electron Main
→ 创建窗口
→ 启动 Server 子进程
→ Server Bootstrap
→ 初始化 HanaEngine
→ 初始化 Managers
→ 初始化 Hub
→ 注册 Routes
→ 启动 HTTP 和 WebSocket
→ Renderer 加载
→ Store 连接 Server

```

### 必须回答

- 哪一步失败会导致白屏？
- 哪一步失败会导致 Server 不可用？
- Server 就绪信号如何传给 Electron？
- 退出应用时 Server 如何关闭？

---

## 链路二：聊天消息链路

```text
用户输入
→ React Component
→ Chat Store/Service
→ Server Chat Route
→ HanaEngine Public API
→ SessionCoordinator
→ Agent Runtime
→ Pi SDK
→ Model Provider
→ Streaming Events
→ WebSocket
→ Zustand Store
→ 消息组件

```

### 必须回答

- Agent 人格在哪里注入？
- 记忆在哪里注入？
- Tool Definition 在哪里注入？
- 用户中断如何传播？
- 流式事件如何去重？

---

## 链路三：工具执行链

```text
模型生成 Tool Call
→ Tool Registry
→ Execution Router
→ Capability Policy
→ PathGuard
→ Approval Gateway
→ Tool Executor
→ OS Sandbox
→ Tool Result
→ 模型继续推理
→ UI 工具卡片

```

### 必须回答

- 哪些工具无需确认？
- 哪些工具只能在工作区执行？
- Tool 超时如何终止？
- 用户拒绝后模型收到什么结果？

---

## 链路四：文件资源链

```text
Agent 创建文件
→ PathGuard
→ 文件写入
→ SessionFile 登记
→ Resource Service
→ Resource Ticket
→ Desktop/Mobile/Bridge
→ 预览、下载或上传

```

### 必须回答

- 为什么不能直接把绝对路径发给客户端？
- 文件如何跨不同客户端保持同一身份？
- 下载链接如何避免长期暴露？

---

## 链路五：记忆链

```text
会话内容
→ 记忆候选
→ Compile
→ Fact Store
→ Snapshot
→ Reflection
→ Memory Search
→ 新 Session Prompt 注入

```

### 必须回答

- 记忆与历史消息有什么区别？
- 记忆何时生成？
- 记忆如何防止无限增长？
- 哪个模型执行深度记忆任务？

---

## 链路六：自动化链

```text
Cron 配置
→ Scheduler
→ Event Bus
→ Agent Executor
→ 后台 Session
→ Agent Runtime
→ Tool/Model Result
→ Notification

```

### 必须回答

- Server 重启后任务如何恢复？
- 前台没有打开聊天时任务是否运行？
- 失败任务如何处理？

---

## 链路七：插件链

```text
发现插件
→ 读取 Manifest
→ 权限验证
→ 加载 Runtime
→ 注册 Tool/Command/Route/Page
→ Agent 或 Server 消费能力
→ 禁用和清理

```

### 必须回答

- restricted 与 full-access 差异是什么？
- 插件路由如何接入 Hono？
- 插件崩溃是否影响宿主？
- 插件 API 如何保持兼容？

---

## 链路八：Bridge 消息链

```text
外部消息
→ 平台 Adapter
→ 身份解析
→ Bridge Session
→ Agent Runtime
→ Agent 回复
→ 文本和媒体转换
→ 平台发送接口

```

### 必须回答

- 外部用户如何隔离？
- 群聊如何映射到内部 Channel？
- 本地文件如何安全发送到外部平台？
- 不同平台能力差异如何处理？

---

# 五、每次源码阅读的固定方法

## 第一步：先看文件轮廓

只看：

- import
- export
- interface
- class
- public 方法
- private 字段
- constructor
- initialize
- dispose

不要立刻陷入实现细节。

## 第二步：标记输入和输出

对每个重要函数记录：

```text
输入：
输出：
读取状态：
修改状态：
调用模块：
抛出错误：
发布事件：
需要清理的资源：

```

## 第三步：查找调用方

使用 IDE：

- Find References
- Go to Definition
- Call Hierarchy
- Type Hierarchy

必须同时回答：

- 谁调用它？
- 它调用谁？
- 它在哪个进程运行？
- 它是否跨越网络或 IPC 边界？

## 第四步：运行验证

至少使用一种方式：

- 日志
- 断点
- 测试
- 网络面板
- WebSocket 面板
- 文件系统观察
- SQLite 查询

## 第五步：形成图或表

每学习一个模块，至少输出一种：

- 时序图
- 状态图
- 依赖图
- 生命周期表
- API 表
- 数据结构表

---

# 六、源码笔记模板

## 模块笔记

```text
模块名称：

所在目录：

核心职责：

不负责什么：

主要入口：

核心类型：

主要依赖：

被谁调用：

保存哪些状态：

发布哪些事件：

监听哪些事件：

涉及哪些文件或数据库：

错误处理方式：

资源清理方式：

安全边界：

测试文件：

我仍不理解的问题：

```

## 函数笔记

```text
函数：

调用方：

输入：

返回值：

副作用：

持久化操作：

网络操作：

权限检查：

可能抛出的错误：

是否需要资源清理：

对应测试：

```

## 链路笔记

```text
链路名称：

触发入口：

步骤 1：
步骤 2：
步骤 3：

进程边界：

网络边界：

持久化边界：

安全检查点：

错误返回路径：

取消路径：

最终用户可见结果：

```

---

# 七、阶段验收标准

## 基础合格

- 能运行项目。
- 能说明主要目录职责。
- 能找到 Electron 和 Server 入口。
- 能说明 Agent 和 Session 的区别。
- 能找到聊天 Route。
- 能找到 Tool Registry。
- 能找到插件入口。

## 中级合格

- 能完整追踪聊天消息。
- 能完整追踪一个工具调用。
- 能解释 Session 生命周期。
- 能解释记忆生成和检索。
- 能解释 Cron 与前台聊天的关系。
- 能解释 SessionFile 的作用。
- 能编写一个简单插件。

## 深入掌握

- 能修改 Engine 公开 API 而不破坏层级边界。
- 能为新功能选择正确目录。
- 能增加一个 Route、Core 方法和前端调用。
- 能增加测试。
- 能分析资源泄漏和并发风险。
- 能指出核心类的拆分方案。
- 能解释插件、Bridge 和多客户端的安全风险。
- 能独立完成端到端功能开发。

---

# 八、学习过程中的常见误区

1. 不要从 `engine.ts` 第一行开始逐行读到最后一行。
2. 不要把所有 `Manager` 都理解为普通工具类。
3. 不要把 Server Route 当作业务逻辑层。
4. 不要绕过 Engine 公开 API 访问内部字段。
5. 不要只阅读前端而忽略独立 Server。
6. 不要只看正常流程，还要跟踪取消、失败和清理路径。
7. 不要忽略 WebSocket 事件和断线恢复。
8. 不要直接使用本地绝对路径理解文件传输。
9. 不要把 Session 压缩等同于长期记忆。
10. 不要把插件看成单纯的 Tool 扩展。
11. 不要只看函数调用，还要关注进程、网络和文件系统边界。
12. 不要在未运行验证的情况下，仅凭命名推断实现。

---

# 九、建议的最终实战课题

推荐以“学习助手插件”作为综合实践。

## 功能清单

1. 新增 `/study-start` 命令。
2. 在 Agent 书桌创建学习日志目录。
3. 记录当前 Session、Agent、模型和开始时间。
4. 提供 `save_study_note` Tool。
5. 将学习总结写入 Markdown 文件。
6. 将文件登记为 SessionFile。
7. 返回可预览卡片。
8. 提供插件设置项。
9. 可选增加每日学习提醒。
10. 添加测试和错误处理。

## 覆盖的知识点

- Plugin SDK
- Command
- Tool
- Config Schema
- Workspace
- PathGuard
- SessionFile
- Resource
- UI Card
- Agent Context
- 测试
- 生命周期清理

完成该课题，基本意味着已经贯通 HanaAgent 的核心扩展链路。

---

# 十、完成定义

满足以下条件，可认为本轮源码学习完成：

- 完成 8 周阅读任务的至少 80%。
- 八条重点链路全部能独立口述。
- 至少完成六张架构或时序图。
- 至少阅读一个 Bridge 和两个内置插件。
- 至少为五个核心模块建立职责表。
- 至少调试一次完整聊天和工具执行过程。
- 至少分析一次记忆生成过程。
- 至少运行一次后台自动化任务。
- 完成一个插件或端到端小功能。
- 最终总结能够明确指出项目的优势、边界和技术债务。
