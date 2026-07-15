# 使命：技能系统

## 为什么
Hermes Agent 最独特的能力是"自进化学习闭环"——在执行任务后自动创建可复用技能、在使用中持续改进。这个能力由 skills/ + optional-skills/ 目录（110 个 Python 文件）驱动，兼容 agentskills.io 开放标准。理解技能的定义格式、加载流程、渐进式披露和策展器自动管理机制，是掌握 Hermes "学习能力"的关键。

## 成功的样子
- 能写出一个符合 agentskills.io 标准的 SKILL.md 技能定义文件
- 能解释技能的三级渐进式披露架构（skills_list → skill_view → 文件读取）
- 能画出技能系统的核心数据流：SKILL.md → 工具注册 → skills_list/skill_view → 运行时注入
- 能说出 Skills Hub 的 7 种技能来源及信任层级
- 能描述 Curator 策展器如何自动管理 agent 创建的技能（标记陈旧 → 归档，永不自删）

## 约束条件
- 学习方式：阅读教学课程 + 对照源码验证
- 先修要求：已完成 L0 Hermes Agent 项目总览，理解整体分层架构
- 本模块聚焦 skills/ 和 optional-skills/ 目录及 tools/skills_*.py 核心文件，不深入具体 skill 的脚本实现细节

## 不在范围内
- 各个 skill 的内部脚本实现逻辑（如 comfyui 的 workflow runner、polymarket 的 API 封装）
- plugins/ 目录的插件系统（属于 plugin 模块课程）
- agent/curator.py 的对话级策展逻辑（属于 agent-core 模块课程）
- tools/ 下除 skills_*.py 以外的其他工具实现
