# 教学笔记：扩展入口与 Pi runtime 注册模块

- 交互语言使用简体中文；代码标识符保留英文。
- 本轮任务限定写入 `teach/open-ai-agent/pi-subagents/module-extension-runtime/`，不更新项目级 `index.md`、进度文件或其他主题目录。
- Lesson 只讲一个学习目标：读懂 `src/extension` 作为 Pi runtime 注册层的边界。
- L0 已覆盖项目整体架构，本主题避免重复 parent/child 全局叙述，只在必要处链接 L0。
- 接口清单、源码索引和测试佐证放入 reference，lesson 只保留最小注册链路。
