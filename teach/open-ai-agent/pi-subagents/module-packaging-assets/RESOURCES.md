# 安装、发布资产、内置 skills/prompts 包装模块资源

## 知识

- [L0 项目整体架构与学习地图](../00-overview/lessons/0001-project-map.html)
  前置课程，说明 `agents/`、`prompts/`、`skills/` 与 `src/` 在目录地图中的位置。
- [pi-subagents README — Installation](https://github.com/nicobailon/pi-subagents#installation)
  官方推荐安装方式：`pi install npm:pi-subagents`。
- [`package.json`](../../../../open-ai-agent/pi-subagents/package.json)
  npm 包元数据、`files` 白名单、`pi` 块（extensions/skills/prompts）和 `bin` 入口。
- [`install.mjs`](../../../../open-ai-agent/pi-subagents/install.mjs)
  `npx pi-subagents` 安装器：克隆或更新 `~/.pi/agent/extensions/subagent`。
- [`skills/pi-subagents/SKILL.md`](../../../../open-ai-agent/pi-subagents/skills/pi-subagents/SKILL.md)
  面向父 orchestrator 的编排规范；子 agent 默认不注入此 skill。
- [`prompts/`](../../../../open-ai-agent/pi-subagents/prompts/)
  7 个可复用工作流模板（parallel-review、review-loop 等），由 `pi.prompts` 声明交付。
- [`agents/`](../../../../open-ai-agent/pi-subagents/agents/)
  8 个内置角色定义，随 `files` 字段一并发布。
- [`.github/workflows/test.yml`](../../../../open-ai-agent/pi-subagents/.github/workflows/test.yml)
  push/PR 时在 Ubuntu 与 Windows 上跑 unit、integration、e2e。
- [`.github/workflows/release.yml`](../../../../open-ai-agent/pi-subagents/.github/workflows/release.yml)
  手动触发的 npm 发布流水线：`test:all` 后 `npm publish --provenance`。

## 智慧（社区）

- [pi-subagents GitHub Issues](https://github.com/nicobailon/pi-subagents/issues)
  适用于核对安装失败、npm 版本、Pi extension 发现路径等真实用户问题。
- [npm — pi-subagents](https://www.npmjs.com/package/pi-subagents)
  适用于核对已发布版本、安装命令和包描述是否与本地 `package.json` 一致。

## 空白

- Pi 官方 `pi install npm:` 机制的内部实现不在本仓库；当前知识依据为 README、`package.json` 的 `pi` 块和 `install.mjs` 行为。
- 本主题未纳入 npm provenance 与 OIDC 发布的详细安全文档；仅记录 `release.yml` 中的 `--provenance` 与 `id-token: write` 权限。
