# 垂直切片设计指南

垂直切片是与"按模块横切"互补的视角：模块总览是"竖着看一层楼"，垂直切片是"从一楼电梯直接坐到顶楼，把沿途每一层都摸一遍"。

## 选取标准

优先选择用户 / 调用方能直接感知的完整行为。典型示例：

- 登录鉴权（前端表单 → 路由 → 中间件 → Service → DB → Token 返回）
- 下单支付（购物车 → 订单创建 → 支付网关 → 回调 → 状态更新）
- 文件上传处理（前端选择 → API 接收 → 校验 → 存储 → 元数据入库）
- CLI 命令执行（参数解析 → 配置加载 → 核心逻辑 → 结果输出）
- 事件驱动流程（消息到达 → 反序列化 → 业务处理 → 确认/重试）

## 每篇垂直切片文档必须包含 5 要素

1. **入口点**：HTTP 路由 / CLI 命令 / 事件监听 / UI 事件处理等，附真实代码片段
2. **沿途每一层**：中间件 → Controller → Service → Repository/DAO → 外部依赖（DB、缓存、消息队列、第三方 API），每一层附真实代码片段
3. **调用时序**：mermaid 时序图或 ASCII 时序描述，清晰展示调用链
4. **至少一条异常/边界路径**：如认证失败、参数非法、超时、资源不存在，展示错误如何逐层传播与处理
5. **交叉链接**：与相关 L1 模块总览、L3 API 参考的链接

## 时序图示例

```mermaid
sequenceDiagram
    participant C as Client
    participant R as Router
    participant M as AuthMiddleware
    participant CTL as AuthController
    participant SVC as AuthService
    participant DB as Database

    C->>R: POST /api/login
    R->>M: 路由到中间件
    M->>M: 解析请求体
    M->>CTL: 放行
    CTL->>SVC: login(username, password)
    SVC->>DB: SELECT user WHERE username=?
    DB-->>SVC: UserRecord
    SVC->>SVC: 验证密码哈希
    alt 密码正确
        SVC-->>CTL: JWT Token
        CTL-->>C: 200 { token }
    else 密码错误
        SVC-->>CTL: null
        CTL-->>C: 401 Unauthorized
    end
```

## 命名规范

每个垂直切片是一个独立 teach 主题目录 `slice-<功能-slug>/`，课程文件命名 `lessons/<功能-slug>.html`（与 output-structure.md 一致）。

- `<功能-slug>`：短横线命名的功能英文简述（如 `auth-login-flow`、`order-checkout-flow`）
- 由于一个切片主题目录只含一节课，不使用 teach SKILL 默认的递增编号前缀；任务单中的 `output_path` 为最终权威路径

## 与 teach SKILL 的协作

垂直切片文档作为 HTML 课程产出，由 teach SKILL 按课程格式生成。teach-goal 在任务单中提供：
- 垂直切片涉及的所有源码文件及行号
- 层级顺序（如"路由 → 中间件 → Service → DAO → 数据库"）
- 必须覆盖的异常路径
- 关联的 L1/L3 文档路径
