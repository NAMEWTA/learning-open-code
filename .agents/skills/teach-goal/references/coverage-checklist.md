# 覆盖率自检清单与 Definition of Done

## Definition of Done（全部达成才算完成）

- [ ] 仓库中**全部源码文件**（第三方 vendor / 自动生成代码 / 二进制资源除外，需单独列出豁免清单并说明理由）至少被一篇教学文档引用或讲解过
- [ ] 每个顶层目录 / 子系统都有一篇 **L1 模块总览**
- [ ] 每一个"用户可感知的核心功能"（从 README、产品文档、路由表、CLI 命令、主要 UI 入口中识别）都至少有一篇 **L2 垂直切片** 文档
- [ ] 所有对外暴露的 API / 公共类 / 公共函数都有 **L3 微观** 记录（内部私有工具函数可归类简述，但不能完全不提）
- [ ] 复杂度较高、体现关键设计决策/算法/设计模式的部分，有独立的 **L4 深度剖析**
- [ ] 生成了一份 `00-index.md` 总导航，能从宏观一路点进到任意微观细节
- [ ] 进度台账中不存在任何 `pending` / `in_progress` / `needs_fix` 状态的条目
- [ ] 所有 done 状态 goal 的 `review_status` 为 `passed` / `conditional_pass` / `skipped`（不存在 `failed` 或 `pending`）
- [ ] 每个 teach 主题目录已生成 SNAPSHOT.md（运行 `.agents/skills/teach/scripts/generate_snapshot.py <project-path> --all`，用法见 `.agents/skills/teach/SKILL.md`）
- [ ] 每个 teach 主题目录都通过 `.agents/skills/teach/scripts/audit_topic.py <project-path> --all`
- [ ] 不存在 reference-only 主题；每个主题至少有 1 个 `lessons/*.html`
- [ ] `MISSION.md`、`RESOURCES.md`、`SNAPSHOT.md` 无 init_topic.sh 占位符残留
- [ ] 所有 lesson 符合 `.agents/skills/teach/SKILL.md` 的短课合约，不存在巨型单页课程
- [ ] `teach/<project>/index.md` 中所有主题条目已填写实际名称与描述（无 init_topic.sh 占位符残留）
- [ ] 所有 goal 的 `output_path` 均以 `teach/` 开头，不含 `.agents/`
- [ ] `.agents/` 下（排除 `.agents/skills/`）无教学产出残留（MISSION.md、lessons/、reference/、_progress.json 等）

在此之前，**不要**声称任务完成，也不要停止循环。`blocked` goal 不阻塞 DoD，但必须在完成报告中单独列出。

## 每轮循环结束前自检

- [ ] 本轮是否有代码因为"太琐碎"被完全跳过而不是"简述"？（不允许。只允许降低详略程度，不允许完全不讲）
- [ ] 配置文件、构建脚本、CI/CD 流程是否至少被简要提及？
- [ ] 测试用例是否被当作"行为佐证"引用，帮助说明该功能的预期行为与边界情况？
- [ ] 本轮新发现的依赖/引用是否已经生成对应 goal 并入队，而不是随手带过？
- [ ] `_progress.md` 是否已同步更新？
- [ ] 本轮所有产出 `output_path` 是否均以 `teach/` 开头？（路径违规 → goal 不得标记 done）
- [ ] 本轮新增/修改的主题是否运行 `audit_topic.py` 并通过？（失败 → goal 标记 `needs_fix`）
- [ ] 是否出现单节 lesson 承载 5 个以上源码文件、多个异常路径或多个设计决策？（出现 → 拆成同主题多节短课）

## 源码豁免清单

在 L0 阶段识别并记录以下类型的文件，从覆盖范围中排除（需逐一说明豁免理由）：

| 豁免类型 | 识别方式 | 示例 |
|---------|---------|------|
| 第三方依赖 | `vendor/`、`node_modules/`、`lib/` 中明确的三方库 | `vendor/github.com/…` |
| 自动生成代码 | 文件头含 `DO NOT EDIT`、`auto-generated`、`.pb.go`、`.gen.ts` | `*.pb.go`、`*.gen.ts` |
| 二进制/资源文件 | 图片、字体、编译产物 | `*.png`、`*.woff2`、`*.jar` |
| 测试固件/数据 | 仅包含测试数据、无逻辑的 JSON/YAML/fixture 文件 | `testdata/*.json` |
| IDE/编辑器配置 | `.vscode/`、`.idea/` 等 | `.vscode/settings.json` |

## 覆盖率终检

当 goal_queue 清空后，执行最终覆盖率扫描：

1. 列出仓库中所有源码文件（排除豁免清单）
2. 与所有已产出文档中引用的源文件做差集
3. 若差集非空，为每个遗漏文件生成 L3 补充 goal 并入队
4. 重复直到差集为空

## 完成报告模板

生成 00-index.md 后，输出总结报告：

```
📊 教学文档生成完成报告
═══════════════════════════
项目: {PROJECT_NAME}
耗时: {N} 轮
产出:
  - L0 项目总览: 1 篇
  - L1 模块总览: {N} 篇
  - L2 垂直切片主题: {N} 个，短课: {M} 节
  - L3 微观 API: {N} 篇
  - L4 深度剖析主题: {N} 个，短课: {M} 节
覆盖:
  - 源码文件: {N} / {M}（{百分比}%）
  - 公共函数/类: {N} / {M}（{百分比}%）
  - 核心功能: {N} / {M}（{百分比}%）
审查:
  - 通过: {N} · 有条件通过: {N} · 采样跳过: {N}
  - 待修复的 Important 问题: {N}（见 _progress.json review_issues）
豁免: {N} 个文件（vendor/自动生成/二进制）
Blocked: {N} 个 goal（如有，逐条列出 id + 原因，留待人工介入）
```
