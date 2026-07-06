---
name: migrate-to-shoehorn
description: 将测试文件从 `as` 类型断言迁移到 @total-typescript/shoehorn。适用于用户提及 shoehorn、想要替换测试中的 `as` 或需要部分测试数据的场景。
---

# 迁移到 Shoehorn

## 为什么用 shoehorn？

`shoehorn` 允许在测试中传递部分数据，同时让 TypeScript 满意。它用类型安全的替代方案替换 `as` 断言。

**仅用于测试代码。** 切勿在生产代码中使用 shoehorn。

测试中使用 `as` 的问题：

- 习惯上不鼓励使用
- 必须手动指定目标类型
- 对于故意传入错误数据需要使用双重 as（`as unknown as Type`）

## 安装

```bash
npm i @total-typescript/shoehorn
```

## 迁移模式

### 大型对象只需少量属性

迁移前：

```ts
type Request = {
  body: { id: string };
  headers: Record<string, string>;
  cookies: Record<string, string>;
  // ...还有 20 个属性
};

it("根据 id 获取用户", () => {
  // 只关心 body.id，但必须伪造整个 Request
  getUser({
    body: { id: "123" },
    headers: {},
    cookies: {},
    // ...伪造全部 20 个属性
  });
});
```

迁移后：

```ts
import { fromPartial } from "@total-typescript/shoehorn";

it("根据 id 获取用户", () => {
  getUser(
    fromPartial({
      body: { id: "123" },
    }),
  );
});
```

### `as Type` → `fromPartial()`

迁移前：

```ts
getUser({ body: { id: "123" } } as Request);
```

迁移后：

```ts
import { fromPartial } from "@total-typescript/shoehorn";

getUser(fromPartial({ body: { id: "123" } }));
```

### `as unknown as Type` → `fromAny()`

迁移前：

```ts
getUser({ body: { id: 123 } } as unknown as Request); // 故意传入错误类型
```

迁移后：

```ts
import { fromAny } from "@total-typescript/shoehorn";

getUser(fromAny({ body: { id: 123 } }));
```

## 各函数使用场景

| 函数             | 使用场景                                           |
| ---------------- | -------------------------------------------------- |
| `fromPartial()`  | 传递部分数据且仍能通过类型检查                     |
| `fromAny()`      | 传递故意错误的数据（保留自动补全）                 |
| `fromExact()`    | 强制完整对象（后续可替换为 fromPartial）           |

## 工作流

1. **收集需求** - 询问用户：
   - 哪些测试文件中有造成问题的 `as` 断言？
   - 是否在处理大型对象，其中只有部分属性相关？
   - 是否需要为错误测试传入故意错误的数据？

2. **安装并迁移**：
   - [ ] 安装：`npm i @total-typescript/shoehorn`
   - [ ] 查找含有 `as` 断言的测试文件：`grep -r " as [A-Z]" --include="*.test.ts" --include="*.spec.ts"`
   - [ ] 将 `as Type` 替换为 `fromPartial()`
   - [ ] 将 `as unknown as Type` 替换为 `fromAny()`
   - [ ] 添加来自 `@total-typescript/shoehorn` 的导入
   - [ ] 运行类型检查以验证
