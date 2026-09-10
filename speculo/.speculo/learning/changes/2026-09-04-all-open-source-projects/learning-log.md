# Learning Log

## 2026-09-04：OBJ-01 首课

- 覆盖目标：`OBJ-01`。
- 已使用背景：学习者知道 Sub2API Plus 是 AI API 网关，并能指出 `backend/cmd` 与 `frontend/index.html` 的入口线索。
- 本课新增：区分前端页面入口与 Go 进程入口；理解 setup/normal 两条启动路径；认识 Wire 依赖组装、Gin 路由与中间件、嵌入式前端和优雅退出。
- 仍待验证：学习者能否独立画出 Docker 首次启动/再次启动的差异图，能否从源码定位每个箭头。
- 下一练习：在 `P-practice` 中提交启动地图，并解释 `frontend/src/main.ts` 到 `App.vue` 的挂载顺序。

## 2026-09-04：OBJ-01 补课

- 覆盖目标：`OBJ-01`。
- 触发原因：学习者对 `NeedsSetup` 的分支语义和前端嵌入时序仍不清楚。
- 本课新增：区分启动时状态判断与 HTTP 路由；说明 `SKIP_SETUP`、配置文件、`.installed`、`AUTO_SETUP` 的关系；区分 Vite 构建、`go:embed` 编译和 Gin 运行时静态文件响应。
- 仍待验证：学习者能否在配置/环境变量组合变化时预测启动路径，能否解释 API bypass 与 SPA fallback 的差别。
- 下一练习：在 `P-practice` 中完成本课的两个独立问题，并用源码路径佐证。
