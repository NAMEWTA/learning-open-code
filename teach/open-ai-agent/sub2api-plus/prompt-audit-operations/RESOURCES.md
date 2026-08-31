# 提示词审计实操资源

## 知识

- [内容提取覆盖矩阵](../../../../open-ai-agent/sub2api-plus/docs/SECURITY_AUDIT_CONTENT_COVERAGE.md) — 判断哪些用户输入会进入 Prompt Audit，哪些内容明确排除。
- [Qwen3Guard 适配器实现](../../../../open-ai-agent/sub2api-plus/backend/internal/securityaudit/prompt_qwen3guard.go) — 核对请求格式、响应格式和风险分类解析规则。
- [提示词审计中文界面文案](../../../../open-ai-agent/sub2api-plus/frontend/src/i18n/locales/zh/admin/promptAudit.ts) — 核对页面字段、运行状态和错误提示的准确含义。
- [Qwen3Guard 官方仓库](https://github.com/QwenLM/Qwen3Guard) — 获取官方 Gen 模型列表、vLLM/SGLang 部署命令和输出示例。
- [Qwen3Guard-Gen-0.6B 官方模型卡](https://huggingface.co/Qwen/Qwen3Guard-Gen-0.6B) — 获取模型文件及 OpenAI 兼容服务示例。
- [sub2api-plus 源仓库](https://github.com/LuckyKuang/sub2api-plus) — 查看上游版本、发布说明和 Issues。

## 智慧（社区）

- [sub2api-plus Issues](https://github.com/LuckyKuang/sub2api-plus/issues) — 搜索与 Prompt Audit、Qwen3Guard、Redis 或部署网络相关的实际问题。

## 空白

- 项目内没有提供第三方 Qwen3Guard 服务商清单；模型 ID、Base URL 和 API Key 必须以实际服务为准。
- Prompt Audit 事件没有发现自动按天清理配置；应根据组织的数据保留政策使用事件页的按筛选删除。
