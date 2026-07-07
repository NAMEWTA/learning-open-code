# 课程快照：ai-integration

## 源项目信息
- **源仓库**：`open-java/RuoYiVuePlus/ruoyi-vue-plus`
  - **Git Commit**：`348141427d86fbe39041ffafbc5b26473722cd63`
  - **短 Commit**：`3481414`
  - **分支**：`6.X`
- **源仓库**：`open-java/RuoYiVuePlus/ruoyi-vue`
  - **Git Commit**：`728fdbfe0eae5b5b4ed186801ea9e96e8365ced7`
  - **短 Commit**：`728fdbf`
  - **分支**：`6.X-Vue`
- **源仓库**：`open-java/RuoYiVuePlus/ruoyi-react`
  - **Git Commit**：`e74984e0e05d8807eda19d0a3f7fb9e23771619d`
  - **短 Commit**：`e74984e`
  - **分支**：`6.X-React`
- **快照时间**：2026-07-06T15:39:54+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `// ruoyi-common-web 中的 BaseController 关键方法
public R&lt;Void&gt; success() { return R.ok(); }
public R&lt;Void&gt; fail(String msg) { return R.fail(msg); }
// 等等...` | 课程分析引用 | 🟡 辅助 |
| `/api/snail/chat/**` | 课程分析引用 | 🟡 辅助 |
| `SDK 内部封装了 gRPC 通信细节` | 课程分析引用 | 🟡 辅助 |
| `application-dev.yml` | 课程分析引用 | 🟡 辅助 |
| `application.yml` | 课程分析引用 | 🟡 辅助 |
| `com.aizuda.snail.ai.* — Maven 依赖引入` | 课程分析引用 | 🟡 辅助 |
| `org.dromara.ai.controller` | 课程分析引用 | 🟡 辅助 |
| `org.dromara.common.ai.config / handler` | 课程分析引用 | 🟡 辅助 |
| `plus-ui-react / plus-ui-vue` | 课程分析引用 | 🟡 辅助 |
| `ruoyi-api` | 课程分析引用 | 🟡 辅助 |
| `ruoyi-common-ai` | 课程分析引用 | 🟡 辅助 |
| `ruoyi-common-web` | 课程分析引用 | 🟡 辅助 |
| `ruoyi-common/ruoyi-common-ai/pom.xml` | 课程分析引用 | 🟡 辅助 |
| `ruoyi-common/ruoyi-common-ai/src/main/java/org/dromara/common/ai/config/SnailAiConfig.java` | 课程分析引用 | 🟡 辅助 |
| `ruoyi-common/ruoyi-common-ai/src/main/java/org/dromara/common/ai/handler/SnailAiChatExceptionHandler.java` | 课程分析引用 | 🟡 辅助 |
| `ruoyi-demo` | 课程分析引用 | 🟡 辅助 |
| `ruoyi-modules/ruoyi-ai` | 课程分析引用 | 🟡 辅助 |
| `ruoyi-modules/ruoyi-ai/pom.xml` | 课程分析引用 | 🟡 辅助 |
| `ruoyi-modules/ruoyi-ai/src/main/java/org/dromara/ai/controller/SnailAiController.java` | 课程分析引用 | 🟡 辅助 |
| `ruoyi-system` | 课程分析引用 | 🟡 辅助 |
| `ruoyi-system-api` | 课程分析引用 | 🟡 辅助 |
| `ruoyi-workflow` | 课程分析引用 | 🟡 辅助 |
| `src/api/ai/agent/index.ts` | 课程分析引用 | 🟡 辅助 |
| `src/pages/ai/chat/index.tsx` | 课程分析引用 | 🟡 辅助 |
| `src/views/ai/chat/index.vue` | 课程分析引用 | 🟡 辅助 |
| `views/monitor/snailai/index.vue` | 课程分析引用 | 🟡 辅助 |
| `不属于本仓库——通过 gRPC 连接` | 课程分析引用 | 🟡 辅助 |
| `依赖:ruoyi-common-satoken` | 课程分析引用 | 🟡 辅助 |
| `关键:assignableTypes 限定范围` | 课程分析引用 | 🟡 辅助 |
| `类型:Snail AI SDK · com.aizuda.snail.ai.common.openapi.dto` | 课程分析引用 | 🟡 辅助 |
| `返回类型:Snail AI SDK · OpenApiUserVO` | 课程分析引用 | 🟡 辅助 |
| `防御性编程:三层 null/status/data 检查` | 课程分析引用 | 🟡 辅助 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| 0001 | `lessons/0001.html` | 第 1 课 · ruoyi-ai 模块全景：可拔插 AI 的三层架构 |
| 0002 | `lessons/0002.html` | 第 2 课 · 自动配置与用户身份桥接 |
| 0003 | `lessons/0003.html` | 第 3 课 · 异常处理双轨制与 SSE 流式对话 |
| 0004 | `lessons/0004.html` | 第 4 课 · 双前端集成路线对比：React 原生组件 vs Vue iframe 嵌入 |
| 0005 | `lessons/0005.html` | 第 5 课 · chat.ui.embed 配置溯源：SDK 内置还是 RuoYi 自造？ |
| 0006 | `lessons/0006.html` | 第 6 课 · UI 页面嵌入与免登入机制全链路详解 |
| 0007 | `lessons/0007.html` | 第 7 课 · API 转发到 SDK Controller 的完整机制 |

## 参考资料

- `reference/0004.html`

## 快照摘要
- 课程数：7
- 引用源文件数：32
- 学习记录数：1
- 参考资料数：1
- 资产文件数：0
