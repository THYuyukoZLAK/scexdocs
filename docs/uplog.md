# 各子服务器更新日志

<div class="caution">这个页面计划直接对接ai自动更新。我还没准备好示例格式所以先搁置。</div>

格式：

```markdown

> 日期 版本号

模组变更：  
// 如果有，按下列格式填写，如果没有，省去这部分并在补充部分说明
// 注意 模组变更： 后方和每行变更内容后方的两个空格换行标记。

    + [模组名] 模组文件名  
    - [模组名] 模组文件名  
    ~ [模组名] 旧版本号 -> 新版本号  

其他内容：  
其他更新内容补充，如配置文件修改等。如果有，简要在此处说明，若没有，省去这部分。  
有关服务器内部运行逻辑的更新等普通玩家无法接触到的部分不要写入更新日志。  

```

版本号更新的逻辑：

大型更新.小型更新.小更改

其中：  
大型更新：多个模组的新增，减少，引入全新的模组体系，玩法等。  
小型更新：新增/减少/更新少数模组，以及其他更新后旧客户端不执行同步操作无法进入服务器的更新。  
小更改：配置文件/资源包的简单调整，客户端不执行更新也不影响进入服务器。  

当更大的一级版本号递增时，比其更小的小版本号重置为0。  

例：v8.1.1 -> v8.1.2 -> v8.2.0 -> v8.2.1 -> v9.0.0  

完整更新日志示例：

## 整合包侧「须臾」

> 2026/7/14 v10.1.0

模组变更：  
    + [轻松村民] easy-villagers-neoforge-1.21.1-1.1.42.jar  

> 2026/7/10 v10.0.1

模组变更：  
    + [应用能源2：水晶科学] ae2cs-1.21.1-1.2.1.jar  
    + [应用能源2：JEI联动] ae2jeiintegration-1.2.1.jar  
    ~ [分子重组仪：怀旧渲染] MolecularTransformer-LegacyRenderer：1.0.3 → 1.0.5  
    ~ [奇点迭代] SingularityIteration：0.1.7.1-beta → 0.1.7.3.1-scex-dsfix  

其他内容：  
    + resourcepacks/IndustrialCraft-Nostalgia-for-SingularityIteration-1.0.6.zip  
    ~ resourcepacks/SCEX-任务图片资源包.zip  
    - resourcepacks/IndustrialCraft-Nostalgia-for-SingularityIteration-1.0.5.zip  

## 创造养老侧「永远」



## 怀旧向子服「旧梦」

<!-- LEGACY-LOG-AUTO:START -->
> 2026/9/25 v2.18.0
怀旧向子服「旧梦」

更新说明
- 奇点迭代更新为 dev8：电网预算、公平续跑、兼容与风水机同步修复；同步 ET compat1、拔刀联动dev.8，客户端分子怀旧渲染改为1.0.11软匹配。
- 戴森立方更新1.0.5-scex.netfix.1，减少空闲机器及全局数据重复同步。
- 额外植物学及神话植物学更新为最新自检修复包；额外植物学充能器同步问题已修复。
- 神秘时代更新port.253恢复并修复库存扫描，配套工匠64、禁忌32、污秽32及已确认的神秘视界dev.41修复包。
- Neo ECO AE更新beta4。
- 更新最新任务图片资源包（2026-09-25任务资源包(3)），保留玩家其他资源与设置。
- 热力本轮不更新；神秘基础学继续port.21。
- 星辉魔法：新增官方构建 2.0.0.12 与 ObserverLib 1.10.3.31，使用模组内置简体中文。
- 综合无线终端 WCWT 1.3.9 因旧存档兼容问题暂缓，沿用 1.3.8。

模组变更
~ [分子重组仪：怀旧渲染] MolecularTransformer-LegacyRenderer：1.0.9 → 1.0.11
~ forbiddenmagic-1.0.0：port.30 → port.32
~ si-slashblade-integration-0.1.0：dev.6 → dev.8
~ taintedmagic-1.0.0：port.30 → port.32
~ thaumcraft-0.2.2.95：port.246 → port.253
~ thaumic_tinkerer-1.0.0：port.59 → port.64
~ [戴森立方计划] dysoncubeproject-1.0.5.jar → dysoncubeproject-1.0.5-scex.netfix.1.jar
~ environmentaltech-1.21.1-2.0.0.33-scex：dev → si-compat1
~ [Neo ECO AE扩展] neoecoae-21.2.0-beta1.jar → neoecoae-21.2.0-beta4.jar
+ AstralSorcery-2.0.0.12.jar
+ mio_icif-0.1.7.12-scex.audit-boundary-dev8.jar
+ ObserverLib-1.10.3.31.jar
~ extrabotany-neoforge-1.21.1-2.0-scex.9-dev.jar
~ mythicbotany-5.0.0-neoforge-1.21.1-scex.3.jar
~ thaumichorizons-1.21.1-0.1.0-scex-dev.41.jar
- [SI] SingularityIteration-0.1.7.10-beta.jar

其他内容
~ resourcepacks/SCEX-任务图片资源包.zip

> 2026/9/22 v2.17.0
怀旧向子服「旧梦」

更新说明
- 神秘视界 dev.41：修复培养缸十二个自我注魔槽位同步，恢复注魔图标与悬停说明。
- 神秘基础学 port.21：修复节点操纵器、灵气链接器和节点链接器的镐类采掘标签与掉落。
- 热力系列 dev.24：修复闪电手雷配方，补齐烈焰之炽焱和板块之层岩的流体、物品、配方及环境效果。

模组变更
（无）

其他内容
~ _updater/portable-stage-daemon.ps1
~ _updater/portable-stage-daemon.py

> 2026/9/20 v2.16.0
怀旧向子服「旧梦」

更新说明
- 修复热力极寒之凛冰等流体名称显示，15 台处理机器增强槽扩展为 3×3 九格。
- 新增 Thermal Endergy，加入三阶合金、强化组件与机器及能源炉配方。
- 神秘视界更新至 dev.40，修复灵魂组装器脑模型的渲染层。
- 退出游戏后运行整合包内更新脚本，更新至 2.16.0 后进入服务器。

模组变更
~ cofh_core-11.0.2：scex.dev.22 → scex.dev.23
~ thaumichorizons-1.21.1-0.1.0-scex：dev.38 → dev.40
~ thermal_cultivation-11.0.2：scex.dev.22 → scex.dev.23
~ thermal_dynamics-11.0.1：scex.dev.22 → scex.dev.23
~ thermal_expansion-11.0.2：scex.dev.22 → scex.dev.23
~ thermal_foundation-11.0.7：scex.dev.22 → scex.dev.23
~ thermal_innovation-11.0.1：scex.dev.22 → scex.dev.23
~ thermal_locomotion-11.0.1：scex.dev.22 → scex.dev.23
~ thermal-11.0.7：scex.dev.22 → scex.dev.23
+ thermalendergy-1.21.1-1.0.0-scex.dev.1.jar

其他内容
~ 更新mod-Mac端.command
~ 更新mod-Windows端.bat

> 2026/9/19 v2.15.1
怀旧向子服「旧梦」

更新说明
- 同步服务器当前 MythicBotany 5.0.0-scex.3 修复构建。
- 同步 CoFH Core 与 Thermal dev22 当前修复构建，修复 AE/槽楔相关显示与交互问题。
- 补发早苗自定义模型包（tlm_custom_pack），避免客户端缺少早苗模型与贴图。
- 退出游戏后运行整合包内更新脚本，更新至 2.15.1 再进入服务器。

模组变更
~ cofh_core-11.0.2-scex.dev.22.jar
~ mythicbotany-5.0.0-neoforge-1.21.1-scex.3.jar
~ thermal-11.0.7-scex.dev.22.jar

