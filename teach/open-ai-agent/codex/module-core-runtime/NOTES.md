# 教学笔记：Core Thread/Turn 与模型上下文

- 用户要求本模块只写入 `teach/open-ai-agent/codex/module-core-runtime/`，不得修改源项目、`.agents/`、`_progress.json`、`_progress.md` 或项目级 `index.md`。
- 本次是 L1 模块导览，优先建立边界、对象和阅读顺序；不要试图一次性解释 `codex-core` 的所有文件。
- 后续 L2 适合按垂直切片拆分：interactive turn、app-server turn、tool call execution、skill activation、session resume/fork。
- 课程中反复提醒：AGENTS.md 明确要求抵制继续膨胀 `codex-core`，新概念应先寻找更合适的 crate 边界。
