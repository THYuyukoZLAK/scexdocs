# 怀旧向子服「Legacy Genesis」更新日志

> 来源：Monarch 本地发布记录与历史归档 · 内容时间：2026-08-31T09:25:35+08:00

## 1.0.37

发布时间记录：2026-08-31T09:25:35+08:00

[更新] SCEX Legacy Genesis 已发布新版本 1.0.37
上一版本：1.0.36

本版说明：
  - 修复 Jade 不显示 AE2 设备在线状态；本版只强制同步对应 Jade 插件开关，覆盖前更新器仍会自动备份。
  - 新增 Woot Revived、RE:Constructed Wands（KOTS 兼容复刻）与 Polymorphic Energistics。
  - 修复石英粉碎与高纯玫瑰石英动力锯的重复配方，统一石英粉、铁粒与硅块标签。
  - 机械动力扳手加入 FTB 连锁严格排除清单，避免扳手拆卸与连锁同时触发造成物品丢失。
  - 请完全退出 Minecraft 后运行更新器；更新器保留玩家额外模组、存档和其他个性配置。

本次变更：
  Mod 新增（3 个）：
    + [建筑法杖：KOTS兼容复刻] constructionwand-kots-1.21.1-2.16.12.jar
    + [刷怪工厂] woot-revived-21.1.1.10-kjs.jar
    + [AE2多配方兼容] polyeng-0.4.1.jar
  其他 新增（6 项）：
    + kubejs/data/c/tags/block/storage_blocks/silicon.json
    + kubejs/data/c/tags/item/dusts/quartz.json
    + kubejs/data/c/tags/item/nuggets/iron.json
    + kubejs/data/c/tags/item/storage_blocks/silicon.json
    + kubejs/data/ftbultimine/tags/item/excluded_tools/strict.json
    + kubejs/server_scripts/scex_recipe_conflict_fixes.js
  强制同步（覆盖前自动备份）：
    ! config/voxy-config.json
    ! config/viscript_shop_config.toml
    ! resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
    ! resourcepacks/SCEX-任务图片资源包.zip
    ! config/dlc_manager/config.dc
    ! mods/[强制汉化资源] SCEX-Localization-1.0.0-neoforge-1.21.1.jar
    ! mods/[应用能源2：水晶科学] ae2cs-1.21.1-1.2.1.jar
    ! mods/[应用能源2：JEI联动] ae2jeiintegration-1.2.1.jar
    ! mods/Just-Enough-Botania-NeoForge-1.21.1-1.0.0-scex.1.jar
    ! mods/SCEX-SJAP-Compat-1.0.0.jar
    ! mods/[分子重组仪：怀旧渲染] MolecularTransformer-LegacyRenderer-1.0.6.jar
    ! resourcepacks/IndustrialCraft-Nostalgia-for-SingularityIteration-1.0.6.zip
    … 以及另外 13 项

玩家可运行同步脚本自动更新。服务器：scex.aerohakugyokurou.top:25566

## 1.0.36

发布时间记录：2026-08-30T21:45:53+08:00

[更新] SCEX Legacy Genesis 已发布新版本 1.0.36
上一版本：1.0.35

本版说明：
  - 新增 KubeJS 2101.7.2-build.374 与 Rhino 2101.2.7-build.81，作为服务器定制内容基础组件。
  - 新增实体货币与钱夹，可兑换为 ViScriptShop 商店余额。
  - 部署新版商店数据与任务内容，加入商店引导、阶段解锁与货币奖励。
  - 请完全退出 Minecraft 后运行更新器；更新器保留玩家额外模组、存档和个性配置。

本次变更：
  Mod 新增（2 个）：
    + [脚本系统] kubejs-neoforge-2101.7.2-build.374.jar
    + [JavaScript引擎] rhino-2101.2.7-build.81.jar
  其他 新增（8 项）：
    + kubejs/assets/kubejs/textures/block/example_block.png
    + kubejs/assets/kubejs/textures/item/example_item.png
    + kubejs/assets/scex/textures/item/coin_1.png
    + kubejs/assets/scex/textures/item/coin_2.png
    + kubejs/assets/scex/textures/item/coin_3.png
    + kubejs/assets/scex/textures/item/coin_bag.png
    + kubejs/server_scripts/coin.js
    + kubejs/startup_scripts/coin.js
  强制同步（覆盖前自动备份）：
    ! config/voxy-config.json
    ! config/viscript_shop_config.toml
    ! resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
    ! resourcepacks/SCEX-任务图片资源包.zip
    ! config/dlc_manager/config.dc
    ! mods/[强制汉化资源] SCEX-Localization-1.0.0-neoforge-1.21.1.jar
    ! mods/[应用能源2：水晶科学] ae2cs-1.21.1-1.2.1.jar
    ! mods/[应用能源2：JEI联动] ae2jeiintegration-1.2.1.jar
    ! mods/Just-Enough-Botania-NeoForge-1.21.1-1.0.0-scex.1.jar
    ! mods/SCEX-SJAP-Compat-1.0.0.jar
    ! mods/[分子重组仪：怀旧渲染] MolecularTransformer-LegacyRenderer-1.0.6.jar
    ! resourcepacks/IndustrialCraft-Nostalgia-for-SingularityIteration-1.0.6.zip
    … 以及另外 9 项

玩家可运行同步脚本自动更新。服务器：scex.aerohakugyokurou.top:25566

## 1.0.35

发布时间记录：2026-08-30T12:24:22+08:00

[更新] SCEX Legacy Genesis 已发布新版本 1.0.35
上一版本：1.0.34

本版说明：
  - 升级奇点迭代至 0.1.7.5-beta。
  - 新增 SCEX 永恒常春藤 0.2.0-core，支持将永恒常春藤附着到可修复物品并消耗植物魔法魔力进行修复。
  - 新增 ExtendedAE 1.21-2.2.35-neoforge 与 ME Requester 1.21.1-1.4.3，扩展 AE2 样板供应与库存请求功能。
  - 更新分子重组仪怀旧渲染器至 1.0.6，适配 SI 0.1.7.5-beta。
  - 新增 AppliedFlux 1.21-2.1.5-neoforge，提供 AE2 能源存储单元。
  - 客户端发行源移除重复的 Curios 9.0.15，仅保留与服务端一致的 Curios 9.5.1。
  - 请完全退出 Minecraft 后运行更新器；更新器保留玩家额外模组、存档和个性配置。