其他内容
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/animation/arm.js
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/animation/float.js
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/lang/de_de.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/lang/en_us.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/lang/es_es.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/lang/fr_fr.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/lang/id_id.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/lang/it_it.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/lang/ja_jp.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/lang/ko_kr.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/lang/la_la.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/lang/pt_br.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/lang/pt_pt.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/lang/ru_ru.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/lang/tr_tr.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/lang/vi_vn.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/lang/zh_cn.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/lang/zh_tw.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/maid_model.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/models/entity/clocklalier.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/models/entity/cyra_pow_wow.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/models/entity/cyra.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/models/entity/fledge.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/models/entity/flower_candy.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/models/entity/mory_chan.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/models/entity/pajinyi.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/models/entity/sazuki.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/models/entity/wine_fox_maid.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/models/entity/wine_fox_taisho.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/textures/entity/clocklalier.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/textures/entity/cyra_pow_wow.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/textures/entity/cyra.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/textures/entity/cyra2.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/textures/entity/fledge.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/textures/entity/flower_candy.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/textures/entity/mory_chan.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/textures/entity/pajinyi.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/textures/entity/sazuki.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/textures/entity/wine_fox_maid.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/textures/entity/wine_fox_taisho.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/authors_and_credits/textures/maid_icon.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/foxmaid.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/foxmaid.tac.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/hailuo.condition.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/hailuo.main.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/kluonoa.condition.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/kluonoa.main.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/kluonoa.tac.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/qingluka.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/rice_cake_fox.condition.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/rice_cake_fox.main.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/rice_cake_fox.tac.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/sta.condition.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/sta.main.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/sta.tac.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_astronaut.condition.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_astronaut.main.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_blue.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_elf.condition.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_elf.iss.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_elf.main.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_hanfu.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_jk.condition.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_jk.main.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_jk.tac.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_kongfu.condition.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_kongfu.main.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_little.condition.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_little.main.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_little.tac.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_magical.condition.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_magical.iss.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_magical.main.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_matured.condition.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_matured.main.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_mini.main.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_momo.condition.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_momo.main.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_nine_tailed.condition.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_nine_tailed.iss.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_nine_tailed.main.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_saint.condition.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_saint.iss.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_saint.main.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_salesperson.condition.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_salesperson.main.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_survivor.condition.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_survivor.main.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_survivor.tac.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_tactics.condition.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_tactics.main.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_tactics.tac.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_wedding.condition.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_wedding.main.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox_wedding.tac.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/winefox.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/zhiban_hanfu.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/animation/zhiban.animation.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/lang/de_de.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/lang/en_us.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/lang/es_es.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/lang/fr_fr.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/lang/id_id.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/lang/it_it.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/lang/ja_jp.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/lang/ko_kr.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/lang/la_la.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/lang/pt_br.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/lang/pt_pt.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/lang/ru_ru.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/lang/tr_tr.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/lang/vi_vn.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/lang/zh_cn.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/lang/zh_tw.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/maid_chair.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/maid_model.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/models/entity/foxmaid.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/models/entity/hailuo_new_year.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/models/entity/kluonoa.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/models/entity/qingluka.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/models/entity/rice_cake_fox.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/models/entity/sta.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/models/entity/winefox_astronaut.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/models/entity/winefox_elf.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/models/entity/winefox_hanfu.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/models/entity/winefox_jk.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/models/entity/winefox_kongfu.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/models/entity/winefox_little.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/models/entity/winefox_magical.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/models/entity/winefox_matured.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/models/entity/winefox_mini.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/models/entity/winefox_momo.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/models/entity/winefox_new_year.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/models/entity/winefox_nine_tailed.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/models/entity/winefox_saint.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/models/entity/winefox_salesperson.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/models/entity/winefox_survivor.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/models/entity/winefox_tactics.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/models/entity/winefox_wedding.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/models/entity/winefox.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/models/entity/zhiban_hanfu.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/models/entity/zhiban_new_year.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/models/entity/zhiban.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/settings/kluonoa.yml
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/settings/winefox.yml
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/settings/zhiban.yml
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/foxmaid.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/hailuo_new_year.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/kluonoa.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/qingluka.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/rice_cake_fox.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/sta.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/winefox_astronaut.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/winefox_blue.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/winefox_elf.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/winefox_hanfu.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/winefox_jk.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/winefox_kongfu_1.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/winefox_kongfu_2.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/winefox_kongfu_3.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/winefox_kongfu_4.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/winefox_kongfu_5.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/winefox_kongfu.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/winefox_little.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/winefox_magical_1.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/winefox_magical_2.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/winefox_magical_3.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/winefox_magical_4.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/winefox_magical_5.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/winefox_magical.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/winefox_matured.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/winefox_mini.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/winefox_momo_1.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/winefox_momo.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/winefox_new_year.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/winefox_nine_tailed_1.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/winefox_nine_tailed.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/winefox_saint_1.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/winefox_saint.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/winefox_salesperson_1.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/winefox_salesperson.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/winefox_survivor.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/winefox_tactics.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/winefox_wedding.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/winefox.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/zhiban_hanfu.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/zhiban_new_year.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/entity/zhiban.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/geckolib/textures/maid_icon.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/lang/de_de.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/lang/en_us.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/lang/es_es.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/lang/fr_fr.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/lang/id_id.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/lang/it_it.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/lang/ja_jp.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/lang/ko_kr.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/lang/la_la.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/lang/pt_br.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/lang/pt_pt.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/lang/ru_ru.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/lang/tr_tr.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/lang/vi_vn.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/lang/zh_cn.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/lang/zh_tw.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/maid_sound.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/death1.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/death10.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/death11.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/death12.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/death13.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/death14.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/death15.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/death16.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/death17.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/death18.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/death19.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/death2.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/death20.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/death21.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/death22.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/death23.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/death24.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/death25.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/death3.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/death4.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/death5.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/death6.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/death7.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/death8.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/death9.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/find_target1.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/find_target10.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/find_target11.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/find_target12.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/find_target13.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/find_target14.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/find_target15.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/find_target16.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/find_target17.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/find_target18.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/find_target2.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/find_target3.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/find_target4.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/find_target5.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/find_target6.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/find_target7.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/find_target8.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/find_target9.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/hurt_fire1.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/hurt_fire10.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/hurt_fire11.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/hurt_fire12.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/hurt_fire2.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/hurt_fire3.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/hurt_fire4.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/hurt_fire5.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/hurt_fire6.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/hurt_fire7.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/hurt_fire8.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/hurt_fire9.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/hurt1.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/hurt10.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/hurt11.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/hurt12.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/hurt13.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/hurt2.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/hurt3.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/hurt4.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/hurt5.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/hurt6.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/hurt7.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/hurt8.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/hurt9.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/item_get1.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/item_get10.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/item_get11.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/item_get12.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/item_get13.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/item_get14.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/item_get15.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/item_get2.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/item_get3.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/item_get4.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/item_get5.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/item_get6.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/item_get7.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/item_get8.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/item_get9.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/tamed1.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/tamed10.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/tamed11.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/tamed12.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/tamed13.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/tamed14.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/tamed15.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/tamed2.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/tamed3.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/tamed4.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/tamed5.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/tamed6.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/tamed7.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/tamed8.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/ai/tamed9.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/morning1.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/morning10.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/morning11.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/morning12.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/morning13.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/morning14.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/morning15.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/morning16.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/morning17.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/morning18.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/morning19.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/morning2.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/morning20.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/morning21.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/morning22.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/morning23.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/morning3.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/morning4.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/morning5.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/morning6.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/morning7.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/morning8.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/morning9.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/night1.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/night10.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/night11.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/night12.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/night13.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/night14.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/night15.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/night16.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/night17.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/night18.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/night2.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/night3.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/night4.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/night5.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/night6.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/night7.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/night8.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/environment/night9.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/attack1.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/attack10.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/attack11.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/attack12.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/attack13.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/attack14.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/attack2.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/attack3.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/attack4.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/attack5.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/attack6.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/attack7.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/attack8.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/attack9.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/farm1.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/farm2.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/farm3.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/farm4.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/farm5.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/farm6.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/feed1.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/feed10.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/feed11.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/feed12.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/feed13.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/feed14.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/feed15.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/feed2.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/feed3.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/feed4.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/feed5.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/feed6.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/feed7.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/feed8.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/feed9.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/furnace1.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/furnace10.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/furnace11.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/furnace12.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/furnace13.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/furnace14.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/furnace15.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/furnace16.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/furnace17.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/furnace18.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/furnace19.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/furnace2.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/furnace20.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/furnace21.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/furnace22.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/furnace23.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/furnace3.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/furnace4.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/furnace5.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/furnace6.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/furnace7.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/furnace8.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/furnace9.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle1.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle10.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle11.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle12.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle13.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle14.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle15.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle16.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle17.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle18.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle19.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle2.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle20.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle21.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle22.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle23.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle24.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle25.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle26.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle27.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle28.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle29.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle3.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle30.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle31.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle32.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle33.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle34.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle35.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle36.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle37.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle38.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle39.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle4.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle40.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle41.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle42.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle43.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle44.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle45.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle46.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle47.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle48.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle49.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle5.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle50.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle51.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle52.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle53.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle54.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle55.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle56.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle57.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle58.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle59.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle6.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle60.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle61.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle62.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle63.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle64.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle65.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle66.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle67.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle68.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle69.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle7.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle70.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle71.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle72.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle73.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle74.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle75.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle76.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle77.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle78.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle8.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/idle9.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/range_attack1.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/range_attack10.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/range_attack11.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/range_attack12.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/range_attack13.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/range_attack14.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/range_attack15.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/range_attack16.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/range_attack17.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/range_attack18.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/range_attack19.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/range_attack2.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/range_attack20.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/range_attack21.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/range_attack22.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/range_attack23.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/range_attack24.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/range_attack25.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/range_attack26.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/range_attack27.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/range_attack28.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/range_attack29.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/range_attack3.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/range_attack4.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/range_attack5.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/range_attack6.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/range_attack7.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/range_attack8.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/range_attack9.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/torch1.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/torch10.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/torch11.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/torch12.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/torch13.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/torch14.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/torch15.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/torch17.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/torch18.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/torch19.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/torch2.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/torch20.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/torch21.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/torch22.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/torch23.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/torch24.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/torch25.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/torch26.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/torch27.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/torch28.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/torch29.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/torch3.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/torch4.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/torch5.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/torch6.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/torch7.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/torch8.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/littlemaid_peco/sounds/maid/mode/torch9.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/minecraft_15th/lang/de_de.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/minecraft_15th/lang/en_us.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/minecraft_15th/lang/es_es.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/minecraft_15th/lang/fr_fr.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/minecraft_15th/lang/id_id.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/minecraft_15th/lang/it_it.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/minecraft_15th/lang/ja_jp.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/minecraft_15th/lang/ko_kr.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/minecraft_15th/lang/la_la.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/minecraft_15th/lang/pt_br.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/minecraft_15th/lang/pt_pt.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/minecraft_15th/lang/ru_ru.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/minecraft_15th/lang/tr_tr.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/minecraft_15th/lang/vi_vn.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/minecraft_15th/lang/zh_cn.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/minecraft_15th/lang/zh_tw.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/minecraft_15th/maid_model.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/minecraft_15th/models/entity/alex.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/minecraft_15th/models/entity/dawn.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/minecraft_15th/models/entity/natalie.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/minecraft_15th/models/entity/rana.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/minecraft_15th/textures/entity/alex.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/minecraft_15th/textures/entity/dawn.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/minecraft_15th/textures/entity/natalie.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/minecraft_15th/textures/entity/rana.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/minecraft_15th/textures/maid_icon.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/lang/de_de.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/lang/en_us.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/lang/es_es.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/lang/fr_fr.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/lang/id_id.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/lang/it_it.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/lang/ja_jp.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/lang/ko_kr.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/lang/la_la.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/lang/pt_br.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/lang/pt_pt.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/lang/ru_ru.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/lang/tr_tr.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/lang/vi_vn.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/lang/zh_cn.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/lang/zh_tw.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/maid_chair.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/models/entity/3d_printer.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/models/entity/backpack.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/models/entity/bathroom.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/models/entity/cabinet.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/models/entity/cumin_lamb_chop.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/models/entity/dining_table_default.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/models/entity/doorbell_ground.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/models/entity/doorbell_wall.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/models/entity/double_bed.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/models/entity/elite_slime.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/models/entity/exchange_machine.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/models/entity/fishpond.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/models/entity/flip_phone.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/models/entity/fox_demon_statue.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/models/entity/hot_spring.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/models/entity/japanese_lottery_machine.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/models/entity/kitchen.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/models/entity/logging_hut.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/models/entity/mine.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/models/entity/picnic_cloth.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/models/entity/shrine.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/models/entity/single_bed.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/models/entity/slime.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/models/entity/stage.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/textures/chair_icon.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/textures/entity/3d_printer.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/textures/entity/backpack.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/textures/entity/bathroom.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/textures/entity/cabinet.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/textures/entity/cumin_lamb_chop.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/textures/entity/dining_table_autumn.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/textures/entity/dining_table_default.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/textures/entity/dining_table_spring.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/textures/entity/dining_table_summer.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/textures/entity/dining_table_winter.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/textures/entity/doorbell_ground.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/textures/entity/doorbell_wall.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/textures/entity/double_bed.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/textures/entity/elite_slime.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/textures/entity/exchange_machine.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/textures/entity/fishpond.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/textures/entity/flip_phone.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/textures/entity/fox_demon_statue_1.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/textures/entity/fox_demon_statue.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/textures/entity/hot_spring.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/textures/entity/japanese_lottery_machine.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/textures/entity/kitchen.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/textures/entity/logging_hut.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/textures/entity/mine.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/textures/entity/picnic_cloth.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/textures/entity/shrine.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/textures/entity/single_bed.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/textures/entity/slime.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/next_update_model/textures/entity/stage.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/lang/de_de.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/lang/en_us.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/lang/es_es.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/lang/fr_fr.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/lang/id_id.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/lang/it_it.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/lang/ja_jp.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/lang/ko_kr.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/lang/la_la.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/lang/pt_br.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/lang/pt_pt.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/lang/ru_ru.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/lang/tr_tr.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/lang/vi_vn.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/lang/zh_cn.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/lang/zh_tw.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/maid_model.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/models/entity/alice.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/models/entity/chiyuri_kitashirakawa.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/models/entity/elis.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/models/entity/ellen.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/models/entity/elly.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/models/entity/gengetsu.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/models/entity/genjii.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/models/entity/kana_anaberal.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/models/entity/kikuri.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/models/entity/kirisame_marisa.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/models/entity/konngara.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/models/entity/kotohime.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/models/entity/kurumi.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/models/entity/louise.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/models/entity/mai.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/models/entity/meira.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/models/entity/mima.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/models/entity/mugetsu.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/models/entity/orange.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/models/entity/reimu_hakurei.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/models/entity/rika.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/models/entity/rikako_asakura.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/models/entity/ruukoto.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/models/entity/sara.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/models/entity/sariel.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/models/entity/shinki.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/models/entity/singyoku2.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/models/entity/singyoku3.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/models/entity/trump_king.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/models/entity/yuki.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/models/entity/yumeko.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/models/entity/yumemi_okazaki.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/models/entity/yuugen_magan.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/models/entity/yuuka_old.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/entity/alice.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/entity/chiyuri_kitashirakawa.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/entity/elis.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/entity/ellen.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/entity/elly.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/entity/gengetsu.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/entity/genjii.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/entity/kana_anaberal.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/entity/kikuri.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/entity/kirisame_marisa.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/entity/konngara.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/entity/kotohime.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/entity/kurumi.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/entity/louise.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/entity/mai.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/entity/meira.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/entity/mima.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/entity/mugetsu.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/entity/orange.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/entity/reimu_hakurei.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/entity/rika.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/entity/rikako_asakura.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/entity/ruukoto.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/entity/sara.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/entity/sariel.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/entity/shinki.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/entity/singyoku2.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/entity/singyoku3.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/entity/trump_king.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/entity/yuki.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/entity/yumeko.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/entity/yumemi_okazaki.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/entity/yuugen_magan.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/entity/yuuka_old.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_old/textures/maid_icon.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_seihou/lang/de_de.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_seihou/lang/en_us.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_seihou/lang/es_es.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_seihou/lang/fr_fr.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_seihou/lang/id_id.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_seihou/lang/it_it.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_seihou/lang/ja_jp.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_seihou/lang/ko_kr.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_seihou/lang/pt_br.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_seihou/lang/ru_ru.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_seihou/lang/tr_tr.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_seihou/lang/vi_vn.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_seihou/lang/zh_cn.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_seihou/lang/zh_tw.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_seihou/maid_model.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_seihou/models/entity/mai.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_seihou/models/entity/mei.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_seihou/models/entity/milia.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_seihou/models/entity/vivit.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_seihou/textures/entity/mai.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_seihou/textures/entity/mei.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_seihou/textures/entity/milia.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_seihou/textures/entity/vivit_2.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_seihou/textures/entity/vivit.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid_seihou/textures/maid_icon.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/lang/de_de.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/lang/en_us.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/lang/es_es.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/lang/fr_fr.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/lang/id_id.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/lang/it_it.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/lang/ja_jp.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/lang/ko_kr.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/lang/la_la.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/lang/pt_br.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/lang/pt_pt.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/lang/ru_ru.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/lang/tr_tr.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/lang/vi_vn.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/lang/zh_cn.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/lang/zh_tw.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/maid_chair.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/maid_model.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/maid_sound.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/aki_sizuha.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/alice_margatroid.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/alice.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/anti_collision_bucket.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/ariya_iwanaga.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/barbecue_booth_2.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/barbecue_booth.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/beach_chair.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/bowl.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/chen.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/chimi_houjuu.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/cirno_maid.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/cirno_slim.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/cirno_tan.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/cirno.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/class_chair.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/class_desk.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/clownpiece.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/crystalizedsuns_moms_tombstone.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/cushion.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/daiyousei.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/doremy_sweet.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/ebisu_eika.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/ema.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/eternity_larva.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/flandre_scarlet.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/fogg05.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/fujiwara_no_mokou.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/goliath_doll.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/goutokuzi_mike.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/hakurei_reimu_type_b.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/hakurei_reimu.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/haniyasushin_keiki.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/hata_no_kokoro.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/head_of_academycraft.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/hecatia_lapislazuli.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/hieda_no_akyuu.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/hijiri_byakuren.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/himekaidou_hatate.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/himemushi_momoyo.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/hinanawi_tenshi.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/hong_meiling.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/horikawa_raiko.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/hoshiguma_yugi.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/houjuu_nue.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/hourai_doll.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/houraisan_kaguya.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/hutatsuiwa_mamizou.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/ibaraki_kasen_2.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/ibaraki_kasen.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/ibuki_suika.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/iizunamaru_megumu.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/imaizumi_kagerou.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/inubashiri_momizi.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/izayoi_sakuya.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/joutougu_mayumi.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/junko.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/kaenbyou_rin.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/kagiyama_hina.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/kaku_seiga.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/kasodani_kyouko.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/kawasiro_nitori.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/kazami_yuka.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/keine_kamishirasawa_2.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/keine_kamishirasawa.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/kijin_seija.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/kirisame_marisa_2.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/kirisame_marisa.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/kisin_sagume.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/kisume.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/kitcho_yachie.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/koakuma.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/kochiya_sanae.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/komakusa_sannyo.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/komano_aunn.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/komeiji_koishi_2.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/komeiji_koishi.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/komeiji_satori.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/konpaku_youmu.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/kotatsu.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/kudamaki_tsukasa.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/kumoi_ichirin.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/kurodani_yamame.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/kurokoma_saki.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/legendary_pig_man.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/letty_whiterock.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/lily_black.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/lily_white.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/long_stool.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/low_stool.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/lucky_cat_2m.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/luna_child.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/lunasa_prismriver.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/lyrica_prismriver.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/mahjong_table.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/maribel_hearn.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/matara_okina.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/medicine_melancholy.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/merlin_prismriver.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/mima.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/minoriko_aki.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/mitsugashira_enoko.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/miyadeguchi_mizuchi.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/miyako_yoshika.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/miyoi_okunoda.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/mizuhashi_parsee.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/moesumika.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/mononobe_no_futo.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/morichika_rinnosuke.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/moriya_suwako.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/moto.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/motoori_kosuzu.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/murasa_minamitsu.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/mystia_lorelei.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/nagae_iku.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/nareko_michigami.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/native_drum.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/nazrin.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/nippaku_zanmu.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/nishida_satono.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/niwatari_kutaka.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/onozuka_komachi.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/parasol.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/park_bench.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/patchouli_knowledge_2.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/patchouli_knowledge.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/play_station.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/reisen_udongein_inaba.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/reisen.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/reiuji_utsuho.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/remilia_scarlet_2.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/remilia_scarlet.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/ringo.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/rinnosuke_children_toys.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/rumia.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/saigyouji_yuyuko.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/saisen_bako.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/sakata_nemuno.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/satsuki_rin.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/seiran.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/sekibanki.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/shanghai_doll.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/shikieiki_yamaxanadu.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/soga_no_toziko.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/son_biten.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/square_table.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/star_sapphire.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/sukuna_shinmyoumaru.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/sunny_milk.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/syameimaru_aya.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/tall_stool.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/tamatsukuri_misumaru.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/tatara_kogasa.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/teireid_mai.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/tenkajin_chiyari.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/tenkyu_chimata.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/tewi_inaba.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/tokiko.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/toramaru_shou.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/torii_2.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/torii_3.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/torii.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/toutetsu_yuma.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/toyosatomimi_no_miko.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/tsukumo_benben.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/tsukumo_yatsuhashi.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/ubame_chirizuka.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/usami_renko.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/usami_sumireko.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/ushizaki_urumi.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/wakasagihime.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/watari_nina.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/watatsuki_no_toyohime.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/watatsuki_no_yorihime.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/water_wheel.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/well.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/wriggle_nightbug.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/yagokoro_eirin.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/yakumo_ran.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/yamashiro_takane.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/yasaka_kanako.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/yatadera_narumi.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/yomotsu_hisami.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/yorigami_jyoon.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/yorigami_shion.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/yuiman_asama.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/yukari_yakumo.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/yumemi_okazaki.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/models/entity/yumemi_strawberry_milk.json
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/ai/death1.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/ai/death2.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/ai/find_target1.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/ai/find_target2.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/ai/find_target3.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/ai/hurt_player1.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/ai/hurt_player2.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/ai/hurt_player3.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/ai/hurt_player4.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/ai/hurt_player5.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/ai/hurt_player6.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/ai/hurt_player7.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/ai/hurt1.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/ai/hurt2.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/ai/hurt3.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/ai/hurt4.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/ai/hurt5.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/ai/hurt6.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/ai/hurt7.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/ai/hurt8.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/ai/hurt9.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/ai/item_get1.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/ai/tamed1.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/ai/tamed2.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/ai/tamed3.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/ai/tamed4.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/ai/tamed5.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/environment/cold1.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/environment/cold2.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/environment/cold3.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/environment/cold4.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/environment/hot1.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/environment/hot2.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/environment/hot3.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/environment/morning1.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/environment/morning2.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/environment/morning3.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/environment/morning4.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/environment/morning5.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/environment/morning6.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/environment/morning7.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/environment/morning8.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/environment/night1.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/environment/night2.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/environment/rain1.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/environment/rain2.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/environment/rain3.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/environment/snow1.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/environment/snow2.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/attack1.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/attack2.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/attack3.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/attack4.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/attack5.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/attack6.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/attack7.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/feed1.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/feed2.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/feed3.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/feed4.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/feed5.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/feed6.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/feed7.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle1.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle10.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle11.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle12.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle13.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle14.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle15.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle16.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle17.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle18.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle19.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle2.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle20.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle21.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle22.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle23.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle24.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle25.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle26.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle27.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle28.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle29.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle3.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle30.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle31.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle32.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle33.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle34.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle35.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle36.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle37.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle38.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle39.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle4.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle5.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle6.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle7.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle8.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/mode/idle9.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/sounds/maid/other/credit.ogg
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/chair_icon.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/aki_sizuha.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/alice_margatroid.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/alice.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/anti_collision_bucket.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/ariya_iwanaga.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/barbecue_booth.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/beach_chair.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/cat_cart.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/chen.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/chimi_houjuu.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/cirno_maid.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/cirno_slim_maid.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/cirno_slim_tan.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/cirno_slim.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/cirno_tan.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/cirno.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/class_chair.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/class_desk.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/clownpiece.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/crystalizedsuns_moms_tombstone.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/cushion.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/daiyousei.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/doremy_sweet.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/ebisu_eika.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/ema.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/eternity_larva.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/flandre_scarlet.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/fogg05.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/fujiwara_no_mokou.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/goliath_doll.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/goutokuzi_mike.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/hakurei_reimu_2.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/hakurei_reimu_type_b_2.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/hakurei_reimu_type_b.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/hakurei_reimu_vengeful_2.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/hakurei_reimu_vengeful.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/hakurei_reimu.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/haniyasushin_keiki.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/hata_no_kokoro.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/head_of_academycraft.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/hecatia_lapislazuli.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/hieda_no_akyuu.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/hijiri_byakuren.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/himekaidou_hatate.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/himemushi_momoyo.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/hinanawi_tenshi.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/hong_meiling.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/horikawa_raiko.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/hoshiguma_yugi.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/houjuu_nue.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/hourai_doll.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/houraisan_kaguya.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/hutatsuiwa_mamizou.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/ibaraki_kasen_2.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/ibaraki_kasen.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/ibuki_suika.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/iizunamaru_megumu.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/imaizumi_kagerou.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/inubashiri_momizi.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/izayoi_sakuya.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/joutougu_mayumi.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/junko.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/kaenbyou_rin.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/kagiyama_hina.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/kaku_seiga.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/kasodani_kyouko.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/kawasiro_nitori.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/kazami_yuka.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/keine_kamishirasawa_2.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/keine_kamishirasawa.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/kijin_seija.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/kirisame_marisa_2.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/kirisame_marisa.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/kisin_sagume.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/kisume.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/kitcho_yachie.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/koakuma.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/kochiya_sanae.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/komakusa_sannyo.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/komano_aunn.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/komeiji_koishi_2.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/komeiji_koishi.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/komeiji_satori.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/konpaku_youmu.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/kotatsu.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/kudamaki_tsukasa.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/kumoi_ichirin.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/kurodani_yamame.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/kurokoma_saki.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/legendary_pig_man.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/letty_whiterock.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/lily_black.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/lily_white.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/long_stool.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/low_stool.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/lucky_cat_2m.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/luna_child.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/lunasa_prismriver.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/lyrica_prismriver.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/mahjong_table.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/maribel_hearn.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/marisa_broom.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/matara_okina.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/medicine_melancholy.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/merlin_prismriver.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/mima.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/minoriko_aki.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/mitsugashira_enoko.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/miyadeguchi_mizuchi.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/miyako_yoshika.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/miyoi_okunoda.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/mizuhashi_parsee.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/moesumika.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/mononobe_no_futo.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/morichika_rinnosuke.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/moriya_suwako.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/moto.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/motoori_kosuzu.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/murasa_minamitsu.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/mystia_lorelei.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/nagae_iku.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/nareko_michigami.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/native_drum.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/nazrin.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/nippaku_zanmu.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/nishida_satono.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/niwatari_kutaka.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/onozuka_komachi.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/parasol.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/park_bench.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/patchouli_knowledge_2.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/patchouli_knowledge.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/play_station.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/reisen_udongein_inaba.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/reisen.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/reiuji_utsuho.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/remilia_scarlet_2.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/remilia_scarlet.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/rickshaw.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/ringo.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/rinnosuke_children_toys.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/rumia.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/saigyouji_yuyuko.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/saisen_bako.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/sakata_nemuno.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/satsuki_rin.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/seiran.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/sekibanki.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/shanghai_doll.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/shikieiki_yamaxanadu.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/singe_plane_danmaku.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/soga_no_toziko.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/son_biten.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/square_table.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/star_danmaku.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/star_sapphire.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/sukuna_shinmyoumaru.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/sunny_milk.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/syameimaru_aya.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/tall_stool.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/tamatsukuri_misumaru.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/tatara_kogasa.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/teireid_mai.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/tenkajin_chiyari.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/tenkyu_chimata.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/tewi_inaba.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/tokiko.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/toramaru_shou.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/torii.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/toutetsu_yuma.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/toyosatomimi_no_miko.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/tsukumo_benben.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/tsukumo_yatsuhashi.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/ubame_chirizuka.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/usami_renko.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/usami_sumireko.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/ushizaki_urumi.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/wakasagihime.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/watari_nina.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/watatsuki_no_toyohime.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/watatsuki_no_yorihime.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/water_wheel.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/well.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/wheel_chair.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/wriggle_nightbug.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/yagokoro_eirin.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/yakumo_ran.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/yamashiro_takane.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/yasaka_kanako.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/yatadera_narumi.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/yomotsu_hisami.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/yorigami_jyoon.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/yorigami_shion.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/yuiman_asama.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/yukari_yakumo.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/yukkuri.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/yumemi_okazaki.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/entity/yumemi_strawberry_milk.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/maid_icon.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/assets/touhou_little_maid/textures/sound_icon.png
+ tlm_custom_pack/touhou_little_maid-1.0.0/pack.mcmeta
+ tlm_custom_pack/touhou_little_maid-1.0.0/pack.png

