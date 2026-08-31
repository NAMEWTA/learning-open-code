// @ts-check
// 为 dependency-cruiser 提供深层模块强制。
//
// packages 根目录下的每个包都是一个深层模块（DEEP MODULE）：大量行为
// 藏在一个小接口后面。包的公共表面（PUBLIC SURFACE）是它的入口点（ENTRY POINTS）——
// 位于包根目录的文件。实现位于子文件夹（SUBFOLDERS）中，是私有的——
// 按惯例 `lib/` 放实现、`tests/` 放测试，不过任何子文件夹都是私有的。
// 一个包可以暴露几个小入口点（index.ts、client.ts、server.ts 等）——
// 这优于一个巨大的 barrel index。
//
// 你唯一需要编辑的就是 PACKAGES_ROOT。

/** 包所在位置。每个包一个直接的子目录（扁平，无嵌套）。 */
const PACKAGES_ROOT = "src/packages";

// --- 派生模式（无需编辑） -------------------------------------
const R = PACKAGES_ROOT;
/**
 * 包的私有内部：包子文件夹内嵌套的任何东西。
 * 包的根文件是它的入口点，不在此匹配——
 * 它们保持从外部可导入。
 */
const PACKAGE_INTERNALS = `^${R}/[^/]+/[^/]+/`;

/** @type {import('dependency-cruiser').IConfiguration} */
module.exports = {
  forbidden: [
    {
      name: "entrypoint-boundary-from-app",
      comment:
        "App/root code may import a package's entry points (its root files), but nothing inside its subfolders.",
      severity: "error",
      from: { pathNot: `^${R}/` }, // importer is NOT inside any package
      to: { path: PACKAGE_INTERNALS },
    },
    {
      name: "entrypoint-boundary-across-packages",
      comment:
        "A package's own files import each other freely, but may reach OTHER packages only through their entry points — never their internals.",
      severity: "error",
      // importer is inside a package ($1), but is not a test file
      from: { path: `^${R}/([^/]+)/`, pathNot: `^${R}/[^/]+/tests/` },
      to: {
        path: PACKAGE_INTERNALS,
        pathNot: `^${R}/$1/`, // same package → intra-package freedom
      },
    },
    {
      name: "tests-through-entrypoints",
      comment:
        "A package's tests exercise it through its entry points like everyone else: they may import any package's entry points and their own tests/ fixtures, but never any package's internals — not even their own.",
      severity: "error",
      from: { path: `^${R}/([^/]+)/tests/` }, // a test file, in package $1
      to: {
        path: PACKAGE_INTERNALS,
        pathNot: `^${R}/$1/tests/`, // own tests/ fixtures → allowed
      },
    },
    {
      name: "tests-folder-is-private",
      comment:
        "A package's tests/ folder is reachable only from tests — nothing else may import fixtures.",
      severity: "error",
      from: { pathNot: `^${R}/[^/]+/tests/` }, // importer is not itself a test
      to: { path: `^${R}/[^/]+/tests/` },
    },
    {
      name: "no-circular",
      comment: "No dependency cycles. Scope to `^${R}/` if you want to allow cycles outside packages.",
      severity: "error",
      from: {},
      to: { circular: true },
    },

    // --- 分层（可选，默认关闭） ----------------------------------
    // 接口隐藏控制的是你如何导入（通过入口点）。
    // 分层控制的是哪些包可以依赖哪些包。在此添加你自己的规则，
    // 例如：
    //
    // {
    //   name: "ui-may-not-depend-on-billing",
    //   severity: "error",
    //   from: { path: `^${R}/ui/` },
    //   to:   { path: `^${R}/billing/` },
    // },
  ],
  options: {
    doNotFollow: { path: "node_modules" },
    tsConfig: { fileName: "tsconfig.json" },
    enhancedResolveOptions: {
      extensions: [".ts", ".tsx", ".js", ".jsx", ".json"],
    },
  },
};
