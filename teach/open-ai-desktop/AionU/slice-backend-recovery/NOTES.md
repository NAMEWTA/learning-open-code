# NOTES

- 本主题是 L2 垂直切片，主线聚焦“启动失败被分类后如何恢复或呈现给用户”。
- 课程入口固定为 `lessons/0001-flow-map.html`，速查参考固定为 `reference/backend-recovery-flow-map.html`。
- 需要明确边界：`installation-integrity.e2e.ts` 证明 debug 注入的安装完整性弹窗路径，不证明所有 backend 启动失败类型都经过真实二进制失败现场。
