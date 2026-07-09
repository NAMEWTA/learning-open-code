# 研报管理全链路 资源

## 知识

- [MyReports.tsx 源码](frontend/src/pages/MyReports.tsx) — 前端研报管理页面：拖拽上传、行业分组展示、下载/删除操作
- [app.py 研报端点](backend/app.py:155-189) — FastAPI 四个研报端点：列表、上传（base64）、文件下载、删除
- [myreports.py 源码](backend/myreports.py) — 研报业务逻辑：存储/索引/行业分类/并发安全
- [api.ts 客户端封装](frontend/src/lib/api.ts) — 前端 API 客户端：MyReport 类型定义、downloadReport blob 下载实现

## 智慧（社区）

- [FastAPI 官方文档](https://fastapi.tiangolo.com/) — FileResponse 与请求体校验
- [MDN FileReader](https://developer.mozilla.org/zh-CN/docs/Web/API/FileReader) — readAsDataURL 与 base64 编码
- [UUID4 RFC 4122](https://www.ietf.org/rfc/rfc4122.txt) — 随机 UUID 的文件命名策略

## 空白

- 暂无行业关键词自动学习的相关资源——当前为静态关键词表，无法根据用户上传模式自动扩展
- 暂无研报全文检索相关资源——当前仅按文件名关键词分类，不解析文件内容
