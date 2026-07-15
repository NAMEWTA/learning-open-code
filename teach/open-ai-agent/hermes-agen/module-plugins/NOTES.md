# 教学笔记：插件系统模块

- 插件系统是 Hermes "微内核 + 插件" 架构的核心体现，重点在于理解 PluginManager 的扫描→分类→加载链路，而非具体插件的实现细节
- backend 和 exclusive 两种形态的加载策略差异是最容易混淆的点——bundled backend 自动加载，exclusive 完全不经过 PluginManager
- 20+ 个 Hook 不需要一次记住，重点掌握 pre_tool_call（可阻止执行）、post_tool_call（观察者）、pre_llm_call（注入上下文）三个最常用的即可
- 后续 L2 课程可按浏览器、记忆、图像生成等插件子模块展开，各自讲授 Provider 实现细节
