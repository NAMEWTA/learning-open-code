# 教学笔记：Android 分享与 Widget 全链路

- 本切片与 `slice-android-native-reminder-flow` 共享「native 队列 + pull 消费」心智模型，讲解时可互相对照。
- 分享链路有 push（`onShareWithAttachment$`）与 pull（`getPendingShareData`）双路径，排障时先确认 `isFrontendReady` 与进程是否被杀。
- Widget drain 的 `onWidgetDoneDrainRequest$` 是无内容信号，任务 ID 始终经 `getWidgetDoneQueue()` 拉取，避免 JS 字符串插值注入风险。