本次变更：
  Mod 升级（1 个）：
    ~ [分子重组仪：怀旧渲染] MolecularTransformer-LegacyRenderer：1.0.5 → 1.0.6
  Mod 新增（1 个）：
    + [AppliedFlux] AppliedFlux-1.21-2.1.5-neoforge.jar
  强制同步（覆盖前自动备份）：
    ! config/voxy-config.json
    ! config/viscript_shop_config.toml
    ! resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
    ! resourcepacks/SCEX-任务图片资源包.zip
    ! config/dlc_manager/config.dc
    ! mods/[强制汉化资源] SCEX-Localization-1.0.0-neoforge-1.21.1.jar
    ! mods/[应用能源2：水晶科学] ae2cs-1.21.1-1.2.1.jar
    ! mods/[应用能源2：JEI联动] ae2jeiintegration-1.2.1.jar
    ! mods/Just-Enough-Botania-NeoForge-1.21.1-1.0.0-scex.1.jar
    ! mods/SCEX-SJAP-Compat-1.0.0.jar
    ! mods/[分子重组仪：怀旧渲染] MolecularTransformer-LegacyRenderer-1.0.6.jar
    ! resourcepacks/IndustrialCraft-Nostalgia-for-SingularityIteration-1.0.6.zip
    … 以及另外 6 项

玩家可运行同步脚本自动更新。服务器：scex.aerohakugyokurou.top:25566

## 1.0.34

发布时间记录：2026-08-30T11:28:55+08:00

[更新] SCEX Legacy Genesis 已发布新版本 1.0.34
上一版本：1.0.33

本版说明：
  - 升级奇点迭代至 0.1.7.5-beta。
  - 新增 SCEX 永恒常春藤 0.2.0-core，支持将永恒常春藤附着到可修复物品并消耗植物魔法魔力进行修复。
  - 新增 ExtendedAE 1.21-2.2.35-neoforge 与 ME Requester 1.21.1-1.4.3，扩展 AE2 样板供应与库存请求功能。
  - 客户端发行源移除重复的 Curios 9.0.15，仅保留与服务端一致的 Curios 9.5.1。
  - 请完全退出 Minecraft 后运行更新器；更新器保留玩家额外模组、存档和个性配置。

本次变更：
  Mod 版本变更（方向无法判断）（1 个）：
    ~ [奇点迭代] SingularityIteration-0.1.7.3.1-scex-dsfix.jar → [SI] SingularityIteration-0.1.7.5-beta.jar
  Mod 新增（2 个）：
    + [ME请求器] MERequester-NeoForge-1.21.1-1.4.3.jar
    + SCEX-Timeless-Ivy-1.21.1-0.2.0-core.jar
  Mod 删除（1 个）：
    - [饰品栏API] curios-neoforge-9.0.15+1.21.1.jar
  强制同步（覆盖前自动备份）：
    ! config/voxy-config.json
    ! config/viscript_shop_config.toml
    ! resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
    ! resourcepacks/SCEX-任务图片资源包.zip
    ! config/dlc_manager/config.dc
    ! mods/[强制汉化资源] SCEX-Localization-1.0.0-neoforge-1.21.1.jar
    ! mods/[应用能源2：水晶科学] ae2cs-1.21.1-1.2.1.jar
    ! mods/[应用能源2：JEI联动] ae2jeiintegration-1.2.1.jar
    ! mods/Just-Enough-Botania-NeoForge-1.21.1-1.0.0-scex.1.jar
    ! mods/SCEX-SJAP-Compat-1.0.0.jar
    ! mods/[分子重组仪：怀旧渲染] MolecularTransformer-LegacyRenderer-1.0.5.jar
    ! resourcepacks/IndustrialCraft-Nostalgia-for-SingularityIteration-1.0.6.zip
    … 以及另外 5 项

玩家可运行同步脚本自动更新。服务器：scex.aerohakugyokurou.top:25566

## 1.0.33

发布时间记录：2026-08-29T22:13:03+08:00

[更新] SCEX Legacy Genesis 已发布新版本 1.0.33
上一版本：1.0.32

本版说明：
  - 1.0.32 客户端包在发布后复核发现压缩完整性问题，现以 1.0.33 重新打包发布。
  - 修复森林法杖 Shift+右键魔力池时 ExtraBotany 与 Botania 456 的声音字段兼容崩溃；本版 JAR 已通过完整 ZIP 校验。
  - 请完全退出 Minecraft 后运行更新器；更新器保留玩家额外模组、存档和配置。若仍有问题，请上传新的崩溃报告和更新器完整输出。

本次变更：
  Mod 更新（1 个）：
    ~ [额外植物学：重燃] extrabotany-neoforge-1.21.1-2.0-SNAPSHOT-patched.jar
  强制同步（覆盖前自动备份）：
    ! config/voxy-config.json
    ! config/viscript_shop_config.toml
    ! resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
    ! resourcepacks/SCEX-任务图片资源包.zip
    ! config/dlc_manager/config.dc
    ! mods/[强制汉化资源] SCEX-Localization-1.0.0-neoforge-1.21.1.jar
    ! mods/[应用能源2：水晶科学] ae2cs-1.21.1-1.2.1.jar
    ! mods/[应用能源2：JEI联动] ae2jeiintegration-1.2.1.jar
    ! mods/Just-Enough-Botania-NeoForge-1.21.1-1.0.0-scex.1.jar
    ! mods/SCEX-SJAP-Compat-1.0.0.jar
    ! mods/[奇点迭代] SingularityIteration-0.1.7.3.1-scex-dsfix.jar
    ! mods/[分子重组仪：怀旧渲染] MolecularTransformer-LegacyRenderer-1.0.5.jar
    … 以及另外 2 项

玩家可运行同步脚本自动更新。服务器：scex.aerohakugyokurou.top:25566