> 2026/9/19 v2.15.0
怀旧向子服「旧梦」

更新说明
- 神秘时代升级至 port.246，六件配套模组同步更新。
- 神秘基础学 port.20：补齐施法手镯长容量接口，保留既有修复。
- Thermal dev22：修复工具显示、能量与液体消耗边界及 JEI、机器流体图标错位。
- 任务图片资源包新增植物魔法任务图片。
- 神秘自动研发 1.3.1-scex.1-rc2：适配神秘时代 port.246，改为软前置并安全隔离缺失或不兼容联动。
- 环境科技升级至 2.0.0.33，为虚空矿机补充热力系列20项可选矿石产出。

模组变更
~ cofh_core-11.0.2：scex.dev.21 → scex.dev.22
~ environmentaltech-1.21.1：2.0.0.32 → 2.0.0.33
~ TC4AutoResearch-1.21.1：1.3.0 → 1.3.1
~ thaumicbases-2.1.189.32：port.19 → port.20
~ thermal_cultivation-11.0.2：scex.dev.21 → scex.dev.22
~ thermal_dynamics-11.0.1：scex.dev.21 → scex.dev.22
~ thermal_expansion-11.0.2：scex.dev.21 → scex.dev.22
~ thermal_foundation-11.0.7：scex.dev.21 → scex.dev.22
~ thermal_innovation-11.0.1：scex.dev.21 → scex.dev.22
~ thermal_locomotion-11.0.1：scex.dev.21 → scex.dev.22
~ thermal-11.0.7：scex.dev.21 → scex.dev.22
~ [禁忌魔法] forbiddenmagic-1.0.0-port.29-scex.1.jar → forbiddenmagic-1.0.0-port.30.jar
~ [污秽魔法] taintedmagic-1.0.0-port.29.jar → taintedmagic-1.0.0-port.30.jar
~ [神秘时代] thaumcraft-0.2.2.95-port.242.jar → thaumcraft-0.2.2.95-port.246.jar
~ [节点机制] nodalmechanics-1.0.0-port.6.jar → nodalmechanics-1.0.0-port.6.jar
~ [天界神秘学] thaumcraftcelestial-1.0.0-port.24.jar → thaumcraftcelestial-1.0.0-port.24.jar
~ [神秘工匠] thaumic_tinkerer-1.0.0-port.59.jar → thaumic_tinkerer-1.0.0-port.59.jar

其他内容
~ resourcepacks/SCEX-任务图片资源包.zip

> 2026/9/18 v2.14.0
怀旧向子服「旧梦」

更新说明
- Thermal dev.21：接入热力系列八个模块。
- 旧梦重铸 dev.4：修复怀旧模式切换状态卡住问题。
- CustomSkinLoader ForgeV3 14.27：修复 NeoForge 1.21.1 SkinManager 补丁崩溃。
- 本轮不包含 PCL 在线轻量客户端包。

