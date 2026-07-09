# 使命：Skill 发现、读取与上下文注入链路

## 为什么
用户已完成 L1-module-extensions-skills-mcp（Skills/Plugins/MCP/Hooks 四种扩展机制的区别）和 L1-module-core-runtime（context 模块与系统提示词组装）两个模块导览。现在需要追踪一个 Skill 从文件系统中的 SKILL.md 被发现，到最终注入模型上下文提示词的完整链路。掌握这条垂直切片后，用户将能够理解 codex 如何让模型"知道"有哪些 Skill 可用，以及 Skill 指令如何进入模型视野。

## 成功的样子
- 能画出从 `discover_skills_under_root()` 目录扫描到 `AvailableSkillsInstructions::body()` 输出系统提示词的完整时序图。
- 能解释 `skill_roots()` 的 5 种 root 来源（Project/User/$HOME/.agents/System/Admin），以及 `repo_agents_skill_roots()` 为什么沿 cwd 向上查找。
- 能说清 `SkillLine` 渲染的预算模型：按 scope 排序、token/character 双预算、别名压缩、平均截断阈值。
- 能在 Skill 解析失败或目录不存在时，根据 error 日志定位根因。

## 约束条件
- 本主题是 L2 垂直切片，2 节 lesson，每节控制在 15 分钟内完成。
- 正文目标 800-1200 中文字，硬上限 1500 中文字。
- 最多 4 个主章节、3 个源码文件、3 个短代码片段（每个不超过 35 行）。
- 只写入 `teach/open-ai-agent/codex/slice-skill-activation/`，不修改源项目。

## 不在范围内
- 不讲 Plugin 的 Skill 发现机制（`plugin_namespace` 解析、`PluginSkillSnapshots` 合并）。
- 不讲 SkillsWatcher 的 file-watcher 底层实现（`notify`/`inotify`/`FSEvents`）。
- 不讲 Skill 的隐式调用检测（`detect_implicit_skill_invocation_for_command`）和执行工具安装。
- 不展开 `codex_ext_skills` 扩展层的渲染逻辑（那是独立 crate）。