## 1.0.32

发布时间记录：2026-08-29T22:05:24+08:00

[更新] SCEX Legacy Genesis 已发布新版本 1.0.32
上一版本：1.0.31

本版说明：
  - 修复怀旧服客户端使用森林法杖 Shift+右键魔力池时的崩溃：ExtraBotany 与 Botania 456 的声音字段兼容性已修正。
  - 服务端与客户端使用同一修复 JAR，玩家请退出游戏后运行更新器获取；不删除玩家额外模组、存档或配置。
  - 若仍遇到崩溃，请上传最新崩溃报告和更新器完整输出。

本次变更：
  Mod 更新（1 个）：
    ~ [额外植物学：重燃] extrabotany-neoforge-1.21.1-2.0-SNAPSHOT-patched.jar
  强制同步（覆盖前自动备份）：
    ! config/voxy-config.json
    ! config/viscript_shop_config.toml
    ! resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
    ! resourcepacks/SCEX-任务图片资源包.zip
    ! config/dlc_manager/config.dc
    ! mods/[强制汉化资源] SCEX-Localization-1.0.0-neoforge-1.21.1.jar
    ! mods/[应用能源2：水晶科学] ae2cs-1.21.1-1.2.1.jar
    ! mods/[应用能源2：JEI联动] ae2jeiintegration-1.2.1.jar
    ! mods/Just-Enough-Botania-NeoForge-1.21.1-1.0.0-scex.1.jar
    ! mods/SCEX-SJAP-Compat-1.0.0.jar
    ! mods/[奇点迭代] SingularityIteration-0.1.7.3.1-scex-dsfix.jar
    ! mods/[分子重组仪：怀旧渲染] MolecularTransformer-LegacyRenderer-1.0.5.jar
    … 以及另外 2 项

玩家可运行同步脚本自动更新。服务器：scex.aerohakugyokurou.top:25566

## 1.0.31

发布时间记录：2026-08-29T13:32:43+08:00

[更新] SCEX Legacy Genesis 已发布新版本 1.0.31
上一版本：1.0.30

本版说明：
  - 新增 BotaniaJEI 1.0.0-scex.1：在 JEI 中显示 Botania 配方的魔力数值和纯净雏菊处理时间。
  - 新增 SCEX-SJAP-Compat 1.0.0：补齐大地之刃与西风太刀的定义、模型、配方和中英文名；客户端与服务端同版。
  - 本次维护包含怀旧服服务端停服、备份和健康检查；玩家退出游戏后运行更新器即可获取客户端文件。
  - 同步器继续保留玩家额外模组、资源包、配置和本地删除状态，不清理玩家数据。

本次变更：
  Mod 新增（2 个）：
    + Just-Enough-Botania-NeoForge-1.21.1-1.0.0-scex.1.jar
    + SCEX-SJAP-Compat-1.0.0.jar
  强制同步（覆盖前自动备份）：
    ! config/voxy-config.json
    ! config/viscript_shop_config.toml
    ! resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
    ! resourcepacks/SCEX-任务图片资源包.zip
    ! config/dlc_manager/config.dc
    ! mods/[强制汉化资源] SCEX-Localization-1.0.0-neoforge-1.21.1.jar
    ! mods/[应用能源2：水晶科学] ae2cs-1.21.1-1.2.1.jar
    ! mods/[应用能源2：JEI联动] ae2jeiintegration-1.2.1.jar
    ! mods/Just-Enough-Botania-NeoForge-1.21.1-1.0.0-scex.1.jar
    ! mods/SCEX-SJAP-Compat-1.0.0.jar
    ! mods/[奇点迭代] SingularityIteration-0.1.7.3.1-scex-dsfix.jar
    ! mods/[分子重组仪：怀旧渲染] MolecularTransformer-LegacyRenderer-1.0.5.jar
    … 以及另外 1 项

玩家可运行同步脚本自动更新。服务器：scex.aerohakugyokurou.top:25566

## 1.0.30

发布时间记录：2026-08-29T08:53:02+08:00

[更新] SCEX Legacy Genesis 已发布新版本 1.0.30
上一版本：1.0.29

本版说明：
  - 新增 Inventory Profiles Next 2.2.5：提供背包整理、物品移动和自动重装等客户端便利功能。
  - 同步新增必需前置 libIPN 6.6.3；现有 Kotlin for Forge 5.12.0 满足加载要求。
  - 按整合包预设关闭“自动重装 → 在启用的槽位上显示图标”，避免槽位左上角出现额外提示图标。
  - 该设置只作为首次安装默认值下发，不永久覆盖玩家之后的个人配置。
  - 本次仅更新玩家客户端和 18088 清单，不需要重启怀旧服；退出游戏后运行更新器并重新启动客户端即可。

本次变更：
  Mod 新增（2 个）：
    + [背包整理] InventoryProfilesNext-neoforge-1.21.1-2.2.5.jar
    + [背包整理前置库] libIPN-neoforge-1.21.1-6.6.3.jar
  配置 新增（1 项）：
    + config/inventoryprofiles.json
  强制同步（覆盖前自动备份）：
    ! config/voxy-config.json
    ! config/viscript_shop_config.toml
    ! resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
    ! resourcepacks/SCEX-任务图片资源包.zip
    ! config/dlc_manager/config.dc
    ! mods/[强制汉化资源] SCEX-Localization-1.0.0-neoforge-1.21.1.jar
    ! mods/[应用能源2：水晶科学] ae2cs-1.21.1-1.2.1.jar
    ! mods/[应用能源2：JEI联动] ae2jeiintegration-1.2.1.jar
    ! mods/[奇点迭代] SingularityIteration-0.1.7.3.1-scex-dsfix.jar
    ! mods/[分子重组仪：怀旧渲染] MolecularTransformer-LegacyRenderer-1.0.5.jar
    ! resourcepacks/IndustrialCraft-Nostalgia-for-SingularityIteration-1.0.6.zip

玩家可运行同步脚本自动更新。服务器：scex.aerohakugyokurou.top:25566

## 1.0.29

