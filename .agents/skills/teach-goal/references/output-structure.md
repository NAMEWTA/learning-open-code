# 输出目录结构（独立主题模式）

> **持久化根目录规则**见 [persistence.md](persistence.md)。所有教学产出只能写入 `teach/<path>/`，严禁写入 `.agents/`。

## 禁止路径对照表

| 错误路径 | 正确路径 | 常见原因 |
|---------|---------|---------|
| `.agents/teach/open-ai-agent/pi/...` | `teach/open-ai-agent/pi/...` | init_topic.sh 工作区根目录计算错误 |
| `.agents/openhanako/00-overview/...` | `teach/open-ai-desktop/openhanako/00-overview/...` | 省略 `teach/` 前缀 |
| `.agents/<项目名>/...` | `teach/<path>/...` | 与 skill 目录混淆 |
| `open-ai-agent/pi/...`（源项目路径） | `teach/open-ai-agent/pi/...` | 与教学产出目录混淆 |

teach-goal 不为所有内容创建单一的大目录，而是**每个 L0 / L1(含L3) / L2 / L4 各自为一个独立的 teach 主题目录**。每个主题目录严格遵循 `.agents/skills/teach/SKILL.md` 的工作区规范（SNAPSHOT.md、MISSION.md、lessons/、reference/ 等）。

teach-goal 自身的进度台账和总导航放在项目级 `teach/<project>/` 下。

## 项目级结构

```
teach/<project>/
├── index.md                         # `.agents/skills/teach/SKILL.md` 定义的项目索引（列出所有主题）
├── _progress.json                   # teach-goal 机器可读进度台账
├── _progress.md                     # teach-goal 人类可读进度看板
├── 00-index.md                      # teach-goal Wiki 总导航
│
├── 00-overview/                     # L0 — 项目总览
├── module-<slug>/                   # L1 + L3 — 模块
├── module-<slug>/                   # L1 + L3 — 模块
├── slice-<slug>/                    # L2 — 垂直切片
├── slice-<slug>/                    # L2 — 垂直切片
└── deep-dive-<slug>/                # L4 — 深度剖析
```

**目录前缀规则（强制）**：

| 前缀 | 层级 | 示例 | 说明 |
|------|------|------|------|
| `00-` | L0 | `00-overview/` | 项目总览，有且仅有一个 |
| `module-` | L1+L3 | `module-admin/`、`module-api/` | 模块总览 + 微观 API 参考 |
| `slice-` | L2 | `slice-auth-login-flow/`、`slice-order-checkout/` | 垂直切片功能全链路 |
| `deep-dive-` | L4 | `deep-dive-jwt-refresh-strategy/` | 深度剖析关键设计

## 各层级主题内部结构

### L0 — 项目总览

```
teach/<project>/00-overview/
├── SNAPSHOT.md                      # 源项目版本快照
├── MISSION.md                       # 自动生成的默认使命
├── RESOURCES.md                     # 源项目资源索引
├── NOTES.md                         # 内部便签
├── learning-records/                # 学习记录
├── lessons/
│   └── 000N-<描述>.html             # L0 短课：项目导览（至少 1 节，数量与命名由模型自主决定）
├── reference/
│   └── 00-overview.html             # L0 产出：项目总览（技术栈、架构图、目录结构、设计哲学）
└── assets/                          # 共享组件
```

### L1 + L3 — 模块（总览 + 微观 API）

L3 微观 API 与其父模块 L1 放在**同一个 teach 主题目录**中，因为 L3 是对该模块的 API 级别补充。

```
teach/<project>/module-<slug>/
├── SNAPSHOT.md
├── MISSION.md
├── RESOURCES.md
├── NOTES.md
├── learning-records/
├── lessons/
│   └── 000N-<描述>.html              # L1 短课：模块导览（至少 1 节，数量与命名由模型自主决定）
├── reference/
│   ├── <slug>-overview.html          # L1 产出：模块总览
│   └── <slug>-api.html               # L3 产出：微观 API 参考
└── assets/
```

### L2 — 垂直切片

```
teach/<project>/slice-<slug>/
├── SNAPSHOT.md
├── MISSION.md
├── RESOURCES.md
├── NOTES.md
├── learning-records/
├── reference/
│   └── <slug>-flow-map.html          # 可选：长链路速查/源码索引
├── lessons/
│   ├── 000N-<描述>.html              # L2 短课（至少 1 节，课程数量与拆分由模型根据功能复杂度自主决定）
│   └── ...                           # 复杂链路拆多节短课，不预设固定课程结构
└── assets/
```

