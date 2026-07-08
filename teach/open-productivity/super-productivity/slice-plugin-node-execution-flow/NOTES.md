# 教学笔记：插件 Node execution grant 全链路

- 本主题按 L2 垂直切片组织：只讲 grant → consent → IPC → 脚本执行边界，不重复插件生命周期全貌。
- 父模块入口：`module-plugin-system/lessons/0001-plugin-system-module-tour.html`；相邻 L2：`slice-plugin-lifecycle-flow/`。
- 安全叙事重点：renderer 不能自写 consent；grant 绑定 webContents；preload one-shot handoff 由 PluginBridgeService 在插件代码前接管。
- uploaded 插件持久 consent 在 disable / uninstall / re-upload 时由 renderer 主动 clear，不在 generic teardown 中清理。