发布时间记录：2026-08-29T00:11:34+08:00

[更新] SCEX Legacy Genesis 已发布新版本 1.0.29
上一版本：1.0.28

本版说明：
  - 新增 AE2 Crystal Science 1.2.1 与 AE2 JEI Integration 1.2.1；已按现有 AE2 19.2.17、JEI 19.44.0.405、NeoForge 21.1.248 核对依赖范围。
  - 奇点迭代由 0.1.7.1 更新至 0.1.7.3.1 SCEX 专服热修版；修复上游 0.1.7.3 在专用服务端误加载客户端类导致的启动崩溃。
  - 分子重组仪怀旧渲染同步更新至 1.0.5，依赖已精确匹配奇点迭代专服热修版。
  - 工业复古材质包更新至 1.0.6 并由更新器强制启用；任务数据与任务图片资源包同步替换为下载目录的新版本。
  - QQ 公告链路改为 UTF-8 文件传递，避免 Windows PowerShell 到 WSL 的标准输入代码页转换导致中文乱码。
  - 本版包含服务端内容模组与任务数据更新；完成维护并退出游戏后重新启动客户端再进入服务器。

本次变更：
  Mod 升级（2 个）：
    ~ [分子重组仪：怀旧渲染] MolecularTransformer-LegacyRenderer：1.0.3 → 1.0.5
    ~ [奇点迭代] SingularityIteration：0.1.7.1-beta → 0.1.7.3.1-scex-dsfix
  Mod 新增（2 个）：
    + [应用能源2：水晶科学] ae2cs-1.21.1-1.2.1.jar
    + [应用能源2：JEI联动] ae2jeiintegration-1.2.1.jar
  其他 新增（1 项）：
    + resourcepacks/IndustrialCraft-Nostalgia-for-SingularityIteration-1.0.6.zip
  其他 更新（1 项）：
    ~ resourcepacks/SCEX-任务图片资源包.zip
  其他 删除（1 项）：
    - resourcepacks/IndustrialCraft-Nostalgia-for-SingularityIteration-1.0.5.zip
  强制同步（覆盖前自动备份）：
    ! config/voxy-config.json
    ! config/viscript_shop_config.toml
    ! resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
    ! resourcepacks/SCEX-任务图片资源包.zip
    ! config/dlc_manager/config.dc
    ! mods/[强制汉化资源] SCEX-Localization-1.0.0-neoforge-1.21.1.jar
    ! mods/[应用能源2：水晶科学] ae2cs-1.21.1-1.2.1.jar
    ! mods/[应用能源2：JEI联动] ae2jeiintegration-1.2.1.jar
    ! mods/[奇点迭代] SingularityIteration-0.1.7.3.1-scex-dsfix.jar
    ! mods/[分子重组仪：怀旧渲染] MolecularTransformer-LegacyRenderer-1.0.5.jar
    ! resourcepacks/IndustrialCraft-Nostalgia-for-SingularityIteration-1.0.6.zip

玩家可运行同步脚本自动更新。服务器：scex.aerohakugyokurou.top:25566

## 1.0.28

发布时间记录：2026-08-28T23:07:13+08:00

[更新] SCEX Legacy Genesis 已发布新版本 1.0.28
上一版本：1.0.27

本版说明：
  - 修复汉化资源包已下载但未实际启用的问题：新增 SCEX 强制汉化资源伴生模组，翻译现在随 NeoForge 的 mod_resources 自动加载，不再只依赖玩家资源包列表。
  - 更新器会补建缺失的 options.txt、固定简体中文，并再次校正汉化包优先级；已有玩家其他资源包仍然保留。
  - 精确清理一个重复的 0Pack2Reload、无效的 Fabric 版自动汉化更新器，以及误放在 mods 目录中的 75 MB 整包；不会删除玩家自行添加的其他模组。
  - Relics 0.12.8 的 547 个翻译键已逐项覆盖；更新完成后必须完整退出游戏进程再重新启动。

本次变更：
  Mod 新增（1 个）：
    + [强制汉化资源] SCEX-Localization-1.0.0-neoforge-1.21.1.jar
  其他 更新（2 项）：
    ~ _updater/player-update-generic.ps1
    ~ _updater/player-update-generic.py
  Mod 删除（3 个）：
    - [重复件：资源包惰性重载] 0Pack2Reload-NeoForge-1.21.1-1.0.1.jar
    - [自动汉化更新] I18nUpdateMod-3.7.0-all.jar
    - [SCEX资源包] scex legacy genesis ver1.0.zip
  强制同步（覆盖前自动备份）：
    ! config/voxy-config.json
    ! config/viscript_shop_config.toml
    ! resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
    ! resourcepacks/SCEX-任务图片资源包.zip
    ! config/dlc_manager/config.dc
    ! mods/[强制汉化资源] SCEX-Localization-1.0.0-neoforge-1.21.1.jar

玩家可运行同步脚本自动更新。服务器：scex.aerohakugyokurou.top:25566

## 1.0.27

发布时间记录：2026-08-28T17:22:09+08:00

[更新] SCEX Legacy Genesis 已发布新版本 1.0.27
上一版本：1.0.26

本版说明：
  - 新增 Applied Create 1.1.7（应用机械动力），在机械动力与应用能源 2 之间提供应力存储、P2P 通道、样板供应器等联动内容。
  - 该模组为双端内容模组，服务器与玩家客户端必须同时安装；Create 6.0.10、AE2 19.2.17 和 Kotlin for Forge 5.12.0 前置均已满足。
  - 1.0.27 同时包含 1.0.26 的神秘系六 MOD 更新；未运行上一版更新器的玩家可以直接更新到本版。
  - 更新完成后请完整退出游戏再重新启动。

本次变更：
  Mod 新增（1 个）：
    + [应用机械动力] appliedcreate-1.21.1-1.1.7.jar
  强制同步（覆盖前自动备份）：
    ! config/voxy-config.json
    ! config/viscript_shop_config.toml
    ! resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
    ! resourcepacks/SCEX-任务图片资源包.zip
    ! config/dlc_manager/config.dc

