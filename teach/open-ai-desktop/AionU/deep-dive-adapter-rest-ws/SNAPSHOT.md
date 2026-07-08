# 课程快照：deep-dive-adapter-rest-ws

## 源项目信息
- **源仓库**：`open-ai-desktop/AionU`
  - **Git Commit**：`0ea13fd0136294ab7ff30215b580b0fc028c6f56`
  - **短 Commit**：`0ea13fd`
  - **分支**：`main`
- **快照时间**：2026-07-07T20:21:11+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `packages/desktop/src/common/adapter/main.ts` | 传统 bridge adapter 与 Electron main 事件广播证据 | 🟡 辅助 |
| `packages/desktop/src/common/adapter/browser.ts` | WebUI browser runtime bridge 与 `/ws` fallback 证据 | 🟡 辅助 |
| `packages/desktop/src/common/api/index.ts` | common API 与 renderer adapter 命名边界对照 | 🟡 辅助 |
| `packages/desktop/src/common/index.ts` | renderer common 调用面暴露证据 | 🟡 辅助 |
| `tests/e2e/helpers/bridge/mappers.ts` | E2E bridge mapper 证据 | 🟡 辅助 |
| `tests/e2e/helpers/bridge/routes.ts` | E2E dotted key 到 HTTP route 映射证据 | 🟡 辅助 |
| `tests/e2e/helpers/httpBridge.ts` | E2E HTTP helper 端口与响应解包证据 | 🟡 辅助 |
| `packages/desktop/src/common/adapter/httpBridge.ts` | provider-like invoke、HTTP 错误与 WS emitter 主证据 | 🔴 核心 |
| `packages/desktop/src/common/adapter/ipcBridge.ts` | renderer 稳定调用面与真实传输选择主证据 | 🔴 核心 |
| `packages/desktop/src/preload/main.ts` | backend port 暴露给 renderer 的证据 | 🟡 辅助 |
| `tests/e2e/helpers/bridge/invoke.ts` | 课程分析引用 | 🟡 辅助 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| 0001-problem-frame | `lessons/0001-problem-frame.html` | REST/WS adapter：问题框架 |
| 0002-provider-like-invoke | `lessons/0002-provider-like-invoke.html` | REST/WS adapter：provider-like invoke |
| 0003-error-events-e2e | `lessons/0003-error-events-e2e.html` | REST/WS adapter：错误、事件与 E2E |

## 参考资料

- `reference/adapter-rest-ws-notes.html` — REST/WS adapter 设计速查

## 快照摘要
- 课程数：3
- 引用源文件数：11
- 学习记录数：0
- 参考资料数：1
- 资产文件数：0
