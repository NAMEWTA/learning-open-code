# 课程快照：module-shared

## 源项目信息
- **源仓库**：`open-ai-desktop/openhanako`
  - **Git Commit**：`acb1b2b860d0d877a9ba57b9022347643e892b1c`
  - **短 Commit**：`acb1b2b`
  - **分支**：`main`
- **快照时间**：2026-07-07T13:30:00+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| shared/config-schema.ts | 配置字段 scope 声明（global/agent），CONFIG_SCHEMA 唯一定义点 | 🔴 核心 |
| shared/config-scope.ts | 配置拆分与注入：splitByScope / injectGlobalFields | 🟡 辅助 |
| shared/experiments-schema.ts | 实验特性定义、状态与 scope 管理 | 🟡 辅助 |
| shared/migrate-config-scope.ts | 一次性配置迁移引擎（agent → global） | 🟡 辅助 |
| shared/hana-root.ts | 项目根目录解析，fromRoot() 路径工具 | 🟡 辅助 |
| shared/hana-runtime-paths.ts | Pi SDK 运行时路径与环境变量注入 | 🟡 辅助 |
| shared/runtime-api-key-ref.ts | 运行时 API Key 引用前缀 | 🟡 辅助 |
| shared/secret-custody.ts | 密钥保管：脱敏、掩码、patch 合并三层机制 | 🔴 核心 |
| shared/safe-fs.ts | 安全文件操作：容错读取、原子写入、安全目录复制 | 🔴 核心 |
| shared/safe-parse.ts | 安全 JSON/HTTP Response 解析 | 🟡 辅助 |
| shared/log-redactor.ts | 日志脱敏引擎：12 类敏感信息正则遮蔽 | 🔴 核心 |
| shared/model-ref.ts | 模型复合键工具：parseModelRef / requireModelRef / modelRefKey | 🔴 核心 |
| shared/model-capabilities.ts | 模型能力探测（Reasoning/Vision/Tool Use） | 🟡 辅助 |
| shared/known-models.ts | 已知模型词典查询 | 🟡 辅助 |
| shared/provider-auth.ts | Provider 认证策略与 Header 规范化 | 🟡 辅助 |
| shared/provider-model-validation.ts | Provider 模型 ID 校验 | 🟡 辅助 |
| shared/ollama-model-metadata.ts | Ollama 本地模型元数据解析 | 🟡 辅助 |
| shared/default-workspace.ts | 默认工作区路径解析与自动创建 | 🟡 辅助 |
| shared/default-workspace-constants.ts | 工作区目录名与心跳间隔常量 | 🟡 辅助 |
| shared/workspace-scope.ts | 工作区 scope 规范化（去重合并） | 🟡 辅助 |
| shared/workspace-output.ts | 工作区输出目录解析 | 🟡 辅助 |
| shared/workspace-history.ts | 工作区历史记录合并去重与过期清理 | 🟡 辅助 |
| shared/workspace-persistence-gc.ts | 工作区持久化 GC（清理失效路径） | 🟡 辅助 |
| shared/workspace-skill-paths.ts | 工作区 Skill 路径检测 | 🟡 辅助 |
| shared/workspace-ui-state.ts | 工作区 UI 状态结构定义 | 🟡 辅助 |
| shared/session-projects.ts | Session 项目管理 | 🟡 辅助 |
| shared/errors.ts | AppError 类型体系 + 20 种预定义错误码 | 🔴 核心 |
| shared/error-bus.ts | ErrorBus 事件总线（发布-订阅、去重、breadcrumb） | 🔴 核心 |
| shared/retry.ts | decorrelated jitter 重试策略 | 🟡 辅助 |
| shared/tool-categories.ts | 工具分类单一事实来源（CORE/STANDARD/OPTIONAL/GLOBAL） | 🟡 辅助 |
| shared/compaction-mode.ts | 会话压缩模式定义 | 🟡 辅助 |
| shared/tool-arg-summary.ts | 工具参数安全摘要 | 🟡 辅助 |
| shared/browser-preferences.ts | 浏览器偏好（cookie/Agent打开行为） | 🟡 辅助 |
| shared/notification-preferences.ts | 通知偏好（Turn 完成通知模式） | 🟡 辅助 |
| shared/access-scope-profiles.ts | 访问权限 Profile（mobile/desktop） | 🟡 辅助 |
| shared/quick-chat-preferences.ts | 快捷对话偏好 | 🟡 辅助 |
| shared/search-providers.ts | 搜索 Provider 注册表 | 🟡 辅助 |
| shared/studio-access-contract.ts | Studio 访问契约 | 🟡 辅助 |
| shared/bridge-visible-text.ts | Bridge 可见文本格式 | 🟡 辅助 |
| shared/net-utils.ts | 本地地址判断工具 | 🟡 辅助 |
| shared/network-proxy.ts | 网络代理配置（system/manual/direct 三种模式） | 🟡 辅助 |
| shared/audio-mime.ts | 音频 MIME 类型定义 | 🟡 辅助 |
| shared/image-mime.ts | 图片 MIME 类型定义 | 🟡 辅助 |
| shared/video-mime.ts | 视频 MIME 类型定义 | 🟡 辅助 |
| shared/link-aware-fs.ts | Link-Aware 符号链接感知文件系统 | 🟡 辅助 |
| shared/text-signature.ts | 文本阶段标记（commentary/final_answer） | 🟡 辅助 |
| shared/cover-gallery-presets.ts | Agent 卡片封面预设 | 🟡 辅助 |
| shared/editor-typography.ts | 编辑器排版常量 | 🟡 辅助 |
| shared/preview-reading-position.ts | 预览阅读位置持久化 | 🟡 辅助 |
| shared/sidebar-ui-state.ts | 侧边栏 UI 状态 | 🟡 辅助 |
| shared/yuan-visuals.ts | Agent 角色视觉标识 | 🟡 辅助 |

## 已生成课程

（无课程 — 本主题为 L1 参考文档，后续可能生成 L3 API 参考作为补充）

## 参考资料

- `reference/shared-overview.html` — L1 模块总览参考文档（速查表式，8 节完整覆盖 51 个文件）

## 快照摘要
- 课程数：0
- 引用源文件数：51
- 学习记录数：0
- 参考资料数：1
- 资产文件数：0