模组变更
~ slashblade-legacy-compat-0.3.0：dev.3 → dev.4
+ [万用皮肤补丁] CustomSkinLoader_ForgeV3-14.27.jar
+ cofh_core-11.0.2-scex.dev.21.jar
+ thermal_cultivation-11.0.2-scex.dev.21.jar
+ thermal_dynamics-11.0.1-scex.dev.21.jar
+ thermal_expansion-11.0.2-scex.dev.21.jar
+ thermal_foundation-11.0.7-scex.dev.21.jar
+ thermal_innovation-11.0.1-scex.dev.21.jar
+ thermal_locomotion-11.0.1-scex.dev.21.jar
+ thermal-11.0.7-scex.dev.21.jar
- [万用皮肤补丁] CustomSkinLoader_Universal-15.0.1.jar

其他内容
（无）

> 2026/9/18 v2.13.0
怀旧向子服「旧梦」

更新说明
- 神秘视界dev.38：修复旧扫描记录导致灵魂滤网研究无法解锁、自我注魔死亡后错误保留、光合皮肤恢复与日照判定，以及因果重组器特效错位。
- 神秘基础学port.19：修复高级炼金炉实际加速、神秘自然研究页显示，以及节点调节器核心取下和移动时重复掉落。默认使用炼金煤时高级炼金炉为两倍速度。

模组变更
~ thaumicbases-2.1.189.32：port.17 → port.19
~ thaumichorizons-1.21.1-0.1.0-scex：dev.36 → dev.38

其他内容
（无）

> 2026/9/17 v2.12.0
怀旧向子服「旧梦」

更新说明
- 旧梦重铸dev.3：修复精准防御恢复药水效果时崩溃，增加刀挂台普通耀魂喂入，怀旧超SA默认尊重无法破坏属性。
- 额外植物学scex.9：修复亚空之矛模型与碰撞箱锚点及横截面对齐。
- 修复暮色森林任务图片资源路径；此前已丢失的背景、任务框和图标需管理员重新指定。

模组变更
~ extrabotany-neoforge-1.21.1-2.0：scex.8 → scex.9
~ slashblade-legacy-compat-0.3.0：dev.2 → dev.3

其他内容
~ resourcepacks/SCEX-任务图片资源包.zip

> 2026/9/17 v2.11.0
怀旧向子服「旧梦」

更新说明
- 学园都市0.0.28：修复开发机EXP布局、按钮叠字与新旧节点名称串用。
- 神秘基础学port.17：修复左轮枪子弹破坏容器和节点、高级炼金炉生存挖掘不掉本体。
- Quest Enhance更新至3.9。

模组变更
~ AcademyCraft-neoforge-1.21.1：0.0.27 → 0.0.28
~ thaumicbases-2.1.189.32：port.16 → port.17
~ [FTB任务增强] quest_enhance-1.21.1-neoforge-3.7.jar → quest_enhance-1.21.1-neoforge-3.9.jar

其他内容
（无）

> 2026/9/17 v2.10.0
怀旧向子服「旧梦」

更新说明
- 神秘基础学：修复镰刀第三人称握持与奥术左轮枪附魔书配方匹配。
- 神秘视界：修复研究文字、插图和结构书页，补齐碎片嬗变及替代傀儡铃铛研究配方。
- 超能力：修复学习机布局、按钮点击、节点名称和图标显示。
- 额外植物学：修复亚空之矛、控煌之境、空之律者皮肤及相关模型、特效和状态同步；同步更新兼容层。

模组变更
~ AcademyCraft-neoforge-1.21.1：0.0.26-scex-projectiles → 0.0.27-scex-machineui
~ extrabotany-neoforge-1.21.1-2.0：scex.7 → scex.8
~ SCEX-Botania-ExtraBotany-Compat-1.21.1：1.4.1 → 1.4.2
~ thaumicbases-2.1.189.32：port.15 → port.16
~ thaumichorizons-1.21.1-0.1.0-scex：dev.34 → dev.36

其他内容
（无）

> 2026/9/16 v2.9.6
怀旧向子服「旧梦」

更新说明
- 撤回尚未完成的热力全家桶及 CoFHCore，避免玩家使用未完成内容。
- 神秘视界 0.1.0-scex-dev.34 与暮色森林界面素材资源包继续保留。

模组变更
- cofh_core-11.0.2-scex.dev.5.jar
- thermal_dynamics-11.0.1-scex.dev.5.jar
- thermal_foundation-11.0.7-scex.dev.5.jar
- thermal-11.0.7-scex.dev.5.jar

其他内容
（无）

> 2026/9/16 v2.9.5
怀旧向子服「旧梦」

更新说明
- 热力全家桶更新至 Scex dev.5，包含热力核心、基础、动力与 CoFHCore。
- 神秘视界更新至 0.1.0-scex-dev.34。
- 任务资源包加入新增的神秘视界界面素材；原有 33 项资源保持不变。

模组变更
+ cofh_core-11.0.2-scex.dev.5.jar
+ thaumichorizons-1.21.1-0.1.0-scex-dev.34.jar
+ thermal_dynamics-11.0.1-scex.dev.5.jar
+ thermal_foundation-11.0.7-scex.dev.5.jar
+ thermal-11.0.7-scex.dev.5.jar

其他内容
~ resourcepacks/SCEX-任务图片资源包.zip

> 2026/9/15 v2.9.4
怀旧向子服「旧梦」

更新说明
- 环境科技补齐超能力束能金属矿产出，一级矿机起可用，灰色镜片可定向。
- ExtendedAE Plus 更新至 1.6.2，包含装配矩阵生命周期与倍增样板供能问题修复。
- 超能力更新至 0.0.26，修复念力投掷、念力针的飞行碰撞、弹药选择和退款，恢复弹丸显示。
- 超能力网络协议同步升级，请所有玩家完成客户端更新并重启游戏后再连接。

模组变更
~ [扩展AE加强] extendedae_plus：1.6.1 → 1.6.2
~ AcademyCraft-neoforge-1.21.1：0.0.23-scex-wireless → 0.0.26-scex-projectiles
~ environmentaltech-1.21.1：2.0.0.31 → 2.0.0.32

其他内容
（无）

> 2026/9/13 v2.9.3
怀旧向子服「旧梦」

更新说明
- 更新 Neo ECO AE，使用上游 21.2.0 发布页提供的 21.2.0-beta1。
- 移除 Retro Draconic 1.5.1，保留龙之进化与相关修复。
- 请完成客户端更新后重新启动游戏。

模组变更
~ [Neo ECO AE扩展] neoecoae-21.2.0：hotfix → beta1
- [复古龙之进化] retrodraconic-1.5.1.jar

其他内容
（无）

> 2026/9/13 v2.9.2
怀旧向子服「旧梦」

更新说明
- 修复女仆持拔刀剑时连招时间轴反复扫描空区间造成的服务器卡顿。
- 旧梦拔刀兼容更新至 0.3.0-dev.2，保留战斗连段、伤害和刀养成数据。
- 请完成客户端更新后重新启动游戏。

模组变更
~ slashblade-legacy-compat-0.3.0：dev.1 → dev.2

其他内容
（无）

> 2026/9/13 v2.9.1
怀旧向子服「旧梦」

更新说明
- 修复 Banira 与现役 JEI 的界面兼容问题，避免打开背包等界面时崩溃。
- 仅新增客户端热修补丁；更新后重新启动客户端即可。

模组变更
+ scex-banira-jei-hotfix-1.21.1-1.0.0.jar

其他内容
（无）

> 2026/9/13 v2.9.0
怀旧向子服「旧梦」

更新说明
- 旧梦重铸0.3：F8切换怀旧/重锋模式，保留刀养成数据。
- 更新额外植物学及兼容层、环境科技、神秘自动研究和神秘基础学。
- 修复精妙背包/存储整叠合成大槽位异常。
- 更新商店数据。
- 新增spark性能分析工具；竹叶清以观察模式安装，自动清理与回收仓库关闭。

模组变更
~ environmentaltech-1.21.1：2.0.0.30 → 2.0.0.31
~ SCEX-Botania-ExtraBotany-Compat-1.21.1：1.4.0 → 1.4.1
~ slashblade-legacy-compat：0.2.0-dev.7 → 0.3.0-dev.1
~ TC4AutoResearch-1.21.1：1.2.0-scex.1-rc1 → 1.3.0-scex.1-rc2
~ thaumicbases-2.1.189.32：port.14 → port.15
~ [额外植物学：重燃] extrabotany-neoforge-1.21.1-2.0-scex.6-dev.jar → extrabotany-neoforge-1.21.1-2.0-scex.7-dev.jar
+ aotake_sweep-neoforge-1.21.1-2.0.0-alpha.2-scex.1.jar
+ banira_codex-neoforge-1.21.1-1.0.3.jar
+ scex-crafting-stack-fix-1.0.0.jar

其他内容
（无）

> 2026/9/10 v2.8.0
怀旧向子服「旧梦」

更新说明
- 旧梦重铸 dev.7：恢复整叠耀魂精炼，修正评分同步计算。
- NegoreRouse scex.8：幻影朝向修正，仅供本服玩家同步。
- 新增神秘要素 JEI 查询附属 rc5。
- 神秘能源更新至2.3.15-alpha，配套生命周期兼容修复1.2.0。
- 奇点迭代复古材质包更新至1.2.3，更新精灵学任务图片资源。
- 更新器补齐缺失的模组资源基线，保留玩家额外资源包与个人设置。

模组变更
~ prinegorerouse-1.3.2：scex.7 → scex.8
~ scex-thaumic-lifecycle-fix：1.1.0 → 1.2.0
~ slashblade-legacy-compat-0.2.0：dev.5 → dev.7
~ ThaumicEnergistics-1.21.1-neoforge：2.3.13 → 2.3.15
+ scex-thaumcraft-aspects-jei-1.21.1-1.0.0-rc5.jar

其他内容
+ resourcepacks/IndustrialCraft-Nostalgia-for-SingularityIteration-1.2.3-si-0.1.7.10-CANDIDATE-20260909.3.zip
~ _updater/player-update-generic.ps1
~ _updater/player-update-generic.py
~ resourcepacks/SCEX-任务图片资源包.zip
- resourcepacks/IndustrialCraft-Nostalgia-for-SingularityIteration-1.2.0-si-0.1.7.10-CANDIDATE-20260905.3.zip

> 2026/9/8 v2.7.0
怀旧向子服「旧梦」

更新说明
- 拔刀三件套更新：空中闪避方向、超级SA等修复；NegoreRouse scex7修复六个材料配方的旧标签及屏障原料问题。
- 神秘基础学更新至port14：修复烟斗烟雾遮挡、魔法树生成与掉落逻辑、镰刀持握方向。
- 加入轮盘快捷预设与聊天指令预填脚本；保留玩家已有菜单，手动导入前请备份；背包项需自行设置独立按键。
- 神秘自动研究更新至1.2候选修复版，改进要素补充与研究快捷操作。
- 新增AE爆炸机，提供自动化爆炸配方加工。
- 环境科技ET30保持现役版本；本次没有新增环境科技修复包。
- 退出游戏运行更新器，更新到2.7.0后重新进服。

模组变更
~ prinegorerouse-1.3.2：scex.5 → scex.7
~ si-slashblade-integration-0.1.0：dev.5 → dev.6
~ slashblade-legacy-compat-0.2.0：dev.3 → dev.5
~ TC4AutoResearch-1.21.1：1.1.0 → 1.2.0
~ thaumicbases-2.1.189.32：port.9 → port.14
+ ae2-blast-chamber-1.21.1-neoforge-0.1.0.jar

其他内容
+ config/ezactions/SCEX-轮盘预设说明.txt
+ config/ezactions/scex-preset-2.7.0.json
+ kubejs/client_scripts/type.js
+ kubejs/server_scripts/typecommand.js

> 2026/9/8 v2.6.1
怀旧向子服「旧梦」

更新说明
- 移除BlueMap网页地图模组。
- 退出游戏运行整包更新器至2.6.1后进服。

模组变更
- [蓝图网页地图] bluemap-5.7-neoforge.jar

其他内容
（无）

> 2026/9/8 v2.6.0
怀旧向子服「旧梦」

更新说明
- 修复龙之进化大范围挖掘掉落收集瓶颈及相关收集问题。
- 修复学园都市无线矩阵名称和密码提交确认及同步，双端协议同步升级。
- 更新拔刀附魔、保护规则、Boss奖励与独立锁定按键，修复超SA蓄力松键释放及结算。
- 修复神秘基础学烟草等状态效果图标。
- 环境科技新增神秘花等312项可选采掘产出，产出权重随新表调整。
- 退出游戏运行更新器，更新到2.6.0后重新进服。

模组变更
~ AcademyCraft-neoforge-1.21.1：0.0.22 → 0.0.23
~ environmentaltech-1.21.1：2.0.0.29 → 2.0.0.30
~ slashblade-legacy-compat-0.2.0：dev.1 → dev.3
~ thaumicbases-2.1.189.32：port.8 → port.9

其他内容
（无）

> 2026/9/8 v2.5.1
怀旧向子服「旧梦」

更新说明
- 修复新版Voxy打开包含aux_beacons等额外数据表的旧缓存时进服崩溃，保留额外数据。
- 仅客户端新增兼容补丁；请完全退出游戏后运行更新脚本，不要删除原Voxy缓存。

模组变更
+ scex-voxy-column-family-compat-1.0.0.jar

其他内容
（无）

> 2026/9/8 v2.5.0
怀旧向子服「旧梦」

更新说明
- 拔刀怀旧玩法以1.7.10 r87为基准重做动作、连段、伤害、幻影剑、附魔与耐久。
- 同步更新NR复刻附属及奇点迭代拔刀集成，保留附属刀定义、SA/SE及电刀能量规则。
- 修复部分NR剑技漏选盖亚等可攻击目标的问题，重锋版本改为软绑定。
- 退出游戏运行整合包更新脚本，更新至2.5.0再进入服务器。

