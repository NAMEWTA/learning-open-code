# 使命：安装、发布资产、内置 skills/prompts 包装模块

## 为什么
用户已从 L0 知道 `pi-subagents` 是 Pi extension，但还不清楚「装到 Pi 里」和「发到 npm」分别靠什么文件完成。本主题要把注意力收窄到仓库根部的包装层：理解 `package.json` 如何把 extension、skills、prompts 和内置 agents 一起交付，以及 `install.mjs` 与 CI 如何保证安装和发布可靠。

## 成功的样子
- 能区分 `pi install npm:pi-subagents` 与 `npx pi-subagents` 两条安装路径各自做什么。
- 能读懂 `package.json` 中 `files`、`pi.extensions`、`pi.skills`、`pi.prompts` 和 `bin` 的分工。
- 能说明 `skills/pi-subagents/SKILL.md` 与 `prompts/*.md` 在运行时的角色差异。
- 能根据 `test.yml` 和 `release.yml` 判断发布前会跑哪些测试、发布如何触发。

## 约束条件
- 本主题是 L1 模块导览，只讲包装与资产交付，不展开 extension 注册或 executor 执行细节。
- 课程面向具备 Node/npm 基础的开发者，正文控制为 15 分钟内完成的短课。
- 本轮只写入 `teach/open-ai-agent/pi-subagents/module-packaging-assets/`，不更新项目进度文件或其他主题目录。

## 不在范围内
- 不逐行讲解 `src/extension/index.ts` 的注册逻辑。
- 不覆盖 slash 命令解析、agent discovery 或 async runner 实现。
- 不做 prompts 全文百科；完整清单与 CI 步骤矩阵放入 reference。
