# deer-flow 教学索引

## 教学主题

| 主题 | 路径 | 描述 |
|------|------|------|
| 项目总览 | `./00-overview/` | deer-flow 的定位、架构、技术栈与学习地图 |
| Gateway API 外壳 | `./module-gateway/` | FastAPI 入口、认证、中间件与路由总览 |
| Agent lead runtime | `./module-lead-agent/` | lead agent、middleware 与 ThreadState 总览 |
| Runtime 与 persistence | `./module-runtime-persistence/` | run 生命周期、stream、checkpointer 与数据库 |
| Frontend workspace | `./module-frontend-workspace/` | 工作区页面、聊天 UI、artifact 与 sidecar |
| Tools 与 MCP | `./module-tools-mcp/` | 工具加载、内置工具、MCP 与 tool_search |
| Sandbox 与文件系统 | `./module-sandbox/` | sandbox provider、虚拟路径与文件工具安全边界 |
| Subagent 系统 | `./module-subagents/` | task tool、executor、状态契约与并发限制 |
| Skills 系统 | `./module-skills/` | skill 解析、安装、激活与 allowed-tools 策略 |

| Memory 与 summarization | `./module-memory-context/` | 长期 memory、上下文压缩与 durable context 三条链路 |

| IM channels 与 GitHub webhook | `./module-channels/` | 外部 IM 与 GitHub webhook 经 MessageBus 接入 Gateway |

| Frontend core 数据层 | `./module-frontend-core/` | core API client、认证、线程流与 skills/MCP/uploads |

| 配置与部署 | `./module-config-deploy/` | config、Makefile、scripts 与 Docker 整栈编排 |

| 聊天流式执行 | `./slice-chat-streaming-run/` | 从输入框到 lead agent 的一次 SSE run 全链路 |

| 定时任务创建与执行 | `./slice-scheduled-task-run/` | 前端创建到调度器触发 run 的 L2 垂直切片 |

| 自定义 agent 管理 | `./slice-custom-agent-management/` | workspace 向导、Gateway CRUD 与 setup/update 工具全链路 |

| goal 自动续跑 | `./slice-goal-continuation/` | worker 检测 goal 状态、evaluator 判定与隐藏续跑触发 |

| skill slash 激活与递进加载 | `./slice-skill-activation/` | `/skill` 显式注入 SKILL.md 与 read_file 递进加载全链路 |

| Subagent 委派 | `./slice-subagent-delegation/` | task 工具→executor→SSE→Subtask 卡片全链路 |

| 上传与 artifact 预览 | `./slice-upload-sandbox-artifact/` | 聊天附件经 Gateway 落盘、进 sandbox、经 artifacts API 回到 UI |

| memory 注入与异步更新 | `./slice-memory-update-injection/` | MemoryMiddleware 入队、queue 防抖、updater 写盘与 DynamicContext 注入 |

| 配置热加载边界 | `./slice-config-hot-reload/` | config.yaml 哪些段可热加载、哪些需重启 Gateway |

| IM 入站消息执行 | `./slice-im-channel-run/` | 平台 adapter 经 MessageBus 触发 Gateway run 的全链路 |

| goal 续跑设计权衡 | `./deep-dive-goal-continuation/` | worker 内隐式续跑环、evaluator 与竞态守卫的 L4 深度剖析 |

| MCP 延迟工具发现 | `./deep-dive-deferred-tool-search/` | tool_search 设计权衡、fail-closed 与 catalog hash promotion |

| Memory 双入队机制 | `./deep-dive-memory-dual-queue/` | after_agent debounce 与 summarization 前 add_nowait 的设计边界 |

| 配置热加载边界深潜 | `./deep-dive-config-reload-boundary/` | 注册表设计、签名检测与启动单例误报排障 |
