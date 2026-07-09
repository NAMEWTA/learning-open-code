# 东财防封限流机制 资源

## 知识

- [a-stock-data SKILL.md § 数据源优先级 & 东财防封](https://github.com/simonlin1212/a-stock-data)
  本课程的主要源码参考。包含东财风控阈值表（社区实测）、防封铁律、em_get() 完整实现代码。适用于：理解每个限流参数的设计依据。

- [requests 库文档 — Session 对象](https://requests.readthedocs.io/en/latest/user/advanced/#session-objects)
  requests.Session 的 Keep-Alive 连接复用机制。适用于：理解 EM_SESSION 为什么比每次新建连接更省时且更"像正常浏览器"。

- [urllib3 Retry 机制文档](https://urllib3.readthedocs.io/en/stable/reference/urllib3.util.html#urllib3.util.Retry)
  HTTPAdapter + Retry 的参数说明，包括 backoff_factor、status_forcelist 的行为。适用于：理解连接重试的指数退避逻辑。

- [Python threading.Lock 文档](https://docs.python.org/3/library/threading.html#lock-objects)
  虽然 em_get() 当前用全局时间戳实现串行而非 threading.Lock，但理解锁的语义对课后扩展方案（如线程安全的限流器）有帮助。

## 智慧（社区）

- [AKShare 社区讨论 — 东财反爬](https://github.com/akfamily/akshare/issues)
  AKShare 用户常讨论东财接口的反爬更新，可以从社区反馈中了解风控策略的变化趋势。适用于：跟踪东财风控阈值是否随版本变化。

## 空白

- 东财风控的精确触发条件（如"5分钟 300 次"是社区实测经验值，非官方文档）——东方财富未公开发布 API 使用条款和速率限制规范
- 分布式场景下的 IP 轮换策略——本 SKILL 假设单机运行，多机器/多 IP 的场景不在覆盖范围内
