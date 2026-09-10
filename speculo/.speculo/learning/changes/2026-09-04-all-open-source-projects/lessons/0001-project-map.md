# Lesson 01：先看懂 Sub2API Plus 的启动地图

## 本课目标

`OBJ-01`

读完后，你应该能回答：程序从哪里启动？第一次运行和正常运行有什么不同？前端怎样被装进后端？服务器怎样开始工作，又怎样停干净？

## 教学表达基线

`5 岁的小孩`

我们把系统想成一间“智能柜台”：前端是窗口，后端是柜台工作人员，数据库和 Redis 是记录本，Provider 是外部服务。先看路线，再记名称。

## 先看全图

```text
+----------------------+       +--------------------------+
| browser                |       | command line             |
| frontend/index.html   |       | backend/cmd/server/main  |
+-----------+----------+       +------------+-------------+
            |                                |
            v                                v
     frontend/src/main.ts             parse flags and version
            |                                |
            v                                v
     Vue + Pinia + Router          NeedsSetup() ?
            |                         /       \
            |                        yes       no
            |                        /           \
            |                       v             v
            |                runSetupServer()  runMainServer()
            |                       |             |
            |                       v             v
            |                 setup routes   LoadForBootstrap()
            |                                     |
            |                                     v
            |                             initializeApplication()
            |                              (Wire dependencies)
            |                                     |
            +--------------------------> internal/server/router.go
                                                   |
                              middleware + web + API routes
                                                   |
                                                   v
                                      http.Server.ListenAndServe()
                                                   |
                                      SIGINT/SIGTERM arrives
                                                   v
                                      Shutdown() + app.Cleanup()
```

这张图只回答一个问题：**谁把系统从“文件”变成“正在监听端口的服务”？** 前端不是另一个独立后端；构建时，前端产物可以被嵌入 Go 二进制，运行时由服务器返回页面和 API。

## 一步一步看

1. `backend/cmd/server/main.go` 先初始化最基础的日志，再解析 `--setup` 和 `--version`。`--version` 只打印版本并退出；`--setup` 直接进入 CLI 配置向导。
2. 普通启动先调用 `setup.NeedsSetup()`。没有配置时进入 `runSetupServer()`，只挂载 setup 路由和必要的安全中间件，帮助第一次运行完成配置。
3. 已配置时进入 `runMainServer()`：加载配置、初始化正式日志，调用 `initializeApplication()`。这个函数由 `wire_gen.go` 把 config、repository、service、handler、middleware 和 server 串起来。
4. 应用启动若干后台服务，然后在 `internal/server/router.go` 统一安装请求日志、会话绑定、CORS、IP 访问控制、安全响应头、服务器计时和嵌入式前端，最后注册 common、auth、user、admin、gateway、payment 等路由。
5. `app.Server.ListenAndServe()` 开始监听。收到 `SIGINT` 或 `SIGTERM` 后，先给 HTTP 请求一个有限的退出时间，再调用 `app.Cleanup()` 停止 worker、调度器、审计服务以及 Redis/Ent 等资源。

前端真正的 JavaScript 入口是 `frontend/src/main.ts`，不是只有页面壳的 `frontend/index.html`。它创建 Vue 应用和 Pinia，读取注入配置，初始化国际化与 Router，等待首轮导航完成后才挂载到 `#app`；`App.vue` 还会检查是否需要 setup，并加载公开设置。

## 用已经会的知识搭桥

你已经知道“API 网关把调用方和上游模型连接起来”。现在把它补成两层：

- **控制面**：setup、登录、管理页面、分组、配额、计费和审计，决定谁能做什么；
- **数据面**：gateway 路由接收一次模型请求，经过认证和策略后才向 Provider 转发。

启动地图先讲控制面怎样出现，下一课才沿着数据面追踪一条请求。

## 术语小词典

- **setup wizard**：第一次运行时的配置向导。
- **Wire**：根据 Provider 函数组装依赖的代码生成工具；`wire_gen.go` 是生成结果。
- **middleware**：请求到达业务处理器前后经过的一层公共检查。
- **graceful shutdown**：收到退出信号后，给正在处理的请求一点时间，再依次关闭资源。

## 类比在哪里失效

柜台类比能帮助你理解“入口、流程、资源”，但它不是安全模型。真实系统还有并发、缓存、流式响应、数据库事务和失败重试；前端页面也不能证明后端已经完成认证。任何关于 Provider 账户、设备识别或合规的判断，都必须回到源码和官方条款，不能从类比推出结论。

## 示范一个

我们只示范“普通启动”的最短路径：

```text
main
  -> NeedsSetup() == false
  -> runMainServer()
  -> LoadForBootstrap()
  -> initializeApplication(buildInfo)
  -> app.Server.ListenAndServe()
```

查源码时按箭头逐个确认：先看 `main.go` 的分支，再看 `runMainServer()`，最后从 `router.go` 找到路由注册。这样你不会把“文件入口”误认为“业务入口”。

## 一起完成一个

打开 `frontend/src/main.ts` 和 `frontend/src/App.vue`，补全这条前端启动链：

```text
createApp(App)
  -> ________
  -> initI18n()
  -> ________
  -> router.isReady()
  -> app.mount('#app')
```

提示：一个空格对应状态管理插件，另一个空格对应路由插件；再从 `App.vue` 找出 setup 检查发生在哪个生命周期钩子里。

## 轮到你独立完成

请画一张不超过 12 个方框的 ASCII 图，描述“Docker 第一次启动”与“已经完成配置后的再次启动”各自经过哪些节点。至少标出：`NeedsSetup`、`runSetupServer`、`runMainServer`、`initializeApplication`、`ListenAndServe`，并写出两条路径的不同点。不要查答案；下一步 `P-practice` 会检查你的图和解释。
