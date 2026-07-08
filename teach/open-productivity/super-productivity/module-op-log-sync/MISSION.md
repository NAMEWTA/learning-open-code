# 使命：Operation Log、本地持久化与同步架构

## 为什么
学习者要能在 super-productivity 中判断一个状态改动是否会被可靠地本地持久化、离线保留并参与同步。掌握这张边界图后，后续读同步算法、修复数据丢失问题或新增 provider 时，不会把 NgRx、IndexedDB、provider 和服务端职责混在一起。

## 成功的样子
- 能用一句话说明 operation log 在本项目中的职责。
- 能从一个 persistent NgRx action 追到 operation 写入 `SUP_OPS`。
- 能区分 app wiring、`@sp/sync-core`、`@sp/sync-providers`、SuperSync server 的边界。
- 能说出文件型 provider 与 SuperSync provider 在同一 op-log 同步口上的差异。

## 约束条件
- 本课是 L1 模块总览，只建立边界和入口，不展开完整冲突解决、上传下载分页或加密细节。
- 每节 lesson 控制在 15 分钟内；长表格和接口清单放入 reference。
- 只写入 `teach/open-productivity/super-productivity/module-op-log-sync/`。

## 不在范围内
- 不逐行讲解完整 sync upload/download 算法。
- 不深挖 LWW 冲突解决、vector clock 剪枝、SuperSync 认证和部署运维。
- 不修改源项目代码或其他教学主题目录。
