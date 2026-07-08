# 使命：memory 注入与异步更新

## 为什么
deer-flow 会把跨会话的用户偏好写进 `memory.json`，并在下一轮对话里自动注入模型上下文。我需要弄清「本轮对话结束」到「下一轮模型看到 `<memory>`」之间究竟经过哪些组件，才能排查记忆没更新、注入为空或 tiktoken 阻塞等问题。

## 成功的样子
- 能按顺序画出：`MemoryMiddleware` 入队 → `queue` 防抖 → `updater` 写盘 → `DynamicContextMiddleware` 注入
- 能解释为何 `user_id` 必须在入队时捕获，而不能依赖 Timer 线程里的 ContextVar
- 能指出注入与更新在 middleware 链上的位置差异（`before_agent` vs `after_agent`）

## 约束条件
- L2 垂直切片：只跟 memory 更新与注入主链路
- 单节短课 15 分钟内，接口表与配置项查参考页

## 不在范围内
- Gateway `/api/memory` CRUD 与前端 Memory 设置页
- per-user 迁移脚本 `migrate_user_isolation.py`
- `format_memory_for_injection` 的 token 预算算法细节