玩家可运行同步脚本自动更新。服务器：scex.aerohakugyokurou.top:25566

## 1.0.26

发布时间记录：2026-08-28T17:18:04+08:00

[更新] SCEX Legacy Genesis 已发布新版本 1.0.26
上一版本：1.0.25

本版说明：
  - 神秘系六 MOD 更新为 2026-08-28 同批构建：神秘时代 port.238、神秘工匠 port.59、禁忌魔法 port.26，并同步替换节点机制、污秽魔法和天界神秘学的同批哈希版本。
  - 修复 BUG 站 #315–#325 中的通用黑染料与木材标签、法杖末端 Vis 抽取、蕴魔石显示、地狱火蝠行为、村庄池兼容等问题，并确认 #313 的 JEI 虚拟要素输入撤回无残留。
  - 更新器会精确备份并移除上一版神秘时代 port.237、神秘工匠 port.58、禁忌魔法 port.25；不会删除玩家自行添加的其他模组。
  - 六个 JAR 必须成套更新，禁止新旧版本共存；更新完成后请完整退出游戏再重新启动。

本次变更：
  Mod 升级（3 个）：
    ~ [禁忌魔法] forbiddenmagic-1.0.0：port.25 → port.26
    ~ [神秘工匠] thaumic_tinkerer-1.0.0：port.58 → port.59
    ~ [神秘时代] thaumcraft-0.2.2.95：port.237 → port.238
  Mod 更新（3 个）：
    ~ [节点机制] nodalmechanics-1.0.0-port.6.jar
    ~ [天界神秘学] thaumcraftcelestial-1.0.0-port.24.jar
    ~ [污秽魔法] taintedmagic-1.0.0-port.29.jar
  强制同步（覆盖前自动备份）：
    ! config/voxy-config.json
    ! config/viscript_shop_config.toml
    ! resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
    ! resourcepacks/SCEX-任务图片资源包.zip
    ! config/dlc_manager/config.dc

玩家可运行同步脚本自动更新。服务器：scex.aerohakugyokurou.top:25566

## 1.0.25

发布时间记录：2026-08-28T15:41:57+08:00

[更新] SCEX Legacy Genesis 已发布新版本 1.0.25
上一版本：1.0.24

本版说明：
  - 新增 DLC Manager 优化模组中心：42 个条目按核心稳定、渲染帧率、网络响应、模组专项、诊断兼容和实验功能分类，并提供完整中文名称与用途说明。
  - 保持当前优化模组启用状态不变；新增 SCEX 推荐、低配稳定、高端远景（实验）和性能诊断 4 套预设，钠与 Cupboard 等前置可自动联动。
  - 实验或预发布优化会在开启前警告；隐藏“全部开启”、路径配置和玩家端服务器管理入口，关闭 API 与自更新，避免误操作。
  - 清理 5 个已确认的旧版或内容重复客户端优化 JAR；同步器仅定向处理这些文件，仍保留玩家自行添加的额外模组及其 DLC 开关状态。
  - DLC 切换会在下次完整启动游戏后生效；更新完成后请退出启动器中的游戏进程再重新启动。

本次变更：
  其他 新增（88 项）：
    + DLC/00-隐藏前置/[Cupboard前置库] cupboard-1.21.1-4.0.jar
    + DLC/01-核心稳定/[光速加载] lightspeed-1.21.1-1.2.3.jar
    + DLC/01-核心稳定/[锂优化] lithium-neoforge-0.15.4+mc1.21.1.jar
    + DLC/01-核心稳定/[内存泄漏修复] alltheleaks-1.1.12+1.21.1-neoforge.jar
    + DLC/01-核心稳定/[轻量加载] lightload-neo-1.0.1fix.jar
    + DLC/01-核心稳定/[世界生成特征修复] worldgenfeaturefix-neoforge-1.21-1.0.1.jar
    + DLC/01-核心稳定/[属性修复] attributefix-neoforge-1.21.1-21.1.3.jar
    + DLC/01-核心稳定/[随意优化] randomoptimization-1.7.4-all.jar
    + DLC/01-核心稳定/[铁氧体磁芯] ferritecore-7.0.3-neoforge.jar
    + DLC/01-核心稳定/[现代化修复] modernfix-neoforge-5.27.20+mc1.21.1.jar
    + DLC/01-核心稳定/[重复实体UUID修复] deuf-1.21.1-1.3.jar
    + DLC/02-渲染与帧率/[更佳群系色彩过渡] betterbiomeblend-neoforge-1.21.1-1.4.1.jar
    … 以及另外 76 项
  配置 更新（1 项）：
    ~ config/dlc_manager/config.dc
  Mod 删除（5 个）：
    - [立即加速] ImmediatelyFast-NeoForge-1.6.11+1.21.1.jar
    - [重复件：铁氧体磁芯] ferritecore-7.0.3-neoforge.jar
    - [重复件：现代化修复] modernfix-neoforge-5.27.20+mc1.21.1.jar
    - [重复件：异步粒子] AsyncParticles-21.1.4.0-beta.3+1.21.1.jar
    - [重复实体UUID修复] deuf-1.21.1-1.0.jar
  强制同步（覆盖前自动备份）：
    ! config/voxy-config.json
    ! config/viscript_shop_config.toml
    ! resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
    ! resourcepacks/SCEX-任务图片资源包.zip
    ! config/dlc_manager/config.dc

玩家可运行同步脚本自动更新。服务器：scex.aerohakugyokurou.top:25566

## 1.0.24

发布时间记录：2026-08-28T08:14:53+08:00

[更新] SCEX Legacy Genesis 已发布新版本 1.0.24
上一版本：1.0.23

本版说明：
  - 更新任务图片资源包，新增任务增强装饰线、TC 背景与返回页图片；该资源包继续强制校验并同步。
  - 新增饮食多样性奖励 Spice of Life: Carrot Edition 1.16.6，客户端与服务端保持同版。
  - 服务端加入《月之风土记》可靠首次发放修复：新 UUID 首登只发 1 本，同 UUID 重登、丢书、死亡或重启后不补发，老玩家不新增。
  - 玩家同步器会先备份被覆盖文件，并保留玩家自行添加或修改的额外模组。更新后请完全退出并重新启动游戏。

