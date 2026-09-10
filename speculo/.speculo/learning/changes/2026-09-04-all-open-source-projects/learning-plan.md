# 学习计划：Sub2API Plus 全链路学习

## 教学表达基线

`5 岁的小孩`

使用简体中文、通俗短句、先 ASCII 图后文字，术语先解释后命名。每次课程控制在 20–30 分钟，并把长链路拆成可恢复的短课。

## 目标合同

| ID | 目标 | 关键 | 深度 | 已有基础 | 完成证据 |
| --- | --- | --- | --- | --- | --- |
| OBJ-01 | 能从仓库结构、构建配置和启动入口画出 Sub2API Plus 的运行地图，解释 setup 模式、正常启动、嵌入式前端、依赖注入和优雅退出 | 是 | standard | 知道 `backend/cmd` 和 `frontend/index.html` 是入口线索，但不清楚生命周期 | 主动回忆 + ASCII 架构图 + 定位 `backend/cmd/server/main.go`、`internal/server/router.go`、前端 `src/main.ts` |
| OBJ-02 | 能追踪一条合法的 OpenAI-compatible Chat Completions 请求，从 HTTP 路由、API Key 认证、分组/模型解析到账号调度、上游转发、流式或非流式响应和错误返回 | 是 | deep | 不知道请求经过哪些模块或如何返回 | 源码逐段导航 + 因果解释 + 对新模型/新错误场景预测调用链 |
| OBJ-03 | 能解释用户、分组、API Key、账号、渠道、订阅、用量和订单等核心实体的关系，以及 Ent、PostgreSQL/SQLite 和 Redis 在其中的职责边界 | 是 | deep | 未知模块和数据模型 | 数据关系 ASCII 图 + 定位 schema/repository/service 查询 + 解释一次配额/用量读写 |
| OBJ-04 | 能比较 OpenAI Chat/Responses、Anthropic Messages、Gemini 及其他 Provider 适配路径，说明协议归一化、模型映射、账号能力和故障转移如何协同 | 是 | deep | 只知道多个大模型厂商被统一接入 | 解释至少两条协议差异 + 追踪一个 model mapping/failover 分支 + 新 Provider 接入位置判断 |
| OBJ-05 | 能解释认证、API Key、配额、订阅、计费、用量记录、审计、并发限制、幂等和后台 worker 如何共同形成控制平面 | 是 | deep | 对控制平面模块没有结构认知 | 按一次请求列出控制点 + 引用对应 service/handler/test + 识别失败时的最小补救范围 |
| OBJ-06 | 能从 Vue 路由、Pinia store、API client 到后端管理路由解释前端控制台；能说明 setup、Docker、反向代理、健康检查和安全配置的运行边界 | 否 | standard | 只指出 `frontend/index.html`，未了解 Vue 应用入口 | 前后端对应表 + 部署拓扑 ASCII 图 + 按配置推断一次启动/健康检查行为 |
| OBJ-07 | 面对一个新增 Provider、端点或业务规则，能提出不改动现有代码的扩展位置、数据/安全影响、测试策略和验证步骤，并区分合法兼容机制与规避供应商检测的请求 | 是 | deep | 尚未形成扩展判断方法 | 新情境设计题 + 迁移解释 + 安全边界辨析；至少一道全新情境通过 |

## 前置知识与缺口

- 已确认：能描述 API 网关的基本产品目标，知道项目含 Go 后端和前端入口。
- 未确认：Go、Gin、依赖注入、Vue/TypeScript、HTTP/SSE/WebSocket、SQL/Ent、Redis、OAuth、计费系统和测试方法的熟练度；课程按需补充，不把“未确认”当作“不会”。
- 首轮重点缺口：模块地图、启动生命周期、路由注册、请求调用链和数据模型。

## 来源范围

以当前 checkout 的 `open-ai-agent/sub2api-plus` 为事实基准，优先读取：

1. `README.md`、`README_CN.md`、`backend/go.mod`、`backend/Makefile` 和 `Dockerfile`；
2. `backend/cmd/server/main.go`、`wire.go`、`internal/server/router.go`；
3. `internal/handler`、`internal/service`、`internal/repository`、`internal/domain`、`internal/model`、`ent`、`frontend/src`、`deploy`；
4. 对应单元/集成/E2E 测试和 `docs/` 中的协议、安全、支付、发布说明；
5. `.gitmodules` 登记的官方仓库 URL 与项目官方文档，仅在使用具体结论时核验。

当前源码快照：submodule `HEAD=8df457f85568ab3b1c80de07ae59b2ef53183e80`。后续课程记录项目相对路径和符号，不复制无关源码。

## 课程与练习顺序

1. 项目总览：产品边界、仓库结构、技术栈和合法使用边界。
2. 启动与运行地图：`main`、setup、Wire、Gin、嵌入式前端和退出清理。
3. 路由与认证：全局中间件、JWT/API Key、管理端与网关路由分层。
4. 一条请求链路：OpenAI-compatible Chat Completions 的成功、流式和错误路径。
5. 数据与持久化：Ent schema、repository/service 边界、PostgreSQL/SQLite、Redis 缓存。
6. Provider 与调度：协议归一化、模型映射、账号选择、会话粘性和故障转移。
7. 配额与运营控制：计费、用量、订阅、审计、幂等、并发和后台 worker。
8. 前端控制平面：Vue Router、Pinia、API client、管理页面与后端契约。
9. 部署与安全：Docker、多阶段构建、反向代理、健康检查、配置和威胁边界。
10. 测试与扩展：从测试证据反推设计，完成新增 Provider/端点的新情境迁移题。

以上是第一轮骨架；每个大主题会继续拆成模块级、垂直切片级和核心函数级短课，直到达到用户要求的全面到细节覆盖。正式教学从 OBJ-01 开始，先不跳到设备指纹或规避检测细节。

## 测验合同

- 即时和保持测验均需总分至少 80%。
- 所有关键目标和至少一道新情境迁移题必须通过。
- 阻塞性误解或 `needs_review` 会阻止归档。
- 任何关于供应商策略、设备识别或合规的结论必须以源码/官方文档为证；不把“让上游发现不了”当作已验证事实，也不提供规避指导。

## Revision 记录

| 时间 | 变化 | 原因 | 是否需要重新测验 |
| --- | --- | --- | --- |
| 2026-09-04 | 学习范围从整个仓库 62 个 submodule 收窄为 `open-ai-agent/sub2api-plus` | 学习者明确先集中学习单个项目 | 否，尚未开始教学或测验 |
| 2026-09-04 | 根据未教学基线锁定 7 个目标，首轮从项目地图和请求链路开始 | 学习者知道产品定位和入口线索，但不知道模块和返回链路 | 否，目标在首次测验前锁定 |