模组变更
~ prinegorerouse-1.3.2：scex.3 → scex.5
~ si-slashblade-integration-0.1.0：dev.4.1 → dev.5
~ slashblade-legacy-compat：0.1.0-dev.13 → 0.2.0-dev.1

其他内容
（无）

> 2026/9/7 v2.4.2
怀旧向子服「旧梦」

更新说明
- 修复ME扩展样板供应器等设备在Jade中缺少在线状态的问题。
- 拔刀怀旧兼容更新至dev13，包含第一人称持刀修正及退出世界后重进的配置生命周期修复。
- 新增末影接口磨粉机、奇点迭代打粉机的钨锭转钨粉配方。
- 更新Windows客户端Voxy远景渲染与配套Sodium；本轮完整光影验收使用8 GiB客户端堆。
- 退出游戏后运行整合包内更新脚本，更新至2.4.2再进入服务器。

模组变更
~ slashblade-legacy-compat-0.1.0：dev.11 → dev.13
~ [应用植物学] applied-botanics-1.21.1-neoforge-21.1.243-botania-456-appbot-20260823-2303-full-materials.jar → applied-botanics-1.21.1-neoforge-21.1.243-botania-456-scex-jade1.jar
~ [钠] sodium-neoforge-0.8.12+mc1.21.1.jar → sodium-neoforge-0.8.13+mc1.21.1.jar
+ voxy-0.2.9-alpha+sodium0.8.13-windows-x64-lite.jar
- [Voxy远景渲染] neo-voxy-0.4.3-beta.1-mc1.21.1-neoforge-integrations.jar

其他内容
+ kubejs/data/scex/recipe/enderio/tungsten_ingot_to_dust.json
+ kubejs/data/scex/recipe/singularity_iteration/tungsten_ingot_to_dust.json

> 2026/9/7 v2.4.1
怀旧向子服「旧梦」

更新说明
- 修复拔刀连续右键动作与横斩剑气方向。
- 加快空中下劈并修复落地动作衔接。
- 修复剑气实体击退值为空时的保存异常。
- 退出游戏后运行整合包内更新脚本，更新至2.4.1再进入服务器。

模组变更
~ slashblade-legacy-compat-0.1.0：dev.10 → dev.11

其他内容
（无）

> 2026/9/7 v2.4.0
怀旧向子服「旧梦」

更新说明
- 更新神秘能源并同步Vis供能、P2P及区块卸载兼容补丁。
- 新增简易磁铁及所需前置。
- 拔刀旧版兼容升级dev10，合并动作、飞刀及攻击事件边界修复。
- 超能力升级0.0.22，修复无线能量守恒并调整相关界面。
- 任务图片资源包新增3张图片，保持原启用方式。
- 本次更新部署后继续停服，等待服主重启电脑及开服验收，恢复时间另行通知。
- 完全退出Minecraft后运行包内更新脚本；私用附属仅限本服务器玩家使用。

模组变更
~ AcademyCraft-neoforge-1.21.1：0.0.21-scex-charging → 0.0.22-scex-wireless
~ slashblade-legacy-compat-0.1.0：dev.7 → dev.10
~ [神秘能源] ThaumicEnergistics-1.21.1-neoforge-2.3.5-alpha-scex.1.jar → ThaumicEnergistics-1.21.1-neoforge-2.3.13-alpha.jar
+ scex-thaumic-lifecycle-fix-1.1.0.jar
+ simplemagnets-1.1.12c-neoforge-mc1.21.jar
+ supermartijn642configlib-1.1.8-neoforge-mc1.21.jar
+ supermartijn642corelib-1.1.24-neoforge-mc1.21.jar

其他内容
~ resourcepacks/SCEX-任务图片资源包.zip

> 2026/9/6 v2.3.0
怀旧向子服「旧梦」

更新说明
- 神话植物学修复精灵魔力戒无法充放魔力，恢复背包及饰品槽供魔，保留收集器与芬布尔之冬修复。
- 环境科技修复旧世界矿机组装与组装杆放置问题。
- 神秘研究自动化改进递归要素合成、库存权限同步和界面操作。
- 新增拔刀剑旧版战斗兼容，调整连段、幻影飞刀与收刀修刀。
- 新增奇点迭代×拔刀剑电力刀联动及NegoreRouse；伤害遵守无敌、取消与上限规则，部分旧版强制秒杀效果改变。
- 相关私用附属仅限本服务器玩家私下同步，禁止公开转载或分发。
- 完全退出Minecraft，运行整合包内更新脚本，完成后再连接服务器。

模组变更
~ environmentaltech-1.21.1：2.0.0.28 → 2.0.0.29
~ [神话植物学] mythicbotany-5.0.0-neoforge-1.21.1-scex.2-fimbultyr-mana-network-fix.jar → mythicbotany-5.0.0-neoforge-1.21.1-scex.3.jar
~ [神秘研究自动化] TC4AutoResearch-1.21.1-1.0.0-scex.1.jar → TC4AutoResearch-1.21.1-1.1.0-scex.1-rc1.jar
+ prinegorerouse-1.3.2-scex.3-dev.jar
+ si-slashblade-integration-0.1.0-dev.4.1.jar
+ slashblade-legacy-compat-0.1.0-dev.7.jar

其他内容
（无）

> 2026/9/6 v2.2.1
怀旧向子服「旧梦」

更新说明
- 紧急修复神话植物学魔力收集器导致专用服务器崩溃的问题，保留既有芬布尔之冬修复。
- 本次仅替换神话植物学，其他模组保持2.2.0版本。
- 完全退出Minecraft，运行整合包内更新脚本，完成后再连接服务器。

模组变更
~ [神话植物学] mythicbotany-5.0.0-neoforge-1.21.1：botania-456-neoforge-21.1.243-fimbultyr-fixed → scex.2-fimbultyr-mana-network-fix

其他内容
（无）

> 2026/9/5 v2.2.0
怀旧向子服「旧梦」

更新说明
- 奇点迭代升级0.1.7.10，同步更新分子重组仪渲染与工业怀旧材质，适配新增机器及线缆。
- Woot优化模拟掉落临时对象开销并修复相关模拟异常；环境科技修复界面槽位与重叠结构识别，补充可选矿物支持。
- 神秘时代及附属更新，神秘基础学修正节点调节器朝向与超限附魔台边框，禁忌魔法补齐元始笔墨修复。
- 额外植物学新增活石桶合成，盖亚三允许携装召唤并在战斗中缴械不允许的装备。
- 超能力修复节点名称、密码与权限同步，补充材质；电流回冲发电倍率提高至2.5倍，整数接口连续使用累计等比，单刻与短按受取整影响。
- 修复配方、标签及资源路径问题，清理四条无效配方。
- 更正此前预告：本轮为额外植物学修复，植物魔法本体不升级。
- 完全退出Minecraft，运行整合包内更新脚本，完成后再连接服务器。

模组变更
~ [额外植物学：重燃] extrabotany-neoforge-1.21.1-2.0：scex.5 → scex.6
~ [方块小镇] yuushya：1.21.0-neoforge-2.3.0 → 2.3.0-scex.1
~ [分子重组仪：怀旧渲染] MolecularTransformer-LegacyRenderer：1.0.8 → 1.0.9-candidate
~ [禁忌魔法] forbiddenmagic-1.0.0：port.28 → port.29-scex.1
~ [森罗物语：下界] kaleidoscope_nether-1.1.4-neoforge：mc1.21.1 → mc1.21.1-scex.1
~ [神秘时代] thaumcraft-0.2.2.95：port.240 → port.242
~ [SI] SingularityIteration：0.1.7.9 → 0.1.7.10
~ AcademyCraft-neoforge-1.21.1：0.0.19-rebuilt → 0.0.21-scex-charging
~ environmentaltech-1.21.1：2.0.0.25 → 2.0.0.28
~ scex_woot_draconic_compat：1.0.0 → 1.0.1
~ SCEX-Botania-ExtraBotany-Compat-1.21.1：1.3.0 → 1.4.0
~ thaumicbases-2.1.189.32：port.6 → port.8
~ [刷怪工厂] woot-revived-21.1.1.10：kjs → kjs-scex.1
~ [节点机制] nodalmechanics-1.0.0-port.6.jar
~ [群系侦测] biomespy-neoforge-1.21.1-1.3.3.jar
~ [神秘工匠] thaumic_tinkerer-1.0.0-port.59.jar
~ [天界神秘学] thaumcraftcelestial-1.0.0-port.24.jar
~ [污秽魔法] taintedmagic-1.0.0-port.29.jar

其他内容
+ kubejs/server_scripts/scex_recipe_tag_repairs.js
+ resourcepacks/IndustrialCraft-Nostalgia-for-SingularityIteration-1.2.0-si-0.1.7.10-CANDIDATE-20260905.3.zip
- resourcepacks/IndustrialCraft-Nostalgia-for-SingularityIteration-1.1.0-si-0.1.7.9.zip

> 2026/9/5 v2.1.0
怀旧向子服「旧梦」

更新说明
- 神秘基础学升级至 port.6，修复八种晶体簇完全透明、节点调节核心显示尺寸过大的问题。
- 修正搬运器透明度，并将火盆名称统一为“奥术火盆”。
- 完全退出 Minecraft，运行整合包内的更新脚本，完成后再进入服务器。

模组变更
~ thaumicbases-2.1.189.32：port.5 → port.6

其他内容
（无）

> 2026/9/5 v2.0.0
怀旧向子服「旧梦」

更新说明
- 修复 Woot 与龙之研究末影龙掉落模拟导致的服务器死锁。
- 修复森林法杖绑定额外植物学产能花、魔力池及魔力链接花的问题，并修复链接保存。
- 修复奇点迭代能源网络计算中反复排序电压等级造成的性能问题，降低大型网络计算开销。
- 升级额外植物学、奇点迭代与配套怀旧材质和分子重组仪渲染。
- 新增模块化路由器、无月光版试验假人、环境科技、神秘基础学与超能力。
- 修复神秘能源注魔监视器导致的停服保存卡住问题，以及元始笔墨耐久问题。
- 完全退出 Minecraft 后运行整合包更新脚本，完成后再进入服务器。

模组变更
~ [额外植物学：重燃] extrabotany-neoforge-1.21.1-2.0：scex.1-gaia3-hotfix → scex.5-dev
~ [分子重组仪：怀旧渲染] MolecularTransformer-LegacyRenderer：1.0.7 → 1.0.8
~ [SI] SingularityIteration：0.1.7.7 → 0.1.7.9
+ AcademyCraft-neoforge-1.21.1-0.0.19-rebuilt.jar
+ dummmmmmy-neoforge-1.21-2.1.0-scex.private.1.jar
+ environmentaltech-1.21.1-2.0.0.25-scex-dev.jar
+ modular-routers-13.2.7+mc1.21.1.jar
+ scex_woot_draconic_compat-1.0.0-neoforge-1.21.1.jar
+ SCEX-Botania-ExtraBotany-Compat-1.21.1-1.3.0.jar
+ thaumicbases-2.1.189.32-port.5.jar
~ [禁忌魔法] forbiddenmagic-1.0.0-port.28.jar
+ SI 能源网络性能修复补丁 1.0.0（服务端）。
+ 神秘能源生命周期修复补丁 1.0.0（服务端），修复区块卸载和停服保存。

其他内容
+ resourcepacks/IndustrialCraft-Nostalgia-for-SingularityIteration-1.1.0-si-0.1.7.9.zip
- resourcepacks/IndustrialCraft-Nostalgia-for-SingularityIteration-1.0.6.zip

> 2026/9/3 v1.7.0
怀旧向子服「旧梦」

更新说明
- 永恒常春藤升级到 0.2.1-assets。
- 补齐中文名称并修复物品缺失贴图。
- 补充许可证与来源记录；物品 ID、注册名、合成配方和存档语义保持不变。
- 更新器仅清理旧版永恒常春藤，保留玩家额外模组、存档和个人配置。

模组变更
~ SCEX-Timeless-Ivy-1.21.1：0.2.0-core → 0.2.1-assets

其他内容
~ 补齐“永恒常春藤”中文名称与物品贴图。
~ 补充模组许可证与来源记录。

> 2026/9/2 v1.6.0
怀旧向子服「旧梦」

更新说明
- 神秘时代升级到 port.240，禁忌魔法升级到 port.28；神秘工匠、污秽魔法、节点机制和天界神秘学同步为同批兼容构建。
- 修复源质缓存管道多出口崩溃、留影水晶与暴怒之笼、工艺权杖核心、妖魔之叉和炽心镐蕴魔石标记等问题。
- 同步更新 ViScriptShop 商店数据和任务图片资源包。
- 六个神秘模组必须成套更新，不得混用旧本体或附属；更新器会保留无关的玩家额外模组、存档和个人配置。

模组变更
~ [禁忌魔法] forbiddenmagic-1.0.0：port.26 → port.28
~ [神秘时代] thaumcraft-0.2.2.95：port.238 → port.240
~ [节点机制] nodalmechanics-1.0.0-port.6.jar
~ [神秘工匠] thaumic_tinkerer-1.0.0-port.59.jar
~ [天界神秘学] thaumcraftcelestial-1.0.0-port.24.jar
~ [污秽魔法] taintedmagic-1.0.0-port.29.jar

其他内容
~ resourcepacks/SCEX-任务图片资源包.zip
~ ViScriptShop 商店数据与任务图片资源包同步更新。

