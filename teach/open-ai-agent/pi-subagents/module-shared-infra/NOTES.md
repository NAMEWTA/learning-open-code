# 教学笔记：共享类型、状态与文件基础设施模块

- 2026-07-07：按 teach-goal 任务单生成 L1 主题，只写入本主题目录。
- 课程设计重点：短课只讲一个目标，即 `src/shared` 如何支撑可观测执行；字段清单、常量和依赖矩阵放入 reference。
- 运行约束：shell 命令使用 `rtk` 前缀；不修改 `_progress.json`、`_progress.md`、`index.md` 或其他主题目录。
- 测试记录：已运行 `node --experimental-strip-types --test test/unit/artifacts.test.ts test/unit/atomic-json.test.ts test/unit/jsonl-writer.test.ts test/unit/status-format.test.ts`，14 个测试通过。