本次变更：
  Mod 新增（1 个）：
    + [饮食多样性奖励] solcarrot-1.21.1-1.16.6.jar
  其他 更新（1 项）：
    ~ resourcepacks/SCEX-任务图片资源包.zip
  强制同步（覆盖前自动备份）：
    ! config/voxy-config.json
    ! config/viscript_shop_config.toml
    ! resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
    ! resourcepacks/SCEX-任务图片资源包.zip

玩家可运行同步脚本自动更新。服务器：scex.aerohakugyokurou.top:25566

## 1.0.23

发布时间记录：2026-08-27T22:36:29+08:00

[更新] SCEX Legacy Genesis 已发布新版本 1.0.23
上一版本：1.0.22

本版说明：
  - 用 Visual Keybinder 0.1.13 替换 Keybind Atlas 1.4.0，提供更直观的键盘、鼠标按键占用与冲突查看界面。
  - 补充 Visual Keybinder 的简体中文按键名称、预设切换和结果提示；汉化资源包会强制校验并同步。
  - 更新器只会备份并移除上一版清单中未被改动的旧 Keybind Atlas；玩家自行添加或修改过的额外模组不会被删除。更新后请完全退出并重新启动游戏。

本次变更：
  Mod 新增（1 个）：
    + [可视化按键绑定] visual_keybinder-1.21.1-0.1.13-neoforge.jar
  其他 更新（1 项）：
    ~ resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
  Mod 删除（1 个）：
    - [按键图谱] KeybindAtlas-v1.4.0-mc1.21.1-neoforge.jar
  配置 删除（1 项）：
    - config/keybindatlas-client.toml
  强制同步（覆盖前自动备份）：
    ! config/voxy-config.json
    ! config/viscript_shop_config.toml
    ! resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
    ! resourcepacks/SCEX-任务图片资源包.zip

玩家可运行同步脚本自动更新。服务器：scex.aerohakugyokurou.top:25566

## 1.0.22

发布时间记录：2026-08-27T22:00:21+08:00

[更新] SCEX Legacy Genesis 已发布新版本 1.0.22
上一版本：1.0.21

本版说明：
  - 怀旧服任务书已按服主要求整体替换为新的神秘时代任务章节；旧任务配置与玩家任务进度均已单独备份，可完整回滚。
  - 新增“SCEX-任务图片资源包”，补齐任务页使用的书页与 Vis 图片；更新器会下载、校验并自动启用该资源包。
  - 同步保存任务文本颜色与格式规范，后续任务扩写统一沿用同一套标记规则。

本次变更：
  其他 新增（1 项）：
    + resourcepacks/SCEX-任务图片资源包.zip
  强制同步（覆盖前自动备份）：
    ! config/voxy-config.json
    ! config/viscript_shop_config.toml
    ! resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
    ! resourcepacks/SCEX-任务图片资源包.zip

玩家可运行同步脚本自动更新。服务器：scex.aerohakugyokurou.top:25566

## 1.0.21

发布时间记录：2026-08-27T20:59:59+08:00

[更新] SCEX Legacy Genesis 已发布新版本 1.0.21
上一版本：1.0.20

本版说明：
  - 恢复分子重组仪中央工作区的原版半透明玻璃效果，并调整绘制顺序，让工作特效能从玻璃后正确显现。
  - 补齐 ASP 十盒体模型的纹理镜像设置，修正各部件表面的贴图方向。
  - 保留工作态等离子与粒子动画，并确保物品栏、主副手及掉落物渲染继续正常；本更新仍仅需客户端。

本次变更：
  Mod 升级（1 个）：
    ~ [分子重组仪：怀旧渲染] MolecularTransformer-LegacyRenderer：1.0.2 → 1.0.3
  强制同步（覆盖前自动备份）：
    ! config/voxy-config.json
    ! config/viscript_shop_config.toml
    ! resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip

玩家可运行同步脚本自动更新。服务器：scex.aerohakugyokurou.top:25566

## 1.0.20

发布时间记录：2026-08-27T20:24:14+08:00

[更新] SCEX Legacy Genesis 已发布新版本 1.0.20
上一版本：1.0.19

本版说明：
  - 修复分子重组仪工作时等离子与粒子动画不显示的问题，并恢复 Advanced Solar Panels 原版动画颜色、帧序列与加法混合效果。
  - 修复分子重组仪在物品栏、手持与掉落状态下完全透明的问题，复用原版十盒体模型与物品显示变换。
  - 保留 1.0.1 的开放式模型遮挡、透光和环境光照修复；本更新仅客户端需要，请退出游戏后再同步更新。

本次变更：
  Mod 升级（1 个）：
    ~ [分子重组仪：怀旧渲染] MolecularTransformer-LegacyRenderer：1.0.1 → 1.0.2
  强制同步（覆盖前自动备份）：
    ! config/voxy-config.json
    ! config/viscript_shop_config.toml
    ! resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip

玩家可运行同步脚本自动更新。服务器：scex.aerohakugyokurou.top:25566

## 1.0.19

发布时间记录：2026-08-27T19:25:39+08:00

[更新] SCEX Legacy Genesis 已发布新版本 1.0.19
上一版本：1.0.18

本版说明：
  - 修复分子重组仪开放式模型与相邻方块连接时出现缺面、空洞的问题。
  - 修复分子重组仪机身受原整立方体遮光影响而明显发暗的问题。
  - 继续使用高级太阳能原始分子重组仪模型与动画；本次只调整客户端遮挡和环境光照。

本次变更：
  Mod 升级（1 个）：
    ~ [分子重组仪：怀旧渲染] MolecularTransformer-LegacyRenderer：1.0.0 → 1.0.1
  强制同步（覆盖前自动备份）：
    ! config/voxy-config.json
    ! config/viscript_shop_config.toml
    ! resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip

玩家可运行同步脚本自动更新。服务器：scex.aerohakugyokurou.top:25566

## 1.0.17

发布时间记录：2026-08-27T16:41:07+08:00

