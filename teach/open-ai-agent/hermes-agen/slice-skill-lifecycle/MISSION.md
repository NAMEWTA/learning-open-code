# 使命：技能生命周期全链路

## 为什么
理解 Hermes Agent 技能系统如何实现"自进化"——从一次对话中 agent 完成复杂任务后自动提炼为可复用技能，到策展器定期巡检决定技能的去留。这条链路是 Hermes 区别于其他 Agent 框架的核心竞争力。

## 成功的样子
- 能画出从 Task Complete 到 Skill Archive 的完整 6 阶段时序图
- 能解释 skill_provenance 的 ContextVar 如何在前台/后台写入之间建立安全边界
- 能说出 curator 状态机的三个门控条件、两个时间阈值、五类保护对象
- 能口头描述一条异常路径：为什么 plan 技能永远不会被 curator 归档

## 约束条件
- 本主题聚焦垂直切片（跨模块串联），不深入各模块内部实现细节
- 与 L1 课程配合：module-skills 提供技能格式/来源知识，module-agent-core 提供对话循环背景
- L2 毕业后应能独立阅读 curator.py 1977 行源码

## 不在范围内
- skills_hub.py 的 7 种来源适配器实现细节（见 module-skills L1）
- agent/curator.py 的 LLM consolidate 通道（默认关闭，本课仅提及）
- 各 skill 内部脚本（comfyui、polymarket 等业务逻辑）
- plugins/ 插件系统与技能系统的交互
