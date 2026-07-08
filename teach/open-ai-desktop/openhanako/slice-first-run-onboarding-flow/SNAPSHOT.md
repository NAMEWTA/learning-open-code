# 课程快照：slice-first-run-onboarding-flow

## 源项目信息
- **源仓库**：`open-ai-desktop/openhanako`
  - **Git Commit**：`acb1b2b860d0d877a9ba57b9022347643e892b1c`
  - **短 Commit**：`acb1b2b`
  - **分支**：`main`
- **快照时间**：2026-07-07T14:00:00+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `core/first-run.ts` | 首次运行检测、数据目录播种、agent 分类处置 | 🔴 核心 |
| `desktop/bootstrap.cjs` | Electron 启动入口、HANA_HOME 解析、诊断基础设施 | 🔴 核心 |
| `desktop/main.cjs` | Onboarding 窗口创建、setupComplete 决策分支、IPC 处理 | 🔴 核心 |
| `desktop/src/onboarding-main.tsx` | React OnboardingApp 渲染入口 | 🔴 核心 |
| `desktop/src/react/onboarding/OnboardingApp.tsx` | 7 步编排组件、步骤切换、Provider 跨步骤传递 | 🔴 核心 |
| `desktop/src/react/onboarding/steps/ProviderStep.tsx` | Provider 选择、API Key 输入、连接测试逻辑 | 🔴 核心 |
| `desktop/src/react/onboarding/steps/ModelStep.tsx` | 模型发现、添加、选择、编辑元数据 | 🔴 核心 |
| `desktop/src/react/onboarding/steps/LocaleStep.tsx` | 语言选择、i18n 动态加载、局域网服务器连接 | 🟡 辅助 |
| `desktop/src/react/onboarding/steps/NameStep.tsx` | 用户名/Agent 名输入、记忆功能开关 | 🟡 辅助 |
| `desktop/src/react/onboarding/steps/ThemeStep.tsx` | 10 种主题选择、localStorage 持久化 | 🟡 辅助 |
| `desktop/src/react/onboarding/steps/WorkspaceStep.tsx` | 工作区路径选择、默认路径推荐 | 🟡 辅助 |
| `desktop/src/react/onboarding/steps/TutorialStep.tsx` | 5 张教学卡片、引导完成入口 | 🟡 辅助 |
| `desktop/src/react/onboarding/onboarding-actions.ts` | 所有 API 调用逻辑（testConnection、saveProvider、loadModels、saveModel 等） | 🔴 核心 |
| `desktop/src/react/onboarding/constants.ts` | Onboarding 常量（TOTAL_STEPS=7、LOCALES、PROVIDER_PRESETS、OB_THEMES） | 🟡 辅助 |
| `desktop/src/react/onboarding/onboarding-ui.tsx` | 共享 UI 组件（StepContainer、Multiline） | 🟡 辅助 |
| `desktop/src/react/onboarding/onboarding-env.d.ts` | 全局类型声明（t()、i18n） | 🟡 辅助 |
| `desktop/src/shared/onboarding-completion.cjs` | setupComplete 持久化 IPC 链路 | 🔴 核心 |
| `desktop/src/onboarding.html` | Onboarding 窗口 HTML 入口 | 🟡 辅助 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| first-run-onboarding-flow | `lessons/first-run-onboarding-flow.html` | L2 垂直切片：首次运行引导全链路，含 Mermaid 时序图、7 层逐层代码分析、异常路径矩阵 |

## 快照摘要
- 课程数：1
- 引用源文件数：18
- 学习记录数：0
- 参考资料数：0
- 资产文件数：0
