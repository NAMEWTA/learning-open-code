# Pi Agent Harness 教学索引

## 教学主题

| 主题 | 路径 | 描述 |
|------|------|------|
| 项目总览 | `./00-overview/` | Pi 的 monorepo 架构、5 个核心包职责、技术栈与设计哲学 |

| pi-ai 模块总览 | `./module-ai/` | 多 Provider 统一 LLM API 层架构、exports 接口与内部分层 |

| Agent 运行时 | `./module-agent/` | pi-agent-core 架构总览：Agent 类 API、主循环、消息队列与事件系统 |

| pi-coding-agent 模块总览 | `./module-coding-agent/` | 交互式编程 CLI 内部分层、工具体系、扩展机制与 SDK 使用 |

| pi-tui 模块总览 | `./module-tui/` | 终端 UI 差异渲染库：组件系统、Markdown 解析、东亚字符宽度布局 |

| pi-orchestrator 模块总览 | `./module-orchestrator/` | 实验性多实例编排器：IPC 协议、子进程 RPC、Radius 云服务集成 |

| 构建脚本与基础设施 | `./module-scripts-infra/` | 质量门禁、锁文件生成、版本发布与 CI/CD 流水线的分层架构 |

| Agent 对话循环全链路 | `./slice-agent-loop/` | 从 prompt() 到 LLM 响应再到工具调用的完整闭环：双层循环控制流与事件时序 |

| 工具执行全链路 | `./slice-tool-execution/` | 从 ToolName 注册到 bash/read/edit/write 的完整 6 阶段调用链 |

| 会话持久化全链路 | `./slice-session-management/` | JSONL 存储/内存仓库/上下文压缩：从 Agent 对话到磁盘的完整数据流 |

| 多 Provider LLM 调度全链路 | `./slice-llm-provider-dispatch/` | 从 builtinModels 到 streamSimple 的完整数据流追踪 |

| TUI 差异渲染循环 | `./slice-tui-render-cycle/` | 从 requestRender 到终端像素：节流调度、组件树渲染、差异比对、ANSI 序列生成 |

| Agent Hook 生命周期 | `./slice-hook-system/` | 31种事件订阅、三层架构与6种emit执行策略全链路 |

| 扩展系统加载与执行全链路 | `./slice-extension-system/` | 从 package.json 声明到自定义工具/Hook 注入的六阶段全链路 |

| CLI 入口与模式选择全链路 | `./slice-cli-entry/` | 从 pi 命令到 Agent 会话启动的 9 阶段管线与三种模式分发 |