### L4 — 深度剖析

```
teach/<project>/deep-dive-<slug>/
├── SNAPSHOT.md
├── MISSION.md
├── RESOURCES.md
├── NOTES.md
├── learning-records/
├── reference/
│   └── <slug>-notes.html             # 可选：长表格/源码索引
├── lessons/
│   ├── 000N-<描述>.html              # L4 短课（至少 1 节，课程数量与拆分由模型自主决定）
│   └── ...                           # 复杂主题拆多节短课，不预设固定课程结构
└── assets/
```

## 各层级产出位置速查

| 层级 | 内容类型 | teach 主题目录 | 必备产出 | 文件类型 |
|------|---------|---------------|---------|---------|
| L0 | 项目总览 | `teach/<project>/00-overview/` | `lessons/` 下至少 1 节短课（数量与命名由模型自主决定） + `reference/00-overview.html` | HTML 课程 + 参考文档 |
| L1 | 模块总览 | `teach/<project>/module-<slug>/` | `lessons/` 下至少 1 节短课（数量与命名由模型自主决定） + `reference/<slug>-overview.html` | HTML 课程 + 参考文档 |
| L2 | 垂直切片 | `teach/<project>/slice-<slug>/` | `lessons/` 下至少 1 节短课，课程数量与拆分由模型自主决定 | HTML 课程 |
| L3 | 微观 API | `teach/<project>/module-<slug>/`（与 L1 同目录） | `reference/<slug>-api.html`；模块主题必须已有 lesson | HTML 参考文档 |
| L4 | 深度剖析 | `teach/<project>/deep-dive-<slug>/` | `lessons/` 下至少 1 节短课，课程数量与拆分由模型自主决定 | HTML 课程 |

## 进度台账

`_progress.json` 和 `_progress.md` 放在**项目级** `teach/<project>/` 下，而非某个主题目录内。

`_progress.json`：机器可读的 Goal 状态数组，每个元素为 Goal 数据结构（见 goal-loop.md）。

`_progress.md`：人类可读的进度看板，含：
- 总体进度百分比
- 按层级分组的完成/进行中/待处理统计
- 最近完成的 5 个 goal 摘要
- 当前队列中的前 5 个 goal 预告

## 00-index.md — Wiki 导航格式

`00-index.md` 放在项目级 `teach/<project>/` 下，是一份**结构化 Wiki 导航页**，让读者能：
- 一眼看清整体进度
- 按层级快速定位到任意文档
- 理解模块→切片→深度剖析之间的关联关系