> 2026/9/2 v1.5.2
怀旧向子服「旧梦」

更新说明
- 任务图片资源包新增 IC2 任务界面标识图片。
- 本次为客户端资源增量更新，不需要停服。
- 更新器继续保留玩家额外模组、存档和个人配置。

模组变更
（无）

其他内容
~ resourcepacks/SCEX-任务图片资源包.zip
~ SCEX 任务图片资源包：新增 IC2 任务界面图片。

> 2026/9/2 v1.5.1
怀旧向子服「旧梦」

更新说明
- 更新 SCEX 任务图片资源包，补充最新任务界面所需图片。
- 本次为客户端资源更新，不需要停服。
- 更新器继续保留玩家额外模组、存档和个人配置。

模组变更
（无）

其他内容
~ resourcepacks/SCEX-任务图片资源包.zip
~ SCEX 任务图片资源包：同步最新任务图片。

> 2026/9/2 v1.5.0
怀旧向子服「旧梦」

更新说明
- 商店 AE2 连接器升级到 0.3.3：离线、断电、缺频道或未组网时显示静态未激活外观，正常联网时显示慢速平滑彩色动画。
- 物品栏和手持连接器改为无彩色基础外观，便于区分放置后的网络状态。
- 同步更新 ViScriptShop 商店内容和玩家阶段脚本。
- 本次按维护授权跳过额外客户端测试；更新器继续保留玩家额外模组、存档和个人配置。

模组变更
~ [商店AE2联动] scex-viscriptshop-ae2-bridge-neoforge-1.21.1：0.2.0 → 0.3.3

其他内容
~ kubejs/server_scripts/shopstage.js
~ ViScriptShop 商店内容和玩家阶段脚本同步更新。

> 2026/9/2 v1.4.0
怀旧向子服「旧梦」

更新说明
- Singularity Iteration 升级到 0.1.7.7，包含新版机器、配方与相关修正。
- 分子重组仪怀旧渲染器同步升级到 1.0.7，已适配并严格匹配 SI 0.1.7.7。
- 渲染器已通过隔离客户端方块/物品渲染烟雾测试；SI 与客户端渲染器必须成对更新。
- 更新器只替换两件明确旧文件，并继续保留玩家额外模组、存档和个性配置。

模组变更
~ [分子重组仪：怀旧渲染] MolecularTransformer-LegacyRenderer：1.0.6 → 1.0.7
~ [SI] SingularityIteration：0.1.7.5 → 0.1.7.7

其他内容
（无）

> 2026/9/2 v1.3.0
怀旧向子服「旧梦」

更新说明
- 新增 ME 商店连接器：玩家可自行合成并放置连接器，将原生 ViScriptShop 交易连接到自己的 AE2 网络。
- 物品支付优先从 ME 网络扣除，不足部分再使用背包；购买的物品奖励可直接进入同一 ME 网络。
- 连接器离线、缺失或区块未加载时自动回退为原生背包交易；交易前会检查容量并使用持久事务日志保护异常中断恢复。
- 该模组需要客户端与服务端同时安装；更新器继续保留玩家额外模组、存档和个性配置。

模组变更
+ [商店AE2联动] scex-viscriptshop-ae2-bridge-neoforge-1.21.1-0.2.0.jar

其他内容
（无）

> 2026/9/1 v1.2.0
怀旧向子服「旧梦」

更新说明
- 修复 ExtraBotany Gaia III Challenge Ticket 召唤时引用失效 Botania 音效字段导致的服务器崩溃。
- 修复 ThaumicEnergistics 奥术合成终端为法杖补充 Vis 时反复计算原质集合，导致服务线程卡死并触发看门狗的问题。
- 本次替换两个双端 JAR；玩家运行更新器后会移除明确列出的旧版本，不影响额外模组、存档和个性配置。

模组变更
~ [额外植物学：重燃] extrabotany-neoforge-1.21.1-2.0：SNAPSHOT-patched → scex.1-gaia3-hotfix
~ [神秘能源] ThaumicEnergistics-1.21.1-neoforge-2.3.5：alpha → alpha-scex.1

其他内容
（无）

> 2026/9/1 v1.1.0
怀旧向子服「旧梦」

更新说明
- 新增 TC4 Auto Research 1.0.0-scex.1，为神秘时代研究桌提供自动解题、重试、自动模式、要素发现与批量合成辅助。
- 新增 TweakerMoreForge 0.0.8，作为 DLC Manager 中的可选功能辅助模组，依赖现役 MaFgLib。
- 更新 ViScriptShop 商店内容，并新增基于下界进度补发 nether 商店阶段的逻辑。
- DLC 包已移除未完成下载缓存并清理本机绝对路径；玩家额外模组、存档和个性配置继续保留。

模组变更
+ [神秘研究自动化] TC4AutoResearch-1.21.1-1.0.0-scex.1.jar
+ [功能辅助] TweakerMoreForge 0.0.8（DLC 可选）

其他内容
+ DLC/07-功能辅助/tweakermore.json
+ DLC/info/TweakerMoreConfig.dc
+ DLC/remote/07-功能辅助/tweakermore.dc
+ kubejs/server_scripts/shopstage.js
~ ViScriptShop 商店数据（服务端）

> 2026/8/31 v1.0.38
怀旧向子服「旧梦」

更新说明
- 更新 ViScriptShop 商店内容，扩充商品分类与兑换项目。
- 本次为服务端商店数据更新，玩家无需下载新的模组或配置文件。

模组变更
（无）

其他内容
（无）

> 2026/8/31 v1.0.37
怀旧向子服「旧梦」

更新说明
- 修复 Jade 不显示 AE2 设备在线状态。
- 新增 Woot Revived、RE:Constructed Wands（KOTS 兼容复刻）与 Polymorphic Energistics。
- 修复石英粉碎与高纯玫瑰石英动力锯的重复配方，统一石英粉、铁粒与硅块标签。
- 机械动力扳手加入 FTB 连锁严格排除清单，避免扳手拆卸与连锁同时触发造成物品丢失。
- 请完全退出 Minecraft 后运行更新器；更新器保留玩家额外模组、存档和其他个性配置。

模组变更
+ [建筑法杖：KOTS兼容复刻] constructionwand-kots-1.21.1-2.16.12.jar
+ [刷怪工厂] woot-revived-21.1.1.10-kjs.jar
+ [AE2多配方兼容] polyeng-0.4.1.jar

其他内容
+ kubejs/data/c/tags/block/storage_blocks/silicon.json
+ kubejs/data/c/tags/item/dusts/quartz.json
+ kubejs/data/c/tags/item/nuggets/iron.json
+ kubejs/data/c/tags/item/storage_blocks/silicon.json
+ kubejs/data/ftbultimine/tags/item/excluded_tools/strict.json
+ kubejs/server_scripts/scex_recipe_conflict_fixes.js

> 2026/8/30 v1.0.36
怀旧向子服「旧梦」

更新说明
- 新增 KubeJS 与 Rhino，作为服务器定制内容基础组件。
- 新增实体货币与钱夹，可兑换为 ViScriptShop 商店余额。
- 部署新版商店数据与任务内容，加入商店引导、阶段解锁与货币奖励。
- 请完全退出 Minecraft 后运行更新器；更新器保留玩家额外模组、存档和个性配置。

模组变更
+ [脚本系统] kubejs-neoforge-2101.7.2-build.374.jar
+ [JavaScript引擎] rhino-2101.2.7-build.81.jar

其他内容
+ kubejs/assets/kubejs/textures/block/example_block.png
+ kubejs/assets/kubejs/textures/item/example_item.png
+ kubejs/assets/scex/textures/item/coin_1.png
+ kubejs/assets/scex/textures/item/coin_2.png
+ kubejs/assets/scex/textures/item/coin_3.png
+ kubejs/assets/scex/textures/item/coin_bag.png
+ kubejs/server_scripts/coin.js
+ kubejs/startup_scripts/coin.js

> 2026/8/30 v1.0.35

更新说明：  
- 升级奇点迭代至 0.1.7.5-beta。
- 新增 SCEX 永恒常春藤 0.2.0-core，支持将永恒常春藤附着到可修复物品并消耗植物魔法魔力进行修复。
- 新增 ExtendedAE 1.21-2.2.35-neoforge 与 ME Requester 1.21.1-1.4.3，扩展 AE2 样板供应与库存请求功能。
- 更新分子重组仪怀旧渲染器至 1.0.6，适配 SI 0.1.7.5-beta。
- 新增 AppliedFlux 1.21-2.1.5-neoforge，提供 AE2 能源存储单元。
- 客户端发行源移除重复的 Curios 9.0.15，仅保留与服务端一致的 Curios 9.5.1。
- 请完全退出 Minecraft 后运行更新器；更新器保留玩家额外模组、存档和个性配置。

模组变更：  
```text
~ [分子重组仪：怀旧渲染] MolecularTransformer-LegacyRenderer：1.0.5 → 1.0.6
+ [AppliedFlux] AppliedFlux-1.21-2.1.5-neoforge.jar
```

其他内容：  
```text
~ config/voxy-config.json
~ config/viscript_shop_config.toml
~ resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
~ resourcepacks/SCEX-任务图片资源包.zip
~ config/dlc_manager/config.dc
~ mods/[强制汉化资源] SCEX-Localization-1.0.0-neoforge-1.21.1.jar
~ mods/[应用能源2：水晶科学] ae2cs-1.21.1-1.2.1.jar
~ mods/[应用能源2：JEI联动] ae2jeiintegration-1.2.1.jar
~ mods/Just-Enough-Botania-NeoForge-1.21.1-1.0.0-scex.1.jar
~ mods/SCEX-SJAP-Compat-1.0.0.jar
~ mods/[分子重组仪：怀旧渲染] MolecularTransformer-LegacyRenderer-1.0.6.jar
~ resourcepacks/IndustrialCraft-Nostalgia-for-SingularityIteration-1.0.6.zip
… 以及另外 6 项
```

> 2026/8/30 v1.0.34

更新说明：  
- 升级奇点迭代至 0.1.7.5-beta。
- 新增 SCEX 永恒常春藤 0.2.0-core，支持将永恒常春藤附着到可修复物品并消耗植物魔法魔力进行修复。
- 新增 ExtendedAE 1.21-2.2.35-neoforge 与 ME Requester 1.21.1-1.4.3，扩展 AE2 样板供应与库存请求功能。
- 客户端发行源移除重复的 Curios 9.0.15，仅保留与服务端一致的 Curios 9.5.1。
- 请完全退出 Minecraft 后运行更新器；更新器保留玩家额外模组、存档和个性配置。

模组变更：  
```text
~ [奇点迭代] SingularityIteration-0.1.7.3.1-scex-dsfix.jar → [SI] SingularityIteration-0.1.7.5-beta.jar
+ [ME请求器] MERequester-NeoForge-1.21.1-1.4.3.jar
+ SCEX-Timeless-Ivy-1.21.1-0.2.0-core.jar
- [饰品栏API] curios-neoforge-9.0.15+1.21.1.jar
```

其他内容：  
```text
~ config/voxy-config.json
~ config/viscript_shop_config.toml
~ resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
~ resourcepacks/SCEX-任务图片资源包.zip
~ config/dlc_manager/config.dc
~ mods/[强制汉化资源] SCEX-Localization-1.0.0-neoforge-1.21.1.jar
~ mods/[应用能源2：水晶科学] ae2cs-1.21.1-1.2.1.jar
~ mods/[应用能源2：JEI联动] ae2jeiintegration-1.2.1.jar
~ mods/Just-Enough-Botania-NeoForge-1.21.1-1.0.0-scex.1.jar
~ mods/SCEX-SJAP-Compat-1.0.0.jar
~ mods/[分子重组仪：怀旧渲染] MolecularTransformer-LegacyRenderer-1.0.5.jar
~ resourcepacks/IndustrialCraft-Nostalgia-for-SingularityIteration-1.0.6.zip
… 以及另外 5 项
```

> 2026/8/29 v1.0.33

更新说明：  
- 1.0.32 客户端包在发布后复核发现压缩完整性问题，现以 1.0.33 重新打包发布。
- 修复森林法杖 Shift+右键魔力池时 ExtraBotany 与 Botania 456 的声音字段兼容崩溃；本版 JAR 已通过完整 ZIP 校验。
- 请完全退出 Minecraft 后运行更新器；更新器保留玩家额外模组、存档和配置。若仍有问题，请上传新的崩溃报告和更新器完整输出。

模组变更：  
```text
~ [额外植物学：重燃] extrabotany-neoforge-1.21.1-2.0-SNAPSHOT-patched.jar
```

其他内容：  
```text
~ config/voxy-config.json
~ config/viscript_shop_config.toml
~ resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
~ resourcepacks/SCEX-任务图片资源包.zip
~ config/dlc_manager/config.dc
~ mods/[强制汉化资源] SCEX-Localization-1.0.0-neoforge-1.21.1.jar
~ mods/[应用能源2：水晶科学] ae2cs-1.21.1-1.2.1.jar
~ mods/[应用能源2：JEI联动] ae2jeiintegration-1.2.1.jar
~ mods/Just-Enough-Botania-NeoForge-1.21.1-1.0.0-scex.1.jar
~ mods/SCEX-SJAP-Compat-1.0.0.jar
~ mods/[奇点迭代] SingularityIteration-0.1.7.3.1-scex-dsfix.jar
~ mods/[分子重组仪：怀旧渲染] MolecularTransformer-LegacyRenderer-1.0.5.jar
… 以及另外 2 项
```

> 2026/8/29 v1.0.32

