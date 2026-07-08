# 测试体系与行为佐证模块资源

## 知识

- `open-ai-agent/pi-subagents/package.json`
  npm 测试脚本入口。适用于确认 `test:unit`、`test:integration`、`test:e2e`、`test:all` 的命令差异与 Node 标志位。
- `open-ai-agent/pi-subagents/test/support/register-loader.mjs`
  integration/e2e 的 TypeScript 加载钩子注册。适用于理解为何 integration 需要 `--experimental-transform-types` 与自定义 loader。
- `open-ai-agent/pi-subagents/test/support/ts-loader.mjs`
  将源码中的 `.js` import 重写为 `.ts`。适用于排查 integration 环境下的模块解析失败。
- `open-ai-agent/pi-subagents/test/support/helpers.ts`
  共享测试工具：临时目录、event bus、agent 工厂、`tryImport` 优雅跳过、`events` JSONL 构造器。
- `open-ai-agent/pi-subagents/test/support/mock-pi.ts`
  mock Pi CLI 安装器。适用于理解 integration 如何在不调用真实 LLM 的情况下跑通 spawn→parse→result 管道。
- `open-ai-agent/pi-subagents/test/support/mock-pi-script.mjs`
  被 PATH 劫持的 `pi` 可执行脚本。适用于理解队列化 JSON 响应如何转成 child stdout JSONL。
- `open-ai-agent/pi-subagents/test/support/real-session-runner.ts`
  e2e 真实 AgentSession 启动器。适用于理解 faux provider 如何驱动父会话调用 `subagent` 工具。
- `open-ai-agent/pi-subagents/test/support/real-session-child-cli.mjs`
  e2e 子进程 CLI，承载真实 `AgentSession` 与 faux provider。
- `open-ai-agent/pi-subagents/test/unit/*.test.ts`（84 个文件）
  纯函数与小型模块的单测。适用于验证类型、解析、格式化、守卫逻辑，不启动子进程。
- `open-ai-agent/pi-subagents/test/integration/*.test.ts`（21 个文件）
  mock Pi CLI 下的执行管道集成测试。适用于验证 single、parallel、chain、async、slash、intercom、render 等跨模块行为。
- `open-ai-agent/pi-subagents/test/e2e/real-session-subagent.test.ts`
  唯一 e2e：真实父会话 + 子进程 + extension 全链路。适用于确认工具注册与结果回传在真实 Pi runtime 下仍成立。
- `open-ai-agent/pi-subagents/README.md`
  用户模型与运行时行为说明。适用于与测试断言对照，确认「文档承诺」与「可执行佐证」一致。

## 智慧（社区）

- 本地分层运行：`npm run test:unit`、`npm run test:integration -- single-execution chain-execution`、`npm run test:e2e`
  适用于把阅读结论转化为可运行断言；integration 可按文件名过滤子集。
- 已生成的 L1 模块课：`teach/open-ai-agent/pi-subagents/module-runs-execution/lessons/0001-runs-execution-module-tour.html`
  适用于回看 runs 执行边界，再对照 `test/integration/single-execution.test.ts` 等佐证文件。
- Upstream 仓库 Issues：`https://github.com/nicobailon/pi-subagents/issues`
  适用于查找真实用户报告的边界案例，与本地测试覆盖范围交叉验证。

## 空白

目前未收录专门的测试设计文档或贡献者 testing guide；本次 L1 以 `package.json` 脚本、support 夹具和现有 `*.test.ts` 为主要可信来源。若 upstream 后续补充 testing CONTRIBUTING 章节，应同步更新本主题 reference。
