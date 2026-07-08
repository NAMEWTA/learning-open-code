# 使命：Agent 管理、覆盖与配置解析全链路

## 为什么
在 pi-subagents 里，同名 `reviewer` 可能同时来自 builtin、package、user 项目目录和 settings override。要回答「最终跑的是哪个 model」「disable 为什么没生效」「create 写到了哪里」，必须能从前台 `subagent` 管理动作或执行路径的 `discoverAgents` 一路指到 frontmatter 解析、settings 覆盖与 scope 合并。

## 成功的样子
- 能画出「管理读路径」与「执行发现路径」的分叉与汇合点
- 能按优先级解释 builtin / package / user / project 与 settings 的叠加顺序
- 能区分 builtin override 与 custom agent override 的字段填充规则
- 能预判 disable、enable、reset、eject 在跨 scope 冲突时的返回信息

## 约束条件
- 以 `scope: "both"` 为主路径，单节课 15 分钟内完成
- 长表、动作清单与测试索引查 `reference/agent-management-config-flow-map.html`

## 不在范围内
- 单次 foreground run 与 executor 会话细节（见 `slice-single-foreground-run`）
- chain / parallel 编排（见 `slice-parallel-chain-execution`）
- skills 发现与注入正文（见 L1 `module-agent-system` 参考页 skills 小节）