[更新] SCEX Legacy Genesis 已发布新版本 1.0.17
上一版本：1.0.16

本版说明：
  - 修正默认 options.txt 的资源包顺序，将服务器汉化包置于最高优先级。
  - 同步器会核验客户端语言与汉化包优先级；修正顺序后会提示完全退出并重启客户端。
  - Relics 仍为 0.12.8，汉化包内容不变；玩家自行添加的其他资源包继续保留。

本次变更：
  其他 更新（2 项）：
    ~ _updater/player-update-generic.ps1
    ~ _updater/player-update-generic.py
  强制同步（覆盖前自动备份）：
    ! config/voxy-config.json
    ! config/viscript_shop_config.toml
    ! resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip

玩家可运行同步脚本自动更新。服务器：scex.aerohakugyokurou.top:25566

## 1.0.16

发布时间记录：2026-08-27T16:12:48+08:00

[更新] SCEX Legacy Genesis 已发布新版本 1.0.16
上一版本：1.0.15

本版说明：
  - 修复服务器汉化包可能被误判为玩家自定义资源包、导致仍显示英文的问题。
  - 仅强制接管服务器专用汉化包；玩家自行添加的其他资源包继续保留。
  - 同步器会自动启用汉化包并置于最高优先级，修改 options.txt 前会创建备份。

本次变更：
  其他 更新（2 项）：
    ~ _updater/player-update-generic.ps1
    ~ _updater/player-update-generic.py
  强制同步（覆盖前自动备份）：
    ! config/voxy-config.json
    ! config/viscript_shop_config.toml
    ! resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip

玩家可运行同步脚本自动更新。服务器：scex.aerohakugyokurou.top:25566

## 1.0.15

发布时间记录：2026-08-27T16:01:06+08:00

[更新] SCEX Legacy Genesis 已发布新版本 1.0.15
上一版本：1.0.14

本版说明：
  - 新增轻松村民（Easy Villagers）1.1.42，已加入客户端发布源和独立服务端。
  - 该模组适配 Minecraft 1.21.1 / NeoForge 21.1.248，没有新增必装前置。
  - 全部模组使用中文分类文件名；同步器会先备份被替换的旧版文件，并保留玩家自行添加的额外模组。

本次变更：
  Mod 新增（1 个）：
    + [轻松村民] easy-villagers-neoforge-1.21.1-1.1.42.jar
  强制同步（覆盖前自动备份）：
    ! config/voxy-config.json
    ! config/viscript_shop_config.toml

玩家可运行同步脚本自动更新。服务器：scex.aerohakugyokurou.top:25566

## 1.0.14

发布时间记录：2026-08-27T13:43:07+08:00

[更新] SCEX Legacy Genesis 已发布新版本 1.0.14
上一版本：1.0.13

本版说明：
  - 新增高级战利品信息、FTB 跨模组兼容与 FTB 任务增强，并将 FTB Quests 从 2101.1.33 升级至 2101.1.34。
  - 新增快捷动作轮盘与 MC 百科搜索；这两项仅安装在客户端，不会放入独立服务端。
  - 新增 RTS 俯视建造与连锁破坏回溯，相关功能模组已同步至客户端和服务端待下次维护加载。
  - 全部模组使用中文分类文件名；同步器会先备份被替换的旧版文件，并保留玩家自行添加的额外模组。

本次变更：
  Mod 升级（1 个）：
    ~ [FTB 任务] ftb-quests-neoforge：2101.1.33 → 2101.1.34
  Mod 新增（7 个）：
    + [高级战利品信息] AdvancedLootInfo-neoforge-1.21.1-1.12.0.jar
    + [快捷动作轮盘] ezactions-neoforge-1.21.1-2.0.3.5.jar
    + [连锁破坏回溯] ultimine_rewind-2.1.0.jar
    + [FTB跨模组兼容] ftb-xmod-compat-neoforge-21.1.11.jar
    + [FTB任务增强] quest_enhance-1.21.1-neoforge-3.7.jar
    + [MC百科搜索] omnisearch-2.1.0.jar
    + [RTS俯视建造] rtsbuilding-neoforge-1.21.1-1.1.7.jar
  强制同步（覆盖前自动备份）：
    ! config/voxy-config.json
    ! config/viscript_shop_config.toml

玩家可运行同步脚本自动更新。服务器：scex.aerohakugyokurou.top:25566

## 1.0.13

发布时间记录：2026-08-27T12:25:27+08:00

[更新] SCEX Legacy Genesis 已发布新版本 1.0.13
上一版本：1.0.12

本版说明：
  - 开启 ViScriptShop 的 FTB Library 侧边栏商店按钮，玩家可从 FTB Library 界面直接打开商店。
  - 该配置列入强制同步项；更新器会先备份玩家原有配置，再写入开启状态。
  - 本次仅更新商店入口配置，不删除玩家自行添加的模组或其他本地内容。

本次变更：
  配置 新增（1 项）：
    + config/viscript_shop_config.toml
  强制同步（覆盖前自动备份）：
    ! config/voxy-config.json
    ! config/viscript_shop_config.toml

玩家可运行同步脚本自动更新。服务器：scex.aerohakugyokurou.top:25566

## 1.0.12

发布时间记录：2026-08-27T11:35:50+08:00

[更新] SCEX Legacy Genesis 已发布新版本 1.0.12
上一版本：1.0.11

本版说明：
  - 新增 FTB 物品筛选系统 21.1.4，可在支持该系统的机器与界面中配置更灵活的物品过滤规则。
  - 新增时装盔甲重制版 1.21.1-v1，可分别设置实际生效的护甲与外观护甲，并可隐藏盔甲显示。
  - 新增 ViScriptShop 1.2.0，并把其前置 LowDragLib2 从 2.2.36.a 升级至官方 2.2.37。
  - 三项功能模组均已同步至服务端与客户端，并使用中文分类文件名；同步器会先备份变更文件，玩家自行添加的额外模组仍会保留。

