# 永安期货 · 澳洲锂矿季度汇总看板

澳洲硬岩锂矿季度经营数据看板（GitHub Pages 部署），覆盖澳大利亚全部主要锂矿山的季度产量/销量/均价/成本、资本开支与 2027 年产量预测。

**在线访问**：https://handizheng232-eng.github.io/cyberland/

## 页面结构

| 序号 | 页面 | 矿山/内容 | 母公司 |
|---|---|---|---|
| 总览 | overview.html | 主页：矿山运行总览 + 近五年产量汇总（SC6 等效折算）+ 资本开支 + 2027 预测汇总 | — |
| 1 | index.html | Greenbushes（格林布什） | IGO（25% 份额，Tianqi/Albemarle 合资） |
| 2 | pilgangoora.html | Pilgangoora（皮尔甘古拉） | Pilbara Minerals（ASX: PLS） |
| 3 | wodgina.html | Wodgina（沃吉纳） | Mineral Resources（ASX: MIN，POSCO 2025-11 收购 30%） |
| 4 | marion.html | Mt Marion（马里恩） | MRL + Ganfeng |
| 5 | kathleenvalley.html | Kathleen Valley（凯瑟琳谷） | Liontown（ASX: LTR） |
| 6 | baldhill.html | Bald Hill（秃山，2026-05 复产） | MRL 100% |
| 7 | mtcattlin.html | Mt Cattlin（卡特林山，C&M） | Rio Tinto（2025-03 收购 Arcadium） |
| 8 | finniss.html | Finniss（芬尼斯，NT 唯一锂矿） | Core Lithium（ASX: CXO） |
| 9 | manna.html | Manna（曼纳，未投产） | Global Lithium（ASX: GL1） |
| 10 | mtholland.html | Mt Holland（荷兰山，矿+精炼一体化） | Covalent（SQM 50% + Wesfarmers 50%） |

每矿山详情页七大板块：① 已有产线运行状况 ② 在建/规划产线 ③ 整体运行 ④ 历史数据（2019Q1 起） ⑤ 2027 年预测 ⑥ 选矿产能核实 ⑦ 原矿产能核实。

## 数据口径

- **季度数据**：日历季度（2019Q1 起），100% 资产口径（份额矿山标注：GB=IGO 25%、Mt Holland=SQM 50%×2）
- **产量单位**：各矿山披露口径（SC6 折算 / dmt 实际品位 / 混合品位 dmt / SC5.5），主页提供 **SC6 等效折算**（×实际品位/6%）统一对比
- **均价/成本**：CIF/FOB + SC6/SC6e 基准各异，跨矿对比注意标注
- **资本开支**：矿山/项目级，财年（6/30）为主，2026E/2027E 为指引或 FID 计划
- **2027 预测**：研究性判断（悲观/基准/乐观），按官方 FY27 指引与公司计划推算
- 未披露季度标 N.D.；美式财季（SQM/NYSE）注意 8 月下旬发布节奏

## 更新方法

1. 修改 `build_data.py`（数据源：各矿山母公司官方季度报告 ASX/SEC）
2. `python build_data.py` 生成 `docs/data.js`
3. `docs/index.html` 为模板，按矿山复制为各详情页（改 MINE_KEY）
4. 推送 `docs/` 至本仓库 main 分支（GitHub Pages 自动部署，约 1 分钟生效）

## 数据来源

IGO / Pilbara Minerals / Mineral Resources / Liontown / Rio Tinto / Core Lithium / Global Lithium / SQM（SEC 20-F/6-K）/ Wesfarmers 官方报告；WA EPA / NT 政府环评；公司官网。

> 免责声明：本看板数据仅供研究参考，不构成投资建议。