更新说明：  
- 修复怀旧服客户端使用森林法杖 Shift+右键魔力池时的崩溃：ExtraBotany 与 Botania 456 的声音字段兼容性已修正。
- 服务端与客户端使用同一修复 JAR，玩家请退出游戏后运行更新器获取；不删除玩家额外模组、存档或配置。
- 若仍遇到崩溃，请上传最新崩溃报告和更新器完整输出。

模组变更：  
```text
~ [额外植物学：重燃] extrabotany-neoforge-1.21.1-2.0-SNAPSHOT-patched.jar
```

其他内容：  
```text
~ config/voxy-config.json
~ config/viscript_shop_config.toml
~ resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
~ resourcepacks/SCEX-任务图片资源包.zip
~ config/dlc_manager/config.dc
~ mods/[强制汉化资源] SCEX-Localization-1.0.0-neoforge-1.21.1.jar
~ mods/[应用能源2：水晶科学] ae2cs-1.21.1-1.2.1.jar
~ mods/[应用能源2：JEI联动] ae2jeiintegration-1.2.1.jar
~ mods/Just-Enough-Botania-NeoForge-1.21.1-1.0.0-scex.1.jar
~ mods/SCEX-SJAP-Compat-1.0.0.jar
~ mods/[奇点迭代] SingularityIteration-0.1.7.3.1-scex-dsfix.jar
~ mods/[分子重组仪：怀旧渲染] MolecularTransformer-LegacyRenderer-1.0.5.jar
… 以及另外 2 项
```

> 2026/8/29 v1.0.31

更新说明：  
- 新增 BotaniaJEI 1.0.0-scex.1：在 JEI 中显示 Botania 配方的魔力数值和纯净雏菊处理时间。
- 新增 SCEX-SJAP-Compat 1.0.0：补齐大地之刃与西风太刀的定义、模型、配方和中英文名；客户端与服务端同版。
- 本次维护包含怀旧服服务端停服、备份和健康检查；玩家退出游戏后运行更新器即可获取客户端文件。
- 同步器继续保留玩家额外模组、资源包、配置和本地删除状态，不清理玩家数据。

模组变更：  
```text
+ Just-Enough-Botania-NeoForge-1.21.1-1.0.0-scex.1.jar
+ SCEX-SJAP-Compat-1.0.0.jar
```

其他内容：  
```text
~ config/voxy-config.json
~ config/viscript_shop_config.toml
~ resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
~ resourcepacks/SCEX-任务图片资源包.zip
~ config/dlc_manager/config.dc
~ mods/[强制汉化资源] SCEX-Localization-1.0.0-neoforge-1.21.1.jar
~ mods/[应用能源2：水晶科学] ae2cs-1.21.1-1.2.1.jar
~ mods/[应用能源2：JEI联动] ae2jeiintegration-1.2.1.jar
~ mods/Just-Enough-Botania-NeoForge-1.21.1-1.0.0-scex.1.jar
~ mods/SCEX-SJAP-Compat-1.0.0.jar
~ mods/[奇点迭代] SingularityIteration-0.1.7.3.1-scex-dsfix.jar
~ mods/[分子重组仪：怀旧渲染] MolecularTransformer-LegacyRenderer-1.0.5.jar
… 以及另外 1 项
```

> 2026/8/29 v1.0.30

更新说明：  
- 新增 Inventory Profiles Next 2.2.5：提供背包整理、物品移动和自动重装等客户端便利功能。
- 同步新增必需前置 libIPN 6.6.3；现有 Kotlin for Forge 5.12.0 满足加载要求。
- 按整合包预设关闭“自动重装 → 在启用的槽位上显示图标”，避免槽位左上角出现额外提示图标。
- 该设置只作为首次安装默认值下发，不永久覆盖玩家之后的个人配置。
- 本次仅更新玩家客户端和 18088 清单，不需要重启怀旧服；退出游戏后运行更新器并重新启动客户端即可。

模组变更：  
```text
+ [背包整理] InventoryProfilesNext-neoforge-1.21.1-2.2.5.jar
+ [背包整理前置库] libIPN-neoforge-1.21.1-6.6.3.jar
```

其他内容：  
```text
+ config/inventoryprofiles.json
~ config/voxy-config.json
~ config/viscript_shop_config.toml
~ resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
~ resourcepacks/SCEX-任务图片资源包.zip
~ config/dlc_manager/config.dc
~ mods/[强制汉化资源] SCEX-Localization-1.0.0-neoforge-1.21.1.jar
~ mods/[应用能源2：水晶科学] ae2cs-1.21.1-1.2.1.jar
~ mods/[应用能源2：JEI联动] ae2jeiintegration-1.2.1.jar
~ mods/[奇点迭代] SingularityIteration-0.1.7.3.1-scex-dsfix.jar
~ mods/[分子重组仪：怀旧渲染] MolecularTransformer-LegacyRenderer-1.0.5.jar
~ resourcepacks/IndustrialCraft-Nostalgia-for-SingularityIteration-1.0.6.zip
```

> 2026/8/29 v1.0.29

更新说明：  
- 新增 AE2 Crystal Science 1.2.1 与 AE2 JEI Integration 1.2.1；已按现有 AE2 19.2.17、JEI 19.44.0.405、NeoForge 21.1.248 核对依赖范围。
- 奇点迭代由 0.1.7.1 更新至 0.1.7.3.1 SCEX 专服热修版；修复上游 0.1.7.3 在专用服务端误加载客户端类导致的启动崩溃。
- 分子重组仪怀旧渲染同步更新至 1.0.5，依赖已精确匹配奇点迭代专服热修版。
- 工业复古材质包更新至 1.0.6 并由更新器强制启用；任务数据与任务图片资源包同步替换为下载目录的新版本。
- QQ 公告链路改为 UTF-8 文件传递，避免 Windows PowerShell 到 WSL 的标准输入代码页转换导致中文乱码。
- 本版包含服务端内容模组与任务数据更新；完成维护并退出游戏后重新启动客户端再进入服务器。

模组变更：  
```text
~ [分子重组仪：怀旧渲染] MolecularTransformer-LegacyRenderer：1.0.3 → 1.0.5
~ [奇点迭代] SingularityIteration：0.1.7.1-beta → 0.1.7.3.1-scex-dsfix
+ [应用能源2：水晶科学] ae2cs-1.21.1-1.2.1.jar
+ [应用能源2：JEI联动] ae2jeiintegration-1.2.1.jar
```

其他内容：  
```text
+ resourcepacks/IndustrialCraft-Nostalgia-for-SingularityIteration-1.0.6.zip
~ resourcepacks/SCEX-任务图片资源包.zip
- resourcepacks/IndustrialCraft-Nostalgia-for-SingularityIteration-1.0.5.zip
~ config/voxy-config.json
~ config/viscript_shop_config.toml
~ resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
~ resourcepacks/SCEX-任务图片资源包.zip
~ config/dlc_manager/config.dc
~ mods/[强制汉化资源] SCEX-Localization-1.0.0-neoforge-1.21.1.jar
~ mods/[应用能源2：水晶科学] ae2cs-1.21.1-1.2.1.jar
~ mods/[应用能源2：JEI联动] ae2jeiintegration-1.2.1.jar
~ mods/[奇点迭代] SingularityIteration-0.1.7.3.1-scex-dsfix.jar
~ mods/[分子重组仪：怀旧渲染] MolecularTransformer-LegacyRenderer-1.0.5.jar
~ resourcepacks/IndustrialCraft-Nostalgia-for-SingularityIteration-1.0.6.zip
```

> 2026/8/29 v1.0.28

更新说明：  
- 修复汉化资源包已下载但未实际启用的问题：新增 SCEX 强制汉化资源伴生模组，翻译现在随 NeoForge 的 mod_resources 自动加载，不再只依赖玩家资源包列表。
- 更新器会补建缺失的 options.txt、固定简体中文，并再次校正汉化包优先级；已有玩家其他资源包仍然保留。
- 精确清理一个重复的 0Pack2Reload、无效的 Fabric 版自动汉化更新器，以及误放在 mods 目录中的 75 MB 整包；不会删除玩家自行添加的其他模组。
- Relics 0.12.8 的 547 个翻译键已逐项覆盖；更新完成后必须完整退出游戏进程再重新启动。

模组变更：  
```text
+ [强制汉化资源] SCEX-Localization-1.0.0-neoforge-1.21.1.jar
- [重复件：资源包惰性重载] 0Pack2Reload-NeoForge-1.21.1-1.0.1.jar
- [自动汉化更新] I18nUpdateMod-3.7.0-all.jar
- [SCEX资源包] scex legacy genesis ver1.0.zip
```

其他内容：  
```text
~ _updater/player-update-generic.ps1
~ _updater/player-update-generic.py
~ config/voxy-config.json
~ config/viscript_shop_config.toml
~ resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
~ resourcepacks/SCEX-任务图片资源包.zip
~ config/dlc_manager/config.dc
~ mods/[强制汉化资源] SCEX-Localization-1.0.0-neoforge-1.21.1.jar
```

> 2026/8/28 v1.0.27

更新说明：  
- 新增 Applied Create 1.1.7（应用机械动力），在机械动力与应用能源 2 之间提供应力存储、P2P 通道、样板供应器等联动内容。
- 该模组为双端内容模组，服务器与玩家客户端必须同时安装；Create 6.0.10、AE2 19.2.17 和 Kotlin for Forge 5.12.0 前置均已满足。
- 1.0.27 同时包含 1.0.26 的神秘系六 MOD 更新；未运行上一版更新器的玩家可以直接更新到本版。
- 更新完成后请完整退出游戏再重新启动。

模组变更：  
```text
+ [应用机械动力] appliedcreate-1.21.1-1.1.7.jar
```

其他内容：  
```text
~ config/voxy-config.json
~ config/viscript_shop_config.toml
~ resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
~ resourcepacks/SCEX-任务图片资源包.zip
~ config/dlc_manager/config.dc
```

> 2026/8/28 v1.0.26

更新说明：  
- 神秘系六 MOD 更新为 2026-08-28 同批构建：神秘时代 port.238、神秘工匠 port.59、禁忌魔法 port.26，并同步替换节点机制、污秽魔法和天界神秘学的同批哈希版本。
- 修复 BUG 站 #315–#325 中的通用黑染料与木材标签、法杖末端 Vis 抽取、蕴魔石显示、地狱火蝠行为、村庄池兼容等问题，并确认 #313 的 JEI 虚拟要素输入撤回无残留。
- 更新器会精确备份并移除上一版神秘时代 port.237、神秘工匠 port.58、禁忌魔法 port.25；不会删除玩家自行添加的其他模组。
- 六个 JAR 必须成套更新，禁止新旧版本共存；更新完成后请完整退出游戏再重新启动。

模组变更：  
```text
~ [禁忌魔法] forbiddenmagic-1.0.0：port.25 → port.26
~ [神秘工匠] thaumic_tinkerer-1.0.0：port.58 → port.59
~ [神秘时代] thaumcraft-0.2.2.95：port.237 → port.238
~ [节点机制] nodalmechanics-1.0.0-port.6.jar
~ [天界神秘学] thaumcraftcelestial-1.0.0-port.24.jar
~ [污秽魔法] taintedmagic-1.0.0-port.29.jar
```

其他内容：  
```text
~ config/voxy-config.json
~ config/viscript_shop_config.toml
~ resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
~ resourcepacks/SCEX-任务图片资源包.zip
~ config/dlc_manager/config.dc
```

> 2026/8/28 v1.0.25

更新说明：  
- 新增 DLC Manager 优化模组中心：42 个条目按核心稳定、渲染帧率、网络响应、模组专项、诊断兼容和实验功能分类，并提供完整中文名称与用途说明。
- 保持当前优化模组启用状态不变；新增 SCEX 推荐、低配稳定、高端远景（实验）和性能诊断 4 套预设，钠与 Cupboard 等前置可自动联动。
- 实验或预发布优化会在开启前警告；隐藏“全部开启”、路径配置和玩家端服务器管理入口，关闭 API 与自更新，避免误操作。
- 清理 5 个已确认的旧版或内容重复客户端优化 JAR；同步器仅定向处理这些文件，仍保留玩家自行添加的额外模组及其 DLC 开关状态。
- DLC 切换会在下次完整启动游戏后生效；更新完成后请退出启动器中的游戏进程再重新启动。

模组变更：  
```text
- [立即加速] ImmediatelyFast-NeoForge-1.6.11+1.21.1.jar
- [重复件：铁氧体磁芯] ferritecore-7.0.3-neoforge.jar
- [重复件：现代化修复] modernfix-neoforge-5.27.20+mc1.21.1.jar
- [重复件：异步粒子] AsyncParticles-21.1.4.0-beta.3+1.21.1.jar
- [重复实体UUID修复] deuf-1.21.1-1.0.jar
```

其他内容：  
```text
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
~ config/dlc_manager/config.dc
~ config/voxy-config.json
~ config/viscript_shop_config.toml
~ resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
~ resourcepacks/SCEX-任务图片资源包.zip
~ config/dlc_manager/config.dc
```

> 2026/8/28 v1.0.24

更新说明：  
- 更新任务图片资源包，新增任务增强装饰线、TC 背景与返回页图片；该资源包继续强制校验并同步。
- 新增饮食多样性奖励 Spice of Life: Carrot Edition 1.16.6，客户端与服务端保持同版。
- 服务端加入《月之风土记》可靠首次发放修复：新 UUID 首登只发 1 本，同 UUID 重登、丢书、死亡或重启后不补发，老玩家不新增。
- 玩家同步器会先备份被覆盖文件，并保留玩家自行添加或修改的额外模组。更新后请完全退出并重新启动游戏。

