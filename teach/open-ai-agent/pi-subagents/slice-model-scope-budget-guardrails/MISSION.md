# 使命：模型范围、预算与安全边界全链路

## 为什么
在 pi-subagents 中，子 agent 可能继承父会话的模型、工具调用次数和对话历史。若缺少边界，一次委派可能悄悄换用昂贵模型、无限 browse，或把父级编排指令带进子进程。需要看清「配置从哪来、在哪 enforced、失败时什么严重度」。

## 成功的样子
- 能按顺序说出 modelScope、toolBudget、turnBudget 从 settings/params 到子进程 runtime 的跳点
- 能区分 explicit 模型越界（硬错误）与 inherited 越界（警告）
- 能判断 fork 上下文与 prompt 重写各自防什么风险

## 约束条件
- L2 垂直切片，首课 15 分钟内完成
- 以源码与 unit 测试为证据，不依赖记忆

## 不在范围内
- profile 生成算法细节（见 module-profiles）
- intercom / supervisor 通道（见 slice-native-supervisor-intercom）
- 完整 executor 分流（见 slice-slash-to-executor）
