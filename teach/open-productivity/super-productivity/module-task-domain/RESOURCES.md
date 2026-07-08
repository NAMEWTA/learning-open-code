# 任务、项目、标签与工作上下文领域资源

## 知识

- `open-productivity/super-productivity/ARCHITECTURE-DECISIONS.md`
  本主题最高优先级的本地架构来源，记录 `dueDay` / `dueWithTime` 互斥、`TODAY_TAG` 虚拟标签和项目完成语义。适用于判断改动是否破坏领域不变量。
- `open-productivity/super-productivity/src/app/features/tasks/`
  Task 模型、TaskService、任务列表/详情、短语法、store、effects、提醒、附件、子任务。适用于追踪任务实体字段与用户操作入口。
- `open-productivity/super-productivity/src/app/features/work-context/`
  Project 与 Tag 统一成工作上下文的 selectors 和 service。适用于理解 Today / Project / Tag 视图如何得到 `taskIds`。
- `open-productivity/super-productivity/src/app/features/tag/`
  `TODAY_TAG`、普通标签、标签 actions/reducer/selectors。适用于区分虚拟 Today 和普通标签的成员规则。
- `open-productivity/super-productivity/src/app/features/project/`
  Project 模型、ProjectService、项目 store、完成/归档逻辑。适用于理解项目任务列表、backlog 和完成语义。
- `open-productivity/super-productivity/src/app/root-store/meta/`
  task shared meta-reducers、meta-reducer 注册顺序和 operation capture 入口。适用于理解跨实体不变量在哪里维护。
- `teach/open-productivity/super-productivity/00-overview/lessons/0001-project-map.html`
  L0 项目导览课，提供整体架构位置和后续 L1 主题锚点。适用于复习本主题在全局地图中的位置。

## 智慧（社区）

- [GitHub Discussions](https://github.com/super-productivity/super-productivity/discussions)
  项目 README 标注的讨论区。适用于验证领域理解、阅读维护者对产品语义的解释。
- [GitHub Issues](https://github.com/super-productivity/super-productivity/issues)
  真实 bug 与功能请求来源。适用于检验 Today、重复任务、提醒、同步等边界条件是否被用户触发过。
- [Reddit r/superProductivity](https://www.reddit.com/r/superProductivity/)
  README 标注的用户社区。适用于观察任务组织、时间追踪和工作流需求如何影响领域建模。

## 空白

- 未查找外部 NgRx 教程资源；本主题假设读者已具备 TypeScript / NgRx 基础，当前以项目源码和 ADR 为准。
