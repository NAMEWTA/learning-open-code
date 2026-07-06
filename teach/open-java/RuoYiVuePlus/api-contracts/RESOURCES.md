# ruoyi-api 模块 Resources

> 本仓库已逐文件核对，**第一信任源是仓库代码本身**。以下外部资源用于补充框架原理。

## Knowledge

- [代码: `ruoyi-api/pom.xml` — 模块唯一依赖](RuoYi-Vue-Plus/ruoyi-api/pom.xml)
  整个模块只依赖 `ruoyi-common-core`，这是依赖倒置的物理证据。理解模块在依赖树中的位置时直接看这里。
- [代码: `ruoyi-system` 中的 `SysUserServiceImpl` — 主要实现方](RuoYi-Vue-Plus/ruoyi-modules/ruoyi-system/src/main/java/org/dromara/system/service/impl/SysUserServiceImpl.java)
  `implements ISysUserService, UserService`，同时实现系统内部接口和 api 公共服务接口。理解「一个类挂两个接口」的模式时查阅。
- [代码: `ruoyi-workflow` 中的 `FlwTaskAssigneeServiceImpl` — 主要消费方](RuoYi-Vue-Plus/ruoyi-modules/ruoyi-workflow/src/main/java/org/dromara/workflow/service/impl/FlwTaskAssigneeServiceImpl.java)
  通过 `private final UserService userService`（Lombok `@RequiredArgsConstructor` 注入）消费 api 接口，无需知道实现类。理解「消费者视角」时查阅。
- [代码: `common-translation` 中的 `UserNameTranslationImpl` — 框架层消费方](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-translation/src/main/java/org/dromara/common/translation/core/impl/UserNameTranslationImpl.java)
  `@TranslationType` + `private final UserService` 的典型使用。理解「为什么 common 层也需要 api」时查阅。
- [代码: `TestLeaveServiceImpl` 中的 `@EventListener` — 事件解耦示例](RuoYi-Vue-Plus/ruoyi-modules/ruoyi-workflow/src/main/java/org/dromara/workflow/service/impl/TestLeaveServiceImpl.java)
  演示了业务模块如何通过监听 `ProcessEvent`/`ProcessTaskEvent`/`ProcessDeleteEvent` 响应流程变化，而不需要引入流程引擎依赖。
- [官方文档: _RuoYi-Vue-Plus 官方文档_ — Lion Li（plus-doc）](https://plus-doc.dromara.org/)
  理解项目整体模块划分、`ruoyi-api` 的设计定位时查阅「模块说明」章节。
- [经典: _依赖倒置原则 (DIP)_ — Robert C. Martin](https://en.wikipedia.org/wiki/Dependency_inversion_principle)
  本模块的核心设计思想来自 DIP：「高层模块不应依赖低层模块，两者都应依赖抽象」。`ruoyi-api` 就是这个抽象。

## Wisdom (Communities)

- [社区: _Dromara 开源社区 / RuoYi-Vue-Plus Issues_](https://gitee.com/dromara/RuoYi-Vue-Plus)
  模块划分的讨论、循环依赖的规避实践在 Issues 中常有涉及。

## Gaps
- 暂无显著缺口。所有 Success 项均可由仓库代码支撑。
