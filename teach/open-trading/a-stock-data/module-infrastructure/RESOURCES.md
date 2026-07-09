# a-stock-data 基础设施 资源

## 知识

- [SKILL.md:104-150 数据源优先级 & 东财防封](open-trading/a-stock-data/SKILL.md)
  优先级原则表格、东财独有数据清单、风控阈值实测数据（2026-05）、防封铁律 5 条。适用于：理解数据源选择策略、评估不同接口的封 IP 风险。

- [SKILL.md:208-264 mootdx 客户端](open-trading/a-stock-data/SKILL.md)
  _TDX_SERVERS 服务器列表（10 个）、_probe() TCP 探测函数、tdx_client() 三级 fallback 实现。适用于：理解 mootdx 0.11.x BESTIP bug 根因及规避方案。

- [SKILL.md:265-289 市场前缀规则 & Ticker 归一化](open-trading/a-stock-data/SKILL.md)
  get_prefix() 前缀映射逻辑、五种输入格式的归一化对照表。适用于：处理任意格式的股票代码输入。

- [SKILL.md:290-354 东财数据中心统一查询](open-trading/a-stock-data/SKILL.md)
  EM_SESSION 全局会话配置、HTTPAdapter+Retry 连接级重试、em_get() 串行限流实现、eastmoney_datacenter() 通用查询 helper。适用于：深入理解东财防封的代码级实现。

- [mootdx GitHub — BESTIP 相关 Issues](https://github.com/rainx/pytdx)
  mootdx 官方仓库，0.11.x BESTIP.HQ 空串 bug 的来源。适用于：了解 bug 的社区讨论和官方修复进展。

- [requests 文档 — HTTPAdapter & Retry](https://requests.readthedocs.io/en/latest/user/advanced/#transport-adapters)
  urllib3 Retry 参数详解（total、backoff_factor、status_forcelist）。适用于：理解 em_get() 中连接级重试的配置含义。

## 智慧（社区）

- [a-stock-data GitHub Issues — 搜索 "风控" / "封IP"](https://github.com/simonlin1212/a-stock-data/issues)
  社区用户分享的东财封 IP 实战经验、阈值验证、解封时间。适用于：了解最新风控规则变化。

- [雪球 / 聚宽社区 — 东财反爬对策](https://xueqiu.com/)
  量化圈对东财接口限流的讨论和应对策略。适用于：了解行业通用的反爬对抗思路。

## 空白

- 缺少东财风控机制的官方文档——所有阈值（>5次/秒、>=10并发、>=300次/5分钟）均来自社区实测，非官方公开
- 缺少 mootdx 0.11.x BESTIP bug 的官方修复路线图——截止快照时（2026-07），mootdx 仓库未发布修复版本
- 缺少通达信 TCP 7709 协议的官方文档——mootdx 本身是基于逆向分析的开源实现
- 缺少国内服务器可达性的权威列表——_TDX_SERVERS 列表需要用户自行维护和更新
