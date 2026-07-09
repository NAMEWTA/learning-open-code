# 使命：工具定义与执行抽象

## 为什么
学习者需要在 Codex 源码中快速判断一个工具从“模型可见定义”到“真实执行”的落点。完成本主题后，阅读者应能定位新增工具、调试工具调用失败、解释权限/沙箱/hook 为什么出现在执行链路中。

## 成功的样子
- 能画出 `ToolSpec -> ToolRouter -> ToolRegistry -> ToolExecutor -> Runtime` 的最小调用链。
- 能说清 `codex-tools` crate 与 `codex-core/src/tools` 的职责边界。
- 能按清单找到 shell、apply_patch、MCP、动态工具、扩展工具和 code mode 工具的注册入口。
- 能沿着一次 shell 或 apply_patch 调用追到权限审批、沙箱执行和模型输出转换。

## 约束条件
- 本主题是 L1 模块导览，lesson 必须保持 15 分钟内完成；完整工具清单放在 reference。
- 本主题正文写入范围限制在 `teach/open-ai-agent/codex/module-tools-execution/`；项目级索引和进度文件由主 Agent 统一维护。

## 不在范围内
- 不逐行讲解每个工具 handler 的业务逻辑。
- 不覆盖 MCP 协议细节、插件安装流程、code mode 沙箱内部实现。
- 不修改 `open-ai-agent/codex/` 源码或本仓库 `.agents/` 脚本。
