# 使命：移动端后台恢复、持久化刷新与同步补偿全链路

## 为什么
学习者需要能排查 Super Productivity 在 Android、iOS 和 PWA 环境中从后台恢复后的数据一致性问题：计时是否补上、操作是否落盘、同步是否补偿、service worker 是否影响首轮同步。

## 成功的样子
- 能从 Android/iOS/PWA 前后台事件追到 Web 层补时、op-log flush 和 sync trigger。
- 能判断一个恢复问题属于原生桥、Angular effects、持久化、同步补偿还是 service worker 缓存边界。
- 能说清 `OperationWriteFlushService.flushPendingWrites()` 为什么是后台前最后一道持久化闸门。

## 约束条件
- 本主题是 L2 垂直切片，只讲“恢复到同步补偿”的主链路和排障判断。
- 短课控制在 15 分钟内；长源码表、边界条件和故障排查放入 reference。
- 源码路径保留源项目内相对路径，代码标识符保留英文。

## 不在范围内
- 不深入通知/提醒调度、Widget、WebDAV bridge、PWA cache update UI 和各同步 provider 的完整实现。
- 不展开 op-log 冲突算法的 L4 细节，只保留与后台恢复/flush 直接相关的判断点。
