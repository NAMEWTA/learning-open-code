# 教学笔记：Backend lifecycle 与 SQLite 竞争规避

## 注意事项

- 本主题聚焦 TypeScript main/WebHost 侧的 backend lifecycle；aioncore 内部 SQLite 打开、migration 和 recovery flag 消费逻辑作为后续缺口记录。
