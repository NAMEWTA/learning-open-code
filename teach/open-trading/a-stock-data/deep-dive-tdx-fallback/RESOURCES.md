# mootdx 客户端三级 fallback 资源

## 知识

- [a-stock-data SKILL.md § mootdx 客户端（必读）](https://github.com/simonlin1212/a-stock-data)
  本课程的主要源码参考。包含 BESTIP 空串 bug 的根因分析、tdx_client() 完整实现、_TDX_SERVERS 服务器列表。适用于：理解每一级 fallback 的设计动机。

- [mootdx 项目仓库](https://github.com/bopjiang/mootdx)
  mootdx 的官方源码。适用于：查看 Quotes.factory() 的 bestip 参数和 server 参数的内部实现。

- [Python socket 文档 — create_connection](https://docs.python.org/3/library/socket.html#socket.create_connection)
  TCP 探测 `_probe()` 使用的底层 API。适用于：理解 timeout 参数对探测速度的影响（默认 2s）。

## 智慧（社区）

- [mootdx Issues](https://github.com/bopjiang/mootdx/issues)
  BESTIP 空串 bug 最早在这里报告。适用于：跟踪 mootdx 版本升级后是否修复了该问题。

## 空白

- 通达信官方服务器列表和 IP 分配策略——通达信不公开其行情服务器的基础设施信息，_TDX_SERVERS 列表来自社区实测
- 海外用户访问通达信 TCP 服务的稳定方案——本课程仅指出问题（海外 IP 通常全部超时），不覆盖代理/VPN 方案
