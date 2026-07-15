# 技能系统 资源

## 知识

- [tools/skills_tool.py — 源码](https://github.com/NousResearch/hermes-agent/blob/main/tools/skills_tool.py)
  技能系统核心工具（~1663 行），实现 skills_list() 和 skill_view()，含平台过滤、前置解析、渐进式披露、关联文件加载、环境变量设置、插件技能限定名路由。适用于理解技能的加载和暴露机制。

- [tools/skills_hub.py — 源码](https://github.com/NousResearch/hermes-agent/blob/main/tools/skills_hub.py)
  Skills Hub 联合库（~4110 行），实现 7 种技能来源适配器：Official、GitHub、skills-sh、well-known、URL、ClawHub、browse-sh。含 GitHub 认证、来源抓取、隔离目录管理。适用于理解技能的外部来源联合发现机制。

- [tools/skill_usage.py — 源码](https://github.com/NousResearch/hermes-agent/blob/main/tools/skill_usage.py)
  技能用量遥测与策展器追踪（管理 `~/.hermes/skills/.usage.json`），实现 bump_view/bump_use/bump_patch、生命周期状态（active/stale/archived）、内置保护列表。适用于理解策展器的自动管理机制。

- [tools/skill_provenance.py — 源码](https://github.com/NousResearch/hermes-agent/blob/main/tools/skill_provenance.py)
  技能写入来源追踪，通过 ContextVar 区分前台用户写入与后台自改进写入，BACKGROUND_REVIEW 哨兵控制策展器写入权限。

- [tools/skills_ast_audit.py — 源码](https://github.com/NousResearch/hermes-agent/blob/main/tools/skills_ast_audit.py)
  技能 Python 文件的 AST 级深度审计，检测动态导入、getattr 非字面参数、__dict__ 访问模式。诊断性工具，非安全网关。

- [hermes_constants.py — 源码](https://github.com/NousResearch/hermes-agent/blob/main/hermes_constants.py)
  常量定义，含 get_skills_dir()、get_bundled_skills_dir()、get_optional_skills_dir() 路径解析逻辑。

- [agentskills.io 规范](https://agentskills.io/specification)
  技能定义文件的开放标准规范，Hermes Agent 的 SKILL.md 格式与此兼容。适用于理解 YAML 前置元数据字段的含义。

- [Hermes Agent 技能文档](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md)
  用户级技能使用文档（~915 行），涵盖技能浏览、安装、创建、管理命令。

- [Hermes Agent 策展器文档](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/curator.md)
  策展器自动管理机制的用户文档，含保护规则、归档策略、配置选项。

## 智慧（社区）

- [r/nousresearch](https://reddit.com/r/nousresearch)
  Nous Research 官方 subreddit，适用于：架构讨论、技能开发经验分享、新功能反馈。

- [Hermes Agent Discord](https://discord.gg/nousresearch)
  官方 Discord 社区，适用于：实时问答、技能开发求助、bug 报告。

## 空白

- agentskills.io 规范的完整技术细节（如版本协商机制）在公开资料中较少，Hermes 的实现是与规范兼容但包含自有扩展。
- Skills Hub 各来源的缓存策略与刷新间隔缺乏独立设计文档。
- 策展器的具体评估算法（如何判断技能"质量"）在源码中有实现但缺乏独立的设计说明。
