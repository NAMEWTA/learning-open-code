# 课程快照：slice-sandbox-exec-flow

## 源项目信息
- **源仓库**：`open-ai-desktop/openhanako`
  - **Git Commit**：`acb1b2b860d0d877a9ba57b9022347643e892b1c`
  - **短 Commit**：`acb1b2b`
  - **分支**：`main`
- **快照时间**：2026-07-07T15:30:00+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `agents/&lt;name&gt;/config.yaml` | 课程分析引用 | 🟡 辅助 |
| `agents/*/config.yaml` | 课程分析引用 | 🟡 辅助 |
| `core/agent.ts` | 课程分析引用 | 🟡 辅助 |
| `core/session-permission-mode.ts` | 课程分析引用 | 🟡 辅助 |
| `hanakoHome/auth.json` | 课程分析引用 | 🟡 辅助 |
| `lib/exec-command/guidance.ts` | 课程分析引用 | 🟡 辅助 |
| `lib/exec-command/policy.ts` | 课程分析引用 | 🟡 辅助 |
| `lib/exec-command/runner.ts` | 课程分析引用 | 🟡 辅助 |
| `lib/exec-command/schema.ts` | 课程分析引用 | 🟡 辅助 |
| `lib/exec-command/shell.ts` | 课程分析引用 | 🟡 辅助 |
| `lib/exec-command/tool.ts` | 课程分析引用 | 🟡 辅助 |
| `lib/permission/approval-review-context.ts` | 课程分析引用 | 🟡 辅助 |
| `lib/permission/safety-policy.ts` | 课程分析引用 | 🟡 辅助 |
| `lib/sandbox/bwrap.ts` | 课程分析引用 | 🟡 辅助 |
| `lib/sandbox/exec-helper.ts` | 课程分析引用 | 🟡 辅助 |
| `lib/sandbox/index.ts` | 课程分析引用 | 🟡 辅助 |
| `lib/sandbox/managed-config-guard.ts` | 课程分析引用 | 🟡 辅助 |
| `lib/sandbox/path-guard.ts` | 课程分析引用 | 🟡 辅助 |
| `lib/sandbox/policy.ts` | 课程分析引用 | 🟡 辅助 |
| `lib/sandbox/seatbelt.ts` | 课程分析引用 | 🟡 辅助 |
| `lib/sandbox/tool-wrapper.ts` | 课程分析引用 | 🟡 辅助 |
| `lib/sandbox/win32-exec.ts` | 课程分析引用 | 🟡 辅助 |
| `lib/shell/command-runner.ts` | Shell 命令执行器（profile 解析 + spawn 调用）| 🔴 核心 |
| `lib/shell/shell-profile.ts` | Shell Profile 解析（平台适配 + 参数构造）| 🟡 辅助 |
| `lib/shell/execution-cwd.ts` | 课程分析引用 | 🟡 辅助 |
| `lib/shell/shell-utils.ts` | 课程分析引用 | 🟡 辅助 |
| `lib/terminal/node-pty-backend.ts` | 课程分析引用 | 🟡 辅助 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| 0001 | `lessons/0001.html` | 沙盒架构总览：安全模型+分层设计+入口点 |
| 0002 | `lessons/0002.html` | 路径守卫与命令分类：PathGuard 11级级联+preflight检查 |
| 0003 | `lessons/0003.html` | Bubblewrap容器执行：bwrap参数构造+spawn+流式输出 |
| 0004 | `lessons/0004.html` | 权限审批与沙盒逃逸防护 |
| 0005 | `lessons/0005.html` | 全链路时序与综合测验：完整mermaid时序图+7条异常路径回顾 |

## 快照摘要
- 课程数：5
- 引用源文件数：26
- 学习记录数：0
- 参考资料数：0
- 资产文件数：0
