# pm-ai-shipping — AI 交付套件

面向对 AI 构建代码负责的 PM 和创业者。为 vibe-coded 应用编写文档，审计其安全性和性能是否与预期行为一致，并产出可供审核的交付包。

## 概述

AI 代理能快速编写代码，但不会留下*意图*记录——即系统应该做什么、谁可以执行哪些操作、密钥存放在哪里。没有这些记录，任何人和任何审计代理都无法判断代码是否可以安全交付。本套件恢复了可审查性：它先为系统编写文档，然后审计文档所述与代码实际行为之间的差距——这是一类通用扫描器因缺乏意图模型而无法发现的缺陷。

从 `/ship-check` 开始执行完整流程，或使用专项命令运行单个阶段。

## 安装

从 [pm-skills 市场](https://github.com/phuryn/pm-skills) 安装并启用 `pm-ai-shipping` 插件。每个命令可通过 `/pm-ai-shipping:<command>` 或其简短形式 `/<command>` 触发；skills 在主题匹配时自动加载。

## Skills（2 个）

- **shipping-artifacts** — 使 AI 构建的应用具备可审查性的持久文档集：每个应用都需要的核心文档（架构、用户/权限流程、权限、变量/密钥、测试覆盖地图），以及仅在适用时添加的条件性文档（邮件、定时任务、SEO、嵌入式代理/自动化）。定义每份文档必须涵盖的内容以及审核者如何使用它们。
- **intended-vs-implemented** — 寻找系统文档所述与代码实际行为之间差距的方法，附有双向引用的证据，避免空泛的结论。

## Commands（5 个）

- `/pm-ai-shipping:ship-check` — 将 vibe-coded 仓库转变为可供审核的交付包：编写文档、接入代理上下文、运行安全和性能审计、映射测试覆盖，并整理结果。
- `/pm-ai-shipping:document-app` — 逆向分析代码库，生成审核者和审计者所需的系统文档——核心文档集（架构、流程、权限、变量）以及适用时的条件性文档（邮件、定时任务、SEO、自动化）。
- `/pm-ai-shipping:derive-tests` — 将文档化的意图转化为测试覆盖地图：盘点现有测试，与建议测试和未验证的覆盖缺口分开，标记为单元测试/受保护实时测试/手动测试，并建议合入前的 CI 门禁。
- `/pm-ai-shipping:security-audit-static` — 静态安全审计：映射信任边界，交叉引用文档化的意图，自行反驳每项发现，仅报告有证据支持的风险。
- `/pm-ai-shipping:performance-audit-static` — 静态性能审计：发现过度获取、缺失索引和缓存优化机会，按工作量和影响排序。

## 作者

Paweł Huryn — [The Product Compass Newsletter](https://www.productcompass.pm)

## 许可证

MIT
