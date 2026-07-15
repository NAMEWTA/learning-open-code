# 课程快照：authentication

## 源项目信息
- **源仓库**：`open-java/RuoYiVuePlus/ruoyi-vue-plus`
  - **Git Commit**：`348141427d86fbe39041ffafbc5b26473722cd63`
  - **短 Commit**：`3481414`
  - **分支**：`6.X`
- **源仓库**：`open-java/RuoYiVuePlus/ruoyi-vue`
  - **Git Commit**：`728fdbfe0eae5b5b4ed186801ea9e96e8365ced7`
  - **短 Commit**：`728fdbf`
  - **分支**：`6.X-Vue`
- **源仓库**：`open-java/RuoYiVuePlus/ruoyi-react`
  - **Git Commit**：`e74984e0e05d8807eda19d0a3f7fb9e23771619d`
  - **短 Commit**：`e74984e`
  - **分支**：`6.X-React`
- **快照时间**：2026-07-06T15:39:54+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `src/utils/request.ts` | 请求/响应拦截器 + 防重提交 + AES 加密 | 🔴 核心 |
| `src/store/modules/user.ts` | Pinia Setup Store：login/getInfo/logout | 🔴 核心 |
| `src/store/modules/permission.ts` | 动态路由：filterAsyncRouter + loadView | 🔴 核心 |
| `src/permission.ts` | Vue Router 守卫 + 白名单守卫 | 🔴 核心 |
| `src/utils/auth.ts` | useStorage token 持久化管理 | 🟡 辅助 |
| `src/utils/validate.ts` | isPathMatch 路径通配符匹配器 | 🟡 辅助 |
| `src/api/login.ts` | 登录 API + isEncrypt/isToken 控制 | 🟡 辅助 |
| `ruoyi-admin/.../AuthController.java` | @ApiEncrypt + @SaIgnore 实战 | 🔴 核心 |
| `ruoyi-admin/.../SysLoginService.java` | LoginUser 构建 + 登录失败计数 | 🔴 核心 |
| `ruoyi-common-encrypt/.../ApiEncrypt.java` | 强制加密注解定义 | 🔴 核心 |
| `ruoyi-common-encrypt/.../CryptoFilter.java` | Servlet Filter 加解密过滤器 | 🔴 核心 |
| `ruoyi-common-satoken/.../LoginHelper.java` | Token-Session 读写 + login/logout | 🔴 核心 |
| `ruoyi-common-satoken/.../SaPermissionImpl.java` | StpInterface 权限回调双源策略 | 🔴 核心 |
| `ruoyi-common-satoken/.../SaTokenExceptionHandler.java` | NotLoginException 类型码 → 用户提示 | 🔴 核心 |
| `ruoyi-common-satoken/.../SaTokenConfig.java` | Sa-Token Bean 注册配置 | 🟡 辅助 |
| `ruoyi-common-security/.../SecurityConfig.java` | SaInterceptor 鉴权 + clientId 校验 | 🔴 核心 |
| `ruoyi-common-security/.../AllUrlHandler.java` | 启动时全量 URL 收集 | 🟡 辅助 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| 0001 | `lessons/0001.html` | 第 1 课 · 鸟瞰：一次密码登录的全栈链路 |
| 0002 | `lessons/0002.html` | 第 2 课 · 客户端体系 + grantType + 策略模式 |
| 0003 | `lessons/0003.html` | 第 3 课 · Sa-Token 怎么签发 token |
| 0004 | `lessons/0004.html` | 第 4 课 · 统一拦截器 + 权限加载 + 异常 |
| 0005 | `lessons/0005.html` | 第 5 课 · 五种登录 + 注册 + 三类验证码 |
| 0006 | `lessons/0006.html` | 第 6 课 · 接口加解密在登录链路中的位置 |
| 0007 | `lessons/0007.html` | 第 7 课 · 前端 Vue 鉴权对接 |
| 0008 | `lessons/0008.html` | 第 8 课 · React 鉴权对接 + 全栈对比收官 |
| 0009 | `lessons/0009.html` | 第 9 课 · request.ts 请求拦截器全解析 |
| 0010 | `lessons/0010.html` | 第 10 课 · request.ts 响应拦截器：401、解密、错误处理 |
| 0011 | `lessons/0011.html` | 第 11 课 · Pinia Store 用户状态：user.ts |
| 0012 | `lessons/0012.html` | 第 12 课 · permission.ts 动态路由：JSON→Vue Router |
| 0013 | `lessons/0013.html` | 第 13 课 · @ApiEncrypt 注解与 CryptoFilter 全链路 |
| 0014 | `lessons/0014.html` | 第 14 课 · Sa-Token Session 存储模型与 LoginHelper |
| 0015 | `lessons/0015.html` | 第 15 课 · 强制下线：NotLoginException 状态码与验签链路 |
| 0016 | `lessons/0016.html` | 第 16 课 · StpInterface 权限回调：SaPermissionImpl 详解 |
| 0017 | `lessons/0017.html` | 第 17 课 · useStorage 语法 + 前后端白名单对比 |

## 参考资料

- `reference/0001.html`
- `reference/0002.html`
- `reference/0003.html`
- `reference/0004.html`
- `reference/0005.html`
- `reference/0006.html`
- `reference/0007.html`
- `reference/0008.html`
- `reference/0009.html` — request.ts 拦截器速查表
- `reference/0013.html` — Filter vs Interceptor vs AOP 选型矩阵
- `reference/0017.html` — 前后端白名单对照表

## 快照摘要
- 课程数：17
- 引用源文件数：22
- 学习记录数：2
- 参考资料数：11
- 资产文件数：0
