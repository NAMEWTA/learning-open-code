# pi-subagents 教学索引

## 教学主题

| 主题 | 路径 | 描述 |
|------|------|------|
| 项目总览 | `./00-overview/` | pi-subagents 的定位、架构、目录与学习路线 |
| 扩展入口与注册 | `./module-extension-runtime/` | Pi extension 入口、tool、slash、RPC 与状态注册 |
| Agent 发现与配置 | `./module-agent-system/` | 内置角色、frontmatter、scope 与管理动作 |
| 运行核心 | `./module-runs-execution/` | 前台、后台、chain、parallel 与 async 执行层 |
| 共享基础设施 | `./module-shared-infra/` | 类型、状态文件、路径、JSONL 与 session 工具 |
| Slash 命令与工作流 | `./module-slash-workflows/` | slash 工具、prompt 模板与执行入口衔接 |
| 父子进程通信 | `./module-intercom/` | intercom bridge、native supervisor 与结果通道 |
| TUI 渲染 | `./module-tui-rendering/` | foreground、async 与 chain 结果的终端展示 |
| 模型 Profile | `./module-profiles/` | profile 解析、模型能力探测与 fallback 选择 |

| 包装与资产交付 | `./module-packaging-assets/` | npm 安装、skills/prompts 打包与 CI 发布闸门 |

| 测试体系 | `./module-test-suite/` | unit/integration/e2e 三层边界与行为佐证索引 |

| 单次前台 run | `./slice-single-foreground-run/` | `{agent,task}` 从 tool 到 SingleResult 的八跳垂直切片 |

| parallel 与 chain 全链路 | `./slice-parallel-chain-execution/` | chain 编排、并行 step、dynamic fanout 与 workflow graph |

| async lifecycle 与 wait | `./slice-async-lifecycle-status-wait/` | 后台 run 从启动到 status/wait/完成通知的全链路 |

| Agent 管理配置全链路 | `./slice-agent-management-config/` | 从 subagent 管理动作到 frontmatter、settings 覆盖与 scope 合并 |

| Slash 到 executor 桥接 | `./slice-slash-to-executor/` | `/run` 等命令经事件桥到 executor 分流的八跳垂直切片 |

| Native supervisor 与 intercom 全链路 | `./slice-native-supervisor-intercom/` | bridge 注入、supervisor 文件通道与 result delivery 的前台协调切片 |

| 模型范围、预算与安全边界 | `./slice-model-scope-budget-guardrails/` | modelScope、tool/turn budget 与 fork/prompt 安全九跳全链路 |
