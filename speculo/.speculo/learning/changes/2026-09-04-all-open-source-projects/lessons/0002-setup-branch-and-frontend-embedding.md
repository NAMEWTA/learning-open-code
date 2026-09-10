# Lesson 02：搞清楚 setup 分支和前端嵌入

## 本课目标

`OBJ-01`

本课专门回答两个问题：为什么 `NeedsSetup() == true` 走 setup，`false` 走正式服务？`frontend` 到底是在什么时候进入二进制的？

## 教学表达基线

`5 岁的小孩`

把程序想成一家商店：第一次开门要先填营业登记表；登记完成后，之后每次开门都直接进入营业状态。前端是店里的屏幕，不是另一个正在后台运行的 Node 店员。

## 先看全图：启动判断

```text
process starts
     |
     v
NeedsSetup()
     |
     +-- SKIP_SETUP=true/1/yes? -- yes --> false
     |
     +-- config.yaml exists? ----- yes --> false
     |
     +-- .installed exists? ------- yes --> false
     |
     +-- all three checks pass ---- yes --> true
                                      |
                         +------------+------------+
                         |                         |
                         v                         v
                 runSetupServer()             runMainServer()
                 first-run setup UI            real application
```

这里的 `yes` 指的是“`NeedsSetup()` 返回 true”，不是“用户发来的 HTTP 请求成功”。它只在 Go 进程启动时判断一次，用来选择启动模式。

## 一步一步看：为什么 true 是 setup

`internal/setup/setup.go` 的 `NeedsSetup()` 有三层保护：

1. 如果显式设置 `SKIP_SETUP=true`、`1` 或 `yes`，直接返回 `false`。这是部署者明确表示“不要进入向导”。
2. 如果数据目录里已经有 `config.yaml`，返回 `false`。配置存在，说明系统至少完成过配置写入。
3. 如果没有配置文件，但有 `.installed` 锁文件，也返回 `false`。锁文件防止只删除配置文件就强迫系统重新进入安装流程。
4. 只有“没有跳过开关、没有配置文件、没有安装锁”同时成立，才返回 `true`。

因此，`true` 的意思是“本次进程没有找到已完成安装的证据”，需要先运行 setup；`false` 的意思是“可以尝试加载正式配置并组装完整应用”。这不是权限放行，也不是 Provider 选择。

还有一个容易漏掉的分支：当 `NeedsSetup()` 为 `true` 且 `AUTO_SETUP=true` 时，`main.go` 会调用 `AutoSetupFromEnv()`，从环境变量生成配置、测试数据库和 Redis、初始化数据库，然后继续进入 `runMainServer()`。所以 Docker 自动安装是：

```text
NeedsSetup == true
  -> AUTO_SETUP == true
  -> AutoSetupFromEnv()
  -> runMainServer()
```

没有 `AUTO_SETUP` 时才会启动 `runSetupServer()`，让浏览器打开向导。setup handler 还会再次检查 `NeedsSetup()`；安装完成后，setup 接口会拒绝继续修改安装状态。

## 先看全图：前端什么时候进入二进制

```text
build time                                      run time
-----------                                     ---------
frontend source                                 one Go process
frontend/index.html                             /app/sub2api
frontend/src/*.ts, *.vue                             |
        |                                            v
        v                                     embed_on.go reads bytes
pnpm run build                                      |
        |                                            v
        v                                     Gin web middleware
frontend/dist  ------------------------------>  HTTP response
        |                                      index.html / assets
        v                                            |
backend/internal/web/dist                         +-- API paths bypass
        |                                            |
        v                                            v
go build -tags embed ./cmd/server             internal handlers
```

关键点是：`pnpm` 和 Vite 只负责**构建**。Dockerfile 先在 `frontend-builder` 阶段执行 `pnpm run build`，再把生成的 `frontend/dist` 复制到 `backend/internal/web/dist`，最后用 `go build -tags embed` 编译 Go 后端。

`backend/internal/web/embed_on.go` 只有在 `embed` 构建标签打开时才参加编译：

```go
//go:build embed

//go:embed all:dist
var frontendFS embed.FS
```

`embed.FS` 是编译器放进可执行文件的数据，不是运行时启动的文件服务器进程。生产容器中的 `/app/sub2api` 可以直接读取这些内置字节，因此不需要在容器里再启动 Node 或 Vite。

如果没有 `-tags embed`，编译器改用 `embed_off.go`：`HasEmbeddedFrontend()` 返回 `false`，访问页面会得到“Frontend not embedded”的 404。这是开发构建和生产构建行为可能不同的原因。

## `router.go` 到底做了什么

`internal/server/router.go` 不是把前端“启动成二进制”，而是把一个 HTTP 中间件挂进 Gin：

1. `web.HasEmbeddedFrontend()` 确认 `dist/index.html` 是否在嵌入文件系统里；
2. `web.NewFrontendServer(settingService)` 读取内置 `index.html`，准备 `http.FileServer`；
3. `r.Use(frontendServer.Middleware())` 让非 API 路径由它处理；
4. `/api/`、`/v1/`、`/health`、`/ready` 等路径会 bypass，继续交给后端路由；
5. 页面请求返回 HTML 或带哈希的静态资源；SPA 未找到的页面路径回退到 `index.html`。

首次返回 `index.html` 时，后端还可以把公开设置写入 `window.__APP_CONFIG__`，并处理 CSP nonce、ETag 和缓存。浏览器拿到 HTML 后，才执行其中引用的 JavaScript，随后由 `frontend/src/main.ts` 挂载 Vue 应用。

## 用已经会的知识搭桥

你可以把它类比成“把菜单印在店门里”：

- `frontend/index.html` 是菜单原稿；
- `pnpm run build` 把原稿和脚本打包成 `dist`；
- `go:embed` 把打包结果印进 Go 程序；
- Gin middleware 在收到浏览器请求时，把印好的内容作为 HTTP 响应交出去。

但类比有边界：二进制里保存的是静态前端文件，不是一个会自己运行的浏览器；真正执行 Vue JavaScript 的仍然是用户浏览器。

## 示范一个

假设 Docker 数据卷是空的、没有设置 `AUTO_SETUP`：

```text
main
  -> NeedsSetup() == true
  -> AutoSetupEnabled() == false
  -> runSetupServer()
  -> browser opens setup page
  -> setup writes config.yaml and .installed
```

下一次重启时，判断条件已经变化：配置文件和锁文件存在，所以 `NeedsSetup() == false`，程序转入 `runMainServer()`。这就是两个分支不是“二选一业务路由”，而是两个连续启动阶段。

## 一起完成一个

补全下面的构建与运行链：

```text
pnpm run build
  -> frontend/dist
  -> COPY to backend/internal/web/dist
  -> go build ________ ./cmd/server
  -> embed_on.go provides frontendFS
  -> router.go installs ________
```

提示：第一个空格是构建标签；第二个空格是负责按 URL 返回页面/静态资源的 Gin 组件。

## 轮到你独立完成

请回答两个小问题，不查答案：

1. `config.yaml` 不存在、`.installed` 存在、`AUTO_SETUP=true` 时，`main.go` 会不会进入 `runSetupServer()`？请按 `NeedsSetup()` 的检查顺序解释。
2. 浏览器请求 `/api/v1/settings/public` 时，为什么不会被嵌入式前端 middleware 当成 SPA 页面返回？请指出 bypass 判断和后端路由之间的关系。

下一步 `P-practice` 会检查你的解释，并让你用源码路径证明每个判断。
