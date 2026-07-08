# 使命：共享协议与类型模块

## 为什么
学习者需要把 `src/shared` 看成 Orca 多进程系统的契约层，而不是普通类型堆放处。掌握它后，阅读 renderer、main、CLI、relay、mobile 之间的数据流时，可以先检查共享类型、schema 和兼容版本，再进入各端实现。

## 成功的样子
- 能说明 `src/shared` 为什么同时被 renderer、main、CLI、relay 和 mobile 依赖。
- 能找到 runtime RPC、SSH、workspace session、worktree id 等关键契约的定义位置。
- 能判断一个跨端字段变化是否需要考虑协议兼容和 schema 容错。

## 约束条件
- 本主题只做 L1 模块总览，不逐个列出所有 shared 类型。
- 课程保持 15 分钟内完成，长类型簇索引放入参考文档。
- 以 commit `61bd98db6faacb8baffa0de369b187c0e40d662a` 为准。

## 不在范围内
- 不逐项讲解 `types.ts` 中的所有业务类型。
- 不替代 L3 API 参考，后续再补关键函数和 schema 的细节。
