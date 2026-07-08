# 使命：本地操作捕获、持久化与同步上传下载全链路

## 为什么
学习者需要能诊断 Super Productivity 的同步问题：一个 NgRx action 是否真的进了 operation log、是否落盘、是否 flush 后上传、下载后是否安全应用，以及加密、压缩、冲突和校验边界分别在哪里生效。

## 成功的样子
- 能从一个带 `meta.isPersistent` 的 action 追到本地 `SUP_OPS` 写入、pending 状态和 immediate upload 触发。
- 能解释 `src/app/op-log/sync/operation-write-flush.service.ts` 为什么是上传和冲突检测前的关键保护。
- 能区分 SuperSync provider 与文件型 provider 的数据格式、加密位置、游标位置和故障排查入口。
- 能判断远端下载后是直接 apply、进入 LWW 冲突解决、接受 full-state import，还是因为校验失败拒绝标记为 `IN_SYNC`。

## 约束条件
- 这是 L2 垂直切片，只讲“本地操作捕获、持久化与同步上传下载”这一条链路。
- 源项目目录只读；课程内容只写入 `teach/open-productivity/super-productivity/slice-op-log-sync-flow/`。
- 所有源码引用尽量使用完整相对路径，避免裸函数名污染快照。

## 不在范围内
- 不展开所有实体 reducer 的业务语义。
- 不深入 SuperSync 服务端数据库、鉴权和部署细节。
- 不做 L3 级别的每个 service API 逐行讲解。
