# 使命：electron-builder 资源裁剪与发布资源校验

## 为什么
学习者需要维护 AionU 的发布资产可靠性：发布包要足够精简，不能把源码、测试和多余 native/vendor 文件塞进安装包；同时又不能误删 aioncore、managed resources、Hub/WebCLI 等运行时必需资源。掌握本主题后，学习者可以在修改打包配置或发布脚本时判断“该裁剪什么、必须保留什么、缺失如何被测试拦住”。

## 成功的样子
- 能解释 `electron-builder.yml` 中 `files`、`extraResources`、`asarUnpack` 各自承担的资源边界。
- 能沿着 bundled-aioncore 从准备、打包、afterPack 校验到测试断言说清关键不变量。
- 能审查 `prepare-release-assets.sh` 与 `verify-release-assets.sh`，指出发布资产校验覆盖了什么、还没有覆盖什么。

## 约束条件
- 本轮只生成 L4 深度剖析内容，不重复 L1 的完整构建流程总览。
- 每节课控制在 15 分钟内，长清单分流到参考文档。
- 只使用当前源码和既有测试作为证据，不改动 AionU 源项目。

## 不在范围内
- 不讲 Electron Vite 编译细节。
- 不展开自动更新服务、CDN 重写和安装 UI。
- 不设计新的发布方案或改写 CI workflow。