本次变更：
  Mod 升级（1 个）：
    ~ [LowDragLib2前置库] ldlib2-neoforge-1.21.1：2.2.36.a → 2.2.37
  Mod 新增（3 个）：
    + [脚本商店] ViScriptShop-neoforge-1.21.1-1.2.0.jar
    + [时装盔甲重制版] cosmeticarmorreworked-1.21.1-v1-neoforge.jar
    + [FTB物品筛选系统] ftb-filter-system-neoforge-21.1.4.jar
  强制同步（覆盖前自动备份）：
    ! config/voxy-config.json

玩家可运行同步脚本自动更新。服务器：scex.aerohakugyokurou.top:25566

## 1.0.11

发布时间记录：2026-08-27T10:48:26+08:00

[更新] SCEX Legacy Genesis 已发布新版本 1.0.11
上一版本：1.0.10

本版说明：
  - 神秘时代更新至 0.2.2.95-port.237，神秘工匠更新至 1.0.0-port.58；禁忌魔法、污秽魔法、节点机制和天界神秘学同步替换为同批次构建。
  - 本批修复 Lootr 战利品箱兼容、研究节点显示、活化工具台研究持久化和木台阶标签兼容，并精确回滚此前不合适的 JEI 要素安瓿输入改动。
  - 服务端与客户端六件套已统一哈希和中文文件名；同步器会先备份被替换文件，玩家自行添加的额外模组仍会保留。

本次变更：
  Mod 升级（2 个）：
    ~ [神秘工匠] thaumic_tinkerer-1.0.0：port.57 → port.58
    ~ [神秘时代] thaumcraft-0.2.2.95：port.236 → port.237
  Mod 更新（4 个）：
    ~ [节点机制] nodalmechanics-1.0.0-port.6.jar
    ~ [禁忌魔法] forbiddenmagic-1.0.0-port.25.jar
    ~ [天界神秘学] thaumcraftcelestial-1.0.0-port.24.jar
    ~ [污秽魔法] taintedmagic-1.0.0-port.29.jar
  强制同步（覆盖前自动备份）：
    ! config/voxy-config.json

玩家可运行同步脚本自动更新。服务器：scex.aerohakugyokurou.top:25566

## 1.0.10

发布时间记录：2026-08-27T10:02:18+08:00

[更新] SCEX Legacy Genesis 已发布新版本 1.0.10
上一版本：1.0.10

本版说明：
  - 全部客户端模组文件现已补充中文名称前缀，便于玩家识别用途；重复副本会明确标注为“重复件”。
  - 本次只调整文件名，模组 JAR 内容和版本没有变化；同步器会按哈希直接接管本地原文件，避免重复下载。
  - 改名前文件会进入 .portable-sync-backups，玩家自行添加的额外模组仍会保留，不会被清理。

本次变更：
  其他 更新（2 项）：
    ~ _updater/player-update-generic.ps1
    ~ _updater/player-update-generic.py
  强制同步（覆盖前自动备份）：
    ! config/voxy-config.json

玩家可运行同步脚本自动更新。服务器：scex.aerohakugyokurou.top:25566

## 1.0.9

发布时间记录：2026-08-27T09:02:49+08:00

[更新] SCEX Legacy Genesis 已发布新版本 1.0.9
上一版本：1.0.8

本版说明：
  - 修复部分玩家进入怀旧服时，Neo-Voxy 因本地 RocksDB 缓存初始化失败而导致的客户端崩溃。
  - 本版会强制同步 config/voxy-config.json，并暂时关闭 Voxy 远景功能；不会删除现有 .voxy 缓存，原配置如存在会先备份。
  - 同步器的完成统计现在会单列配置变更，并显示实际修改的配置文件；早苗公告也会附带本版说明和具体文件。

本次变更：
  其他 更新（2 项）：
    ~ _updater/player-update-generic.ps1
    ~ _updater/player-update-generic.py
  强制同步（覆盖前自动备份）：
    ! config/voxy-config.json

玩家可运行同步脚本自动更新。服务器：scex.aerohakugyokurou.top:25566

## 1.0.8

发布时间记录：2026-08-29T13:55:40+08:00

便携发布 1.0.8；文件数量 681。现有归档仅保留发布摘要，未保留逐项变更清单。

## 1.0.7

发布时间记录：2026-08-29T13:55:39+08:00

便携发布 1.0.7；文件数量 680。现有归档仅保留发布摘要，未保留逐项变更清单。

## 1.0.6

发布时间记录：2026-08-29T13:55:39+08:00

历史归档索引：SCEX Legacy Genesis 1.0.6。

现有 Monarch 发布目录未保留本版本的逐项变更清单；为避免臆造内容，本条仅保留版本号，待找到可核验公告或发布包后补充。

## 1.0.5

发布时间记录：2026-08-29T13:55:39+08:00

历史归档索引：SCEX Legacy Genesis 1.0.5。

现有 Monarch 发布目录未保留本版本的逐项变更清单；为避免臆造内容，本条仅保留版本号，待找到可核验公告或发布包后补充。

## 1.0.4

发布时间记录：2026-08-29T13:55:39+08:00

历史归档索引：SCEX Legacy Genesis 1.0.4。

现有 Monarch 发布目录未保留本版本的逐项变更清单；为避免臆造内容，本条仅保留版本号，待找到可核验公告或发布包后补充。

## 1.0.3

发布时间记录：2026-08-29T13:55:38+08:00

历史归档索引：SCEX Legacy Genesis 1.0.3。

现有 Monarch 发布目录未保留本版本的逐项变更清单；为避免臆造内容，本条仅保留版本号，待找到可核验公告或发布包后补充。

## 1.0.2

发布时间记录：2026-08-29T13:55:38+08:00

历史归档索引：SCEX Legacy Genesis 1.0.2。

现有 Monarch 发布目录未保留本版本的逐项变更清单；为避免臆造内容，本条仅保留版本号，待找到可核验公告或发布包后补充。

## 1.0.1

发布时间记录：2026-08-29T13:55:38+08:00

历史归档索引：SCEX Legacy Genesis 1.0.1。

现有 Monarch 发布目录未保留本版本的逐项变更清单；为避免臆造内容，本条仅保留版本号，待找到可核验公告或发布包后补充。
