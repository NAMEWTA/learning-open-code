# 文件树可视化规范

在课程 HTML 中用文件树展示项目结构、模块骨架时的**完整格式规范**。避免出现"挤成一坨"、难以阅读的树形结构。

## 目录

1. [核心规则](#核心规则)
2. [树形字符集](#树形字符集)
3. [正确示例](#正确示例)
4. [禁止的反模式](#禁止的反模式)
5. [深度超标时的拆分策略](#深度超标时的拆分策略)
6. [HTML 容器要求](#html-容器要求)

---

## 核心规则

1. **一行一节点**：每个文件/目录独占一行。禁止将多级路径压缩在一行（例如 `├── system/api/ ← 说明`），必须逐层展开（`├── system/` → `│   └── api/`）
2. **最深 5 层**：从根到叶不超过 5 层。超过时必须拆分为多棵子树或展平处理
3. **注释对齐**：`←` 后的注释用空格填充到对齐列（同类节点注释起始列一致）
4. **目录汇总**：目录节点的注释概括内容及数量（如 `← 5 个策略实现`、`← 共 8 个接口`）

## 树形字符集

统一使用 Unicode 方框绘制字符，**禁止**用 ASCII 替代（`|`、`+-` 等）：

| 字符 | 用法 | 说明 |
|------|------|------|
| `├── ` | 中间节点前缀 | 同级后面还有节点 |
| `└── ` | 末尾节点前缀 | 同级最后一个 |
| `│   ` | 垂直连线 | 非末尾节点的下方延伸 |
| `    ` | 空白占位 | 末尾节点下方无连线，4 空格 |

### 缩进规则

- 根节点不缩进，不加任何前缀
- 每深入一层，子节点前缀为父节点的连线延伸：
  - 父节点用 `├── ` 或 `└── ` → 其子节点前缀加 `│   `（父非末尾）或 `    `（父为末尾）
- 文件节点（无子节点）不加垂直连线

**前缀组合速查**（假设深度为 3，父为非末尾）：

```
父（根下的中间节点）
├── 子目录/              ← 深度 1，前缀 = ├──
│   ├── 孙文件.java       ← 深度 2，前缀 = │   ├──
│   └── 孙目录/           ← 深度 2，前缀 = │   └──
│       └── 曾孙文件.java  ← 深度 3，前缀 = │       └──
```

## 正确示例

```
ruoyi-admin/src/main/java/org/dromara/
├── DromaraApplication.java          ← Spring Boot 启动入口
├── DromaraServletInitializer.java   ← WAR 部署支持
└── web/
    ├── controller/
    │   ├── AuthController.java      ← 登录/注册/退出
    │   ├── CaptchaController.java   ← 验证码生成
    │   └── IndexController.java     ← 默认首页
    ├── service/
    │   ├── IAuthStrategy.java       ← 策略接口（含工厂方法）
    │   ├── SysLoginService.java     ← 登录校验/用户构建
    │   ├── SysRegisterService.java  ← 注册服务
    │   └── impl/                    ← 5 个策略实现
    ├── event/
    │   └── UserLoginSuccessEvent.java
    └── listener/
        ├── UserActionListener.java
        └── UserLoginSuccessListener.java
```

**要点**：
- 每行一个节点
- `←` 注释在同类节点间对齐到同一列（用空格填充）
- 目录下有子节点时用 `│   ` 延伸连线
- 最后一个子节点用 `└── `，其下方子节点前缀用 4 空格占位（而非 `│   `）
- `.java` 文件不加 `│   ` 延伸（它们没有子节点）

## 禁止的反模式

以下两种写法**严格禁止**：

### 反模式 1：路径压缩

将多级目录挤在一行节点名中：

```
# ❌ 错误：system/api/ 是两级目录，不应压缩在一行
├── system/api/ ← 系统域契约（8 接口 + 模型）
│   ├── UserService.java ← 用户查询
│   ├── model/ ← 模型对象（LoginUser 等）
│   │   ├── LoginUser.java
│   │   └── ...
```

**问题**：读者分不清 `system/api/` 是一个名叫 `system/api` 的目录还是两级嵌套。必须拆为：

```
├── system/
│   └── api/  ← 系统域契约（8 接口 + 模型）
│       ├── UserService.java ← 用户查询
```

### 反模式 2：嵌套过深

```
# ❌ 错误：深层嵌套让 │ 前缀累积到 12+ 字符宽
    └── workflow/api/ ← 工作流域契约
        ├── WorkflowService.java
        ├── domain/
        │   ├── StartProcessDTO.java
        │   └── ...
        └── event/ ← 工作流事件（Spring 事件解耦）
            ├── ProcessEvent.java
            ├── ProcessTaskEvent.java
            └── ProcessDeleteEvent.java
```

**问题**：`│   │   │   ├──` 前缀占据 12-16 字符宽，在移动端或窄容器中文件名被挤到极右侧。

**解决**：使用拆分策略（见下一节）。

## 深度超标时的拆分策略

当树超过 5 层时，选择以下策略之一：

### 策略 A — 拆分子树（优先）

将深层的子目录单独提出来，在上层树中只保留目录节点和简短注释：

```
# 上层概览（≤3 层）
ruoyi-api/src/main/java/org/dromara/
├── system/api/     ← 系统域契约（详见下方）
└── workflow/api/   ← 工作流域契约（详见下方）

# 子树 1：系统域契约
system/api/
├── RemoteUserService.java          ← 用户查询
├── RemoteDeptService.java          ← 部门查询
├── RemoteRoleService.java          ← 角色名称查询
├── RemotePostService.java          ← 岗位名称查询
├── RemoteConfigService.java        ← 参数配置（带 default 方法）
├── RemoteMessageService.java       ← 消息推送
├── RemoteOssService.java           ← OSS 文件查询
├── RemoteTaskAssigneeService.java  ← 工作流办理人查询
├── model/                          ← 模型对象（9 个类）
│   ├── LoginUser.java
│   ├── XcxLoginUser.java
│   └── ...
└── domain/                         ← 传输对象（8 个 DTO）
    └── ...

# 子树 2：工作流域契约
workflow/api/
├── WorkflowService.java
├── domain/
│   ├── StartProcessDTO.java
│   ├── StartProcessReturnDTO.java  ← Java record
│   ├── CompleteTaskDTO.java
│   ├── FlowCopyDTO.java            ← Java record
│   └── FlowInstanceBizExtDTO.java
└── event/                          ← Spring 事件解耦
    ├── ProcessEvent.java
    ├── ProcessTaskEvent.java
    └── ProcessDeleteEvent.java
```

**原则**：优先使用策略 A。策略 B 仅用于扁平模块（如全是同级接口文件的 api 包）。

### 策略 B — 展平路径

深度超过限制时不再逐层展开，将完整路径作为节点名：

```
ruoyi-api/src/main/java/org/dromara/
├── system/api/RemoteUserService.java       ← 用户查询
├── system/api/RemoteDeptService.java       ← 部门查询
├── system/api/model/LoginUser.java         ← 登录用户模型
└── workflow/api/WorkflowService.java       ← 工作流服务
```

## HTML 容器要求

文件树**必须**包裹在 `<div class="filetree">` 中，配合以下 CSS：

```css
.filetree {
  font-family: "SF Mono", Consolas, monospace;
  font-size: 0.82rem;
  line-height: 1.75;
  background: #fafbfc;
  border: 1px solid #ebebeb;
  border-radius: 8px;
  padding: 1rem 1.2rem;
  white-space: pre;        /* 关键：保留空格和换行 */
  overflow-x: auto;        /* 防止移动端溢出 */
}
```

### 强制要求

- **`white-space: pre`** 是强制要求——缺少它会导致树形结构塌陷为连续文本，所有缩进和换行丢失
- 每个 HTML 课程文件的 `<style>` 块中必须包含 `.filetree` 类定义
- 流程图使用 `.diagram` 类，文件树使用 `.filetree` 类，两者不可混用

## 检查清单

生成课程中的每棵树之前，逐项确认：

- [ ] 每个文件/目录独占一行，无路径压缩
- [ ] 深度 ≤ 5 层，超标已拆分
- [ ] 同类节点 `←` 注释对齐到同一列
- [ ] 使用 `├──`/`└──`/`│   `，无 ASCII 替代
- [ ] HTML 包裹在 `<div class="filetree">` 中
- [ ] CSS 包含 `white-space: pre`
- [ ] 目录节点注释包含内容概括
