# 使命：Backend lifecycle 与 SQLite 竞争规避

## 为什么
维护者需要判断 AionU 在桌面、WebUI、密码重置和恢复路径中到底应该由谁启动 aioncore。掌握这个主题后，面对 backend 启动失败、`database is locked`、数据目录不一致或 WebUI 复用问题时，可以先检查生命周期 owner 和数据目录契约，而不是在 renderer 或静态服务器里盲查。

## 成功的样子
- 能解释为什么 Desktop main 必须先完成 `initializeProcess()` 和 legacy SQLite 迁移，再启动 backend。
- 能从源码判断某条路径是在复用现有 backend，还是会冒险启动第二个 backend。
- 能区分 SQLite 竞争的长期治理手段、短期缓冲手段和错误诊断边界。

## 约束条件
- 本主题是 L4 深度剖析，不重复 L1/L2 的完整启动链路图。
- 课程保持短课形式，长表格和源码索引放入 `reference/`。
- 只基于当前 AionU 源码、测试和已生成教学资料，不修改源项目。

## 不在范围内
- 不讲 aioncore Rust 内部数据库实现。
- 不重新展开 WebUI 远程访问、backend recovery UI 或桌面启动全链路。
- 不覆盖所有数据库 migration SQL 的业务字段含义。
