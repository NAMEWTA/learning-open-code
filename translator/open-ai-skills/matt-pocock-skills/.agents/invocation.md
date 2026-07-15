# 模型调用 vs 用户调用

此仓库中的每个 `SKILL.md` 都是一个 skill。区分它们的唯一维度是**调用方式**——谁能访问它：

- **用户调用**——**只能由用户输入其名称来访问**。在 frontmatter 中设置 `disable-model-invocation: true`。`description` 是**面向用户**的：供浏览斜杠命令的人员阅读的一行摘要。去掉触发列表（"Use when the user says…"）。
- **模型调用**——**模型或用户均可访问**。默认模式：省略 `disable-model-invocation`。`description` 是**面向模型**的，保留丰富的触发措辞（"Use when the user wants…, mentions…, asks for…"），以便自动调用能够触发。判断一个 skill 是否应保持模型调用的测试标准：*模型能否有用地自主访问此 skill？*（复用是提取 skill 的理由，但不是测试标准。）

由于用户调用的 skill 没有 description，除了用户之外没有人能访问它——其他 skill 也无法触发它。因此，用户调用的 skill 可以调用模型调用的 skill，但绝不能访问另一个用户调用的 skill。

分类 `README.md` 和顶层 `README.md` 将条目分组为**用户调用**和**模型调用**。

## 它们之间的依赖关系

依赖关系以 **`/skill` 风格的散文调用**（"Run the `/grilling` skill"）表示，而非深层 `../other-skill/FILE.md` 交叉引用。共享参考文档位于拥有它的 skill 内部；其他 skill 通过调用该 skill 来访问这些材料，而非跨目录链接。

## 被动 vs 主动领域工作

仅仅*阅读* `CONTEXT.md` 获取词汇是一行散文指针，不是 `domain-modeling` skill。只有主动的构建/打磨准则（挑战术语、边界场景、编写 ADR、内联更新 `CONTEXT.md`）才是 `domain-modeling`。