模组变更：  
```text
+ [饮食多样性奖励] solcarrot-1.21.1-1.16.6.jar
```

其他内容：  
```text
~ resourcepacks/SCEX-任务图片资源包.zip
~ config/voxy-config.json
~ config/viscript_shop_config.toml
~ resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
~ resourcepacks/SCEX-任务图片资源包.zip
```

> 2026/8/27 v1.0.23

更新说明：  
- 用 Visual Keybinder 0.1.13 替换 Keybind Atlas 1.4.0，提供更直观的键盘、鼠标按键占用与冲突查看界面。
- 补充 Visual Keybinder 的简体中文按键名称、预设切换和结果提示；汉化资源包会强制校验并同步。
- 更新器只会备份并移除上一版清单中未被改动的旧 Keybind Atlas；玩家自行添加或修改过的额外模组不会被删除。更新后请完全退出并重新启动游戏。

模组变更：  
```text
+ [可视化按键绑定] visual_keybinder-1.21.1-0.1.13-neoforge.jar
- [按键图谱] KeybindAtlas-v1.4.0-mc1.21.1-neoforge.jar
```

其他内容：  
```text
~ resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
- config/keybindatlas-client.toml
~ config/voxy-config.json
~ config/viscript_shop_config.toml
~ resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
~ resourcepacks/SCEX-任务图片资源包.zip
```

> 2026/8/27 v1.0.22

更新说明：  
- 怀旧服任务书已按服主要求整体替换为新的神秘时代任务章节；旧任务配置与玩家任务进度均已单独备份，可完整回滚。
- 新增“SCEX-任务图片资源包”，补齐任务页使用的书页与 Vis 图片；更新器会下载、校验并自动启用该资源包。
- 同步保存任务文本颜色与格式规范，后续任务扩写统一沿用同一套标记规则。

其他内容：  
```text
+ resourcepacks/SCEX-任务图片资源包.zip
~ config/voxy-config.json
~ config/viscript_shop_config.toml
~ resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
~ resourcepacks/SCEX-任务图片资源包.zip
```

> 2026/8/27 v1.0.21

更新说明：  
- 恢复分子重组仪中央工作区的原版半透明玻璃效果，并调整绘制顺序，让工作特效能从玻璃后正确显现。
- 补齐 ASP 十盒体模型的纹理镜像设置，修正各部件表面的贴图方向。
- 保留工作态等离子与粒子动画，并确保物品栏、主副手及掉落物渲染继续正常；本更新仍仅需客户端。

模组变更：  
```text
~ [分子重组仪：怀旧渲染] MolecularTransformer-LegacyRenderer：1.0.2 → 1.0.3
```

其他内容：  
```text
~ config/voxy-config.json
~ config/viscript_shop_config.toml
~ resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
```

> 2026/8/27 v1.0.20

更新说明：  
- 修复分子重组仪工作时等离子与粒子动画不显示的问题，并恢复 Advanced Solar Panels 原版动画颜色、帧序列与加法混合效果。
- 修复分子重组仪在物品栏、手持与掉落状态下完全透明的问题，复用原版十盒体模型与物品显示变换。
- 保留 1.0.1 的开放式模型遮挡、透光和环境光照修复；本更新仅客户端需要，请退出游戏后再同步更新。

模组变更：  
```text
~ [分子重组仪：怀旧渲染] MolecularTransformer-LegacyRenderer：1.0.1 → 1.0.2
```

其他内容：  
```text
~ config/voxy-config.json
~ config/viscript_shop_config.toml
~ resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
```

> 2026/8/27 v1.0.19

更新说明：  
- 修复分子重组仪开放式模型与相邻方块连接时出现缺面、空洞的问题。
- 修复分子重组仪机身受原整立方体遮光影响而明显发暗的问题。
- 继续使用高级太阳能原始分子重组仪模型与动画；本次只调整客户端遮挡和环境光照。

模组变更：  
```text
~ [分子重组仪：怀旧渲染] MolecularTransformer-LegacyRenderer：1.0.0 → 1.0.1
```

其他内容：  
```text
~ config/voxy-config.json
~ config/viscript_shop_config.toml
~ resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
```

> 2026/8/27 v1.0.17

更新说明：  
- 修正默认 options.txt 的资源包顺序，将服务器汉化包置于最高优先级。
- 同步器会核验客户端语言与汉化包优先级；修正顺序后会提示完全退出并重启客户端。
- Relics 仍为 0.12.8，汉化包内容不变；玩家自行添加的其他资源包继续保留。

其他内容：  
```text
~ _updater/player-update-generic.ps1
~ _updater/player-update-generic.py
~ config/voxy-config.json
~ config/viscript_shop_config.toml
~ resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
```

> 2026/8/27 v1.0.16

更新说明：  
- 修复服务器汉化包可能被误判为玩家自定义资源包、导致仍显示英文的问题。
- 仅强制接管服务器专用汉化包；玩家自行添加的其他资源包继续保留。
- 同步器会自动启用汉化包并置于最高优先级，修改 options.txt 前会创建备份。

其他内容：  
```text
~ _updater/player-update-generic.ps1
~ _updater/player-update-generic.py
~ config/voxy-config.json
~ config/viscript_shop_config.toml
~ resourcepacks/Minecraft-Mod-Language-Modpack-Converted-1.21.1.zip
```

> 2026/8/27 v1.0.15

更新说明：  
- 新增轻松村民（Easy Villagers）1.1.42，已加入客户端发布源和独立服务端。
- 该模组适配 Minecraft 1.21.1 / NeoForge 21.1.248，没有新增必装前置。
- 全部模组使用中文分类文件名；同步器会先备份被替换的旧版文件，并保留玩家自行添加的额外模组。

模组变更：  
```text
+ [轻松村民] easy-villagers-neoforge-1.21.1-1.1.42.jar
```

其他内容：  
```text
~ config/voxy-config.json
~ config/viscript_shop_config.toml
```

> 2026/8/27 v1.0.14

更新说明：  
- 新增高级战利品信息、FTB 跨模组兼容与 FTB 任务增强，并将 FTB Quests 从 2101.1.33 升级至 2101.1.34。
- 新增快捷动作轮盘与 MC 百科搜索；这两项仅安装在客户端，不会放入独立服务端。
- 新增 RTS 俯视建造与连锁破坏回溯，相关功能模组已同步至客户端和服务端待下次维护加载。
- 全部模组使用中文分类文件名；同步器会先备份被替换的旧版文件，并保留玩家自行添加的额外模组。

模组变更：  
```text
~ [FTB 任务] ftb-quests-neoforge：2101.1.33 → 2101.1.34
+ [高级战利品信息] AdvancedLootInfo-neoforge-1.21.1-1.12.0.jar
+ [快捷动作轮盘] ezactions-neoforge-1.21.1-2.0.3.5.jar
+ [连锁破坏回溯] ultimine_rewind-2.1.0.jar
+ [FTB跨模组兼容] ftb-xmod-compat-neoforge-21.1.11.jar
+ [FTB任务增强] quest_enhance-1.21.1-neoforge-3.7.jar
+ [MC百科搜索] omnisearch-2.1.0.jar
+ [RTS俯视建造] rtsbuilding-neoforge-1.21.1-1.1.7.jar
```

其他内容：  
```text
~ config/voxy-config.json
~ config/viscript_shop_config.toml
```

> 2026/8/27 v1.0.13

更新说明：  
- 开启 ViScriptShop 的 FTB Library 侧边栏商店按钮，玩家可从 FTB Library 界面直接打开商店。
- 该配置列入强制同步项；更新器会先备份玩家原有配置，再写入开启状态。
- 本次仅更新商店入口配置，不删除玩家自行添加的模组或其他本地内容。

其他内容：  
```text
+ config/viscript_shop_config.toml
~ config/voxy-config.json
~ config/viscript_shop_config.toml
```

> 2026/8/27 v1.0.12

更新说明：  
- 新增 FTB 物品筛选系统 21.1.4，可在支持该系统的机器与界面中配置更灵活的物品过滤规则。
- 新增时装盔甲重制版 1.21.1-v1，可分别设置实际生效的护甲与外观护甲，并可隐藏盔甲显示。
- 新增 ViScriptShop 1.2.0，并把其前置 LowDragLib2 从 2.2.36.a 升级至官方 2.2.37。
- 三项功能模组均已同步至服务端与客户端，并使用中文分类文件名；同步器会先备份变更文件，玩家自行添加的额外模组仍会保留。

模组变更：  
```text
~ [LowDragLib2前置库] ldlib2-neoforge-1.21.1：2.2.36.a → 2.2.37
+ [脚本商店] ViScriptShop-neoforge-1.21.1-1.2.0.jar
+ [时装盔甲重制版] cosmeticarmorreworked-1.21.1-v1-neoforge.jar
+ [FTB物品筛选系统] ftb-filter-system-neoforge-21.1.4.jar
```

其他内容：  
```text
~ config/voxy-config.json
```

> 2026/8/27 v1.0.11

更新说明：  
- 神秘时代更新至 0.2.2.95-port.237，神秘工匠更新至 1.0.0-port.58；禁忌魔法、污秽魔法、节点机制和天界神秘学同步替换为同批次构建。
- 本批修复 Lootr 战利品箱兼容、研究节点显示、活化工具台研究持久化和木台阶标签兼容，并精确回滚此前不合适的 JEI 要素安瓿输入改动。
- 服务端与客户端六件套已统一哈希和中文文件名；同步器会先备份被替换文件，玩家自行添加的额外模组仍会保留。

模组变更：  
```text
~ [神秘工匠] thaumic_tinkerer-1.0.0：port.57 → port.58
~ [神秘时代] thaumcraft-0.2.2.95：port.236 → port.237
~ [节点机制] nodalmechanics-1.0.0-port.6.jar
~ [禁忌魔法] forbiddenmagic-1.0.0-port.25.jar
~ [天界神秘学] thaumcraftcelestial-1.0.0-port.24.jar
~ [污秽魔法] taintedmagic-1.0.0-port.29.jar
```

其他内容：  
```text
~ config/voxy-config.json
```

> 2026/8/27 v1.0.10

更新说明：  
- 全部客户端模组文件现已补充中文名称前缀，便于玩家识别用途；重复副本会明确标注为“重复件”。
- 本次只调整文件名，模组 JAR 内容和版本没有变化；同步器会按哈希直接接管本地原文件，避免重复下载。
- 改名前文件会进入 .portable-sync-backups，玩家自行添加的额外模组仍会保留，不会被清理。

其他内容：  
```text
~ _updater/player-update-generic.ps1
~ _updater/player-update-generic.py
~ config/voxy-config.json
```

> 2026/8/27 v1.0.9

更新说明：  
- 修复部分玩家进入怀旧服时，Neo-Voxy 因本地 RocksDB 缓存初始化失败而导致的客户端崩溃。
- 本版会强制同步 config/voxy-config.json，并暂时关闭 Voxy 远景功能；不会删除现有 .voxy 缓存，原配置如存在会先备份。
- 同步器的完成统计现在会单列配置变更，并显示实际修改的配置文件；早苗公告也会附带本版说明和具体文件。

其他内容：  
```text
~ _updater/player-update-generic.ps1
~ _updater/player-update-generic.py
~ config/voxy-config.json
```

> 2026/8/29 v1.0.8

更新说明：  
- 便携发布 1.0.8；文件数量 681。现有归档仅保留发布摘要，未保留逐项变更清单。

> 2026/8/29 v1.0.7

更新说明：  
- 便携发布 1.0.7；文件数量 680。现有归档仅保留发布摘要，未保留逐项变更清单。

> 2026/8/29 v1.0.6

更新说明：  
- 历史归档索引：SCEX Legacy Genesis 1.0.6。
- 现有 Monarch 发布目录未保留本版本的逐项变更清单；为避免臆造内容，本条仅保留版本号，待找到可核验公告或发布包后补充。

> 2026/8/29 v1.0.5

更新说明：  
- 历史归档索引：SCEX Legacy Genesis 1.0.5。
- 现有 Monarch 发布目录未保留本版本的逐项变更清单；为避免臆造内容，本条仅保留版本号，待找到可核验公告或发布包后补充。

> 2026/8/29 v1.0.4

更新说明：  
- 历史归档索引：SCEX Legacy Genesis 1.0.4。
- 现有 Monarch 发布目录未保留本版本的逐项变更清单；为避免臆造内容，本条仅保留版本号，待找到可核验公告或发布包后补充。

> 2026/8/29 v1.0.3

更新说明：  
- 历史归档索引：SCEX Legacy Genesis 1.0.3。
- 现有 Monarch 发布目录未保留本版本的逐项变更清单；为避免臆造内容，本条仅保留版本号，待找到可核验公告或发布包后补充。

> 2026/8/29 v1.0.2

更新说明：  
- 历史归档索引：SCEX Legacy Genesis 1.0.2。
- 现有 Monarch 发布目录未保留本版本的逐项变更清单；为避免臆造内容，本条仅保留版本号，待找到可核验公告或发布包后补充。

> 2026/8/29 v1.0.1

更新说明：  
- 历史归档索引：SCEX Legacy Genesis 1.0.1。
- 现有 Monarch 发布目录未保留本版本的逐项变更清单；为避免臆造内容，本条仅保留版本号，待找到可核验公告或发布包后补充。
<!-- LEGACY-LOG-AUTO:END -->