# Gateway API 外壳资源

## 知识

- `open-ai-agent/deer-flow/backend/app/gateway/app.py`
  Gateway 主入口。适用于理解 FastAPI app factory、lifespan、middleware 顺序、router 注册和 `/health`。
- `open-ai-agent/deer-flow/backend/app/gateway/deps.py`
  request 级依赖集中入口。适用于理解 `app.state` 单例、`RunContext`、配置热加载边界和认证 helper。
- `open-ai-agent/deer-flow/backend/app/gateway/auth_middleware.py`
  全局认证安全网。适用于判断哪些路径公开、session cookie 如何变成 `request.state.user`。
- `open-ai-agent/deer-flow/backend/app/gateway/csrf_middleware.py`
  Double Submit Cookie 保护。适用于理解状态变更请求、auth endpoint 例外和 CORS origin 对齐。
- `open-ai-agent/deer-flow/backend/app/gateway/routers/`
  HTTP router 清单。适用于查找 models、threads、runs、skills、uploads、memory、auth、channels 等对外 API。
- `open-ai-agent/deer-flow/backend/app/gateway/auth/`
  本地用户、JWT、OIDC 和密码处理子系统。适用于理解登录、注册、token version 和用户仓储。
- `open-ai-agent/deer-flow/backend/app/gateway/langgraph_auth.py`
  LangGraph Server/Studio 兼容认证接线。适用于理解非默认运行路径如何复用 Gateway JWT/CSRF 规则。
- `open-ai-agent/deer-flow/backend/README.md`
  后端架构说明。适用于确认 nginx、Gateway、lead agent、sandbox、memory 和 API 族的官方项目描述。
- `open-ai-agent/deer-flow/docker/nginx/nginx.conf`
  统一入口路由。适用于确认 `/api/langgraph/*` 如何改写到 Gateway 原生 `/api/*`。
- `open-ai-agent/deer-flow/docker/docker-compose.yaml`
  生产服务拓扑。适用于确认 `gateway` 容器以 `uvicorn app.gateway.app:app` 运行 embedded runtime。

## 智慧（社区）

- [bytedance/deer-flow GitHub Issues](https://github.com/bytedance/deer-flow/issues)
  适用于检索 Gateway、认证、SSE、配置和部署问题的真实 bug 讨论。

## 空白

- 本次任务未进行外部社区深度调研；如果后续要讲生产运维经验，需要补充真实部署案例、反向代理安全配置和多 worker SSE 事故复盘。