```markdown
# {PROJECT_NAME} · 架构教学 Wiki

> 📊 整体进度：{完成数}/{总数} goals · {百分比}% · 已执行 {N} 轮
> 🕐 最后更新：{日期}

---

## 📋 进度面板

| 层级 | 完成 | 总数 | 进度 |
|------|------|------|------|
| L0 项目总览 | {N} | 1 | {██░░░░░░} |
| L1 模块总览 | {N} | {M} | {████░░░░} |
| L2 垂直切片 | {N} | {M} | {███░░░░░} |
| L3 微观 API | {N} | {M} | {██░░░░░░} |
| L4 深度剖析 | {N} | {M} | {█░░░░░░░} |

---

## 🏗️ L0 · 项目总览

- **[📘 项目导览短课](00-overview/lessons/000N-<slug>.html)**
  > 15 分钟建立全局地图，再进入各模块。
- **[📄 {PROJECT_NAME} 项目总览参考](00-overview/reference/00-overview.html)**
  > 技术栈：{语言 + 框架} · 架构风格：{分层/微服务/…} · {N} 个顶层模块

---

## 📦 L1 · 模块总览

### module-admin — 后台管理模块
- **[📘 模块导览短课](module-admin/lessons/000N-<slug>.html)**
  > 15 分钟理解模块边界、入口和主要依赖
- **[📄 模块总览参考](module-admin/reference/admin-overview.html)**
  > 职责：RBAC 权限管理、用户 CRUD、系统配置
  > 分层：Controller → Service → Mapper → DB
- **[🔬 API 参考 (L3)](module-admin/reference/admin-api.html)** — {N} 个公共接口
- **关联垂直切片**：
  - [🔪 用户登录全链路](slice-auth-login-flow/lessons/000N-<slug>.html)
  - [🔪 角色权限校验全链路](slice-role-permission-check/lessons/000N-<slug>.html)
- **关联深度剖析**：
  - [🧠 JWT 令牌刷新策略](deep-dive-jwt-refresh-strategy/lessons/000N-<slug>.html)

### module-api — 对外 API 模块
- **[📘 模块导览短课](module-api/lessons/000N-<slug>.html)**
  > 对外 API 的入口、认证和限流边界
- **[📄 模块总览参考](module-api/reference/api-overview.html)**
  > 职责：REST API 网关、认证拦截、限流、版本管理
- **[🔬 API 参考 (L3)](module-api/reference/api-api.html)** — {N} 个公共接口
- **关联垂直切片**：
  - [🔪 API 限流全链路](slice-api-rate-limit/lessons/000N-<slug>.html)

---

## 🔪 L2 · 垂直切片

### slice-auth-login-flow — 用户登录鉴权全链路
- **[📘 课程](slice-auth-login-flow/lessons/000N-<slug>.html)**
  > 入口、层级顺序和关键数据流。复杂链路可拆多节课程。
- **所属模块**：[module-admin](module-admin/reference/admin-overview.html)
- **关联深度剖析**：[🧠 JWT 令牌刷新策略](deep-dive-jwt-refresh-strategy/lessons/000N-<slug>.html)

### slice-order-checkout — 下单支付全链路
- **[📘 课程](slice-order-checkout/lessons/000N-<slug>.html)**
  > 链路：购物车 → OrderController → OrderService → PayGateway → 回调 → 状态机
  > 所属模块：[module-trade](module-trade/reference/trade-overview.html)

---

## 🧠 L4 · 深度剖析

### deep-dive-jwt-refresh-strategy — JWT 令牌刷新策略
- **[📘 课程](deep-dive-jwt-refresh-strategy/lessons/000N-<slug>.html)**
  > 为什么需要双令牌与刷新令牌轮转。复杂主题可拆多节课程。
  > 关联模块：[module-admin](module-admin/reference/admin-overview.html)
  > 关联切片：[🔪 用户登录全链路](slice-auth-login-flow/lessons/000N-<slug>.html)

---

## 📊 源码覆盖统计

| 指标 | 数值 |
|------|------|
| 源码文件 | {N} / {M}（{百分比}%） |
| 公共函数/类 | {N} / {M}（{百分比}%） |
| 核心功能 | {N} / {M}（{百分比}%） |
| 豁免文件 | {N}（vendor / 自动生成 / 二进制） |
```

### Wiki 导航的编写规则

1. **进度面板**必须实时反映 `_progress.json` 的当前状态
2. **每个 L1 模块**下方列出其 L3 API 参考 + 关联的 L2 切片 + 关联的 L4 深度剖析，形成**双向交叉引用**
3. **每个 L2 切片**标注所属模块和关联深度剖析
4. **每个 L4 深度剖析**标注关联模块和关联切片
5. **emoji 前缀**用于视觉区分：🏗️ L0、📦 L1、🔬 L3、🔪 L2、🧠 L4
6. 摘要行（`>` 引用）≤ 80 字，提供足够信息让读者判断是否需要点进去

## 文件命名说明

`.agents/skills/teach/SKILL.md` 默认对 lessons/ 使用递增编号命名（`000N-<slug>.html`），teach-goal 沿用该规则。**课程数量与每节课的 `<slug>` 命名由模型根据实际内容自主决定**，不预设固定课程名称或数量。复杂 L2 / L4 在同一主题目录内拆成多节短课，禁止生成巨型单页课程。`output_path` 仅代表该 goal 的主入口文件；完整交付物以任务单中的 `required_outputs` 和主题审计结果为准。

## teach-goal 与 `.agents/skills/teach/SKILL.md` 的分工

- **teach-goal 负责**：创建每个 teach 主题目录（使用 `.agents/skills/teach/scripts/init_topic.sh`，由主 Agent 在派发前执行）、通过任务单驱动 subagent 激活 `.agents/skills/teach/SKILL.md` 生成内容、管理项目级进度台账和 00-index.md
- **`.agents/skills/teach/SKILL.md` 负责**：在每个主题目录内按自己的规范维护 SNAPSHOT.md、MISSION.md、lessons/、reference/、assets/ 等，生成 HTML 课程和参考文档
- **互不冲突**：teach-goal 的 `_progress.json`、`_progress.md`、`00-index.md` 在项目级；`.agents/skills/teach/SKILL.md` 管理每个主题目录内部的内容
- **收尾同步**：全部 goal 完成后，主 Agent 运行 `.agents/skills/teach/scripts/generate_snapshot.py <project-path> --all` 生成各主题的 SNAPSHOT.md，并补全 `index.md` 中 init_topic.sh 留下的占位条目（主题名称 + ≤50 字描述）
