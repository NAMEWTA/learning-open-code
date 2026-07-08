# deer-flow 项目总览资源

## 知识

- [README.md](../../../../open-ai-agent/deer-flow/README.md)
  英文项目定位、快速开始、核心能力和安全边界。适用于确认 deer-flow 的产品叙事与主干功能。
- [README_zh.md](../../../../open-ai-agent/deer-flow/README_zh.md)
  中文项目说明。适用于统一术语，例如 super agent harness、sub-agents、memory、sandbox、skills。
- [backend/README.md](../../../../open-ai-agent/deer-flow/backend/README.md)
  后端架构图、核心组件、Gateway API、sandbox、subagent 和项目结构说明。适用于 L0/L1 架构锚定。
- [config.example.yaml](../../../../open-ai-agent/deer-flow/config.example.yaml)
  运行配置全量模板。适用于识别模型、工具、sandbox、skills、memory、database、scheduler、stream bridge 等配置入口。
- [backend/pyproject.toml](../../../../open-ai-agent/deer-flow/backend/pyproject.toml)
  Python 后端依赖与 workspace 定义。适用于确认 FastAPI、LangGraph SDK、deerflow-harness、IM channel、sandbox extras 等技术栈。
- [backend/langgraph.json](../../../../open-ai-agent/deer-flow/backend/langgraph.json)
  LangGraph tooling/Studio 入口，指向 `deerflow.agents:make_lead_agent`。适用于定位 lead agent 注册点。
- [frontend/package.json](../../../../open-ai-agent/deer-flow/frontend/package.json)
  前端依赖和脚本。适用于确认 Next.js、React、LangGraph SDK、React Query、Playwright、Rstest 等技术栈。
- [docker/docker-compose.yaml](../../../../open-ai-agent/deer-flow/docker/docker-compose.yaml)
  生产部署拓扑。适用于确认 nginx、frontend、gateway、Redis 和可选 provisioner 的服务关系。
- [Makefile](../../../../open-ai-agent/deer-flow/Makefile)
  顶层开发命令。适用于理解 setup、doctor、dev、Docker dev、production up/down 的入口。
- [backend/packages/harness/deerflow/agents/lead_agent/agent.py](../../../../open-ai-agent/deer-flow/backend/packages/harness/deerflow/agents/lead_agent/agent.py)
  lead agent 工厂和中间件组装源码。适用于后续 L1/L2 分析 agent 执行链路。
- [backend/app/gateway/app.py](../../../../open-ai-agent/deer-flow/backend/app/gateway/app.py)
  FastAPI Gateway 生命周期、中间件和 router 注册。适用于后续 L1 Gateway 模块分析。
- [frontend/src/app/workspace/chats/[thread_id]/page.tsx](../../../../open-ai-agent/deer-flow/frontend/src/app/workspace/chats/%5Bthread_id%5D/page.tsx)
  前端聊天页面入口。适用于后续 L2 “一次对话如何流转”切片。

## 智慧（社区）

- [bytedance/deer-flow GitHub Issues](https://github.com/bytedance/deer-flow/issues)
  真实用户问题、配置故障和维护者回复。适用于验证教学中的部署、配置、sandbox 和运行时判断。
- [bytedance/deer-flow Pull Requests](https://github.com/bytedance/deer-flow/pulls)
  设计变更和回归修复记录。适用于后续 L4 深度剖析时追溯“为什么这样改”。

## 空白

- 本次未做外部竞品或第三方博客横向搜索；L0 只使用仓库内 README、配置与源码建立基线。
- 还缺少维护者视角的正式架构决策记录；后续 L4 需要结合 `docs/plans/`、`docs/superpowers/` 与 PR 讨论补证据。
