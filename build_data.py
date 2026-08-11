# -*- coding: utf-8 -*-
"""构建永安期货-澳洲锂矿汇总格式的 GitHub Pages 数据文件。

- 历史数据：从「季度数据_Greenbushes更新至2026Q2.xlsx」的「季度生产数据」sheet 提取（已用 IGO 官方季报核对）
- 运行状况描述：26Q2（IGO FY26 Q4）最新季度表述，来源 = IGO June 2026 Quarterly Activities Report (2026-07-28)

用法: python build_data.py
输出: docs/data.js
"""
import openpyxl
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "季度数据_Greenbushes更新至2026Q2.xlsx")
OUT = os.path.join(HERE, "docs", "data.js")

# ============ 矿山列表（永安期货格式：每个矿山一个块） ============
# 当前数据源为 IGO 官网（Greenbushes 母公司）；结构可扩展多矿山
MINES = [
    {
        "company": "IGO",
        "mine": "Greenbushes",
        "sc6": 1.0,   # SC6 折算系数（用户规范 2026-08-10：精矿产量/产能/预测全站统一 SC6 口径）
        "sc6_note": "官方 SC6 折算（6% Li₂O）口径",
        "grade": "6% Li₂O（SC6 官方折算）",   # 精矿品位标注（用户规范 2026-08-11：产量/销量描述必须明确品位）
        "lat": -33.8567,  # 卫星影像定位（Yandex/Google Maps）
        "lng": 116.0622,
        "current_q": "26Q2",
        "prev_q": "26Q1",
        "current_q_date": "2026年4-6月",
        "mine_cn": "Greenbushes（格林布什矿山）",
        "report": "IGO June 2026 Quarterly Activities Report（2026-07-28 发布，FY26 Q4 / 日历26Q2）",
        "source_url": "https://www.igo.com.au/site/investor-center/investor-center1",
        "equity_note": "100% 资产口径（Talison 运营）；IGO→TLEA 49%，TLEA/Windfield→Greenbushes 51%，Albemarle 49%",
        "history_labels": [
            ("production", "精矿产量（万吨，SC6 折算 6% Li₂O）"),
            ("tech_grade", "技术级精矿产量（万吨，实际品位）"),
            ("chem_grade", "化学级精矿产量（万吨，实际品位）"),
            ("sales", "销量（万吨，SC6 折算 6% Li₂O）"),
            ("inv_change", "库存变动量（万吨）"),
            ("inventory", "库存（万吨）"),
            ("prod_sales_ratio", "产销比"),
            ("avg_price", "平均售价（US$/t，SC6）"),
            ("cost_with_royalty", "单位成本—含权益金（A$/t，FOB SC6）"),
            ("cost_no_royalty", "单位成本—不含权益金（A$/t，FOB SC6）"),
            ("cash_cost", "cash cost（A$/t，FOB SC6）"),
        ],
        "status_26q2": {
            "existing_lines": [
                {
                    "name": "已有产能1：技术级锂精矿工厂 — 14万吨/年（原矿由 Talison 采矿供给，原矿处理能力未单独披露）",
                    "q26q2": "未单独披露运行数据（IGO 自 1Q25 起不再拆分技术级/化学级产量，并入总量披露）。26Q2 矿山总产量 387kt 含技术级与化学级全部产线。",
                    "q26q1": "同样未单独披露（并入总量披露），26Q1 矿山总产量 351kt。",
                    "compare": "两季均无单独口径，无实质变化。"
                },
                {
                    "name": "已有产能2：化学级锂精矿工厂 1号（CGP1）— 60万吨/年 SC6",
                    "q26q2": "26Q2 Talison 重点提升 CGP1 性能，特别是可靠性、停机合规性和回收率，已引入外部专家团队制定综合回收率改善计划。本季回收率下降与工厂停机部分抵消了品位上升带来的产量增益（采矿转向高品位矿体）。",
                    "q26q1": "26Q1 受入选品位下降、回收率下降及维护停机增加影响，运营结果偏弱；季度内为优先推进安全整改实施两次安全停工。",
                    "compare": "本季采矿品位改善（转向高品位矿体）是环比亮点，但回收率与停机问题延续，改善措施落地仍需时间——改善方向超预期，兑现进度未超预期。"
                },
                {
                    "name": "已有产能3：化学级锂精矿工厂 2号（CGP2）— 60万吨/年 SC6",
                    "q26q2": "26Q2 同 CGP1：重点改善可靠性、停机合规性和回收率；外部专家支持的综合回收率改善计划推进中。",
                    "q26q1": "26Q1 同 CGP1：品位、回收率、停机三重拖累，运营偏弱。",
                    "compare": "两季表述一致：CGP2 回收率持续低于 CGP1（此前报告披露 CGP1 回收率稳定在 80% 以上、CGP2 约 70%），提升 CGP2 回收率仍是主要看点。"
                },
                {
                    "name": "已有产能4：尾矿再处理厂 — 28万吨/年 SC6",
                    "q26q2": "26Q2 维持性+增长性+资本化剥离支出合计 A$42M，主要用于尾矿设施（TSF）工程。",
                    "q26q1": "26Q1 支出合计 A$75M，主要投向 CGP3 与尾矿库工程。",
                    "compare": "本季资本开支环比下降 44%（A$75M→A$42M），主因 CGP3 建设高峰已过、投入转向尾矿设施——资本开支节奏符合投产后的正常回落。"
                },
                {
                    "name": "已有产能5：化学级锂精矿工厂 3号（CGP3）— 52万吨/年 SC6【2025年新增投产】",
                    "q26q2": "CGP3 于 2025 年 12 月季度（25Q4）首次投产，26Q2 贡献 71kt（26Q1：33kt），爬坡进度超前于计划；2026 年 6 月发生火灾，该厂停产约 7 周，预计近日复产。",
                    "q26q1": "26Q1 爬坡基本符合计划（1 月曾有延迟），贡献约 33kt；自 2 月起 CGP3 运营成本开始计入单位成本。",
                    "compare": "重大超预期：单季贡献从 33kt 翻倍至 71kt，爬坡由「基本符合计划」转为「超前于计划」；但 6 月火灾（停产约 7 周）为重大负面意外，26Q3 初期产量将受拖累，复产后的爬坡节奏是后续关键观察点。"
                }
            ],
            "planned_lines": [
                {
                    "name": "未来产能：化学级锂精矿工厂 4号（CGP4）— 52万吨",
                    "q26q2": "公司规划于 2027 年完成 CGP4 项目建设并投产，预计接下来几个季度内进行投资决策（最新季报未更新该项进展）。",
                    "q26q1": "同样维持 2027 年投产规划，投资决策待后续季度推进。",
                    "compare": "两季均无新进展披露；CGP3 爬坡验证后，CGP4 投资决策时点值得关注。"
                }
            ],
            "overall": {
                "operation_changes": (
                    "26Q2 产量 387kt，环比 +10%（26Q1：351kt），增量主要来自 CGP3 贡献提升（71kt vs 33kt）；"
                    "采矿品位改善，但回收率下降与工厂停机抵消了部分预期产量增益；"
                    "销量 391kt，环比 +12%（含上季因港口拥堵延迟至本季的装运）；"
                    "平均实现价 US$2,286/t，环比 +37%，反映锂市场持续走强；"
                    "现金成本（production 口径）A$448/t，环比基本持平；EBITDA 利润率 80%（FY26 全年 73%）；"
                    "6 月 CGP3 火灾停产约 7 周，预计近日复产；"
                    "Windfield 期末现金 A$183.8M，有息负债 A$1,965.4M，本季向股东分红 A$390.0M。"
                ),
                "operation_changes_prev": (
                    "26Q1 产量 351kt，环比持平（25Q4：352kt），CGP3 贡献约 33kt；"
                    "运营受入选品位下降、回收率下降及维护停机增加拖累，季度内实施两次安全停工；"
                    "销量 349kt，环比 +6%，一船因港口拥堵延迟至 4 月装运；"
                    "平均实现价 US$1,668/t，环比近翻倍（25Q4：US$850/t）；"
                    "现金成本 A$446/t，环比 +20%（CGP3 运营成本自 2 月起计入、维护成本增加、剥离资本化减少）；"
                    "EBITDA 利润率 75%；资本开支 A$75M，主要投向 CGP3 与尾矿库。"
                ),
                "future_outlook": (
                    "FY27 指引：精矿产量 155-175 万吨，现金成本 A$380-440/t，资本开支 A$250-300M；"
                    "FY26 全年实际：产量 141.0 万吨（1,410kt），销量 136.8 万吨，现金成本 A$415/t，均价 US$1,443/t；"
                    "26Q3/26Q4 按指引中值 165 万吨/年 ÷ 4 = 41.25 万吨/季预测；"
                    "注意 CGP3 火灾后复产爬坡进度或影响 26Q3 初期产量。"
                ),
                "highlights": [
                    "产量环比 +10% 至 387kt，高于市场预期——CGP3 单季贡献翻倍（33kt→71kt）是核心驱动",
                    "均价连续两季大涨：US$850（25Q4）→1,668（26Q1）→2,286（26Q2），锂价强势程度超预期",
                    "EBITDA 利润率 80%（环比 +5pct），FY26 全年 73%，成本持平（A$448/t）下盈利弹性显著",
                    "CGP3 爬坡由「基本符合计划」提速至「超前于计划」（火灾前），产能释放节奏超预期",
                    "负面意外：6 月 CGP3 火灾停产约 7 周，将拖累 26Q3 初期产量与爬坡节奏"
                ]
            }
        },
"forecast_unit": "万吨 SC6（6% Li₂O 折算；IGO FY27 指引 155-175 万吨对应）",
        "forecast_2027": {
            "title": "2027 年产量预测（日历年度 · 100% 资产口径 · SC6 官方折算口径，品位 6%）",
            "basis": (
                "官方指引：IGO FY27 精矿产量指引 155-175 万吨（FY27 = 2026年7月-2027年6月，即日历 26Q3-27Q2）。"
                "产能基础：存量产线铭牌 162 万吨/年（CGP1 60 + CGP2 60 + 技术级 14 + 尾矿再处理 28），"
                "CGP3 铭牌 52 万吨/年，CGP4 铭牌 52 万吨/年（规划 2027 建成投产，投资决策未定）。"
                "FY26 全年实际产量 141 万吨，其中 CGP3 贡献约 10.4 万吨（33+71kt），"
                "即存量产线 FY26 实际约 130 万吨/年（利用率约 80%）。"
            ),
            "assumptions": [
                "CGP3 复产爬坡：26Q3 复产（7月底火灾后近日复产），26Q4 利用率升至 ~70-80%，2027 年上半年爬满（52 万吨/年）",
                "存量产线维持 FY26 实际水平 ~130 万吨/年，回收率改善计划（CGP1/CGP2）带来 2-5 万吨/年小幅提升",
                "CGP4 2027 年内不贡献产量（投资决策未定 + 建设周期 2 年+），最快 2028H2 贡献",
                "锂价走势不影响产量预测（矿端按指引生产，销量弹性另议）"
            ],
            "scenarios": {
                "bear": {
                    "label": "悲观（火灾影响超预期 + CGP3 爬坡延迟）",
                    "production_kt": 1600,
                    "note": "CGP3 复产推迟至 26Q4、2027 年中才达满产，全年贡献仅 ~35 万吨；存量产线回收率改善不及预期；日历 2027 ≈ 164 万吨（线性覆写口径）。"
                },
                "base": {
                    "label": "基准（CGP3 按计划爬满 + 存量小幅改善）",
                    "production_kt": 1740,
                    "note": "CGP3 2027 年初爬至 ~85% 利用率、年中满产；线性序列 27Q1/27Q2=41.25（FY27 指引期）+ 27Q3/27Q4 线性延至 CGP 满产 43.5 → 2027 基准 ≈ 168.5 万吨（页面统一值，审计修正）。"
                          "口径说明：日历 2027 = FY27 后两季（27Q1-27Q2，落在公司 FY27 指引 155-175 万吨区间）+ FY28 前两季（27Q3-27Q4，满产稳态），"
                          "故略高于 FY27 财年指引中枢 165 万吨是合理的。"
                },
                "bull": {
                    "label": "乐观（CGP3 快速满产 + 回收率超预期 + 火灾复产节奏顺利）",
                    "production_kt": 1850,
                    "note": "CGP3 2027 年初即满产（~50 万吨/年贡献）；回收率改善兑现；日历 2027 ≈ 173 万吨（超铭牌运行；CGP4 无最新 FID，不进入 2027 乐观——审计修正）。"
                }
            },
            "quarterly_base": {
                "27Q1": 40,
                "27Q2": 43,
                "27Q3": 45,
                "27Q4": 46,
                "total": 174
            },
            "confidence": "中高：基于公司官方指引与 CGP3 实测爬坡速率外推；主要不确定性为火灾复产节奏、CGP4 FID 时点、锂价对销量而非产量的传导。",
            "disclaimer": "预测为研究性判断，非公司指引；公司 FY27 指引为 155-175 万吨（财年口径，含 26Q3-27Q2），与本预测的日历年度口径不同。"
        },
        "capacity_verification": {
            "title": "产能核实（多来源交叉印证）",
            "method": "对每条产线产能，交叉核对 4 类独立公开来源：① 公司年报（IGO AR 2022/2023/2025）；② 公司官网资产页（IGO Our Business）；③ 美股监管披露（Albemarle 10-K + SLR S-K1300 技术报告，SEC 公开文件）；④ 行业/第三方（券商研报、咨询机构、天齐锂业 H 股披露——公开可获取部分）。",
            "summary": "口径差异是关键：官方来源披露的是矿石处理能力（Mtpa 矿石）与精矿产能两个维度。SLR 技术报告逐厂矿石能力：CGP1=1.8、CGP2=2.4、TRP=2.0、TGP=0.35、CGP3=2.4（合计 8.95 Mtpa）；IGO 官网与 SLR 一致（存量 6.55→精矿 ~1.5Mtpa，CGP3 后 8.25→精矿 ~1.8Mtpa）。Excel 的 60/60/14/28 万吨是精矿铭牌口径，与官方矿石能力口径不同维度，不可直接对比；精矿产率按官方口径约 23-30%（品位/回收率而异）。",
            "items": [
                {
                    "line": "CGP1（化学级1号）",
                    "excel_capacity": "60 万吨/年 SC6（IGO 官方 SC6 折算口径）",
                    "verified": "⚠️ 多来源矿石口径交叉确认，精矿口径为推算",
                    "sources": [
                        {"src": "SLR 技术报告 (2026-02)", "data": "矿石处理能力 1.8 Mtpa；2025 实际年处理 ~1.7-1.8Mt、入选品位 ~2.7% Li₂O"},
                        {"src": "IGO 官网", "data": "计入存量四厂合计 6.5Mtpa 矿石 → 精矿 up to 1.5Mtpa"},
                        {"src": "IGO 年报", "data": "未单独披露；仅描述为四座处理厂之一"},
                        {"src": "推算", "data": "按官方产率 ~23-33%，1.8Mtpa 矿石对应精矿约 42-60 万吨/年——Excel 60 万吨处于上限"}
                    ],
                    "status": "warn"
                },
                {
                    "line": "CGP2（化学级2号）",
                    "excel_capacity": "60 万吨/年 SC6（IGO 官方 SC6 折算口径）",
                    "verified": "⚠️ 多来源矿石口径交叉确认，精矿口径为推算",
                    "sources": [
                        {"src": "SLR 技术报告 (2026-02)", "data": "矿石处理能力 2.4 Mtpa（设计）；实际仅 ~2.0 Mt（品位 2.0% Li₂O 偏低，未达设计）"},
                        {"src": "IGO 官网", "data": "计入存量合计 6.5Mtpa 矿石 → 1.5Mtpa 精矿"},
                        {"src": "IGO 年报 2022", "data": "CGP3 设计基于 CGP2、名义矿石处理量 2.4Mtpa（佐证 CGP2=2.4）"},
                        {"src": "推算", "data": "2.4Mtpa 矿石 × ~25% 产率 ≈ 60 万吨精矿——与 Excel 一致，但实际品位下降后产率或走低"}
                    ],
                    "status": "warn"
                },
                {
                    "line": "TGP（技术级）",
                    "excel_capacity": "14 万吨精矿/年",
                    "verified": "⚠️ 官方矿石口径远低于 Excel 精矿口径",
                    "sources": [
                        {"src": "SLR 技术报告 (2026-02)", "data": "矿石处理能力仅 0.35 Mtpa——按 40% 产率推算精矿约 14 万吨/年，与 Excel 一致；但近年技术级占比已降至 1% 以下（IGO 不再单独披露）"},
                        {"src": "IGO 官网", "data": "四厂之一，未单独披露产能"},
                        {"src": "Albemarle 10-K", "data": "技术级精矿厂在产"}
                    ],
                    "status": "warn"
                },
                {
                    "line": "TRP（尾矿再处理厂）",
                    "excel_capacity": "28 万吨精矿/年",
                    "verified": "✓ 官方精矿口径确认（280ktpa）",
                    "sources": [
                        {"src": "IGO 年报 2022", "data": "'Nominal production from the TRP is expected to be 280ktpa...nameplate capacity expected FY23'——28 万吨精矿/年官方确认"},
                        {"src": "SLR 技术报告 (2026-02)", "data": "矿石处理能力 2.0 Mtpa（处理 TSF1 旧钽尾矿，平均品位 1.4% Li₂O）"},
                        {"src": "IGO 官网", "data": "计入存量合计 6.5Mtpa → 1.5Mtpa 精矿"}
                    ],
                    "status": "ok"
                },
                {
                    "line": "CGP3（化学级3号）",
                    "excel_capacity": "52 万吨/年 SC6（IGO 官方 SC6 折算口径）",
                    "verified": "✓ 官方精矿口径确认（520ktpa）",
                    "sources": [
                        {"src": "IGO 年报 2022/2023", "data": "'contribute an additional 520ktpa'；'designed to deliver approximately 0.52Mtpa'"},
                        {"src": "IGO 官网", "data": "处理能力 2.4Mtpa 矿石 → up to 500ktpa 精矿"},
                        {"src": "SLR 技术报告 (2026-02)", "data": "矿石处理能力 2.4 Mtpa；CGP3 后 LOM 合计 8.95 Mtpa、精矿 up to 1.8 Mtpa"},
                        {"src": "Albemarle 10-K", "data": "第三座化学级厂建成，商业化生产预计 2026 年；2026-06-10 火灾公告确认 CGP1/CGP2 不受影响"}
                    ],
                    "status": "ok"
                },
                {
                    "line": "CGP4（化学级4号）",
                    "excel_capacity": "52 万吨精矿/年（规划）",
                    "verified": "⚠️ 规划未定，多来源均无最新进展",
                    "sources": [
                        {"src": "IGO 年报 2023", "data": "'IGO expects a decision on the FID on CGP4 during FY24'——FY24 已过，截至 2026 年中无 FID 公告，项目实际推迟"},
                        {"src": "SLR 技术报告 (2026-02)", "data": "LOM 计划（表 14-1）未含 CGP4——第三方技术评估亦按无 CGP4 处理"},
                        {"src": "IGO 官网 / Albemarle 10-K", "data": "均无 CGP4 进展披露"}
                    ],
                    "status": "warn"
                },
                {
                    "line": "全矿合计",
                    "excel_capacity": "214 万吨精矿/年（162 存量 + 52 CGP3）",
                    "verified": "⚠️ 官方矿石口径 6.55→8.95 Mtpa；精矿口径 1.5→1.8 Mtpa",
                    "sources": [
                        {"src": "IGO 官网 + SLR", "data": "存量四厂 6.55 Mtpa 矿石 → 精矿 up to 1.5 Mtpa；含 CGP3 后 8.95 Mtpa → 精矿 up to 1.8 Mtpa——官方精矿上限（150-180 万吨/年）低于 Excel 的 214 万吨"},
                        {"src": "IGO 年报 2023", "data": "'~2.5Mtpa by FY27'——该口径显著高于官网/SLR 的 1.8Mtpa，疑含 CGP4 或更高有效产能假设，未被第三方技术报告支持"},
                        {"src": "SLR 技术报告 (2026-02)", "data": "2025 实际：5.85 Mtpa 矿石 → ~1.4 Mtpa SC6.0（作为可兑现基准）"}
                    ],
                    "status": "warn"
                }
            ],
            "sources_index": {
                "公司年报": "IGO Annual Report 2022/2023/2025（IGO 官网可下载）",
                "公司官网": "IGO Our Business → Lithium Joint Venture → Talison（igo.com.au）",
                "美股监管": "Albemarle Corp 10-K FY2025（2026-02-11）+ SLR International 'Greenbushes Mine S-K 1300 Technical Report Summary'（2026-02-11，Exhibit 96.1，SEC EDGAR）",
                "券商/咨询": "公开可获取的券商研报与 Benchmark/WoodMac 摘要本轮未能穿透付费墙；天齐锂业（H 股 9696）官网连接受限，其年报含 Talison 描述可作后续补充"
            },
            "note": "核实时间：2026-08-04。关键结论：① TRP 与 CGP3 的精矿铭牌（28/52 万吨）获公司年报+官网+SLR 三方一致确认；② CGP1/CGP2/TGP 官方只披露矿石处理能力（1.8/2.4/0.35 Mtpa），Excel 的 60/60/14 万吨精矿为按产率推算的上限值，非官方直接披露；③ 官方精矿总上限（CGP3 后 ~1.8Mtpa）低于 Excel 的 214 万吨，未来产能规划应以 SLR/官网口径为基准；④ CGP4 未被 SLR LOM 计划纳入，且 FID 迟迟未做，2027 年投产假设不成立。",
            "images": [
                {"url": "img/sat_greenbushes.jpg", "src": "卫星影像（Yandex Maps，坐标 -33.8567,116.0622）", "cap": "Greenbushes 矿区卫星影像（Zoom 14）——露天矿坑与选矿厂区在卫星影像上的实际形态，卫星追踪第一参照"},
                {"url": "img/slr_plants_aerial.jpg", "src": "SLR 技术报告 Fig 14-1/14-2", "cap": "选矿厂工艺流程总览 + 厂区航拍位置图（Fig 14-2 Aerial Image），标出 CGP1/CGP2/CGP3/TGP/TRP 各厂相对位置"},
                {"url": "img/slr_overall_layout.jpg", "src": "SLR 技术报告 Fig 15-1", "cap": "Greenbushes 整体场地布局图（含选矿厂/尾矿库/储水设施位置）——技术报告项目总览图"},
                {"url": "img/greenbushes_aerial_official.jpg", "src": "IGO 官网（Our Business）", "cap": "Greenbushes 矿山官方航拍实景——露天矿坑 + 选矿厂区，可与卫星影像直接对照定位"}
            ],
            "mining_side": {
                "title": "原矿供应侧（矿坑 / 矿体 / 尾矿库）核实",
                "method": "选矿厂（CGP1/2/3、TGP、TRP）的原矿来源为 Greenbushes 露天矿及尾矿库；本栏以 SLR 技术报告（Table 1-2 LOM Physicals、Section 1.5/1.8）与 Albemarle 10-K 交叉核对采矿侧建成与规划信息。",
                "summary": "Greenbushes 为单一露天矿（Central Lode 主矿体 + Kapanga 东矿体），原矿经卡车-铲运至四座选矿厂；LOM 规划矿山寿命 24 年（至 2048，选矿至 2049），总剥离 656.5Mt、采出矿石 160.9Mt、再处理尾矿 2.8Mt，按 22.5% 回收率产出精矿 37.0Mt。地下开采研究尚处概念阶段。",
                "items": [
                    {
                        "item": "原矿矿山：Greenbushes 露天矿（Central Lode / Kapanga）",
                        "built_plan": "✅ 建成（1983 年起连续生产锂精矿）",
                        "status": "ok",
                        "sources": [
                            {"src": "Albemarle 10-K", "data": "大型露天矿（南纬33°52′、珀斯以南约250km）；主矿体 Central Lode + 东侧平行 Kapanga 矿体；开采区约 3,500 公顷、三个采矿租约"},
                            {"src": "SLR 技术报告", "data": "Central Lode 走向 3km、厚度数十至 300m、倾角 40-60°SW，连续性优于 Kapanga；Kapanga 近六年新增钻探为主（DD 占 75%）"}
                        ]
                    },
                    {
                        "item": "采矿方法与产能",
                        "built_plan": "✅ 建成（传统露天开采）",
                        "status": "ok",
                        "sources": [
                            {"src": "SLR 技术报告", "data": "传统露天金属矿开采（卡车+铲运），10m 工作台阶（5m 分段）；全部 ROM 矿石运往四座选矿厂；LOM 年物料总移动量 2034 年起升至 ~53Mt、废石移动 2033-2040 年 >40Mt（峰值 46Mt/2039）；剥采比（ROM）3.4:1"}
                        ]
                    },
                    {
                        "item": "矿坑规划（露天境界）",
                        "built_plan": "⚠️ 规划中（LOM 24 年）",
                        "status": "warn",
                        "sources": [
                            {"src": "SLR 技术报告", "data": "LOM 计划假设矿山寿命 24 年：采矿至 2048、堆存矿石 2049 处理完毕；矿坑境界基于资源模型（Indicated 资源仅在露天境界内、距钻孔外推 50m 内分类）；矿坑内排土（in-pit dumping）为优化项"}
                        ]
                    },
                    {
                        "item": "尾矿库 TSF1-TSF4（TRP 原矿来源）",
                        "built_plan": "✅ 建成（TSF1-4）；⚠️ TSF5 规划中",
                        "status": "warn",
                        "sources": [
                            {"src": "SLR 技术报告", "data": "TSF4 按当前 LOM 容量可用至 2034 年；之后需加高 TSF4 并新建 TSF5（拟建于场外、设计容量待确认）；TRP 处理 TSF1 旧钽尾矿（品位 1.4% Li₂O、2.0Mtpa）"},
                            {"src": "IGO 年报 2022", "data": "TRP 设计再处理 2Mtpa 旧钽选矿尾矿（TSF1），名义产出 280ktpa 精矿五年期"}
                        ]
                    },
                    {
                        "item": "废石堆 S1（Floyds）及后续规划",
                        "built_plan": "✅ 建成（S1 Floyds）；⚠️ 后续废石堆规划中",
                        "status": "warn",
                        "sources": [
                            {"src": "SLR 技术报告", "data": "目前唯一运行废石堆 S1（Floyds），容量 77Mbcm、预计 2034 年达容；之后需新建多个废石堆支撑 LOM 废石需求（需逐项取得审批）"},
                            {"src": "Albemarle 10-K", "data": "废石堆与尾矿库均位于三个采矿租约+两个通用租约范围内"}
                        ]
                    },
                    {
                        "item": "地下开采研究（未来原矿来源）",
                        "built_plan": "⚠️ 概念研究阶段（无建成）",
                        "status": "warn",
                        "sources": [
                            {"src": "SLR 技术报告", "data": "地下开采研究含露天-地下切换（open pit underground trade-off）研究，目前概念级；未来若实施地下开采，可通过膏体充填（paste fill）减少废石与尾矿需求；Central Lode 北部历史地下采空区已按实测形态从资源中扣除"},
                            {"src": "IGO 年报 2023", "data": "评估 Greenbushes 地下开采及潜在卫星矿供矿机会"}
                        ]
                    },
                    {
                        "item": "卫星矿 / 外围供矿",
                        "built_plan": "⚠️ 评估阶段（无建成）",
                        "status": "warn",
                        "sources": [
                            {"src": "IGO 年报 2023", "data": "额外研究将评估潜在卫星矿（satellite feed）供矿机会，以延长矿山服务年限"},
                            {"src": "Albemarle 10-K", "data": "矿权区约 10,000 公顷，含历史锡/钽/锂采区；Talison 持有全部锂矿采矿权"}
                        ]
                    },
                    {
                        "item": "矿石堆存（库存矿石）",
                        "built_plan": "✅ 建成（堆场）",
                        "status": "ok",
                        "sources": [
                            {"src": "SLR 技术报告", "data": "LOM 计划利用现有矿石堆存 0.9Mt；未处理矿石堆存另有 30.5Mt（含尾矿再处理 2.8Mt）；选矿厂总给矿 164.5Mt、平均品位 1.90% Li₂O"}
                        ]
                    }
                ],
                "note": "核实时间：2026-08-04。采矿侧要点：① 单一露天矿（Central Lode 主矿体）服务全部选矿厂，矿体禀赋为全球最高品位硬岩锂矿之一；② TSF4 尾矿库 2034 年达容后需新建 TSF5（场外、容量待定）——长期原矿/尾矿处理能力的审批是关键风险；③ 地下开采仅概念研究，若实施可缓解废石/尾矿压力并延长矿山寿命；④ LOM 按 22.5% 回收率、1.90% 平均品位测算，产出精矿 37.0Mt——该回收率假设与 26Q2 实际回收率走低趋势存在张力，后续需跟踪。",
                "images": [
                    {"url": "img/slr_location_plan.jpg", "src": "SLR 技术报告 Fig 3-1/3-2", "cap": "矿区位置图（含经纬度 33°51'24\"S 116°03'44\"E 与区域交通/港口关系）——卫星锁定第一参照"},
                    {"url": "img/slr_site_layout.jpg", "src": "SLR 技术报告 Fig 3-3", "cap": "Greenbushes Mine Operation Layout——矿坑、选矿厂、尾矿库、废石堆整体布置（技术报告项目总览图）"},
                    {"url": "img/slr_pit_limit.jpg", "src": "SLR 技术报告 Fig 12-3/12-5", "cap": "矿坑境界优化壳与最终边坡设计图（含坐标网格），用于识别矿坑边界"},
                    {"url": "img/slr_geo_map.jpg", "src": "SLR 技术报告 Fig 6-1/6-2", "cap": "Greenbushes 区域地质图与矿体剖面——矿体分布与矿坑位置的地质背景"},
                    {"url": "img/slr_tsf.jpg", "src": "SLR 技术报告 Fig 15-7/15-8", "cap": "尾矿库 TSF1/2/4 布置图——TRP 原矿来源与尾矿设施卫星定位"},
                    {"url": "img/greenbushes_ar2023_mine.jpg", "src": "IGO Annual Report 2023", "cap": "Greenbushes 露天矿实景（FY23），主矿坑与采矿设备，可对照卫星影像识别矿坑轮廓"}
                ]
            }
        }
    },
    {
        "company": "PLS（Pilbara Minerals）",
        "mine": "Pilgangoora",
        "sc6": 0.883,   # SC6 折算系数（2026-08-11 用户指正：PLS Jun2026 QAR 披露品位 5.3%，5.3/6=0.883，原 5.2% 有误）
        "sc6_note": "SC6 折算（原 dmt，逐季 grade produced 5.1-5.3% Li₂O；PLS Jun2026 QAR 附表逐季披露）",
        "grade": "~5.3% Li₂O（dmt 实际品位）",   # 精矿品位标注（PLS Jun2026 QAR 5.3%）
        "grade_series": {"2023Q3": 5.2, "2023Q4": 5.2, "2024Q1": 5.2, "2024Q2": 5.2, "2024Q3": 5.3, "2024Q4": 5.2, "2025Q1": 5.1, "2025Q2": 5.1, "2025Q3": 5.3, "2025Q4": 5.2, "2026Q1": 5.3, "2026Q2": 5.3},   # 逐季品位（2026-08-11 机制：FY25/FY26 QAR 附表 grade produced——Dec-23/Mar-24/Jun-24=5.2、Sep-24=5.3、Dec-24=5.2、Mar-25/Jun-25=5.1、Sep-25=5.3、Dec-25=5.2、Mar-26/Jun-26=5.3；其余未披露按统一 5.3%）（用户规范 2026-08-11：产量/销量描述必须明确品位）
        "lat": -21.7939,  # 卫星影像定位（Yandex/Google Maps）
        "lng": 119.6346,
        "current_q": "26Q2",
        "prev_q": "26Q1",
        "current_q_date": "2026年4-6月",
        "mine_cn": "Pilgangoora（皮尔甘古拉矿山）",
        "report": "PLS June 2026 Quarterly Activities Report（2026-07-30 发布，FY26 Q4 / 日历26Q2）；FY25 Annual Report",
        "source_url": "https://www.pls.com/invest/asx-announcements",
        "equity_note": "100% 资产口径（PLS 全资拥有并运营）；Pilgangoora 为世界最大独立拥有的硬岩锂矿",
        "history_labels": [
            ("production", "精矿产量（万吨，dmt 实际品位 ~5.3% SC）"),
            ("sales", "销量（万吨，dmt 实际品位 ~5.3% SC）"),
            ("prod_sales_ratio", "产销比"),
            ("avg_price", "平均售价（US$/t，CIF China ~SC5.2）"),
            ("cash_cost", "单位成本 FOB（A$/t，dmt）"),
            ("cif_cost", "单位成本 CIF（A$/t，dmt）"),
        ],
        "status_26q2": {
            "existing_lines": [
                {
                    "name": "已有产能1：Pilgan 选矿厂（Pilgan Plant）— 铭牌 ~1.0Mtpa 精矿 dmt（P1000 扩产后；官网口径 spodumene concentrate=产品吨位，实际品位 ~SC5.2-5.3%；配套原矿处理未单独披露）",
                    "q26q2": "26Q2（Jun Q）产量 214.3kt（环比 -8%，主因上季创纪录高基数）；回收率小幅升至 76.8%；矿石分选机（世界最大）性能改善提供运营灵活性；FY26 全年 879.5kt 超指引上限",
                    "q26q1": "26Q1（Mar Q）创纪录产量 232.4kt，回收率 ~75%；P1000 扩建（2025年1月完成）使 Pilgan 产能达 ~1.0Mtpa 基础",
                    "compare": "产量环比 -8% 属高基数回落（232.4→214.3kt），但 FY26 全年 879.5kt 超指引上限 ~10kt；回收率 76.8% 创改善——全年表现超预期"
                },
                {
                    "name": "已有产能2：Ngungaju 选矿厂（Ngungaju Plant）— 铭牌 ~250ktpa 精矿 dmt（2026-07 重启；产品吨位口径）",
                    "q26q2": "26Q2 处于重启准备期（临时维护状态，无产量）；季报后事件：**2026 年 7 月 1 日正式重启**，预计 FY27 前 4 个月（2026年10月底前）达到目标产能；26Q2 FOB 成本上升主因之一即 Ngungaju 重启成本",
                    "q26q1": "25Q4（Dec Q）同处于维护状态；2026-02-19 董事会批准重启，计划 2026年7月初复产",
                    "compare": "重大正面进展：7 月 1 日按计划重启、比 3 月预期更明确（原计划「7月初+9月爬坡」，现明确「FY27 前 4 个月内达目标产能」）；26Q2 已开始计重启成本"
                }
            ],
            "planned_lines": [
                {
                    "name": "P2000 扩建项目 — 2.0Mtpa（可研阶段，预FID支出已批）",
                    "q26q2": "26Q2 可研持续推进，预计 2026 年 12 月季度发布结果；**2026 年 6 月批准 ~$175M 预 FID 资本支出**（详细工程+长周期设备采购）；FID 取决于可研结果、融资与市场条件；新建选矿厂紧邻 Pilgan 设施，全矿浮选流程",
                    "q26q1": "26Q1 可研按更新后时间表推进；评估 FY27 预 FID 资本支出",
                    "compare": "重大进展：预 FID 支出 $175M 于 6 月正式获批（此前仅为评估）——项目推进节奏超预期，FID 决策窗口锁定 2026-12"
                },
                {
                    "name": "Mid-Stream 中游示范厂项目（电煅烧炉）",
                    "q26q2": "26Q2 调试推进中；世界首座工业级电煅烧炉，目标降低排放强度、减少运输需求、矿场就地增值",
                    "q26q1": "26Q1 达成 JV 重组+政府拨款 A$38.1M+承购协议+开始调试四大里程碑",
                    "compare": "持续调试推进；26Q1 已实现里程碑，26Q2 无新增重大披露"
                },
                {
                    "name": "Colina 项目（巴西）— 可研阶段",
                    "q26q2": "26Q2 可研推进中（勘探钻探等）；预 FID 支出待董事会批准；FY27 资本开支表列示 Colina pre-FID 为 Subject to Board approval",
                    "q26q1": "26Q1 可研同步推进（与 P2000 同口径表述）",
                    "compare": "无重大进展变化；与 P2000 并行推进"
                }
            ],
            "overall": {
                "operation_changes": "26Q2 产量 214.3kt（环比 -8%，上季创纪录高基数）；销量 249.9kt（环比 +28%，创纪录，受益港口拥堵缓解后集中发运）；均价 US$2,107/t（环比 +13%，SC5.2 CIF，SC6 等价 US$2,415）；FOB 单位成本 A$616/t（环比 +18%，Ngungaju 重启成本+柴油涨价）；经营现金利润率 A$579M（环比 +26%）；季末现金 A$2,290M（+57%，含 US$600M 债券发行）。",
                "operation_changes_prev": "26Q1 产量 232.4kt（创纪录）；销量 195.7kt；均价 US$1,867/t；FOB 成本 A$520/t；现金 A$1,455M。",
                "future_outlook": "FY26 全年产量 879.5kt 超指引上限（820-870kt）约 10kt；FY27 指引已发布：产量 1,030-1,100kt（中值 106.5 万吨）、FOB 成本 A$575-625/t、资本开支 A$620-685M；Ngungaju 2026年7月1日重启、FY27 前 4 个月达目标产能；P2000 可研 2026-12 发布、FID 决策同期；中游示范厂调试中。",
                "highlights": [
                    "FY26 全年产量 879.5kt 超指引上限（820-870kt）约 10kt——年度指引超预期兑现",
                    "26Q2 销量 249.9kt 创纪录（环比 +28%），5 月港口拥堵缓解后集中发运",
                    "均价连续第三季大涨：US$1,161（25Q4）→1,867（26Q1）→2,107（26Q2），SC6 等价 US$2,415",
                    "Ngungaju 2026年7月1日按计划重启，FY27 前 4 个月达目标产能——双厂模式恢复",
                    "FY27 指引产量 1,030-1,100kt（+17-25% YoY），Ngungaju 重启 + P2000 预FID $175M 已批是双催化"
                ]
            }
        },
"forecast_unit": "万吨 SC6 折算（原 dmt，品位 ~SC5.2——FY27 官方指引品位假设；逐季 grade produced 5.1-5.3%；FY27 指引 1,030-1,100kt dmt（财年口径 2026-07至2027-06）→ SC6 893-953kt；日历 2027 预测=FY27 指引覆盖前两季+FY28 外推后两季；双厂 dmt 产能 ~1.25Mtpa → SC6 ~1.1Mt，利用率 85-90%（27Q3/27Q4 稳态接近满产））",
        "forecast_2027": {
            "basis": "PLS FY27 官方指引已发布（2026-07-30 June QAR）：产量 1,030-1,100kt（财年口径 = 2026年7月-2027年6月，中值 ~1,065kt）；日历 2027 = FY27 后两季（含 Ngungaju 满产）+ FY28 前两季（满产稳态），预计落在指引区间上沿附近；产能基础：Pilgan ~1.0Mtpa（P1000 后，dmt 产品吨位）+ Ngungaju 重启后目标产能 ~250ktpa → 双厂合计 ~1.25Mtpa dmt（SC6 折算 ~1.1Mt）；P2000 可研 2026-12 出结果、FID 若通过则 2028H2 起贡献（2027 年内不纳入）。",
            "assumptions": [
                "Ngungaju 2026年7月重启，FY27 前 4 个月（2026年10月底前）达目标产能——2027 年全年双厂运行",
                "Pilgan 维持 ~200-215kt/季（FY26 后两季实际 205.3/214.3kt，利用率高）",
                "P2000 2027 年内不贡献产量（可研 2026-12 出结果、FID+建设周期 >2 年）",
                "FY27 指引 1,030-1,100kt 为官方锚；日历 2027 因跨 FY27/FY28 两财年，按指引上沿 + Ngungaju 满产推算"
            ],
            "scenarios": {
                "bear": {"label": "悲观（Ngungaju 爬坡慢于计划 + 锂价回落压缩产量）", "production_kt": 1040, "note": "Ngungaju 爬坡慢、Pilgan 利用率回落；全年 ~106 万吨 dmt → SC6 折算 ~93.6（×0.883，品位 ~SC5.2）"},
                "base": {"label": "基准（日历 2027：FY27 指引覆盖 H1 + FY28 外推 H2）", "production_kt": 1080, "note": "Pilgan ~210kt/季×2（FY27 指引期）+ 双厂稳态 ~28.25kt/季×2（FY28 前两季——Ngungaju 满产、利用率 ~90%）→ ~109.7 万吨 dmt → SC6 折算 ~96.9（×0.883，品位 ~SC5.2）"},
                "bull": {"label": "乐观（锂价大涨 + 双厂超产接近满产 90%）", "production_kt": 1100, "note": "双厂超产运行 → ~112.5 万吨 dmt（90% 利用率满产水平）→ SC6 折算 ~99.3（×0.883，品位 ~SC5.2；P2000 仅 pre-FID、FID 2026-12 未定，不进入 2027——审计修正）"}
            },
            "quarterly_base": {"27Q1": 26, "27Q2": 27, "27Q3": 28, "27Q4": 28, "total": 109},
            "confidence": "高：FY27 官方指引 1,030-1,100kt 已发布（首次含 Ngungaju 重启后双厂口径），基准情景取指引上沿附近；不确定性主要在 Ngungaju 爬坡节奏与锂价对产量的传导；P2000 是 2027 年后大变量（FID 2026-12）。",
            "disclaimer": "预测为研究性判断，基于 PLS FY27 官方指引（2026-07-30 发布）推算，非公司直接给出的日历年度数字；日历 2027 与 FY27 财年（2026/7-2027/6）口径不同，已在预测中说明。"
        },
        "capacity_verification": {
            "title": "选矿产能核实（多来源交叉印证）",
            "method": "以 PLS 官网（Wayback 存档）、FY25 年报、June 2026 季报（2026-07-30）及历史季报为来源，逐条核对铭牌产能；官方未单独披露的标 ⚠️，官方确认的标 ✓。",
            "summary": "产能演进脉络：Pilgan 铭牌 ~580ktpa（Pilgan+Ngungaju 合计，FY25 年报口径）→ P680 项目（2024年8月，矿石分选机+HIMS）→ P1000 项目（2025年1月，+320kt）→ 合计 ~1.0Mtpa（官网确认）；Ngungaju 于 2026年7月1日重启（FY27 前 4 个月达目标产能）；P2000 规划 2.0Mtpa（可研 2026-12 出结果，$175M 预FID支出 2026年6月已批）；FY27 指引产量 1,030-1,100kt。",
            "items": [
                {
                    "line": "Pilgan 选矿厂",
                    "excel_capacity": "~1.0Mtpa dmt（P1000 后；SC6 折算 ~875kt）",
                    "verified": "✓ 官方确认（合计口径）",
                    "sources": [
                        {"src": "PLS 官网（2026-06 存档）", "data": "'Following completion of the P1000 Expansion Project in 2025, Pilgangoora has the capacity to produce up to one million tonnes of spodumene concentrate per annum'——1.0Mtpa 官方确认"},
                        {"src": "FY25 年报", "data": "P1000 完成于 FY25，'adding ~320kt to the nameplate capacity'；Pilgan+Ngungaju 合计铭牌 ~580ktpa（P1000 前）；P680 于 2024年8月交付矿石分选机+HIMS"},
                        {"src": "FY25 年报", "data": "P1000 资本支出 $560M，2025-01-31 首矿、3月季度完成爬坡"}
                    ],
                    "status": "ok"
                },
                {
                    "line": "Ngungaju 选矿厂",
                    "excel_capacity": "铭牌 ~250ktpa 精矿 dmt（2026-07 重启；品位 ~5.3%，SC6 折算 ~220kt）",
                    "verified": "⚠️ 铭牌为推算（官方未单独披露精矿口径）",
                    "sources": [
                        {"src": "June 2026 QAR", "data": "2026年7月1日按计划重启（季报后事件），预计 FY27 前 4 个月（2026年10月底前）达目标产能；26Q2 FOB 成本 +18% 含重启成本"},
                        {"src": "FY25 年报", "data": "2024年12月转入临时维护（P850 单厂模式）；FY25 产量 754.6kt 全部来自 Pilgan"}
                    ],
                    "status": "warn"
                },
                {
                    "line": "P2000 扩建项目",
                    "excel_capacity": "2.0Mtpa（规划）",
                    "verified": "⚠️ 可研阶段（2026-12 出结果，预FID $175M 已批）",
                    "sources": [
                        {"src": "June 2026 QAR", "data": "可研结果 2026 年 12 月季度发布；2026年6月批准 ~$175M 预 FID 资本支出；新建选矿厂紧邻 Pilgan 设施，全矿浮选流程；FID 取决于可研/融资/市场"},
                        {"src": "PLS 官网", "data": "'potential to increase production capacity to two million tonnes per annum'"}
                    ],
                    "status": "warn"
                },
                {
                    "line": "全矿合计（双厂）",
                    "excel_capacity": "~1.25Mtpa dmt（Pilgan 1.0 + Ngungaju ~0.25；SC6 折算 ~1.1Mt）",
                    "verified": "⚠️ 官方 FY27 指引 1.03-1.10Mtpa（双厂口径）",
                    "sources": [
                        {"src": "June 2026 QAR", "data": "FY27 指引产量 1,030-1,100kt——首次含 Ngungaju 重启后的双厂口径；FY26 实际 879.5kt 超指引上限"},
                        {"src": "PLS 官网", "data": "P1000 后 1.0Mtpa（Pilgan 单厂口径）"}
                    ],
                    "status": "warn"
                }
            ],
            "sources_index": {
                "公司官网": "PLS 官网 Pilgangoora Operation 页（2026-06-30 Wayback 存档，Cloudflare 防护无法直连）；ASX 公告页 pls.com/invest/asx-announcements",
                "公司季报": "PLS June 2026 Quarterly Activities Report（2026-07-30，最新；via investorpa.com 镜像）",
                "公司年报": "PLS FY25 Annual Report（2025-08-25，含 Appendix 4E）",
                "第三方看板": "飞书海外锂矿季度经营看板（Pilgangoora 3Q2024-2Q2026 产量/销量，标'官方'）",
                "券商/咨询": "本轮未获取付费报告；ASX 公告系统 API 受限"
            },
            "note": "核实时间：2026-08-05（已更新至 June 2026 QAR）。关键结论：① Pilgan 产能 1.0Mtpa 获官网+年报确认（P680→P1000 路径清晰）；② Ngungaju 铭牌未单独披露，2026年7月1日重启、FY27 前 4 个月达目标产能；③ P2000 预FID $175M 已批、可研 2026-12 出结果；④ FY27 官方指引产量 1,030-1,100kt（双厂口径）为产能锚。",
            "images": [
                {"url": "img/sat_pilgangoora.jpg", "src": "卫星影像（Yandex Maps，坐标 -21.7939,119.6346）", "cap": "Pilgangoora 矿区卫星影像（Zoom 13）——露天矿坑与 Pilgan/Ngungaju 选矿厂在卫星影像上的实际形态，卫星追踪第一参照"},
                {"url": "img/pilgangoora_overlook.jpg", "src": "PLS FY25 年报", "cap": "勘探队俯瞰 Pilgangoora 全景——露天矿坑与选矿厂区，可对照卫星影像识别"},
                {"url": "img/pilgangoora_p1000.jpg", "src": "PLS FY25 年报", "cap": "P1000 扩建项目完成图（Pilgan 选矿厂升级后）——项目总览展示图"},
                {"url": "img/pilgangoora_ops.jpg", "src": "PLS FY25 年报", "cap": "Pilgangoora 运营配图（选矿厂与堆场）"}
            ],
            "mining_side": {
                "title": "原矿产能核实（矿坑 / 矿体 / 尾矿库）",
                "method": "以 PLS 官网（Wayback 存档）、FY25 年报、Albermarle 类公开资料交叉核对采矿侧信息。",
                "summary": "Pilgangoora 为单一露天矿（Pilgangoora 伟晶岩区，Central 与 South 矿段），2018 年首次生产；矿权面积庞大（~51,000 公顷 consolidated tenure）；矿山寿命 ~31-32 年；26Q2 总物料移动 10.2Mt、矿石 1.7Mt（为 Ngungaju 重启铺路）；FY26 全年产量 879.5kt 超指引上限。",
                "items": [
                    {
                        "item": "原矿矿山：Pilgangoora 露天矿",
                        "built_plan": "✅ 建成（2018 年首次生产）",
                        "status": "ok",
                        "sources": [
                            {"src": "PLS 官网", "data": "位于 Port Hedland 东南 ~140km，Pilbara 地区；'First production 2018'；31 年矿山寿命"},
                            {"src": "FY25 年报", "data": "FY25 采矿 5.2Mt @ 1.4% Li₂O；~32 年矿山寿命；Mineral Resource 445Mt、Ore Reserve 207.2Mt（官网口径）"}
                        ]
                    },
                    {
                        "item": "矿段与矿体（Central / South）",
                        "built_plan": "✅ 建成（多矿段露天开采）",
                        "status": "ok",
                        "sources": [
                            {"src": "FY25 年报", "data": "FY25 勘探：109 个钻孔 48,194m；900m 深金刚石钻孔（政府共助）发现北部延伸多个伟晶岩域；矿权区为世界最大 LCT 伟晶岩省之一"}
                        ]
                    },
                    {
                        "item": "采矿方法与产能",
                        "built_plan": "✅ 建成（传统露天开采）",
                        "status": "ok",
                        "sources": [
                            {"src": "June 2026 QAR", "data": "26Q2 总物料移动 10.2Mt（26Q1: 9.9Mt）、矿石 1.7Mt（26Q1: 1.3Mt）——增加采矿与剥离为 Ngungaju 重启与未来生产铺路"}
                        ]
                    },
                    {
                        "item": "尾矿库（TSF）",
                        "built_plan": "✅ 建成；⚠️ 扩展规划中",
                        "status": "warn",
                        "sources": [
                            {"src": "FY25 年报", "data": "Pilgan+Ngungaju 尾矿设施持续运营；年报提及尾矿管理政策与扩展计划（未披露具体容量）"}
                        ]
                    },
                    {
                        "item": "P2000 新选矿厂选址（未来）",
                        "built_plan": "⚠️ 可研阶段",
                        "status": "warn",
                        "sources": [
                            {"src": "March 2026 QAR", "data": "P2000 拟新建选矿厂紧邻现有 Pilgan/Ngungaju 设施"}
                        ]
                    }
                ],
                "note": "核实时间：2026-08-05（已更新至 June 2026 QAR）。采矿侧要点：① 单一露天矿服务两座选矿厂（Pilgan + Ngungaju）；② 31-32 年矿山寿命、资源 445Mt/储量 207.2Mt 支撑长期产能；③ PLS 未披露逐坑/逐尾矿库的详细技术参数（无 S-K1300 类 QP 报告），采矿侧细节不及 Greenbushes 丰富；④ 26Q2 总物料移动 10.2Mt、矿石 1.7Mt 创新高，为 Ngungaju 重启铺路。",
                "images": [
                    {"url": "img/pilgangoora_tenure.jpg", "src": "PLS FY25 年报", "cap": "Pilgangoora 矿权地图（consolidated tenure，~51,000 公顷）——卫星锁定矿区范围参照"},
                    {"url": "img/sat_pilgangoora.jpg", "src": "卫星影像（Yandex Maps，坐标 -21.7939,119.6346）", "cap": "Pilgangoora 矿区卫星影像（Zoom 13）——矿坑与选矿厂相对位置，与矿权图对照定位"},
                    {"url": "img/pilgangoora_stockpile.jpg", "src": "PLS 官网", "cap": "Pilgangoora 精矿堆场实景（堆场在卫星影像上通常呈浅色矩形区域）"}
                ]
            }
        }
    },
    {
        "company": "MRL（Mineral Resources）",
        "mine": "Wodgina",
        "sc6": 1.0,   # 2026-08-11：数据层已用官方 SC6（MRL 季报 Produced SC6/Sales SC6，50%→×2）
        "sc6_note": "官方 SC6（MRL 季报 Produced SC6/Sales SC6，100% 口径；50% 权益×2）",
        "grade": "5.5% Li₂O（官方 SC6）",   # 精矿品位标注（用户规范 2026-08-11：产量/销量描述必须明确品位）
        "lat": -21.1746,  # 卫星影像定位（Yandex/Google Maps）
        "lng": 118.6764,
        "current_q": "26Q2",
        "prev_q": "26Q1",
        "current_q_date": "2026年4-6月",
        "mine_cn": "Wodgina（沃吉纳矿山）",
        "report": "MRL Quarterly Activity Report Q4 FY26（2026-07-29 发布，FY26 Q4 / 日历26Q2）；MRL 官网资产页（2025-10 快照）",
        "source_url": "https://www.mineralresources.com.au/our-business/lithium/wodgina/",
        "equity_note": "100% 资产口径为推算（官方披露 50% attributable；MARBL JV = MinRes 50% / Albemarle 50%，MinRes 运营）；销售 100% 为 50%×2 估算",
        "history_labels": [
            ("production", "精矿产量（万吨，100% 推算 · 混合品位 dmt）"),
            ("sales", "销量（万吨，100% 推算 · 混合品位 dmt）"),
            ("prod_sales_ratio", "产销比"),
            ("avg_price", "平均售价（US$/t，CIF SC6）"),
            ("cash_cost", "单位成本 FOB（A$/t SC6）"),
        ],
        "status_26q2": {
            "existing_lines": [
                {
                    "name": "已有产能1：选矿厂 Train 1（A1 产线）— 设计 ~250ktpa 精矿 dmt（SC5.5 品位产品吨位；SC6 折算 ~229kt）",
                    "q26q2": "26Q2 三线利用率提升（产 94k dmt，+21% qoq）；2026-05-19 投资者现场会披露 Q1 FY27 起三线全开；回收率 68%（Stage 2 耗尽、全面转 Stage 3 矿石）；FY26 销量 317k dmt SC6 超指引上限（270-290k）",
                    "q26q1": "26Q1 产 78k dmt（-8% qoq），高品位 Stage 2 矿石减少、更多 Stage 3 低品位矿石入厂，回收率约 69%",
                    "compare": "产量环比 +21% 超预期（94 vs 78k dmt），三线利用改善；但回收率降至 68%——Stage 2 高品位矿石枯竭、Stage 3 全面供矿是中期观察点"
                },
                {
                    "name": "已有产能2：选矿厂 Train 2 / Train 3（A2/A3 产线）— 设计各 ~250ktpa 精矿 dmt（SC5.5 品位；SC6 折算各 ~229kt；三线合计 688-752kt SC6）",
                    "q26q2": "与 Train 1 同为三线运行的一部分；Q1 FY27 起三线全开（此前部分产线间歇运行）；矿石来自 Stage 3 与库存矿石混合",
                    "q26q1": "26Q1 亦在三线运行框架内，但产量受 Stage 2/3 矿石切换影响",
                    "compare": "三线全开是 Q1 FY27 明确指引（2026-05-19 现场会），Q4 已为三线运行铺路——产能利用率提升超预期"
                },
                {
                    "name": "选矿厂配套：破碎 + 浮选 + 尾矿设施（配套产能未单独披露）",
                    "q26q2": "选矿厂含球磨、脱泥旋流器、磁选、浮选与精矿/尾矿脱水；细尾矿泵送至湿式尾矿库，粗尾矿与废石混合回填",
                    "q26q1": "同口径（尾矿设施持续运行）",
                    "compare": "无实质变化"
                }
            ],
            "future_lines": [
                {
                    "name": "Stage 4 矿坑预剥离（2026-07 起；原矿扩能——新增原矿产能未披露，原矿非精矿不折算 SC6）",
                    "q26q2": "Q1 FY27 启动 Stage 4 预剥离——为下一阶段矿石供应做准备；目前无 Train 4 计划（官网未提及）",
                    "q26q1": "26Q1 提及 Stage 4 预剥离计划",
                    "compare": "按计划推进；产能扩张路径为矿坑扩展而非新选矿列车"
                }
            ],
            "overall": {
                "operation_changes": "26Q2 三线利用率提升推动产量 +21% qoq（94k dmt），FY26 销量 317k SC6 超指引；回收率 68%（Stage 2→3 切换）；Stage 4 预剥离 7 月启动",
                "prev_operation_changes": "26Q1 产量 78k dmt（-8%），高品位 Stage 2 矿石减少、更多 Stage 3 低品位矿石入厂，回收率约 69%",
                "highlights": [
                    "FY26 销量 317k dmt SC6，超上调后指引（270-290k）上限约 10%——三线利用驱动的年度超预期",
                    "Q4 产量 94k dmt 环比 +21%，三线利用率提升；Q1 FY27 起三线全开（2026-05-19 投资者现场会）",
                    "26Q2 均价 US$2,450/dmt CIF SC6（+15% qoq）——锂价回升周期受益",
                    "FY26 FOB 成本 $738/dmt SC6，达指引下沿（$730-800）——成本控制优于指引",
                    "Stage 4 预剥离 Q1 FY27 启动——矿坑扩展保障未来 3 年矿石供应"
                ]
            }
        },
        "fc_unit": "万吨/年 SC6（官方口径 · 品位 5.5% Li₂O——MRL 季报 Produced SC6/Sales SC6，100%）",
        "fc_2027": [
            {"label": "悲观", "val": 70, "note": "三线利用率不足 + Stage 3 品位走低（年化低于当前 ~72 万吨 dmt → SC6 ~66）"},
            {"label": "基准", "val": 75, "note": "谨慎基准（2026-08-11 用户要求下调）：≈Q4 FY26 年化 66.4 万吨 SC6（83k×2×4），三线 Q1 FY27 全开但 Stage 3 低品位+回收率 68% 压制——铭牌 69 SC6 仅乐观情景"},
            {"label": "乐观", "val": 90, "note": "三线超产 + 品位回升 + 价格上行释放库存"}
        ],
        "capacity_verification": {
            "title": "选矿产能核实（多来源交叉印证）",
            "method": "以 MRL 官网资产页（2025-10 快照）、MRL 年报、季度报告为来源，逐条核对选矿产能；官方未单独披露的标 ⚠️，官方确认的标 ✓。",
            "summary": "Wodgina 三列选矿列车（Train 1/2/3）总产能约 750ktpa SC5.5%（官网原文）或 820ktpa（官网 PDF 另一处表述），采用保守值 ~750ktpa；每列车为球磨+脱泥+磁选+浮选流程。",
            "items": [
                {
                    "line": "选矿厂 Train 1/2/3（A1-A3）",
                    "excel_capacity": "~250kt × 3 = 750kt dmt（SC5.5 品位；SC6 折算 ~688kt）",
                    "verified": "✓ 官方确认（总产能口径）",
                    "sources": [
                        {"src": "MRL 官网资产页（2025-10 快照）", "data": "three processing trains with a total annual production capacity of approximately 820,000 tonnes of spodumene concentrate at a grade of 5.5% Li2O——三列列车总产能官方确认；每列车含球磨机+脱泥旋流器+磁选+浮选"},
                        {"src": "MRL 官网（2026-08 抓取）", "data": "总设计产能约 750,000 t/a SC @ 5.5% Li2O（≈3×250ktpa）——官网另一处表述，取保守值"},
                        {"src": "Q4 FY26 季报", "data": "三线利用率提升、Q1 FY27 起三线全开；Q4 产量 94k dmt 为三线运行成果——实际产能利用率验证"}
                    ]
                },
                {
                    "line": "破碎厂（CSI Mining Services 运营）",
                    "excel_capacity": "配套选矿厂",
                    "verified": "✓ 官方确认",
                    "sources": [
                        {"src": "MRL 官网资产页", "data": "破碎厂由 CSI Mining Services（MinRes 子公司）运营，压碎后进入选矿厂"},
                        {"src": "Q4 FY26 季报", "data": "TMM 10,100k wmt（100%）、矿石开采 1,118k dmt——采矿+破碎系统满负荷运行"}
                    ]
                },
                {
                    "line": "全矿合计（100% 口径）",
                    "excel_capacity": "~750-820kt dmt（SC5.5 品位；SC6 折算 ~688-752kt）",
                    "verified": "✓ 官网双表述（750/820）",
                    "sources": [
                        {"src": "MRL 官网", "data": "三列列车总产能 750-820ktpa（官网两处表述差异）——页面取 750ktpa 保守值"},
                        {"src": "FY26 实际", "data": "FY26 销量 317k dmt SC6（50%）→ 100% 约 634k——产能利用率约 85%（含爬坡期）"}
                    ]
                }
            ],
            "note": "核实时间：2026-08-05。关键结论：① 三列选矿列车总产能 750-820ktpa SC5.5%（官网确认）；② 无 Train 4 计划（官网未提及），产能扩张靠矿坑 Stage 4；③ 2023-10-18 起 MRL 权益从 40% 升至 50%（此前 Wodgina 按 40% 披露）。",
            "sources_index": {"公司官网": "MRL 资产页（2025-10 快照）+ 官网抓取", "公司季报": "MRL 季度活动报告（Q4 FY26 等）", "公司公告": "JORC 资源储量更新（2022/2023）、2026-05 FID 公告", "数据站": "USGS/Wikipedia/OSM 坐标验证", "券商咨询": "本轮未引用（公开数据充分）"},
            "images": [
                {"url": "img/sat_wodgina.jpg", "src": "卫星影像（Yandex Maps，坐标 -21.1746,118.6764）", "cap": "Wodgina 矿区卫星影像（Zoom 13）——露天矿坑与选矿厂区在卫星影像上的实际形态，卫星追踪第一参照"},
                {"url": "img/wodgina_location.jpg", "src": "MRL 官网资产页", "cap": "Wodgina 位置图——矿区相对 Port Hedland / Marble Bar / Karratha 的位置"},
                {"url": "img/wa_lithium_map.jpg", "src": "MRL 官网", "cap": "西澳锂矿分布图（Wodgina/Mt Marion/其他锂矿位置总览）"},
                {"url": "img/wodgina_processing.jpg", "src": "MRL 官网资产页", "cap": "Wodgina 选矿厂（三列浮选列车）——项目展示图"},
                {"url": "img/wodgina_aerial.jpg", "src": "MRL 官方媒体库", "cap": "Wodgina 矿区航拍全景——露天矿坑与选矿厂布局"}
            ],
            "mining_side": {
                "title": "原矿产能核实（矿坑 / 矿体 / 尾矿库）",
                "method": "以 MRL 官网资产页、JORC 资源储量公告（2022/2023）、季报运营描述为来源。",
                "items": [
                    {
                        "line": "原矿矿山：Wodgina 露天矿",
                        "status": "✅ 建成（2019 年前 DSO 时代已开采）",
                        "sources": [
                            {"src": "MRL 官网资产页", "data": "露天开采（钻爆-装载-运输循环）；上部 20-50m 强风化、下部坚硬岩石；矿石堆存于 ROM pad"},
                            {"src": "Q4 FY26 季报", "data": "26Q2 总物料移动 10,100k wmt（100%）、矿石 1,118k dmt"}
                        ]
                    },
                    {
                        "line": "矿体与品位（Stage 1-4）",
                        "status": "✅ 多阶段矿坑",
                        "sources": [
                            {"src": "MRL 2023 资源储量更新", "data": "资源 217.4 Mt @ 1.15% Li₂O（2023-06-30）；储量 164.6 Mt @ 1.15%"},
                            {"src": "Q4 FY26 季报", "data": "Stage 2 矿石耗尽、全面转 Stage 3；Stage 4 预剥离 2026 年 7 月启动——多阶段开采规划"}
                        ]
                    },
                    {
                        "line": "地下开采（未来）",
                        "status": "⚠️ 评估中",
                        "sources": [
                            {"src": "MRL 官网资产页", "data": "future opportunities to mine ore at depth via underground mining methods which are being assessed——地下开采评估中"}
                        ]
                    },
                    {
                        "line": "尾矿库（TSF）",
                        "status": "✅ 建成",
                        "sources": [
                            {"src": "MRL 官网资产页", "data": "细尾矿泵送至湿式尾矿库，粗尾矿与废石混合回填——现场有尾矿储存设施"}
                        ]
                    },
                    {
                        "line": "废石堆 / ROM pad",
                        "status": "✅ 建成",
                        "sources": [
                            {"src": "MRL 官网资产页", "data": "废石堆、ROM pad、破碎站为现场基础设施"}
                        ]
                    }
                ],
                "note": "核实时间：2026-08-05。采矿侧要点：① Wodgina 为世界最大已知硬岩锂矿床之一，多阶段露天开采（Stage 1-4）；② 地下开采评估中（官网确认）；③ 2022 年资源 259.2 Mt @ 1.17% → 2023 年 217.4 Mt @ 1.15%（采矿消耗+边界调整），储量 164.6 Mt 支撑多年开采。",
                "images": [
                    {"url": "img/sat_wodgina.jpg", "src": "卫星影像（Yandex Maps）", "cap": "Wodgina 矿区卫星影像——矿坑轮廓与选矿厂相对位置"},
                    {"url": "img/wodgina_location.jpg", "src": "MRL 官网", "cap": "Wodgina 位置图（含 Port Hedland 关系）"},
                    {"url": "img/wodgina_mining.jpg", "src": "MRL 官网资产页", "cap": "Wodgina 露天采矿（钻爆-装载-运输）实景"}
                ]
            }
        }
    },
    {
        "company": "MRL（Mineral Resources）",
        "mine": "Mt Marion",
        "sc6": 1.0,   # 2026-08-11：数据层已用官方 SC6（MRL 季报 Produced SC6/Sales SC6；产 50%×2、销 51%÷0.51）
        "sc6_note": "官方 SC6（MRL 季报 Produced SC6/Sales SC6，100% 口径；产 50%×2、销 51%÷0.51）",
        "grade": "4.3-4.5% Li₂O（官方 SC6；双品位混合）",   # 精矿品位标注（用户规范 2026-08-11：产量/销量描述必须明确品位）
        "lat": -31.0738,  # 卫星影像定位（Yandex/Google Maps）
        "lng": 121.4611,
        "current_q": "26Q2",
        "prev_q": "26Q1",
        "current_q_date": "2026年4-6月",
        "mine_cn": "Mt Marion（马里恩矿山）",
        "report": "MRL Quarterly Activity Report Q4 FY26（2026-07-29 发布，FY26 Q4 / 日历26Q2）；MRL 官网资产页",
        "source_url": "https://www.mineralresources.com.au/our-business/lithium/mt-marion/",
        "equity_note": "100% 资产口径为推算（官方披露 50% attributable 产量、51% 包销份额销量；JV = MinRes 50% / Ganfeng 50%，MinRes 运营）；销量 100% 为 51%÷0.51 估算",
        "history_labels": [
            ("production", "精矿产量（万吨，100% 推算 · 混合品位 dmt）"),
            ("sales", "销量（万吨，100% 推算 · 混合品位 dmt）"),
            ("prod_sales_ratio", "产销比"),
            ("avg_price", "平均售价（US$/t，CIF SC6）"),
            ("cash_cost", "单位成本 FOB（A$/t SC6）"),
        ],
        "status_26q2": {
            "existing_lines": [
                {
                    "name": "已有产能1：DMS 重介质选矿厂（主回路）— 设计 ~500ktpa 精矿 dmt（5%/3.5% 双品位混合产品；SC6 折算 ~459kt）",
                    "q26q2": "26Q2 产 82k dmt（+3% qoq）；回收率 59%（26Q1: 60%）；矿石分选机（ore sorting）已投产，FY27 处理低品位接触矿堆；矿石来源 N9（N4 完成开采）；DMS 回路按粒度分 3 个产品流",
                    "q26q1": "26Q1 产 80k dmt（-1% qoq），回收率 60%；矿石来自 N9/N4；预剥离在 N11 推进",
                    "compare": "产量温和 +3%，回收率 59-60% 稳定；ore sorting 投产是 FY27 低品位矿石处理的关键变量——技术升级超预期"
                },
            ],
            "future_lines": [
                {
                    "name": "已有产能2：浮选厂（FID 2026-05-26，$490M；2027 年中投产；设计产能未披露——回收 DMS 尾矿 SC6）",
                    "q26q2": "浮选厂建设推进中（FID 2026-05-26，$240M 100% 口径）；FID 装机由约 500ktpa SC6 增至 600ktpa SC6（新增铭牌）；建筑团队已进场、长周期设备采购已启动；调试爬坡安排在 2H FY28（即日历 2028H1，不计入 2027 产量——审计修正）",
                    "q26q1": "26Q1 浮选厂处于 FID 前评估",
                    "compare": "FID 2026-05-26 正式通过（投资 $490M 含浮选+地下+基建）——扩建项目进入执行期，超预期"
                },
                {
                    "name": "地下开发（预生产开发；产能未披露）",
                    "q26q2": "地下预生产开发 FID（$220M）；2026-07-15 任命 Macmahon 为地下采矿合同伙伴；North/Central 坑内 portal 支护工程 7 月开工；此前 2024 年曾建 exploration decline、2024-12 因市场进入维护，现重启",
                    "q26q1": "26Q1 地下开发处于评估/重启准备",
                    "compare": "Macmahon 任命（2026-07-15）标志地下开发重启进入执行——重大进展"
                },
                {
                    "name": "N11 矿坑过渡（FY27）",
                    "q26q2": "北坑从 N9 过渡到 N11 作为主要矿石来源（预剥离推进中）；ore sorting 用于处理低品位 contact ore 库存；N10 预剥离后续启动",
                    "q26q1": "26Q1 N9 开采中、N11 预剥离进行",
                    "compare": "N9→N11 过渡按计划推进"
                }
            ],
            "overall": {
                "operation_changes": "26Q2 产量 82k dmt（+3%）、销量 94k dmt（51% 口径，+32% qoq）；回收率 59%；FY26 销量 242k SC6 超指引；浮选厂 FID + 地下开发 Macmahon 任命",
                "prev_operation_changes": "26Q1 产量 80k dmt（-1%）、销量 71k（-20% qoq 因船期）；回收率 60%",
                "highlights": [
                    "FY26 销量 242k dmt SC6，超上调后指引（210-230k）上限约 5%",
                    "26Q2 销量 94k dmt（51%）环比 +32%——含补发 Q3 船期；均价 US$2,392/dmt CIF SC6（+15% qoq）",
                    "浮选厂+地下开发 FID 2026-05-26 通过（$490M 总投资）——双项目进入执行期，超预期",
                    "Macmahon 被任命为地下采矿承包商（2026-07-15），portal 工程 7 月开工——地下开发重启落地",
                    "ore sorting 投产，FY27 起处理低品位接触矿堆——回收率提升技术路径明确"
                ]
            }
        },
        "fc_unit": "万吨/年 SC6（官方口径 · 品位 4.3-4.5% Li₂O——MRL 季报 Produced SC6/Sales SC6，100%）",
        "fc_2027": [
            {"label": "悲观", "val": 45.0, "note": "浮选厂延期 + N9→N11 过渡品位波动 + 回收率 59%（低于 DMS 满产 45.4 SC6）"},
            {"label": "基准", "val": 47.0, "note": "适度乐观（2026-08-11 用户要求）：DMS 满产 45.4 万吨 SC6（FY26 227k×2 官方）+ 浮选厂 2027H2 调试贡献 ~1.6（FID 装机 500→600ktpa SC6，2027 年中投产）——基准 47 SC6"},
            {"label": "乐观", "val": 50.0, "note": "浮选厂提前投产 + 地下开发贡献 + 回收率升至 63%（50 SC6）"}
        ],
            "capacity_verification": {
            "title": "选矿产能核实（多来源交叉印证）",
            "method": "以 MRL 官网资产页、季度报告、FID 公告为来源，逐条核对选矿产能；官方未单独披露的标 ⚠️，官方确认的标 ✓。",
            "summary": "Mt Marion DMS 选矿厂设计年产能约 500,000 t SC（5%/3.5% 双品位）；浮选厂在建（$240M）投产后处理 DMS 细粒产品；地下开发与浮选厂为 FY27-28 主要扩建。",
            "items": [
                {
                    "line": "DMS 重介质选矿厂",
                    "excel_capacity": "~500ktpa 精矿 dmt（5%/3.5% 双品位混合；SC6 折算 ~459kt）",
                    "verified": "✓ 官网确认（总产能口径）",
                    "sources": [
                        {"src": "MRL 官网资产页", "data": "DMS 回路按粒度分 3 个产品流；设计年产能约 500,000 t spodumene concentrate（典型 5% 与 3.5% Li₂O 两种品位）"},
                        {"src": "Q4 FY26 季报", "data": "26Q2 产量 82k dmt、回收率 59%；ore sorting 投产——产能利用率与技术进步验证"}
                    ]
                },
                {
                    "line": "浮选厂（在建）",
                    "excel_capacity": "处理 DMS 细粒（不新增精矿铭牌）",
                    "verified": "✓ FID 确认",
                    "sources": [
                        {"src": "FID 公告 2026-05-26", "data": "浮选厂 $240M（100% 口径）；投产后处理 DMS 细粒/低品位产品、提升综合回收率；建筑团队已进场、长周期采购启动"},
                        {"src": "MRL 官网新闻", "data": "2024-03 曾宣布锂加工枢纽计划——浮选厂前身"}
                    ]
                },
                {
                    "line": "地下开发（预生产）",
                    "excel_capacity": "地下预生产开发 $220M（原矿产能未披露——地下采矿非精矿，不折算 SC6）",
                    "verified": "✓ FID 确认",
                    "sources": [
                        {"src": "FID 公告 2026-05-26", "data": "地下预生产开发 $220M；Macmahon 任命（2026-07-15）；North/Central portal 支护开工"},
                        {"src": "2024-02 资源更新", "data": "地下资源 19.3 Mt @ 1.22%（+111%）；North Pit 地下矿体 500m 走向、30-60m 厚、1.2km 深"}
                    ]
                }
            ],
            "note": "核实时间：2026-08-05。关键结论：① DMS 选矿厂 ~500ktpa（官网确认）；② 浮选厂 FID 2026-05-26（$240M）在建；③ 地下开发 FID 同步通过（$220M）；④ FY27-28 为浮选+地下双项目执行期。",
            "sources_index": {"公司官网": "MRL 资产页", "公司季报": "MRL 季度活动报告（Q4 FY26 等）", "公司公告": "JORC 资源储量更新（2018/2022/2023）、2024-02 地下资源更新、2026-05 FID 公告", "数据站": "USGS/Wikipedia/OSM 坐标验证", "券商咨询": "本轮未引用（公开数据充分）"},
            "images": [
                {"url": "img/sat_marion.jpg", "src": "卫星影像（Yandex Maps，坐标 -31.0738,121.4611）", "cap": "Mt Marion 矿区卫星影像（Zoom 13）——露天矿坑与选矿厂区在卫星影像上的实际形态，卫星追踪第一参照"},
                {"url": "img/marion_location.jpg", "src": "MRL 官网资产页", "cap": "Mt Marion 位置图——Kalgoorlie 以北 70km，Goldfields 地区"},
                {"url": "img/wa_lithium_map.jpg", "src": "MRL 官网", "cap": "西澳锂矿分布图（Wodgina/Mt Marion/其他锂矿位置总览）"},
                {"url": "img/marion_processing.jpg", "src": "MRL 官网资产页", "cap": "Mt Marion DMS 选矿厂——项目展示图"},
                {"url": "img/marion_drone_fid.jpg", "src": "MRL 官网（FID 新闻头图）", "cap": "Mt Marion 浮选厂/地下开发 FID 无人机航拍"}
            ],
            "mining_side": {
                "title": "原矿产能核实（矿坑 / 矿体 / 尾矿库）",
                "method": "以 MRL 官网资产页、JORC 资源储量公告（2018/2022/2023）、地下资源更新（2024）、季报运营描述为来源。",
                "items": [
                    {
                        "line": "原矿矿山：Mt Marion 露天矿（北坑 N9/N11 + 南坑）",
                        "status": "✅ 建成（2016 年投产）",
                        "sources": [
                            {"src": "MRL 官网资产页", "data": "露天锂矿，世界第二大高品位锂资源（约 71 Mt spodumene）；上部 15-40m 风化；新鲜废石密度接近锂辉石，DMS 需控制贫化"},
                            {"src": "Q4 FY26 季报", "data": "26Q2 矿石来源 N9（N4 完成）；N11 预剥离推进；TMM 9,578k wmt（+81% qoq）"}
                        ]
                    },
                    {
                        "line": "矿体与品位（N4/N9/N10/N11 + Central/C2）",
                        "status": "✅ 多矿坑多阶段",
                        "sources": [
                            {"src": "MRL 2023 资源储量更新", "data": "资源 64.8 Mt @ 1.42%（2023-06-30）；储量 35.7 Mt @ 1.42%（+107%）"},
                            {"src": "2024-02 地下资源更新", "data": "地下资源 19.3 Mt @ 1.22%（+111%）；露天 46.8 Mt @ 1.42%——合计 66.1 Mt；North Pit 地下矿体 500m 走向、30-60m 厚、1.2km 深"}
                        ]
                    },
                    {
                        "line": "地下开发（North/Central portal）",
                        "status": "⚠️ 预生产开发（FID 2026-05）",
                        "sources": [
                            {"src": "FID 公告 + Macmahon 任命", "data": "地下预生产开发 $220M；2026-07-15 Macmahon 为合同伙伴；portal 支护工程 7 月开工；此前 exploration decline 2024-12 因市场进入维护"},
                            {"src": "2024-02 资源更新", "data": "地下资源 19.3 Mt @ 1.22%"}
                        ]
                    },
                    {
                        "line": "尾矿库（TSF）",
                        "status": "✅ 建成",
                        "sources": [
                            {"src": "MRL 官网资产页", "data": "现场含尾矿设施（DMS 回路尾矿）"}
                        ]
                    },
                    {
                        "line": "废石堆 / ROM pad",
                        "status": "✅ 建成",
                        "sources": [
                            {"src": "MRL 官网资产页", "data": "多个露天矿坑、废石堆、ROM pad 为现场基础设施"}
                        ]
                    }
                ],
                "note": "核实时间：2026-08-05。采矿侧要点：① 露天多坑开采（N4/N9/N11 + Central/C2），北坑为主；② 地下资源 19.3 Mt 支撑地下开发 FID；③ 资源储量：2018 年 71.3 Mt → 2023 年 64.8 Mt 露天 + 19.3 Mt 地下（口径变化+消耗）。",
                "images": [
                    {"url": "img/sat_marion.jpg", "src": "卫星影像（Yandex Maps）", "cap": "Mt Marion 矿区卫星影像——矿坑轮廓与选矿厂相对位置"},
                    {"url": "img/marion_location.jpg", "src": "MRL 官网", "cap": "Mt Marion 位置图（Kalgoorlie 以北 70km）"},
                    {"url": "img/marion_mining.jpg", "src": "MRL 官网资产页", "cap": "Mt Marion 露天采矿实景（多矿坑）"}
                ]
            }
        }
    }
,
    {
        "company": "Liontown（Liontown Resources）",
        "mine": "Kathleen Valley",
        "sc6": 0.833,   # SC6 折算系数（用户规范 2026-08-10：精矿产量/产能/预测全站统一 SC6 口径）
        "sc6_note": "SC6 折算（原 dmt ~5.0% Li₂O；Liontown 披露实际品位精矿）",
        "grade": "~5.0% Li₂O（dmt 实际品位）",   # 精矿品位标注（用户规范 2026-08-11：产量/销量描述必须明确品位）
        "grade_series": {},   # 逐季品位（Liontown QAR 披露实际品位 ~5.0%，各季 QAR 未逐一提取——网络受限，按统一 5.0% 折算）
        "lat": -27.4678,  # 卫星影像定位（Yandex/Google Maps）
        "lng": 120.7047,
        "current_q": "26Q2",
        "prev_q": "26Q1",
        "current_q_date": "2026年4-6月",
        "mine_cn": "Kathleen Valley（凯瑟琳谷矿山）",
        "report": "Liontown Quarterly Activities Report June 2026（2026-07-29 发布，FY26 Q4 / 日历26Q2）；June Quarter FY26 Results Presentation",
        "source_url": "https://www.liontown.com/project/kathleen-valley/",
        "equity_note": "100% 资产口径（Liontown 全资拥有并运营）；历史承购方含 LG Energy Solution / Tesla / Ford / Canmax；LGES 可转债 2026-01 转股",
        "history_labels": [
            ("production", "精矿产量（万吨，dmt 实际品位 ~5.0% SC）"),
            ("sales", "销量（万吨，dmt 实际品位 ~5.0% SC）"),
            ("prod_sales_ratio", "产销比"),
            ("avg_price", "平均售价（US$/t，SC6e）"),
            ("cash_cost", "单位成本 FOB（A$/t sold）"),
        ],
        "status_26q2": {
            "existing_lines": [
                {
                    "name": "已有产能1：选矿厂（第四代浮选流程）— 设计 ~500ktpa 精矿 dmt（Liontown 官网 nameplate concentrate 产品吨位；2.5Mtpa 原矿；SC6 折算 ~417kt）",
                    "q26q2": "26Q2 产 103,111 dmt（+7% qoq）、销 108,489 dmt（+29%）；平均品位 5.0%；回收率 ~63%（纯净地下矿时 70%）；工厂可用率 92%；55% 地下矿 + 45% 露天库存料入厂（露天采矿已于 2025-12 结束——审计修正）",
                    "q26q1": "26Q1 产 96,367 dmt（-9% qoq，高基数）；回收率受入料混合影响；露天矿接近收尾（2025-12 完成）",
                    "compare": "产量 +7%、销量 +29% 超预期；回收率 63% 仍受露天矿污染拖累——2026 转纯地下后回收率有望升至 70%"
                },
                {
                    "name": "已有产能2：地下矿（澳洲首个地下锂矿；地下产能未单独披露，全矿原矿 2.5-2.8Mtpa）",
                    "q26q2": "地下开发创纪录 3,316m（+35% qoq）；采出地下矿 356kt；向 2.8Mtpa 原矿运行率（FY27 底）推进；长孔空场采矿+膏体充填（南半球最大膏体厂）",
                    "q26q1": "26Q1 地下开发 2,450m（+X%）；地下/露天混合供矿",
                    "compare": "开发米数创纪录 +35% 是核心超预期——为 Q2 FY27 起的产量跃升铺路"
                },
                {
                    "name": "选矿厂配套：矿石分选（ore sorting）+ 钽副产（配套产能未单独披露）",
                    "q26q2": "Steinert 矿石分选 2 列运行；钽精矿产 99 dmt（Q1: 235，因入料变化）；尾矿处理含膏体充填回填地下采空区",
                    "q26q1": "26Q1 钽精矿产 235 dmt",
                    "compare": "钽产量下降与地下矿为主相关（地下矿钽品位低）——副产品贡献减弱但非核心"
                }
            ],
            "future_lines": [
                {
                    "name": "Kathleen Valley 扩建（FID 预计 Q1 FY27 底）",
                    "q26q2": "扩建研究推进中，FID 预计 2026 年 9 月底；范围：球磨机 5.5MW 采购（吞吐量/回收率关键路径）、NW Flats 地下开发（从 Kathleen's Corner 露天坑进入）、MSA Stage 1；FY26 early works $14M 已发生、FID 前最高 $77M",
                    "q26q1": "26Q1 扩建研究进行中；2026-04-29 宣布 early works + long-lead procurement 启动",
                    "compare": "FID 时间表明确（Q1 FY27 底）+ 长周期设备采购启动——扩建进入执行前夜，超预期"
                }
            ],
            "overall": {
                "operation_changes": "26Q2 产 103.1kt（+7%）、销 108.5kt（+29%）；均价 US$1,880 SC6e（+2%）；净现金流 +$137M、现金 $561M；地下开发 3,316m 创纪录；FY26 产量 392k dmt 达指引中段（365-450k）",
                "prev_operation_changes": "26Q1 产 96.4kt（-9%）；均价 US$1,845 SC6e；现金 $424M",
                "highlights": [
                    "FY26 产 391,992 dmt / 销 381,997 dmt，达指引（365-450k SC6）中段——首个完整财年超预期兑现",
                    "净现金流 +$137M（季）、现金升至 $561M——财务自造血能力确立",
                    "地下开发 3,316m 创纪录（+35% qoq）——2.8Mtpa 目标 FY27 底按计划推进",
                    "26Q2 均价 US$1,880 SC6e（+2% qoq）——锂价回升周期受益",
                    "扩建 FID 锁定 Q1 FY27 底（球磨机 5.5MW + NW Flats 地下开发）——产能翻倍路径清晰"
                ]
            }
        },
        "fc_unit": "万吨 SC6 折算（原 dmt ~5.0%：FY27 指引 390-440k dmt ×0.833，Liontown 披露实际品位精矿）",
        "fc_2027": [
            {"label": "悲观", "val": 40, "note": "地下爬坡不及预期 + 回收率维持 63%（FY27 指引下沿 390k dmt concentrate）"},
            {"label": "基准", "val": 44, "note": "FY27 指引中值 415k dmt concentrate（390-440k，实际精矿 dmt）+ 2.8Mtpa 原矿运行率 FY27 底达成"},
            {"label": "乐观", "val": 50, "note": "扩建 FID 后加速 + 纯地下矿回收率 70%+ 提前兑现"}
        ],
        "capacity_verification": {
            "title": "选矿产能核实（多来源交叉印证）",
            "method": "以 DFS 2021（ASX 公告 02450567）、2025-09 资源储量更新（61285782）、Liontown 官网、季度报告为来源，逐条核对选矿产能；官方未单独披露的标 ⚠️，官方确认的标 ✓。",
            "summary": "Kathleen Valley 选矿厂（第四代流程：破碎+矿石分选+浮选）设计产能 2.5Mtpa 原矿 → ~500ktpa SC6.0（DFS 2021）；实际爬坡目标 2.8Mtpa 原矿运行率（FY27 底，地下采矿运行率目标；550-560ktpa 为按回收率的研究推算，非官方精矿铭牌）；扩建（球磨机 5.5MW + NW Flats）FID 预计 Q1 FY27 底。",
            "items": [
                {
                    "line": "选矿厂（第四代浮选流程）",
                    "excel_capacity": "~500ktpa 精矿 dmt（concentrate 产品吨位；SC6 折算 ~417kt；2.5Mtpa 原矿）",
                    "verified": "✓ DFS 官方确认（设计口径）",
                    "sources": [
                        {"src": "DFS 2021-11-11（ASX 02450567）", "data": "基准产能 2.5Mtpa 原矿 → ~500ktpa SC6.0；第 6 年扩至 4Mtpa → ~700ktpa；建厂 Q3 2022-Q4 2023、投产 Q2 2024"},
                        {"src": "Liontown 官网资产页", "data": "爬坡至 2.8Mtpa 原矿（FY27 底）；第四代选矿厂；南半球最大膏体充填厂"},
                        {"src": "2025-09 资源储量更新", "data": "地下矿设计 ~2.8Mtpa（FY2031 前），NW 开发后 3.0Mtpa（FY2031-2046）"}
                    ]
                },
                {
                    "line": "矿石分选（ore sorting）",
                    "excel_capacity": "2 列 Steinert（20ktpm 上限）",
                    "verified": "✓ 官方确认",
                    "sources": [
                        {"src": "2025-09 资源储量更新", "data": "Steinert ore sorting trains 2 列，处理上限 20ktpm；分选精矿计入储量"},
                        {"src": "Q4 FY26 季报", "data": "26Q2 55% 地下矿 + 45% 露天矿入厂，矿石分选持续运行"}
                    ]
                },
                {
                    "line": "扩建（FID Q1 FY27 底）",
                    "excel_capacity": "球磨机 5.5MW + NW Flats",
                    "verified": "✓ 官方公告（2026-04-29）",
                    "sources": [
                        {"src": "June FY26 Results Presentation", "data": "FID 预计 Q1 FY27 底；球磨机 5.5MW 采购为关键路径；NW Flats 地下开发从 Kathleen's Corner 露天坑进入；MSA Stage 1 建设"},
                        {"src": "新闻 2026-04-29", "data": "early works + long-lead procurement 已启动；FY26 early works $14M、FID 前最高 $77M"}
                    ]
                }
            ],
            "note": "核实时间：2026-08-05。关键结论：① DFS 设计 500ktpa SC6（2.5Mtpa 原矿），2024-11 战略调整至 2.8Mtpa 运行率（FY27 底），工厂设计产能 3.0Mtpa；② 扩建 FID 锁定 Q1 FY27 底（球磨机+NW Flats+MSA），4Mtpa 扩建路径保留；③ FY26 产 392k dmt 达指引中段；④ FY27 指引：精矿 390-440k dmt concentrate（2026-07-29 澄清非 SC6）、FOB A$1,050-1,250、资本开支 A$320-370M；⑤ 2026 转纯地下开采（露天 2025-12 完成）。",
            "sources_index": {"公司公告": "DFS 2021、2025-09 资源储量更新、2026-04 扩建公告、季度报告", "公司官网": "Kathleen Valley 资产页（含 Google Earth 位置图）", "公司展示": "June Quarter FY26 Results（2026-07-29）", "数据站": "USGS/Wikipedia/OSM 坐标验证", "券商咨询": "本轮未引用（公开数据充分）"},
            "images": [
                {"url": "img/kv_google_earth.jpg", "src": "Liontown 官网（Google Earth 图）", "cap": "Kathleen Valley 位置图（Google Earth 底图）——Leinster 以北 60km、Geraldton 港出口，卫星追踪区域参照"},
                {"url": "img/sat_kathleen_z13.jpg", "src": "卫星影像（Yandex Maps，坐标 -27.4678,120.7047）", "cap": "Kathleen Valley 矿区卫星影像（Zoom 13）——地下矿/露天坑/选矿厂在卫星影像上的实际形态，卫星追踪第一参照"},
                {"url": "img/kv_main_overview.jpg", "src": "Liontown 官网（2026-05-19）", "cap": "Kathleen Valley 主视图（2026-05）——选矿厂与矿区布局总览"},
                {"url": "img/kv_process_plant.jpg", "src": "Liontown 官网", "cap": "Kathleen Valley 选矿厂（第四代浮选流程）——项目展示图"},
                {"url": "img/kv_ore_circuit.jpg", "src": "Liontown 官网", "cap": "全矿石浮选回路——选矿工艺项目图"}
            ],
            "mining_side": {
                "title": "原矿产能核实（矿坑 / 矿体 / 尾矿库）",
                "method": "以 DFS 2021、2025-09 资源储量更新、Liontown 官网、季度报告为来源。",
                "items": [
                    {
                        "line": "原矿矿山：露天矿（Kathleen's Corner / Mt Mann）",
                        "status": "✅ 建成（2024-07 投产）；⚠️ 2025-12 完成开采",
                        "sources": [
                            {"src": "2025-09 资源储量更新", "data": "露天开采 2025 年 12 月完成，之后转纯地下；露天矿体 Kathleen's Corner 与 Mt Mann"},
                            {"src": "Q4 FY26 季报", "data": "26Q2 45% 露天库存料入厂（露天采矿 2025-12 结束、库存料收尾阶段）"}
                        ]
                    },
                    {
                        "line": "地下矿（澳洲首个地下锂矿）",
                        "status": "✅ 建成（2024 起开发）",
                        "sources": [
                            {"src": "Liontown 官网", "data": "澳洲首个地下锂矿、全球首批之一；长孔空场采矿+膏体充填；地下矿减少环境足迹、瞄准高品位矿"},
                            {"src": "Q4 FY26 季报", "data": "地下开发 3,316m 创纪录（+35% qoq）；26Q2 采出地下矿 356kt；2.8Mtpa 目标 FY27 底"}
                        ]
                    },
                    {
                        "line": "矿体与品位（Kathleen's Corner / Mt Mann / NW Flats）",
                        "status": "✅ 多矿体",
                        "sources": [
                            {"src": "2025-09 资源储量更新", "data": "资源 150Mt @ 1.33% Li₂O（2025-09）；储量 71.7Mt @ 1.32%；2024-06 资源 155Mt @ 1.34%"},
                            {"src": "DFS 2021", "data": "Ore Reserve 68.5Mt @ 1.34%（2021）；生产库存 82.7Mt @ 1.30%；品位 1.3-1.4% Li₂O"}
                        ]
                    },
                    {
                        "line": "膏体充填厂（paste plant）",
                        "status": "✅ 建成（南半球最大）",
                        "sources": [
                            {"src": "Liontown 官网", "data": "南半球最大膏体充填厂——尾矿回填地下采空区，减少地表尾矿库"},
                            {"src": "DFS 2021", "data": "地下开采产生 ~7Mt 废石回填露天坑/地表堆场"}
                        ]
                    },
                    {
                        "line": "尾矿设施（TSF）",
                        "status": "✅ 建成",
                        "sources": [
                            {"src": "Liontown 官网", "data": "尾矿管理含膏体回填与地表储存（Tailings and Waste Rock Policy 2025-10）"}
                        ]
                    }
                ],
                "note": "核实时间：2026-08-05。采矿侧要点：① 露天+地下双模式，2026 起转纯地下（露天 2025-12 完成）；② 地下矿为全球首批之一，膏体充填减少地表尾矿；③ 资源 150Mt @ 1.33% 支撑长寿命（矿山寿命 >20 年）；④ NW Flats 为下一开发区域（扩建 FID 范围）。",
                "images": [
                    {"url": "img/sat_kathleen_z13.jpg", "src": "卫星影像（Yandex Maps）", "cap": "Kathleen Valley 矿区卫星影像——露天坑/地下矿口/选矿厂相对位置"},
                    {"url": "img/kv_google_earth.jpg", "src": "Liontown 官网", "cap": "Kathleen Valley 位置图（Google Earth 底图，含 Geraldton 港关系）"},
                    {"url": "img/kv_underground.jpg", "src": "Liontown 官网", "cap": "澳洲首个地下锂矿——地下开采实景"}
                ]
            }
        }
    }
,
    {
        "company": "MRL（Mineral Resources）",
        "mine": "Bald Hill",
        "sc6": 1.0,   # 数据层官方 SC6（MRL 季报 Produced SC6 1k/100% basis；FY25 54k）
        "sc6_note": "官方 SC6（MRL 季报 Produced SC6/Sales SC6，100% 资产口径）",
        "grade": "5.1% Li₂O（官方 SC6）",   # 精矿品位标注（用户规范 2026-08-11：产量/销量描述必须明确品位）
        "lat": -31.52,  # 卫星影像定位（Yandex/Google Maps）
        "lng": 121.97,
        "current_q": "26Q2",
        "prev_q": "26Q1",
        "current_q_date": "2026年4-6月",
        "mine_cn": "Bald Hill（秃山矿山）",
        "report": "MRL Quarterly Activity Report Q4 FY26（2026-07-29 发布）；Bald Hill lithium mine restart 公告（2026-05-18）；Bald Hill Operations and Mineral Resources Update（2024-11-13）",
        "source_url": "https://www.mineralresources.com.au/our-business/lithium/bald-hill/",
        "equity_note": "100% 资产口径（MinRes 全资拥有并运营）；原属 Tawana Resources/Alliance Mineral Assets（后合并为 Alita Resources），Alita 2019-08-29 自愿托管（KordaMentha）、2024-04-04 清算终止；MinRes 2023-09-04 签约收购、2023-11-01 生效；2024-11 C&M、2026-05 复产",
        "history_labels": [
            ("production", "精矿产量（万吨，100% · 混合品位 dmt）"),
            ("sales", "销量（万吨，100% · 混合品位 dmt）"),
            ("prod_sales_ratio", "产销比"),
            ("avg_price", "平均售价（US$/t，SC6）"),
            ("cash_cost", "单位成本 FOB（A$/t，SC6）"),
        ],
        "status_26q2": {
            "existing_lines": [
                {
                    "name": "已有产能1：选矿厂（DMS + spirals）— 产能 ~165ktpa SC @ 5.1% Li₂O（=140kt SC6）",
                    "q26q2": "26Q2 复产爬坡：2026-05 现场活动启动（坑内抽水完成）、6 月采矿/破碎与首产精矿（产 1k dmt）；选矿厂为 2018 年建 DMS/spirals 线（2019 C&M、2022 重启）+ 2024 年新建破碎厂",
                    "q26q1": "26Q1 处于 care & maintenance（2024-11 起），选矿厂停产待命；2026-05-18 宣布复产",
                    "compare": "复产首月即出精矿是超预期点（公告原计划 7 月首产，实际 6 月提前）；坑抽水完成扫清复产最大障碍"
                },
                {
                    "name": "已有产能2：露天矿（采矿服务全内部；原矿处理能力未单独披露）",
                    "q26q2": "采矿恢复（传统露天钻爆-装载-运输）；TMM 426k wmt、矿石 15k dmt（26Q2 复产首月）；MinRes Mining Services 全链条自营（采矿/破碎/加工/运输）",
                    "q26q1": "C&M 期间无采矿",
                    "compare": "采矿爬坡快速（内置设备 + 人员调配），恢复至满产仅需 4-6 周爬坡窗口（2024-11 公告口径）"
                }
            ],
            "future_lines": [
                {
                    "name": "满产爬坡（Q2 FY27 达 140k dmt SC6/年）",
                    "q26q2": "2026-07 首批发运（Esperance 港）；Q1 FY27（26Q3）首批销售 + 爬坡；**Q2 FY27（26Q4）满产 140k dmt SC6/年**；FY27 Bald Hill 指引（销量/FOB 成本/capex）将在 2026 年 8 月 FY26 年报时发布",
                    "q26q1": "2026-05-18 公告：5 月末现场爬坡、6 月采矿/破碎、7 月首产、Q1 FY27 首批 Esperance 发运、Q2 FY27 满产",
                    "compare": "时间线按计划兑现（7 月首运已发生）；FY27 指引 8 月发布是下一催化剂"
                },
                {
                    "name": "选矿厂扩建研究（增产 + 延长矿山寿命）",
                    "q26q2": "MinRes 正在研究 Bald Hill 选矿厂扩建选项（增加产量 + 延长矿山寿命）——Q4 FY26 季报确认",
                    "q26q1": "未披露（C&M 期间）",
                    "compare": "扩建研究启动是复产后的新增长线索——潜在产能超越 140k SC6/年"
                }
            ],
            "overall": {
                "operation_changes": "26Q2 复产首季：2026-05 公告并启动现场、6 月首产精矿（产 1k dmt SC6）、7 月首批发运（季末后）；产 1k mixed / 1k SC6、销 0；TMM 426k wmt；重启成本 ~$20M（Q4 FY26 发生，含营运资本）",
                "prev_operation_changes": "26Q1 处于 care & maintenance（2024-11 起），无产量；2026-05-18 董事会宣布复产（锂价显著持续回升驱动）",
                "highlights": [
                    "2026-05-18 正式宣布复产——锂价显著回升 + 前期精心规划驱动（Chris Ellison：市场回暖时机成熟）",
                    "复产节奏超预期：公告计划 7 月首产，实际 6 月即产首批精矿（1k dmt SC6）；坑内抽水完成扫清采矿障碍",
                    "2026-07 首批发运（Esperance 港）——季报后事件确认销售通道打通",
                    "满产目标 140k dmt SC6/年锁定 Q2 FY27（2026 年 10-12 月）——复产 6 个月内达满产",
                    "选矿厂扩建研究启动（增产 + 延长矿山寿命）——复产后的增长期权",
                    "复产创造 ~370 岗位（110 人从 MinRes 其他矿山调派）——公司整合运营模式"
                ]
            }
        },
        "fc_unit": "万吨 SC6（官方口径 · 品位 5.1% Li₂O，满产 140k SC6/年）",
        "fc_2027": [
            {"label": "悲观", "val": 12, "note": "满产爬坡延迟（Q2 FY27 未达 140k SC6 满产目标·品位 5.1%）+ 锂价回落影响销售节奏"},
            {"label": "基准", "val": 14, "note": "Q2 FY27 满产 140k dmt SC6/年兑现，2027 年全年满产运行（= 14 万吨 SC6）"},
            {"label": "乐观", "val": 17, "note": "选矿厂扩建研究通过 + 2027 年内新增产能释放"}
        ],
        "capacity_verification": {
            "title": "选矿产能核实（多来源交叉印证 · 复产阶段矿山）",
            "method": "以 MRL 官网资产页、2026-05-18 重启公告、2024-11-13 资源储量更新、Q4 FY26 季报、Tawana 2018 历史公告为来源；复产阶段矿山以公司公告/新闻中的投产时间与建设进度为核心。",
            "summary": "Bald Hill 选矿厂（2018 建 DMS/spirals + 2024 新建破碎厂）产能 ~165,000 dmt/年 SC @ 5.1% Li₂O = 140,000 dmt SC6/年（官网与重启公告双确认）；2026-05 复产、6 月首产、7 月首运、Q2 FY27 满产；选矿厂扩建研究中。",
            "items": [
                {
                    "line": "选矿厂（DMS + spirals + 破碎）",
                    "excel_capacity": "~165ktpa SC @ 5.1% Li₂O（=140kt SC6）",
                    "verified": "✓ 官网 + 重启公告双确认",
                    "sources": [
                        {"src": "MRL 官网资产页", "data": "annual production capacity of approximately 165,000 tonnes of spodumene concentrate at a grade of 5.1% Li2O；破碎厂 2024 年新建、DMS/spirals 厂 2018 年建（2019 C&M、2022 重启）"},
                        {"src": "Bald Hill restart 公告（2026-05-18）", "data": "production capacity of circa 165,000 dmt per annum of 5.1% spodumene concentrate, equivalent to 140,000 dmt SC6 per annum——165kt SC5.1% = 140kt SC6 换算自洽"},
                        {"src": "Q4 FY26 季报", "data": "ramp-up to full capacity of 140k dmt SC6 is on track for Q2 FY27；MinRes studying plant expansion options"},
                        {"src": "2023-11 收购公告（MinRes 官网新闻）", "data": "收购时口径 circa 150,000 tpa @ 5.5% 精矿——产能表述沿革（150kt SC5.5% → 165kt SC5.1%）"}
                    ]
                },
                {
                    "line": "加工流程",
                    "excel_capacity": "DMS 重介质 + spirals（2018）+ 新破碎厂（2024）",
                    "verified": "✓ 官方确认",
                    "sources": [
                        {"src": "MRL 官网资产页", "data": "crushing and processing plant via Dense Media Separation (DMS) concentrator；crushing plant – a new plant was commissioned in 2024"},
                        {"src": "2017-07 PFS（Tawana，被收购前时代）", "data": "1,200 ktpa 锂辉石 DMS 回路 + 独立钽厂 350 ktpa；capex A$42M（全澳最低）、IRR 185%、12 个月回本、~155,000 tpa SC + 260,000 lbs/yr Ta₂O₅；包销 US$880/t（6% Li₂O，FOB Esperance）"},
                        {"src": "2024-11-13 更新公告", "data": "spodumene concentrate plant 在 C&M 期间保养，复产爬坡 4-6 周（公告口径）"}
                    ]
                },
                {
                    "line": "全矿合计（满产）",
                    "excel_capacity": "140kt SC6/年",
                    "verified": "✓ 官方目标（Q2 FY27）",
                    "sources": [
                        {"src": "Q4 FY26 季报", "data": "Ramp-up to full capacity of 140k dmt SC6 is on track for Q2 FY27——官方满产目标"},
                        {"src": "锂业现场会（2026-05-19）", "data": "Bald Hill 100% internal 服务链（采矿/破碎/加工/运输全自营）；MinRes 将成全球唯一运营三个硬岩锂矿的公司"}
                    ]
                }
            ],
            "note": "核实时间：2026-08-05。关键结论：① 选矿产能 165ktpa SC5.1% = 140kt SC6/年（官网+公告双确认）；② 2026-05 复产、6 月首产、7 月首运、Q2 FY27 满产——复产时间线按计划兑现；③ 选矿厂扩建研究启动（增产+延长寿命）；④ 重启成本 ~$20M、~370 岗位；⑤ FY27 指引（销量/FOB/capex）2026 年 8 月发布。",
            "sources_index": {"公司公告": "2026-05-18 重启公告、2024-11-13 资源储量更新、Q4 FY26 季报", "公司官网": "Bald Hill 资产页（含位置图）", "公司展示": "2026-05-19 锂业现场会展示", "历史公告": "Tawana 2018-06-06（被收购前）", "数据站": "WA MINEDEX（登记号 87101）、Wikipedia"},
            "images": [
                {"url": "img/sat_baldhill_z13.jpg", "src": "卫星影像（Yandex Maps，坐标 ≈-31.52,121.97 推算）", "cap": "Bald Hill 矿区卫星影像（Zoom 13）——Kambalda 东南 50km，卫星追踪第一参照"},
                {"url": "img/baldhill_map.png", "src": "MRL 官网", "cap": "Bald Hill 位置图（西澳全州示意）——Kalgoorlie/Mt Marion/Esperance 港关系，卫星追踪区域参照"},
                {"url": "img/baldhill_processing.jpg", "src": "MRL 官网", "cap": "Bald Hill 选矿厂（DMS + spirals + 2024 新破碎厂）"},
                {"url": "img/baldhill_ops.jpg", "src": "MRL 官网", "cap": "Bald Hill 矿区运营总览（露天矿 + 选矿厂）"},
                {"url": "img/baldhill_drone.jpg", "src": "MRL 官网（无人机航拍）", "cap": "Bald Hill 矿区无人机航拍——复产后的现场实景"}
            ],
            "mining_side": {
                "title": "原矿产能核实（矿坑 / 矿体 / 尾矿库 · 复产阶段矿山）",
                "method": "以 2024-11-13 资源储量更新、Tawana 2018 历史公告、MRL 官网、Q4 FY26 季报为来源。",
                "items": [
                    {
                        "line": "原矿矿山：Bald Hill 露天矿",
                        "status": "✅ 建成（钽矿时代已开采；2019 起锂生产）",
                        "sources": [
                            {"src": "MRL 官网资产页", "data": "originally mined for tantalum, before commencing spodumene production in 2019；open pit mine, waste dumps, ROM pad and tailings storage facility"},
                            {"src": "Q4 FY26 季报", "data": "2026-05 复产：pit was dewatered, enabling mining operations to ramp up（坑内抽水完成）；26Q2 TMM 426k wmt、矿石 15k dmt"}
                        ]
                    },
                    {
                        "line": "矿体与资源（多伟晶岩脉）",
                        "status": "✅ 资源确认；⚠️ 储量未更新",
                        "sources": [
                            {"src": "2024-11-13 资源储量更新", "data": "Mineral Resources 58.1Mt @ 0.94% Li₂O（2024-06-30，>0.3% 边界，扣开采）：Indicated 17.2Mt @ 0.91% + Inferred 40.9Mt @ 0.95%（无 Measured）；较 2018-06 的 21.7Mt +168%（777 解释孔+599 估算孔）；矿权 M15/400（501 公顷）；权利金 5%"},
                            {"src": "Tawana 2018-06-06 公告", "data": "资源 26.5Mt @ 0.96% Li₂O（149ppm Ta₂O₅）；储量 11.3Mt @ 1.01% Li₂O + 160ppm Ta₂O₅；钽储量 2.0Mt @ 313ppm——矿山寿命 9 年 @ 1.2Mtpa（被收购前时代）"},
                            {"src": "MRL Resources & Reserves 页面", "data": "仅列 Bald Hill Resources（2024-11-13），无 Reserves 条目——MRL 未发布最新储量"}
                        ]
                    },
                    {
                        "line": "环评与许可（WA 政府）",
                        "status": "✅ 已获批（DMP/DWER 体系）",
                        "sources": [
                            {"src": "2017-07-24 公告（Tawana+AMAL）", "data": "ENVIRONMENTAL APPROVALS FINALISED：DWER 修订运营许可（1.2Mtpa DMS 建设运营）+ DMP 更新 Environmental Mining Proposal 批准"},
                            {"src": "MINEDEX 环境登记 #87101", "data": "Bald Hill Tantalum-Lithium Project：Mining Proposal + Mine Closure Plan，V4 Rev1 2020-08；矿权 M15/400、G15/28、L15/348、L15/384、L15/366、L15/365、M15/1305、M15/1308"},
                            {"src": "EPA 检索", "data": "EPA（西澳环保局）正式评估：未检索到——项目通过 DMP Mining Proposal + DWER 运营许可体系监管（诚实标注：未找到）"}
                        ]
                    },
                    {
                        "line": "尾矿库（TSF）",
                        "status": "✅ 建成",
                        "sources": [
                            {"src": "MRL 官网资产页", "data": "tailings storage facility 为现场基础设施之一；C&M 期间保养"}
                        ]
                    },
                    {
                        "line": "基础设施（营地/发电/供水）",
                        "status": "✅ 建成（FIFO 营地 300 人）",
                        "sources": [
                            {"src": "MRL 官网资产页", "data": "workshops, offices, diesel power generation and bore fields；FIFO camp accommodation up to 300 people"},
                            {"src": "2024-11-13 公告", "data": "C&M 时 ~300 员工受影响；复产新增 ~370 岗位"}
                        ]
                    }
                ],
                "note": "核实时间：2026-08-05。采矿侧要点：① 露天矿（钽矿转型锂矿 2019 首产）；② 资源 58.1Mt @ 0.94%（2024-06，Indicated 17.2 + Inferred 40.9，无 Measured），历史储量 11.3Mt @ 1.01%（2018，Tawana 时代）——MRL 未发布最新储量；③ 2017-07 PFS：1.2Mtpa DMS 回路、capex A$42M、矿山寿命 9 年（@1.2Mtpa）；④ 环评经 DMP Mining Proposal + DWER 运营许可（2017-07-24 批准），MINEDEX 登记 #87101；EPA 正式评估未检索到；⑤ 2026-05 复产坑抽水完成、采矿爬坡；⑥ Alita 时代产量轨迹：2018-03 投产、CY2018 产 51k wmt SC6、2019 指引 180k SC6/年。",
                "images": [
                    {"url": "img/sat_baldhill_z13.jpg", "src": "卫星影像（Yandex Maps）", "cap": "Bald Hill 露天矿/选矿厂卫星影像——复产现场相对位置"},
                    {"url": "img/baldhill_mining.jpg", "src": "MRL 官网", "cap": "Bald Hill 露天开采作业（钻爆-装载-运输循环）"},
                    {"url": "img/baldhill_tsf.jpg", "src": "MRL 官网", "cap": "Bald Hill 尾矿库与矿区设施"}
                ]
            }
        }
    }
,
    {
        "company": "Rio Tinto（力拓）",
        "mine": "Mt Cattlin",
        "sc6": 0.892,   # SC6 折算系数（用户规范 2026-08-10：精矿产量/产能/预测全站统一 SC6 口径）
        "sc6_note": "SC6 折算（原 dmt ~5.35% Li₂O）",
        "grade": "~5.35% Li₂O（dmt 实际品位）",   # 精矿品位标注（用户规范 2026-08-11：产量/销量描述必须明确品位）
        "grade_series": {},   # 逐季品位（历史 QAR 披露品位 5.2-5.5% 波动，各季未逐一提取——按统一 5.35% 折算）
        "lat": -33.5625,  # 卫星影像定位（Yandex/Google Maps）
        "lng": 120.0352,
        "est_qs": [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],  # 2019Q1-2023Q4 年度值均分估算（审计修正 2026-08-07 标 E）
        "current_q": "26Q2",
        "prev_q": "26Q1",
        "current_q_date": "2026年4-6月",
        "mine_cn": "Mt Cattlin（卡特林山矿山）",
        "report": "Rio Tinto Operations Review Q2 2026（2026-07-15 发布）；Allkem Mt Cattlin NI 43-101 Technical Report（2023）；力拓官网 Mt Cattlin 资产页（C&M 状态确认）",
        "source_url": "https://www.riotinto.com/en/operations/anz/western-australia/mt-cattlin",
        "equity_note": "100% 资产口径（力拓全资；2024-10-09 签约、2025-03-06 完成收购 Arcadium Lithium 每股 $5.85，归入 Rio Tinto Lithium）；历史：Galaxy Resources 2009-2012 运营 → 2013 C&M → 2016-03 复产 → 2021-08 Galaxy 与 Orocobre 合并为 Allkem → 2024-01 Allkem 与 Livent 合并为 Arcadium → 2025-03 力拓完成收购",
        "history_labels": [
            ("production", "精矿产量（万吨，dmt SC 5.2-5.5%）"),
            ("sales", "销量（万吨，dmt）"),
            ("prod_sales_ratio", "产销比"),
            ("avg_price", "平均售价（US$/t，SC6）"),
            ("cash_cost", "单位成本 FOB（A$/t，SC6）"),
        ],
        "status_26q2": {
            "existing_lines": [
                {
                    "name": "已有产能1：选矿厂（破碎 + 光选 + DMS + 重力选）— 设计 1.8Mtpa 原矿（精矿产能未单独披露，历史按 ~10% 回收率估算）",
                    "q26q2": "26Q2 处于 care & maintenance（2025 年起，因锂价低）；选矿厂（2013-2016 建，含光学矿石分选、DMS、重力选）保养待命；力拓官网状态标注 Care and maintenance；产能标注 10kpta（力拓官网口径，疑为显示截断，实际铭牌 ~160ktpa SC）",
                    "q26q1": "26Q1 同为 C&M；无复产计划公告",
                    "compare": "持续停产；力拓收购后未宣布复产计划——锂价未回到重启激励水平"
                },
                {
                    "name": "已有产能2：露天矿（NW pit 等；原矿 1.8Mtpa 与选矿厂匹配）",
                    "q26q2": "采矿暂停（C&M）；矿坑：North-West pit（Stage 3 NW）等；2016 复产时 17 年矿山寿命 @800ktpa，后扩至 1.8Mtpa 连续给料",
                    "q26q1": "C&M 无采矿",
                    "compare": "无变化"
                }
            ],
            "future_lines": [
                {
                    "name": "复产评估（力拓未宣布时间表）",
                    "q26q2": "力拓未披露 Mt Cattlin 复产计划；资产页状态 Care and maintenance；全球锂业务重心在盐湖（Fénix/Rincon/Olaroz）与在建项目（Jadar/Nemaska）",
                    "q26q1": "同（无新增披露）",
                    "compare": "无新进展——C&M 持续"
                }
            ],
            "overall": {
                "operation_changes": "26Q2 持续 care & maintenance（2025 年起）：产 0、销 0；力拓 Q2 2026 Operations Review 无 Mt Cattlin 产量（C&M 项目）；力拓 2025 年完成 $6.7B 收购 Arcadium 后，锂业务整合为 Rio Tinto Lithium",
                "prev_operation_changes": "26Q1 同（C&M）",
                "highlights": [
                    "力拓 2025-03-06 完成 $6.7B 收购 Arcadium Lithium（2024-10-09 签约、每股 $5.85）——Mt Cattlin 归入 Rio Tinto Lithium（全球最大锂组合之一）",
                    "2025 年起进入 care & maintenance（力拓官网确认）——Arcadium 2024-09-04 公告暂停 Stage 4A 剥采、完成 Stage 3 后 2025 H1 底前 C&M；2024Q3 计提 $51.7M 减值",
                    "历史产量轨迹：2019 年峰值 191.6kt SC（Galaxy 时代）→ 2022 年 107.4kt → FY23 131.99kt（Allkem）→ 2024 年后走低",
                    "资源储量（Arcadium 10-K，2024-12-31）：M&I 6.48Mt @ 1.41% Li₂O + Inferred 4.81Mt @ 1.27%、储量 P&P 3.73Mt @ 1.02%——C&M 官方原因为锂辉石价格下降（非资源枯竭；较 2023-06 的 12.1Mt 下降近半）",
                    "选矿厂 1.8Mtpa 原矿设计 + DMS/光选/重力选工艺——复产时爬坡快（2016 年经验：4 个月恢复）"
                ]
            }
        },
        "fc_unit": "万吨 SC6 折算（原 SC 5.2-5.5% ×0.892；C&M 状态：2027 严谨基准=0；3/8 万吨仅列纯上行情景）",
        "fc_2027": [
            {"label": "悲观", "val": 0, "note": "持续 C&M——锂价未回升、资源枯竭无复产动力（基准情形概率最高；3/8 万吨为 dmt → SC6 折算 2.7/7.1）"},
            {"label": "基准", "val": 3, "note": "2027 年锂价回升 + 力拓决定有限复产（低品位库存处理，~40-80kt SC/年）"},
            {"label": "乐观", "val": 8, "note": "力拓利用自有销售渠道重启 + 尾矿/低品位回收，2027 年中恢复 ~80kt SC/年"}
        ],
        "capacity_verification": {
            "title": "选矿产能核实（多来源交叉印证 · C&M 状态矿山）",
            "method": "以 Allkem NI 43-101 技术报告（2023）、力拓官网资产页、Wikipedia、历史季报为来源；C&M 状态矿山以历史产能与当前状态为核心。",
            "summary": "Mt Cattlin 选矿厂（破碎 + 光学矿石分选 + DMS + 重力选，2013-2016 建）设计处理量 1.8Mtpa 原矿 → 精矿产能 ~160ktpa SC（历史峰值 FY18/19 产 163kt @ 5.8%）；2025 年起 C&M（力拓确认，因锂价低）；力拓官网标注产能 10kpta（疑显示截断，以 NI 43-101 设计口径为准）。",
            "items": [
                {
                    "line": "选矿厂（破碎+光选+DMS+重力选）",
                    "excel_capacity": "1.8Mtpa 原矿 → ~143ktpa SC6 折算（原 ~160kt SC，品位 ~5.35%）",
                    "verified": "✓ NI 43-101 设计口径 + 历史产量验证",
                    "sources": [
                        {"src": "Allkem NI 43-101（2023）", "data": "Ore mining rates are based on providing continuous feed to the nominal 1.8 Mtpa processing plant；plant consists of crushing circuit, optical beneficiation circuit, DMS circuit, product handling, TSF"},
                        {"src": "NI 43-101 Table 17-1", "data": "FY18/19 产 163kt @ 5.8% Li₂O（回收率 50%）、FY19/20 146kt @ 6.0%、FY20/21 187kt @ 5.8%、FY21/22 177kt @ 5.6%——实际产能验证 146-187ktpa"},
                        {"src": "力拓官网资产页", "data": "Mt Cattlin 100% 力拓、Care and maintenance、标注 Capacity 10kpta（疑为显示截断，与 NI 43-101 的 1.8Mtpa/160ktpa 差距大，页面采用 NI 口径并注明差异）"}, {"src": "Arcadium FY2024 10-K", "data": "capacity to process up to 1.8 million metric tons of ore per year, since upgrades from the original 1 Mtpa when commissioned in 2010；产品品位 SC 5.2-5.5% Li₂O；2022 新增磁选机；选厂 90 人；副产钽精矿（spiral/gravity，回收率 ~20%）"}, {"src": "NI 43-101 §5.6（许可）", "data": "Prescribed Premises Licence L8469/2010/2：设计产能 2,000,000 tpa（Category 5 选矿，2022-02-11 修订、2039？到期 13/10/2029）——许可证口径 2.0Mtpa vs 标称 1.8Mtpa"}
                    ]
                },
                {
                    "line": "加工流程",
                    "excel_capacity": "破碎 + 光学分选 + DMS + 重力选",
                    "verified": "✓ NI 43-101 确认",
                    "sources": [
                        {"src": "Allkem NI 43-101（2023）", "data": "multi-stage crushing, screening, optical ore sorting, dense media separation, and gravity concentration（2013-2016 建）；光学分选 1ktpd、可达总处理量 30%"},
                        {"src": "Wikipedia", "data": "2016-03-31 复产，800ktpa 原矿起步（后扩至 1.8Mtpa）"}
                    ]
                },
                {
                    "line": "全矿合计（C&M 状态）",
                    "excel_capacity": "停产 C&M（2025 起；原设计 1.8Mtpa 原矿 → ~143ktpa SC6 折算）",
                    "verified": "✓ 力拓官网确认",
                    "sources": [
                        {"src": "力拓官网资产页", "data": "Mt Cattlin was placed into care and maintenance in 2025 due to lower spodumene prices"},
                        {"src": "Rio Tinto Q2 2026 Operations Review", "data": "锂业务产量表无 Mt Cattlin（C&M 项目不产）——2026 年持续停产"}
                    ]
                }
            ],
            "note": "核实时间：2026-08-05。关键结论：① 选矿厂 1.8Mtpa 原矿设计 → ~160ktpa SC（NI 43-101 双确认）；② 2025 年起 C&M（力拓确认，官方原因为锂辉石价格下降——非资源枯竭）；③ 力拓官网产能标注 10kpta 疑为显示截断，页面采用 NI 43-101 口径并注明差异；④ 历史峰值 2019 年 191.6kt SC；⑤ 复产时间表未披露。",
            "sources_index": {"技术报告": "Allkem Mt Cattlin NI 43-101（2023，entech 编制）", "公司官网": "力拓 Mt Cattlin 资产页（C&M 状态）", "公司报告": "Rio Tinto Q2 2026 Operations Review", "历史披露": "Galaxy/Allkem/Arcadium 季报与年报", "数据站": "Wikipedia（坐标/历史）、WA DEMIRS"},
            "images": [
                {"url": "img/sat_mtcattlin_z13.jpg", "src": "卫星影像（Yandex Maps，坐标 -33.5625,120.0352）", "cap": "Mt Cattlin 矿区卫星影像（Zoom 13）——Ravensthorpe 北 2.2km，卫星追踪第一参照"},
                {"url": "img/rt_mtcattlin_hero.jpg", "src": "力拓官网", "cap": "Mt Cattlin 资产页主图（力拓官方）"},
                {"url": "img/rt_lithium_ops.jpg", "src": "力拓官网（锂产品页）", "cap": "力拓全球锂资产布局（Mt Cattlin 为西澳硬岩项目之一）"}
            ],
            "mining_side": {
                "title": "原矿产能核实（矿坑 / 矿体 / 尾矿库 · C&M 状态矿山）",
                "method": "以 Allkem NI 43-101（2023）、Wikipedia、WA 政府登记为来源。",
                "items": [
                    {
                        "line": "原矿矿山：露天矿（NW pit 等）",
                        "status": "✅ 建成（2009-2012 首产；2016-03 复产）；⚠️ C&M 中",
                        "sources": [
                            {"src": "Wikipedia", "data": "2.2km north of Ravensthorpe；Galaxy 2009-2012 运营 → 2013 C&M → 2016-03-31 复产（17 年矿山寿命 @800ktpa）"},
                            {"src": "Allkem NI 43-101（2023）", "data": "North-West pit（Stage 3 NW）只采一个伟晶岩脉；Stage 4 NW 扩展；1.8Mtpa 连续给料"}
                        ]
                    },
                    {
                        "line": "矿体与资源（伟晶岩锂-钽矿）",
                        "status": "✅ 资源确认（总 11.29Mt；C&M 主因=锂价）",
                        "sources": [
                            {"src": "Arcadium FY2024 10-K（最新，2024-12-31，S-K1300）", "data": "资源 M&I 6.48Mt @ 1.41% Li₂O + Inferred 4.81Mt @ 1.27%（COG 0.3% 露天 / 0.58% 地下）；储量 P&P 3.73Mt @ 1.02%（Proven 89kt + Probable 3,644kt）——较 2023-06 的 12.1Mt 下降（开采消耗 + 口径调整；非停产主因——官方原因为锂价）"}, {"src": "Allkem NI 43-101（2023）", "data": "历史资源 12.1Mt @ 1.3% Li₂O + 167ppm Ta₂O₅（2023-06-30，COG 0.3%）；储量 7.1Mt @ 1.2% Li₂O（2023，Proven 0.2 + Probable 5.2 + 堆存 1.8）"},
                            {"src": "NI 43-101 MRE 2017-12", "data": "历史资源 10.3Mt @ 1.25% Li₂O + 151ppm Ta₂O₅（2017-12）"},
                            {"src": "Wikipedia", "data": "2019 年储量 8.2Mt @ 1.29% Li₂O + 155ppm Ta₂O₅"}
                        ]
                    },
                    {
                        "line": "环评与许可（WA 政府）",
                        "status": "✅ 已获批（DWER 体系）",
                        "sources": [
                            {"src": "Allkem NI 43-101（2023）", "data": "Part V Prescribed Premises Licence L 8469/2010/2（DWER，1.8Mtpa 选矿厂）；Part V Clearing Permits CPS 3045/5、CPS 8052/2、CPS 8049/1；Mining Proposal Reg IDs 22377、69112、73856"},
                            {"src": "Allkem NI 43-101（2023）", "data": "Environmental Protection Act 1986 Part V Clearing Regulations（DWER 管辖）；Shire of Ravensthorpe 当地政府"}
                        ]
                    },
                    {
                        "line": "尾矿库（TSF）",
                        "status": "✅ 建成",
                        "sources": [
                            {"src": "Allkem NI 43-101（2023）", "data": "TSF 按 ANCOLD/DMIRS 与 Works Approval 指南设计运营；含尾矿库 + 废石堆稳定性管理"}
                        ]
                    }
                ],
                "note": "核实时间：2026-08-05。采矿侧要点：① 露天伟晶岩锂-钽矿（Ravensthorpe 北 2.2km）；② 资源（Arcadium 10-K 2024-12-31）M&I 6.48Mt @ 1.41% + Inferred 4.81Mt、储量 P&P 3.73Mt @ 1.02%——；2025 C&M 官方原因为锂辉石价格下降（非资源枯竭）；③ 环评经 DWER Part V 许可体系（L 8469/2010/2 + Clearing Permits）；④ 2016-03 复产（800ktpa→1.8Mtpa 扩产）；⑤ 2025 起 C&M，复产时间表未披露。",
                "images": [
                    {"url": "img/sat_mtcattlin_z13.jpg", "src": "卫星影像（Yandex Maps）", "cap": "Mt Cattlin 露天矿/选矿厂卫星影像——矿坑与设施相对位置"},
                    {"url": "img/rt_mtcattlin_hero.jpg", "src": "力拓官网", "cap": "Mt Cattlin 露天矿实景（力拓官方）"}
                ]
            }
        }
    }
,
    {
        "company": "Core Lithium（ASX: CXO）",
        "mine": "Finniss",
        "sc6": 1.0,   # SC6 折算系数（用户规范 2026-08-10：精矿产量/产能/预测全站统一 SC6 口径）
        "sc6_note": "官方 SC6 等效口径（Core 披露 SC6e）",
        "grade": "SC6e（官方口径）",   # 精矿品位标注（用户规范 2026-08-11：产量/销量描述必须明确品位）
        "lat": -12.713,  # 卫星影像定位（Yandex/Google Maps）
        "lng": 130.789,
        "current_q": "26Q2",
        "prev_q": "26Q1",
        "current_q_date": "2026年4-6月",
        "mine_cn": "Finniss（芬尼斯矿山）",
        "report": "Core Lithium June 2026 Quarterly Activities Report（2026-07-15）；Finniss Restart Study and Operations Update（2025-03-27）；2026-03-18 FID；2026-02-26 库存精矿销售公告",
        "source_url": "https://corelithium.com.au/finniss-lithium-operation",
        "equity_note": "100% 资产口径（Core Lithium 全资拥有运营，ASX: CXO）；北领地（NT）唯一锂矿——Darwin 西南 88km；2023-02 商业投产（Grants 露天）、2024 年中暂停进入 C&M、2025-05-14 重启研究完成、2026-03-18 FID（214ktpa SC6e）、2026-05 重启采矿",
        "history_labels": [
            ("production", "精矿产量（万吨，dmt SC6 等效）"),
            ("sales", "销量（万吨，dmt）"),
            ("prod_sales_ratio", "产销比"),
            ("avg_price", "平均售价（US$/t，SC6）"),
            ("cash_cost", "单位成本 FOB（A$/t）"),
        ],
        "status_26q2": {
            "existing_lines": [
                {
                    "name": "已有产能1：DMS 选矿厂（重介质分离）— 设计 214ktpa SC6e（2026 FID 口径）",
                    "q26q2": "26Q2 重启推进：2026-05 恢复采矿（Grants，两年前 2024 年暂停后）；DMS 首产精矿目标 2026 年 9 月季度（26Q3）、首批新产精矿发运目标 26Q4；名称产能 214ktpa SC6e（2026 FID 口径），1.2Mtpa 为原矿稳态规模（目标 2028 年中）",
                    "q26q1": "26Q1 处于 C&M（2024 年中起）；2026-03-18 FID 重启获批：US$120M 融资（Glencore/InfraVia/Nebari）+ A$120M 股权募资，fully funded 重启包；$19.5M 结束遗留运营合同",
                    "compare": "2026-05 重启是超预期点（miningweekly 2026-05-20 报道）；FID 后约 2 个月即重启——资本效率高（$250M+ 已投资产复用）"
                },
                {
                    "name": "已有产能2：Grants 露天矿 + BP33 地下矿（原矿开采产能未单独披露）",
                    "q26q2": "采矿恢复（Grants 露天优先 + BP33 地下规划中）；BP33 为基石矿床（2024-09-25 储量 8.7Mt @ 1.38%，亚垂直伟晶岩 350m 走向/40m 真宽，纵向空场采矿）；重启研究：地下 20 年寿命、前 10 年由储量支撑",
                    "q26q1": "C&M 无采矿",
                    "compare": "重启后采矿爬坡；BP33 地下开发是重启核心（优化后矿计划 + 独立顾问团队）"
                }
            ],
            "future_lines": [
                {
                    "name": "BP33 地下矿开发（重启第二阶段；产能未披露）",
                    "q26q2": "BP33 地下矿计划推进中（纵向空场采矿）；重启研究优化矿计划完成；地下 20 年寿命（重启研究口径）",
                    "q26q1": "BP33 开发暂停（C&M）",
                    "compare": "重启后 BP33 是长期价值核心（储量 8.7Mt 支撑）"
                }
            ],
            "overall": {
                "operation_changes": "26Q2 重启：2026-05 恢复运营（2024 年中暂停后约两年）；重启研究（2025-05-14 完成）+ FID（2026-03-18）→ 2026-05 实际重启；重启方案（2026 FID）：采矿 A$78/t mined、加工及尾矿 A$40/t processed、G&A A$7/t processed、运输 A$36/t product、综合 A$762/t SC6e FOB（不含权利金）；名称产能 214ktpa SC6e（原重启研究 205ktpa）",
                "prev_operation_changes": "26Q1 C&M 中（DMS 保养 $0.3M/季、重启研究费用）；2026-03-18 FID 公告为重启铺路",
                "highlights": [
                    "2026-05 重启（两年停滞后，miningweekly 2026-05-20 报道）——FID 后约 2 个月实现，资本效率高",
                    "重启研究（2025-05-14 完成）→ FID（2026-03-18）：名称产能 214ktpa SC6e、FID 成本口径（采矿 A$78/t mined 等）、地下 20 年寿命",
                    "2026-03-18 FID：US$120M 融资（Glencore/InfraVia/Nebari）+ A$120M 股权募资；$19.5M 结束遗留合同 → 100% 基础设施所有权；首产精矿目标 26Q3、2028 年中达 1.2Mtpa 名称产能",
                    "BP33 储量 8.7Mt @ 1.38%（2024-09-25 更新）——重启的基石；最新总储量 10.73Mt @ 1.29%（2025-04-30）",
                    "最新资源 48.5Mt @ 1.26%（2025-04-30，从 2022 年 18.9Mt 大幅增长）；$250M+ 已投资产（Grants + BP33）"
                ]
            }
        },
        "fc_unit": "万吨 SC6 等效（官方口径 · SC6e 品位，重启满产 20.5 万吨/年对应）",
        "fc_2027": [
            {"label": "悲观", "val": 10, "note": "重启爬坡慢于计划 + 锂价波动——2027 年运行率 50%"},
            {"label": "基准", "val": 16, "note": "2027 年全年运行 + BP33 地下爬坡——~70% 名称产能（15/21.4，214ktpa SC6e 2026 FID 口径；研究情景非公司指导）"},
            {"label": "乐观", "val": 20, "note": "2027 年约 70% 名铭牌（214ktpa SC6e）——不写满产（研究情景）"}
        ],
        "capacity_verification": {
            "title": "选矿产能核实（多来源交叉印证 · 重启矿山）",
            "method": "以 Core Lithium DFS（2019/2021）、重启研究（2025）、2025 年 6 月季报、FY24 年报为来源；重启矿山以最新研究产能与历史运行数据为核心。",
            "summary": "Finniss DMS 选矿厂（重介质分离 + 粗粒精矿，Grants 露天 2023 投产）原设计 180,000 tpa 精矿（2019 DFS）；重启研究（2025-05-14 完成）优化后名称产能 205,000 tpa SC6 等效粗粒精矿、成本降至 $40-46/t；2023 年实际产量：FY24 全年产 95,020 dmt。2024 年中 C&M、2026-05 重启。",
            "items": [
                {
                    "line": "DMS 选矿厂（重介质分离）",
                    "excel_capacity": "214ktpa SC6e（2026 FID）——原重启研究 205ktpa",
                    "verified": "✓ DFS + 重启研究双来源",
                    "sources": [
                        {"src": "2019 DFS（Core Lithium）", "data": "DMS processing up to 180,000 tpa of high-quality lithium concentrate；露天 + 简单重力 DMS 工艺；Pre-Tax IRR 80%、NPV A$114M"},
                        {"src": "2025 重启研究（2025-05-14 完成）", "data": "nameplate production of 205ktpa SC6 equivalent coarse-grained concentrate；成本 $40-46/t（从 $69/t）；产量 +7% 通过更高吞吐量；DMS 厂冶金优化（提高回收率/产量/产能）"},
                        {"src": "FY24 年报", "data": "FY24（2023Q3-2024Q2）产 95,020 dmt（指引 90-95k）、销 97,423 dmt @ US$1,574/dmt、精矿品位 4.8% Li₂O、C1 $1,396/dmt——实际运行验证"}, {"src": "2021 Stage 1 DFS（2021-07-26）", "data": "1Mtpa DMS、up to 197,000 tpa、精矿品位 5.8% Li₂O、矿山寿命 8 年、AISC US$441/t、回收率 71.7%、pre-production capex A$89m、NPV8 A$221m / IRR 53%"}, {"src": "2025 Restart Study 详细参数", "data": "Annual production throughput 1,200 ktpa；Nameplate 205 ktpa SC6-eq（FID 口径 214ktpa）；矿山寿命 20 年（前 10 年储量支撑）；Pre-Production Capital A$175-200m；UG 盈亏平衡 $110/t NSR；长期 SC 价假设 US$1,330/t"}
                    ]
                },
                {
                    "line": "加工流程",
                    "excel_capacity": "简单重力 DMS（粗粒精矿）",
                    "verified": "✓ 官方确认",
                    "sources": [
                        {"src": "2019 DFS", "data": "simple gravity DMS processing producing high quality, coarse concentrate"},
                        {"src": "重启研究（2025）", "data": "DMS Plant optimisation：冶金测试提高回收率、产量、产能；流程优化（process flowsheet）"}
                    ]
                },
                {
                    "line": "全矿合计（重启目标）",
                    "excel_capacity": "214ktpa SC6e（2026 FID 口径，2027 ~70% 名铭牌研究）",
                    "verified": "✓ 重启研究口径",
                    "sources": [
                        {"src": "2025 重启研究", "data": "205ktpa SC6e nameplate；地下（BP33）20 年寿命、前 10 年储量支撑"},
                        {"src": "2025-06 季度报告", "data": "restart 计划 2026 年推进（FID 2026-03-18、2026-05 重启）"}
                    ]
                }
            ],
            "note": "核实时间：2026-08-05。关键结论：① DMS 产能 180ktpa（2019 DFS）→ 205ktpa SC6e（2025 重启研究优化）；② 2023 年实际产（FY24 95,020 dmt，爬坡期）；③ 2024 年中 C&M（2024-09-08 Darwin 最后一船）；④ 2025-05-14 重启研究完成、2026-03-18 FID、2026-05 重启；⑤ FID 2026-03-18 后 2026-05 恢复采矿、首产精矿 26Q3、2028 年中达 1.2Mtpa 名称产能；⑥ 2027 满产路径 205-214ktpa SC6e。",
            "sources_index": {"技术报告": "Core Lithium DFS 2019 / DFS 2021 Stage 1 / 重启研究 2025", "公司报告": "2025 年 6 月季报、FY24 年报", "公司公告": "Finniss Restart Study（2025-03-27）、BP33 储量更新（2024-09-25）", "媒体": "Mining Weekly 2026-05-20（重启报道）", "数据站": "Wikipedia（坐标/历史）"},
            "images": [
                {"url": "img/sat_finniss_z13.jpg", "src": "卫星影像（Yandex Maps，坐标 -12.713,130.789）", "cap": "Finniss 矿区卫星影像（Zoom 13）——Darwin 西南，卫星追踪第一参照"},
                {"url": "img/core_finniss_ops.jpg", "src": "Core Lithium 官网", "cap": "Finniss 运营图（Core Lithium 官方）"}
            ],
            "mining_side": {
                "title": "原矿产能核实（矿坑 / 矿体 / 尾矿库 · 重启矿山）",
                "method": "以 Core Lithium DFS/季报/储量公告、Wikipedia、NT 政府（MMP）为来源。",
                "items": [
                    {
                        "line": "原矿矿山：Grants 露天 + BP33 地下",
                        "status": "✅ 建成（Grants 2023 投产）；🔧 BP33 重启开发中",
                        "sources": [
                            {"src": "Wikipedia", "data": "5 个矿体：Grants、Carlton、Sandras、Hang Gong SW、BP33；Bynoe 伟晶岩田（BPF）；LCT 伟晶岩（Burrell Creek 地层）；2022-10 全面采矿、2023-05 首运（Port Darwin）"},
                            {"src": "2025 重启研究", "data": "BP33 是基石矿床：亚垂直伟晶岩 350m 走向、40m 真宽；纵向空场采矿；地下 20 年寿命；$250M+ 已投资本（Grants + BP33）"},
                            {"src": "2019 DFS", "data": "LOM 40 个月（2019 口径）、剥采比 13:1、Grants + BP33"}
                        ]
                    },
                    {
                        "line": "矿体与资源（LCT 伟晶岩）",
                        "status": "✅ 资源确认（大幅增长）",
                        "sources": [
                            {"src": "2025-05-14 重启研究", "data": "最新 MRE 48.5Mt @ 1.26%（2025-04-30，M6.3/1.41 + I21.9/1.29 + Inf20.3/1.18）；储量 10.73Mt @ 1.29% 矿山拆分：BP33 地下 9.29Mt @ 1.31% + Grants 地下 1.15Mt @ 1.31% + TSF/料堆 0.28Mt @ 0.68%"},
                            {"src": "BP33 储量更新（2024-09-25）", "data": "BP33 储量 8.7Mt @ 1.38% Li₂O（Proved 2.43Mt @ 1.33% + Probable 6.25Mt @ 1.40%）——重启基石"},
                            {"src": "FY24 年报 / 2022 公告", "data": "资源链：18.9Mt @ 1.32%（2022-07-12）→ 30.6Mt @ 1.31%（FY23）→ 48.2Mt @ 1.26%（2024-04-11，+58%）→ 48.5Mt（2025-04-30）"},
                            {"src": "Wikipedia（历史）", "data": "初始 JORC 资源 3.45Mt @ 1.4%（2021 前口径，已被大幅更新取代）"}
                        ]
                    },
                    {
                        "line": "环评与许可（NT 政府）",
                        "status": "✅ 已获批（NT Mining Management Plan 体系）",
                        "sources": [
                            {"src": "Wayback 存档（corelithium.com.au）", "data": "2018 MMP（Finniss Project）；Grants Project Mining Management Plan Amendment（Public ID 227052）；BP33 Public Mining Management Plan（2023）——NT 政府 MMP 体系"},
                            {"src": "采矿租约/审批", "data": "ML 31726（768 公顷，Grants 厂区）；2023-05 NT 政府批准 BP33 地下开采；BP33 Underground SER（Supplementary Environmental Report，2021-12）；EL29698 Finniss MMP Amendment（2021-05）；2021-03 联邦 Major Project Status"}
                        ]
                    },
                    {
                        "line": "尾矿库（TSF）与库存",
                        "status": "✅ 建成",
                        "sources": [
                            {"src": "2025-06 季度报告", "data": "TSF/粗尾矿含 310kt @ 0.66% Li₂O 矿物化物料（计入 MRE）；~5,000t 精矿 + 75,000t 库存（2025 Q2）"},
                            {"src": "重启研究", "data": "TSF 物料回收纳入重启方案"}
                        ]
                    }
                ],
                "note": "核实时间：2026-08-05。采矿侧要点：① Grants 露天（2023 投产）+ BP33 地下（重启第二阶段）；② 资源 48.5Mt @ 1.26%（2025-04-30）、储量 10.73Mt @ 1.29%（BP33 占 8.7Mt @ 1.38%）；③ NT 政府 MMP 体系环评（2018 初始 + Grants/BP33 修订）；④ 2024 年中 C&M、2026-03-18 FID、2026-05 恢复采矿、首产精矿目标 26Q3；⑤ Bynoe 伟晶岩田 500km² 土地持有——长期勘探潜力。",
                "images": [
                    {"url": "img/sat_finniss_z13.jpg", "src": "卫星影像（Yandex Maps）", "cap": "Finniss 矿区卫星影像——Grants 露天与选矿厂相对位置"},
                    {"url": "img/core_finniss_ops.jpg", "src": "Core Lithium 官网", "cap": "Finniss 运营现场（Core Lithium 官方）"}
                ]
            }
        }
    }
,
    {
        "company": "Global Lithium（ASX: GL1）",
        "mine": "Manna",
        "sc6": 0.917,   # SC6 折算系数（用户规范 2026-08-10：精矿产量/产能/预测全站统一 SC6 口径）
        "sc6_note": "SC6 折算（原 SC5.5 目标品位 ≥5.5% Li₂O）",
        "grade": "≥5.5% Li₂O（SC5.5 目标品位）",   # 精矿品位标注（用户规范 2026-08-11：产量/销量描述必须明确品位）
        "lat": -30.864,  # 卫星影像定位（Yandex/Google Maps）
        "lng": 122.574,
        "est_qs": [28, 29],  # 26Q1/26Q2 未披露 → 按投产进度推测 0（未投产）
        "current_q": "26Q2",
        "prev_q": "26Q1",
        "current_q_date": "2026年4-6月",
        "mine_cn": "Manna（曼纳矿山）",
        "report": "Global Lithium July 2026 Investor Presentation（2026-07-28）；Manna MDCP approved 公告（2026-08-04）；Manna DFS Results 公告（2025-12-04）；Quarterly Activities Report（2026-07-31）",
        "source_url": "https://globallithium.com.au/lithium-assets/manna-lithium-project/",
        "equity_note": "100% 资产口径（Global Lithium Resources 全资，ASX: GL1）；**未投产/开发阶段矿山**——Kalgoorlie 锂矿区第三大资源；原权属 Breaker Resources（BRB，2018-11 发现），GL1 2021-12-30 收购 80%（A$33M 上限）+ 2022-11-15 收购剩余 20%（A$60M，BRB 保留贵金属权 + 1.5% NSR）；2024-06-12 资源 +43%（51.6Mt）；2025-08-25 ML M28/414 授予（21 年期）；2025-12-03 优化 DFS 完成；2026-08-04 MDCP 批准；FID 目标 Q4 2026；DSO生产启动目标 Q1 2027、首产 SC5.5 精矿 2027 年中",
        "history_labels": [
            ("production", "精矿产量（万吨，SC5.5）"),
            ("sales", "销量（万吨）"),
            ("prod_sales_ratio", "产销比"),
            ("avg_price", "平均售价（US$/t，SC6）"),
            ("cash_cost", "单位成本 FOB（A$/t）"),
        ],
        "status_26q2": {
            "existing_lines": [
                {
                    "name": "暂无已有产线——Manna 未投产（FID 目标 Q4 2026、首产精矿 mid-2027）",
                    "q26q2": "26Q2 无生产（开发阶段）：MDCP 2026-08-04 批准；Nova 收购（2026-07-15）推进中（2026-11/12 完成）；FID 目标 Q4 2026",
                    "q26q1": "26Q1 同（开发阶段）：ML M28/414（2025-08-25）+ Native Title 协议（2025-08-13）已就绪",
                    "compare": "全部产能处于拟建/在建阶段——已移入下方②在建/规划板块"
                }
            ],
            "future_lines": [
                {
                    "name": "拟建产线1：Manna 露天矿（Manna Main + North + South）——原矿产能未披露（DFS 支撑 ~216ktpa SC6 折算/年，原 236,470tpa SC5.5）",
                    "q26q2": "26Q2 未投产（开发阶段）：Manna Main 主坑 + Manna North/South 卫星坑设计完成；MDCP 2026-08-04 批准（含多个露天坑、废石堆、干堆尾矿、营地、水井场）；FID 目标 Q4 2026",
                    "q26q1": "26Q1 同（开发阶段）：ML M28/414（2025-08-25）+ Native Title 协议（2025-08-13）已就绪",
                    "compare": "MDCP 批准（2026-08-04，略早于内部时间表）是超预期点——进一步去风险、支持 Manna-Nova 战略早期工程"
                },
                {
                    "name": "拟建产线2：选矿厂（Nova 1.8Mtpa 原矿路线 vs Manna 绿地厂）——Nova 方案：1.8Mtpa 原矿 → ~216ktpa SC6 折算（原 ~236kt SC5.5）",
                    "q26q2": "选矿策略：收购 Nova Operation（Manna 南 170km，A$7m，2026-11/12 完成）——Nova 1.8Mtpa 选矿厂可大幅降 capex、加速首产（首产精矿目标 2027 年中 vs Manna 绿地厂）；Manna-Nova 整合研究进行中（量化 capex 削减 + DSO 现金流）",
                    "q26q1": "DFS（2025-12-04）：Manna 绿地厂 capex A$439.1M、LOM 14.3 年",
                    "compare": "Nova 收购（2026-07-15 公告）改变产能路径——从绿地建厂转向收购现成厂改造，首产时间大幅提前"
                },
                {
                    "name": "DSO 运营 + 精矿生产（2027；Q2 2027 首批 DSO 销售）",
                    "q26q2": "时间表：FID Q4 2026 → DSO生产启动目标 Q1 2027（直接装运矿石）→ 首产 SC5.5 精矿 2027 年中（Nova 厂改造）；Lopal 40% 包销 + US$75M 预付款（FID 后）",
                    "q26q1": "DFS 完成后推进 FID 准备",
                    "compare": "DSO 先行是快速现金流策略（Manna-Nova 整合研究捕获 DSO 价值）"
                }
            ],
            "overall": {
                "operation_changes": "26Q2 未投产：开发推进——2026-07-15 Nova 收购公告（A$7m）、2026-08-04 MDCP 批准、FID 目标 Q4 2026；DFS（2025-12-04）经济参数：NPV8 A$472M、IRR 25.7%、Payback 3.5 年、capex A$439.1M（绿地）、AISC US$738/t SC5.5、LOM 14.3 年",
                "prev_operation_changes": "26Q1 开发推进：Lopal 战略融资（2026-04-22，配售 A$7.3m + 40% 包销 + US$75M 预付款）、Marble Bar 出售（A$14.85M，专注 Manna）",
                "highlights": [
                    "MDCP 批准（2026-08-04，DMPE）——Manna 开发关键许可，略早于内部时间表（超预期）；2024Q4-2025Q1 曾因锂价下行暂停 DFS（2025-01-29 季报官方确认）+ 249D 股东行动/诉讼干扰（2024-09 至 2025-02），2025-12-03 恢复发布优化 DFS",
                    "Nova 收购（2026-07-15）：A$7m 获 1.8Mtpa 选矿厂 → 首产精矿目标 2027 年中（vs 绿地厂更晚）",
                    "FID 目标 Q4 2026 + DSO生产启动目标 Q1 2027——fast-track 时间表（2026年7月投资者演示第18页）",
                    "DFS（2025-12-04）：NPV8 A$472M、IRR 25.7%、Payback 3.5 年、Breakeven US$784/t SC6.0——价格韧性",
                    "Kalgoorlie 锂矿区第三大资源：51.6Mt @ 1.00%（≥0.6% 边界）+ Maiden 储量 19.4Mt @ 0.91%（LOM 14.3 年）；Esperance 港出口 MOU（2025-12-18，Southern Ports）",
                    "Lopal 战略合作（2026-04-22）：40% 产量包销（10 年 SC5.5，前三年地板价 US$1,000/t CIF）+ US$75M 预付款融资 + A$7.32M 配售（2026-05-28 完成，Lopal ~5%）——资金与下游双锁定；既有 Canmax（原 Suzhou TA&A）10 年最低 30% 包销（2022-03-02，2025-04-08 变更续期）"
                ]
            }
        },
        "fc_unit": "万吨 SC6 折算（原 SC5.5 ×0.917；2027 预测：首产精矿 mid-2027 后爬坡）",
        "fc_2027": [
            {"label": "悲观", "val": 4, "note": "FID 延后 + Nova 完成延迟——2027 年仅 DSO 与精矿试产"},
            {"label": "基准", "val": 6, "note": "谨慎基准（2026-08-11 用户要求）：FID Q4 26 未定 + Nova 收购 2026-11/12 才完成 + 改造爬坡延期风险——首产可能延至 2027H2/2028，2027 ≈ 6 万吨 SC5.5（SC6 折算 5.5）"},
            {"label": "乐观", "val": 8, "note": "谨慎（2026-08-11）：Nova 改造顺利 + 爬坡快——2027 H2 接近 1.8Mtpa 原矿对应产能（SC6 折算 7.3，原 236kt SC5.5）"}
        ],
        "capacity_verification": {
            "title": "选矿产能核实（多来源交叉印证 · 未投产/开发阶段矿山）",
            "method": "以 Global Lithium DFS（2025-12-04）、2026-07 投资者展示、MDCP 公告（2026-08-04）、官网为来源；未投产矿山以 DFS 设计参数与战略路线为核心。",
            "summary": "Manna 为 Kalgoorlie 锂矿区第三大资源（51.6Mt @ 1.00%）+ Maiden 储量 19.4Mt @ 0.91%（LOM 14.3 年）；DFS（2025-12-04）绿地厂 capex A$439.1M；2026-07-15 Nova 收购战略（1.8Mtpa 选矿厂）将 Manna 矿石运至 Nova 加工，首产 SC5.5 精矿目标 2027 年中；FID 目标 Q4 2026、DSO生产启动目标 Q1 2027。",
            "items": [
                {
                    "line": "选矿产能（Manna DFS 浮选厂 vs Nova 1.8Mtpa 厂）",
                    "excel_capacity": "Manna DFS：1.8Mtpa 磨机 → ~236ktpa 精矿 dmt（236,470 tpa SC5.5 目标品位；SC6 折算 ~216kt；Nova：1.8Mtpa concentrator（收购）",
                    "verified": "✓ 2026-07 展示 + DFS 双来源",
                    "sources": [
                        {"src": "2026-07 投资者展示", "data": "GL1 to acquire 100% of Nova Operation (approx. 170km south of Manna) securing an established processing plant——1.8Mtpa concentrator plus power, camp and site infrastructure；substantial capex savings vs Manna greenfield plant；first spodumene concentrate targeted mid-2027"},
                        {"src": "Manna 优化 DFS（2025-12-03）", "data": "精矿产能 236,470 tpa SC5.5（干吨）、LOM 总 SC5.5 精矿 2.76Mt、目标品位 ≥5.5% Li₂O、LOM 平均回收率 72.8%；磨机产能 1.8Mtpa（预选后 1.5-1.6Mtpa）；剥采比 14.9、第 7 年起地下（sublevel open stoping）；CAPEX A$439.1M（动迁 81.9 + 选厂 157.5 + 间接 49.3 + 业主 110.4 + 应急 40.0）+ 可选 10MW 光伏 A$20M；NPV8 A$472M（税后含权利金）、IRR 25.7%、Payback 3.5 年、Breakeven US$784/t SC6.0、AISC US$738/t SC5.5（不含海运费）"},
                        {"src": "Nova 收购公告（2026-07-15）", "data": "A$7m consideration（A$3m cash + A$2m GL1 shares + A$2m deferred）；completion Nov/Dec 2026"}
                    ]
                },
                {
                    "line": "加工流程（⚠️ 非 DMS——浮选工艺）",
                    "excel_capacity": "三段破碎 + 矿石预选 + 单球磨 + 浮选 + 脱泥/云母浮选/磁选",
                    "verified": "✓ DFS 原文确认（DMS not suitable）",
                    "sources": [
                        {"src": "Manna 优化 DFS（2025-12-03）", "data": "Dense-Media Separation (DMS) technology is not suitable for the Manna deposit——三段破碎 + 矿石预选（ore sorting）+ 单一球磨 + 浮选 + 脱泥/云母浮选/磁选；2023-11-16 冶金试验确认浮选路线"},
                        {"src": "2026-07 投资者展示 / MDCP 公告（2026-08-04）", "data": "第18页：DSO production expected to commence March quarter 2027；SC5.5 spodumene concentrate production planned for mid 2027"}
                    ]
                },
                {
                    "line": "全矿合计（DFS 设计 vs Nova 路线）",
                    "excel_capacity": "DFS：~216ktpa SC6 折算（原 236,470 tpa SC5.5，LOM 14.3 年）；Nova 路线：1.8Mtpa concentrator 改造",
                    "verified": "✓ DFS 官方产能（236,470 tpa SC5.5 精矿 = 216kt SC6 折算）",
                    "sources": [
                        {"src": "Manna 优化 DFS（2025-12-03）", "data": "SC5.5 年产能 236,470 t（干吨）、LOM 总 SC5.5 精矿 2.76Mt——官方精矿产能"}, {"src": "2026-07 投资者展示", "data": "Nova 1.8Mtpa concentrator 收购（A$7m）→ capex 削减 + 首产提前（mid-2027）；Manna-Nova Integration Study underway to quantify capex reduction and capture cashflow from DSO production"}
                    ]
                }
            ],
            "note": "核实时间：2026-08-10。关键结论：① 未投产矿山——资源 51.6Mt @ 1.00%、储量 19.4Mt @ 0.91%（LOM 14.3 年）；② DFS（2025-12-04）：capex A$439.1M（绿地）、NPV8 A$472M、IRR 25.7%、AISC US$738/t SC5.5；③ Nova 收购（2026-07-15，A$7m）1.8Mtpa 选矿厂 → 首产精矿目标 2027 年中（提前于绿地厂）；④ FID 目标 Q4 2026、DSO生产启动目标 Q1 2027（2026年7月投资者演示第18页）；⑤ 精矿产能官方值 236,470 tpa SC5.5（DFS）；⑥ 注意 2023 Scoping Study（2.0Mtpa/NPV A$2.8B@US$2,500 高价假设）与 2025 优化 DFS（1.8Mtpa/NPV A$472M）勿混用——以 DFS 为准。",
            "sources_index": {"技术报告": "Manna DFS（2025-12-04）、MRE 更新（2024-06-12）", "公司公告": "MDCP 批准（2026-08-04）、Nova 收购（2026-07-15）、Lopal 融资（2026-04-22）", "公司展示": "July 2026 Investor Presentation", "官网": "globallithium.com.au Manna 项目页", "数据站": "区域位置图（Kalgoorlie 锂矿区对比）"},
            "images": [
                {"url": "img/sat_manna_z13.jpg", "src": "卫星影像（Yandex Maps）", "cap": "Manna 项目区卫星影像——Kalgoorlie 东 110km（未开发地形）"},
                {"url": "img/manna_region_map.jpg", "src": "Global Lithium 官网", "cap": "Kalgoorlie 锂矿区位置图——Manna vs Mt Marion/Bald Hill/Pioneer Dome/Buldania 资源对比"},
                {"url": "img/manna_tenement_map.jpg", "src": "Global Lithium 官网", "cap": "Manna 矿权位置图（M28/414 等）"}
            ],
            "mining_side": {
                "title": "原矿产能核实（矿坑 / 矿体 / 尾矿库 · 未投产/开发阶段矿山）",
                "method": "以 Global Lithium DFS/MRE 公告、MDCP 公告、官网为来源。",
                "items": [
                    {
                        "line": "原矿矿山：Manna Main + North + South 露天",
                        "status": "🔧 设计完成（未投产）；MDCP 已批准",
                        "sources": [
                            {"src": "MDCP 公告（2026-08-04）", "data": "multiple open pits: one main (Manna Main) and two satellites (Manna North and Manna South)；waste rock and dry stack tailings, ore stockpiles, accommodation village, bore field, topsoil stockpiles"},
                            {"src": "官网/DFS/MDCP", "data": "110km east of Kalgoorlie-Boulder（Kalgoorlie-Boulder 郡）on Mining Lease M28/414；坐标 ≈ -30.87, 122.53（MGA94 Zone 51 换算 + miningdataonline -30.864, 122.574 印证）——Lake Roe 项目区内、Bombora 金矿体西南 15km；LCT 伟晶岩脉群：脉厚 1-14m 平均 3.6m、倾向 -60~-70° SE"}
                        ]
                    },
                    {
                        "line": "矿体与资源（spodumene/lepidolite 伟晶岩）",
                        "status": "✅ 资源确认（第三大）",
                        "sources": [
                            {"src": "MRE 更新（2024-06-12，现行）", "data": "MRE 51.6Mt @ 1.00% Li₂O（≥0.6% Li₂O 边界、Fe<8%，JORC 2012）：Indicated 32.9Mt @ 1.04%/52ppm + Inferred 18.7Mt @ 0.92%/50ppm（LCE 1,276kt）；敏感性：0.5%→55.7Mt@0.97%、0.8%→39.5Mt@1.09%、1.0%→22.8Mt@1.22%"}, {"src": "DFS 储量（2025-12-03）", "data": "Maiden Ore Reserve 19.4Mt @ 0.907% Li₂O（全部 Probable）：露天 14.4Mt @ 0.93%（0.5% 边界）+ 地下 5.0Mt @ 0.84%（0.6% 边界）→ LOM 14.3 年（82% 采矿库存由储量支撑）"}, {"src": "历史资源链", "data": "9.9Mt @ 1.14%（2022-02-16 首次，80% 权益）→ 50.7Mt（2022-12-14，Manna 32.7Mt@1.0%）→ 36.0Mt @ 1.13%（2023-07-26）→ 51.6Mt（2024-06-12 +43%）"},
                            {"src": "区域位置图（官网）", "data": "Kalgoorlie 锂矿区：Mt Marion 66.1Mt @ 1.36% > Bald Hill 58.1Mt @ 0.94% > Manna 51.6Mt @ 1.00%（第三）"}
                        ]
                    },
                    {
                        "line": "环评与许可（WA 政府）",
                        "status": "✅ MDCP 已批准（2026-08-04）",
                        "sources": [
                            {"src": "MDCP 公告（2026-08-04）", "data": "Mining Development and Closure Proposal (MDCP) approved by DMPE（Department of Mines, Petroleum and Exploration），on schedule，slightly ahead of internal timelines"},
                            {"src": "官网/2025 公告", "data": "Mining Lease M28/414 granted 2025-08-25；Native Title Mining Agreement signed with Kakarra Part B Native Title Group 2025-08-13"}
                        ]
                    },
                    {
                        "line": "尾矿库（干堆尾矿）",
                        "status": "🔧 设计阶段（dry stack tailings）",
                        "sources": [
                            {"src": "MDCP 公告（2026-08-04）", "data": "dry stack tailings 为 MDCP 设计设施之一"}
                        ]
                    }
                ],
                "note": "核实时间：2026-08-10。采矿侧要点：① 未投产——Manna Main + North + South 露天设计完成、MDCP 2026-08-04 批准；② 资源 51.6Mt @ 1.00%（2024-06，+43%）、Maiden 储量 19.4Mt @ 0.91%（LOM 14.3 年）；③ 环评：MDCP（DMPE）+ ML M28/414（2025-08-25）+ Native Title 协议（2025-08-13）；④ FID 目标 Q4 2026、DSO生产启动目标 Q1 2027、首产精矿 2027 年中；⑤ Kalgoorlie 锂矿区第三大资源（Mt Marion > Bald Hill > Manna）。",
                "images": [
                    {"url": "img/manna_core_sample.jpg", "src": "Global Lithium 官网", "cap": "Manna 岩芯样本（spodumene 伟晶岩）"},
                    {"url": "img/manna_drill.jpg", "src": "Global Lithium 官网", "cap": "Manna RC 钻探作业（2022-2024 大规模钻探）"},
                    {"url": "img/manna_aerial.jpg", "src": "Global Lithium 官网", "cap": "Manna 项目区航拍（未开发地形）"}
                ]
            }
        }
    }
,
    {
        "company": "Covalent Lithium（SQM 50% + Wesfarmers 50%）",
        "mine": "Mt Holland",
        "sc6": 0.917,   # SC6 折算系数（用户规范 2026-08-10：精矿产量/产能/预测全站统一 SC6 口径）
        "sc6_note": "SC6 折算（原 dmt SC5.5 名义品位；SQM 官方销量即 SC6）",
        "grade": "5.5% Li₂O（SC5.5）",   # 精矿品位标注（用户规范 2026-08-11：产量/销量描述必须明确品位）
        "lat": -32.083,  # 卫星影像定位（Yandex/Google Maps）
        "lng": 119.748,
        "est_qs": [28, 29],  # 26Q1/26Q2 未披露（SQM 不披露季度产量）→ 按满产推测 9.5
        "current_q": "26Q2",
        "prev_q": "26Q1",
        "current_q_date": "2026年4-6月",
        "mine_cn": "Mt Holland（荷兰山矿山）",
        "report": "SQM 1Q2026 Earnings Release（2026-05-27，美式季度）；SQM 4Q2025 Earnings Release（2026-03-02）；SQM & Wesfarmers Mt Holland Expansion FID 公告（2026-07-21）；SQM-I 官网 Mt Holland 页",
        "source_url": "https://sqm-i.com/what-we-do/operations-and-projects/mt-holland/",
        "equity_note": "100% 资产基准（页面按 SQM 50% 份额 ×2 换算并标注）；Covalent Lithium = SQM（智利，NYSE: SQM，SQM-I 国际锂业务运营）+ Wesfarmers（ASX: WES）50:50 JV；**矿 + Kwinana 精炼厂一体化**（精矿 SC5.5 运至珀斯 Kwinana 转电池级氢氧化锂）；历史：Kidman Resources（ASX: KDR）2016 发现 Earl Grey → 2017-09-12 SQM US$110M JV 协议（50:50）→ 2018-12 IPFS + 首份储量 94.2Mt@1.5% → 2019-09-23 Wesfarmers $1.90/股收购 Kidman（~A$776M，溢价 47.3%）→ Covalent 50:50 JV；**SQM-I 为 SQM 国际锂业务分部（2024 设立，非独立上市）——SQM 本身 NYSE 上市（CIK 0000909037，Form 20-F）**；**美式财季（Q1-Q4）与 MM/DD/YYYY 日期格式**——最新披露 = SQM 2026Q1（2026-05-27），Q2 2026 报告 2026 年 8 月下旬发布；投产：首采 2022、选厂 2023Q3 调试、2023Q4 双回路首产精矿、2024 H1 首出口、2025 达名义产能 383ktpa",
        "history_labels": [
            ("production", "产量（万吨，100% dmt SC5.5——SQM 不披露季度产量：2026Q1-Q4 为按满产推测值（E 标记，依据 SQM 满产运营确认 + 383ktpa÷4）；年度产量见表格下方注记）"),
            ("sales", "销量（万吨，SQM 50% 份额 SC6 ×2 = 100% 估算）"),
            ("avg_price", "平均售价（US$/t，SC6；FOB/CIF 未披露）"),
        ],
        "status_26q2": {
            "existing_lines": [
                {
                    "name": "已有产能1：Mt Holland 矿 + 选矿厂（Earl Grey 伟晶岩）— ~380ktpa 精矿 dmt（SC5.5 品位产品吨位，100%；SC6 折算 ~348kt；原矿由 Earl Grey 露天矿供给，原矿产能未单独披露）",
                    "q26q2": "26Q2 数据未发布（SQM 美式财季 Q2 2026 报告 2026 年 8 月下旬发布）；**期后事项（2026-07-21）**：扩产 FID 380→760ktpa（第二选矿厂 2027 H2 建设、扩产首产 H1 2030），FID 确认矿山满产运营（SQM 2026Q1 口径）；1Q2026 精矿销量 38.1kt（SQM 50% 份额 SC6）；选矿工艺 = DMS + 浮选混合",
                    "q26q1": "26Q1 满产运营（SQM 1Q2026 确认 'operating at full capacity'）；1Q2026 精矿销量 38.1kt（SQM 50%）；2025 全年 156.4kt（SQM 50%）为首个完整生产年",
                    "compare": "26Q2 实际待 Q2 财报（8 月下旬）确认——当前信息以 26Q1 口径 + 期后 FID 为准；扩产 FID（2026-07-21，SQM 份额 capex US$450-500M）确认满产运营并进入倍增阶段"
                },
                {
                    "name": "已有产能2：Kwinana 氢氧化锂精炼厂 — 50ktpa 电池级 LOH",
                    "q26q2": "Kwinana 爬坡中：2025-07 首产（SQM 2025Q2 确认）、SQM 指引预计 2027 达名称产能（爬坡约 18 个月）；1Q2026 氢氧化锂 0.9kt LCE（SQM 50% 份额）；2025 全年 1.6kt LCE（SQM 50%）",
                    "q26q1": "爬坡初期（2025 年首产后）",
                    "compare": "精炼厂爬坡约 18 个月（2025-07 首产 → 2027 名称产能）；扩产 FID 保留 Kwinana 下游扩产选项（或直接卖精矿）"
                }
            ],
            "future_lines": [
                {
                    "name": "扩产项目（380→760ktpa 精矿 dmt SC5.5，SC6 折算 348→697kt，FID 2026-07-21）",
                    "q26q2": "扩产 FID 通过（2026-07-21，期后事项）：矿 + 选矿厂 + 新集成矿石分选设施；第二选矿厂 2027 H2 开工、扩产首产精矿 H1 2030；SQM 份额 capex US$450-500M（Wesfarmers 份额 A$645-715M）；FID 公告称相关审批 'secured or underway'——LOM 扩建 EPA 部长决定仍待定（2026-08）；扩产提供 Kwinana 下游扩产或直接卖精矿的选择权",
                    "q26q1": "扩产 DFS 研究中（2026 年前）",
                    "compare": "FID 后 12 个月开工——2027 H2 建设启动是下一催化剂"
                }
            ],
            "overall": {
                "operation_changes": "26Q2 数据未发布（SQM 美式 Q2 报告 8 月下旬）——当前状态以 26Q1 口径为准：矿/选矿厂满产运营（SQM 官方）、Kwinana 精炼厂爬坡中（2027 达名称产能）；精矿实现均价 US$1,461/t（1Q2026，+72% yoy，FOB/CIF 未披露）；**期后（2026-07-21）**：扩产 FID 380→760ktpa——进入倍增阶段",
                "prev_operation_changes": "26Q1 满产运营（1Q2026 38.1kt 50% 份额 SC6 销量）；2025 全年精矿销量 156.4kt（50%）+ 氢氧化锂 1.6kt LCE（50%）",
                "highlights": [
                    "2026-07-21 扩产 FID：精矿 380→760ktpa @ 5.5% Li₂O（100%，翻倍）——SQM 份额 capex US$450-500M、2027 H2 建设、H1 2030 首产",
                    "2026Q1 满产运营确认（SQM 官方）——2023Q4 双回路首产精矿 → 2025 达名义产能 383ktpa → 2026Q1 满产（爬坡约 5 个季度）",
                    "Kwinana 精炼厂 2025-07 首产（一体化最后一块拼图）——2025 全年氢氧化锂 1.6kt LCE（50%），2027 达名称产能 50ktpa",
                    "2025 全年精矿销量 156.4kt（SQM 50% 份额 SC6）——首个完整生产年；官方年度产量（20-F 100% dmt SC5.5）：2023=15.0kt、2024=232.4kt、2025=329.6kt",
                    "储量 84.7Mt @ 1.45%（20-F 2025-12-31；官网 85.6 为 FY2024 末口径）——Earl Grey 伟晶岩西澳前五、矿山寿命 50+ 年",
                    "扩产含 ore sorting 设施：回收堆存料 +约 3Mt 精矿（LOM）——扩产保留 Kwinana 下游扩产选择权"
                ]
            }
        },
        "fc_unit": "万吨 SC6 折算（原 SC5.5 ×0.917；名义产能 383ktpa→351kt SC6——MH 无官方 FY27 指引，按产能利用率情景，非线性）",
        "fc_2027": [
            {"label": "悲观", "val": 36, "note": "名义产能 383ktpa 的 94.0% 利用率（36.0/38.3）——需求/发运节奏影响下的保守运行；2027 扩产不贡献产量（2027 H2 才开工、首产 H1 2030）"},
            {"label": "基准", "val": 38, "note": "约 380kt ≈ 名义产能 99.2%（38.0/38.3）——Wesfarmers FY27 项目口径约 380kt 为依据的满产稳定运行"},
            {"label": "乐观", "val": 40, "note": "名义产能的 104.4%（40.0/38.3）——超名义产能的乐观假设（扩产前期/直接销售增加）"}
        ],
        "capacity_verification": {
            "title": "选矿产能核实（多来源交叉印证 · 矿+精炼一体化项目）",
            "method": "以 SQM-I 官网、SQM 美式季报（SEC 6-K）、扩产 FID 公告（2026-07-21）为来源；产能为 100% 基准（SQM 披露 50% 份额）。",
            "summary": "Mt Holland（Earl Grey 伟晶岩，Forrestania 地区）选矿厂 DMS + 浮选混合工艺，产能 383,000 dmtpa SC5.5（100%）；Kwinana 精炼厂 50,000 tpa 电池级氢氧化锂（2025-07 首产、2027 达名称产能）；2026-07-21 扩产 FID（期后事项）：380→760ktpa 翻倍。官方年度产量（20-F，100% dmt SC5.5）：2023=15.0kt、2024=232.4kt、2025=329.6kt；SQM 50% 份额 SC6 销量：2025 全年 156.4kt。",
            "items": [
                {
                    "line": "Mt Holland 选矿厂（DMS + 浮选混合）",
                    "excel_capacity": "~380ktpa 精矿 dmt（SC5.5，100% 基准；SC6 折算 ~348kt）",
                    "verified": "✓ 官网 + SQM 报告双确认",
                    "sources": [
                        {"src": "SQM 20-F FY2025", "data": "concentrator nameplate 383,000 dmtpa SC 5.5% Li₂O；2023=15.0kt / 2024=232.4kt / 2025=329.6kt（100%，dmt SC5.5）；首采 2022、选厂 2023Q3 调试、2023Q4 双回路首产、2024 H1 首出口、2025 达名义产能；流程：DMS 粗粒 + 球磨/磁选/脱泥 + 浮选细粒"}, {"src": "SQM-I 官网", "data": "hybrid Dense Media Separation (DMS) and flotation process；expected annual output of approximately 380,000 dry tonnes at 5.5% Li₂O"},
                        {"src": "扩产 FID（2026-07-21）", "data": "existing nameplate approximately 380,000 tpa → expansion to 760,000 tpa at 5.5% Li₂O (100% basis)；second concentrator construction H2 2027、first expansion production H1 2030；ore sorting facility 回收堆存料 +约 3Mt 精矿（LOM）；SQM share capex US$450-500M（Wesfarmers 份额 A$645-715M）"},
                        {"src": "SQM 2025 全年报告", "data": "2025 实际销量 156.4kt SC6（SQM 50% 份额）——首个完整生产年；年度产量与销量为不同口径（产量=100% dmt SC5.5、销量=50% 份额 SC6），不可直接比较"}
                    ]
                },
                {
                    "line": "Kwinana 氢氧化锂精炼厂",
                    "excel_capacity": "50ktpa 电池级 LOH（约 1M EVs/年）",
                    "verified": "✓ 官网 + SQM 报告确认",
                    "sources": [
                        {"src": "SQM-I 官网", "data": "refinery expected to produce approximately 50,000 tonnes of battery-grade lithium hydroxide；located in Kwinana Industrial Area ~35km south of Perth；completion and successful commissioning in 2025 marked the start of lithium hydroxide production in Australia"},
                        {"src": "SQM 2025Q2/Q4 报告", "data": "Kwinana first product July 2025；ramp-up expected ~18 months；2025 全年氢氧化锂 1.6kt LCE（50% = 3.2kt 100%）；2026Q1 0.9kt LCE（50%）"}
                    ]
                },
                {
                    "line": "全矿合计（一体化）",
                    "excel_capacity": "~380kt 精矿 dmt（SC5.5）+ 50kt LOH → 扩产 ~760kt dmt（SC6 折算 348→697kt）",
                    "verified": "✓ 官方确认（FID）",
                    "sources": [
                        {"src": "扩产 FID（2026-07-21）", "data": "expansion provides optionality to supply any future expansion of downstream processing at Kwinana refinery or sell expanded production as spodumene concentrate"},
                        {"src": "SQM 2026Q1 报告", "data": "Mt Holland mine and concentrator currently operating at full capacity；Kwinana expected to reach nameplate in 2027"}
                    ]
                }
            ],
            "note": "核实时间：2026-08-05。关键结论：① 选矿厂 380ktpa SC5.5（100%）+ 扩产 FID 760ktpa（2026-07-21，2027 H2 建设、H1 2030 首产）；② Kwinana 精炼厂 50ktpa LOH（2025-07 首产、2027 达名称产能）；③ 20-F 产量：2023=15kt / 2024=232.4kt / 2025=329.6kt（100%）——2025 达名义产能 86%；④ 2026Q1 满产运营（SQM 官方）；⑤ SQM 披露为 50% 份额（页面 ×2 = 100% 基准并标注）；⑥ 美式财季——最新披露 2026Q1（2026-05-27），Q2 2026 报告 8 月下旬。",
            "sources_index": {"公司官网": "SQM-I（sqm-i.com）Mt Holland 页", "公司报告": "SQM 美式季报（SEC 6-K：2025Q1-Q4、2026Q1）", "公司公告": "SQM & Wesfarmers 扩产 FID（2026-07-21）", "前股东": "Kidman Resources（KDR）2016-2018 DFS/JORC", "母公司": "Wesfarmers（ASX: WES）公告"},
            "images": [
                {"url": "img/sat_mtholland_z13.jpg", "src": "卫星影像（Yandex Maps）", "cap": "Mt Holland 矿区卫星影像（Forrestania 地区）——Earl Grey 露天矿与选矿厂"},
                {"url": "img/sqmi_mtholland_hero.jpg", "src": "SQM-I 官网", "cap": "Mt Holland 项目图（SQM-I 官方）"}
            ],
            "mining_side": {
                "title": "原矿产能核实（矿坑 / 矿体 / 尾矿库 · 一体化项目）",
                "method": "以 SQM-I 官网、SQM 报告、Kidman 时代资料为来源。",
                "items": [
                    {
                        "line": "原矿矿山：Earl Grey 露天矿",
                        "status": "✅ 生产运营中（2023Q4 首产精矿）",
                        "sources": [
                            {"src": "SQM-I 官网", "data": "open-cut mining operation with run-of-mine ore processed on-site；Earl Grey pegmatite：tabular ore body extending over 2km in dip, ~1km strike, up to 100m thickness"},
                            {"src": "SQM 2026Q1 报告", "data": "mine and concentrator currently operating at full capacity"}
                        ]
                    },
                    {
                        "line": "矿体与资源（Earl Grey 伟晶岩）",
                        "status": "✅ 储量确认（西澳前五）",
                        "sources": [
                            {"src": "SQM 20-F FY2025（S-K1300，2025-12-31）", "data": "Mineral Reserves 84.7Mt @ 1.45% Li₂O（Proven 38.5Mt@1.56% + Probable 43.7Mt@1.38% + 堆存 2.5Mt@0.89%；0.5% cut-off；冶金回收率 75%；SQM 50% = 42.4Mt；FY2024 末为 85.6Mt -1% 开采消耗）；Mineral Resource（excl. reserves）121.1Mt（0.5%/0.78% petalite cut-off）——西澳前五、矿山寿命 50+ 年"}, {"src": "Kidman 时代（历史链）", "data": "2016-12-05 首份 MRE 128Mt @ 1.44%（当时 ASX 最大硬岩锂资源）→ 2018-03-19 MRE 189Mt @ 1.50%（+54%，91% M+I）→ 2018-12-18 首份 Ore Reserve 94.2Mt @ 1.5%（IPFS 伴生）"},
                        ]
                    },
                    {
                        "line": "环评与许可（WA 政府）",
                        "status": "✅ 已有项目已获批（矿 + 精炼厂）；⚠️ 扩产许可：EPA Report 1809 建议批准、部长决定待定（2026-08）",
                        "sources": [
                            {"src": "WA EPA（矿山）", "data": "EPA Assessment 2123 → Ministerial Statement 1118（2019-11-21）；修订 2315 → MS 1199（2022-11-23）；LOM 扩建 2387 → EPA Report 1809（2026，EPA 建议批准、部长决定待定）；Mining Proposal Stage 2 REG 121883（2023-11）；联邦 EPBC 2017-7950"}, {"src": "WA EPA（Kwinana 精炼厂）", "data": "EPA Assessment 2282 → EPA Report 1700 → Ministerial Statement 1170（2021-07-15）；DWER Works Approval W6499/2021/1（2025-04-08 修订，勿混 Tianqi 的 W5977）"},
                            {"src": "Kidman 时代", "data": "Mt Holland Mining Proposal 2017-2018 获批（DMP/DMIRS）——投产前许可齐全"}
                        ]
                    },
                    {
                        "line": "尾矿库（TSF）与物流",
                        "status": "✅ 建成",
                        "sources": [
                            {"src": "SQM-I 官网", "data": "精矿由陆路运至 Kwinana（Perth 南）精炼——一体化物流；⚠️ 尾矿库为推断表述（20-F 未逐项披露 TSF 细节，待核实）"}
                        ]
                    }
                ],
                "note": "核实时间：2026-08-05。采矿侧要点：① Earl Grey 露天矿（Forrestania 地区，Perth 东 500km、Southern Cross 东南 120km）；② 储量 84.7Mt @ 1.45%（20-F 2025-12-31；官网 85.6 为 FY2024 末）；③ 矿+精炼一体化（Kwinana 50ktpa LOH）；④ 首采 2022、2023Q4 首产精矿、2025 达名义产能 383ktpa、2026Q1 满产；⑤ 2026-07-21 扩产 FID（380→760ktpa）；⑥ 坐标 ≈ -32.083, 119.748（Kidman 钻探孔位 GDA94 Z50→WGS84 换算：KEGR001 -32.08222,119.74634；KEGM039 -32.08693,119.75211）；矿业权 M77/1065、M77/1066、M77/1080（合计 4,626 ha）。",
                "images": [
                    {"url": "img/sat_mtholland_z13.jpg", "src": "卫星影像（Yandex Maps）", "cap": "Mt Holland Earl Grey 露天矿卫星影像"},
                    {"url": "img/sqmi_mtholland_hero.jpg", "src": "SQM-I 官网", "cap": "Mt Holland 项目实景（SQM-I 官方）"}
                ]
            }
        }
    }
]

# ============ 企业官方项目进展表 / 历程图 ============
# 仅收录公司官网、官方季度报告或投资者演示中的原图；计划日期是公司当时的
# 前瞻性安排，不等同于已完成事实。页面放在②在建/规划板块内，避免改变①-⑦编号。
MILESTONE_TIMELINES = {
    "Manna": {
        "title": "Manna-Nova 项目关键里程碑",
        "document": "Global Lithium Resources Investor Presentation",
        "date": "2026-07",
        "page": 15,
        "source_url": "https://wcsecure.weblink.com.au/pdf/GL1/03114698.pdf",
        "summary": "公司2026年7月计划：Q3 2026完成整合研究及多项Pre-FID工作，Q4 2026作出FID；Q1-Q2 2027进行Nova选厂转换与调试并开展DSO运营，Q3 2027起生产SC5.5并完成首批SC5.5出口。",
        "note": "图中日期属于公司发布时的前瞻性目标，并非已完成事实；Nova收购交割、审批、FID、改造和调试均可能影响实际进度。DSO与SC5.5精矿是不同产品，页面预测不把DSO计入SC5.5精矿产量。",
        "images": [
            {
                "url": "img/manna_nova_milestones_official.png",
                "src": "Global Lithium《Investor Presentation — July 2026》第15页",
                "cap": "Manna-Nova Project Key Milestones：Pre-FID、FID、Nova选厂转换与调试、DSO运营、SC5.5生产及首批出口的公司计划时序（点击放大）"
            }
        ]
    },
    "Greenbushes": {
        "title": "Greenbushes 项目历程与产线进度（2022官方快照）",
        "document": "IGO Greenbushes Site Visit Presentation",
        "date": "2022-07-29",
        "page": "PDF第8、19页（页脚7、18）",
        "source_url": "https://www.igo.com.au/site/pdf/c5d6ce55-e0f1-49ea-8e94-e3d95b1f3da2/Platform/ListPage/Greenbushes-Site-Visit-Presentation.pdf",
        "summary": "IGO官方材料以时间线展示1886发现锡矿、1983首次生产锂矿物、1997产能达150ktpa、2021 CGP2重启/TRP开工及FY22产量；产线表列出TGP、CGP1、CGP2、TRP与CGP3在2022年7月的状态、产能和恢复率。",
        "note": "两图均为2022年历史快照：其中CGP3“预计2025年初调试”已被后续实际进度取代，CGP3已于25Q4首产；CGP4截至2026年中仍未宣布FID。图中产能为公司当时口径，勿直接替代页面当前季度数据。",
        "images": [
            {
                "url": "img/greenbushes_project_timeline_official.png",
                "src": "IGO《Greenbushes Site Visit Presentation》2022-07-29，PDF第8页（页脚7）",
                "cap": "Project Timeline：1886年至FY22的Greenbushes项目发展历程（点击放大）"
            },
            {
                "url": "img/greenbushes_line_progress_official.png",
                "src": "IGO《Greenbushes Site Visit Presentation》2022-07-29，PDF第19页（页脚18）",
                "cap": "Expanding concentrate production capacity to meet demand：TGP、CGP1、CGP2、TRP与CGP3的2022年状态/产能/进展表（点击放大）"
            }
        ]
    },
    "Pilgangoora": {
        "title": "Pilgangoora 扩产至1Mtpa路径（历史官方图）",
        "document": "PLS December 2022 Quarterly Activities Presentation",
        "date": "2023-01-19",
        "page": 8,
        "source_url": "https://pls.com/wp-content/uploads/2023/01/December2022QuarterlyActivitiesPresentation.pdf",
        "summary": "PLS图示产能从580ktpa经P680提升至680ktpa，再经P1000提升至约1,000ktpa；发布时P680在建，P1000处于Pre-FID并计划2023年一季度作出FID。",
        "note": "这是2023年初历史扩产路径，不是当前待建计划；P680和P1000后来均于FY25完成。当前页面的下一阶段是P2000预FID研究，不能套用本图原时序。PLS旧PDF现行路径返回404，原始公司URL通过Wayback归档取回核验。",
        "images": [
            {
                "url": "img/pilgangoora_expansion_pathway_official.png",
                "src": "PLS《December 2022 Quarterly Activities Presentation》2023-01-19，第8页（官方原URL，Wayback取回核验）",
                "cap": "Expansion pathway to 1Mtpa：P680与P1000扩产阶梯及当时计划时序（点击放大）"
            }
        ]
    },
    "Wodgina": {
        "title": "Wodgina 棕地扩产选择与建设周期",
        "document": "Mineral Resources Lithium Investor Tour Presentation",
        "date": "2026-05-19",
        "page": 25,
        "source_url": "https://clients3.weblink.com.au/pdf/MIN/03091270.pdf",
        "summary": "公司评估两条棕地扩产路径：升级现有三条产线及新建4号线，分别可增产约30%；截至演示发布时仍待方案评估、FID和JV批准，获批后至投产预计18个月。",
        "note": "这是可选扩产方案，不是已批准项目或产量指引；18个月从未来FID/JV批准日起算，不应直接写成固定投产日期。",
        "images": [
            {
                "url": "img/wodgina_growth_timeline_official.png",
                "src": "MinRes《Lithium Investor Tour Presentation》2026-05-19，第25页",
                "cap": "Wodgina processing plant layout / Brownfields Growth Optionality：三线升级、4号线选址、审批状态及获批后18个月建设周期（点击放大）"
            }
        ]
    },
    "Mt Marion": {
        "title": "Mt Marion 浮选厂与地下开发时序",
        "document": "Mineral Resources Lithium Investor Tour Presentation",
        "date": "2026-05-19",
        "page": 36,
        "source_url": "https://clients3.weblink.com.au/pdf/MIN/03091270.pdf",
        "summary": "演示给出的建设周期为：浮选厂从建设到爬坡18个月，地下开发至首矿12个月；方案目标将SC6产能从500ktpa提高至600ktpa并延长矿山寿命。",
        "note": "图中“FID targeted Q1 FY27”已被2026-05-26正式FID取代；最新FID公告口径为Q1 FY27开工、2H FY28调试和爬坡。时间轴用于展示公司建设路径，不代表当前已投产。",
        "updates": [
            {"label": "2026-05-26 Mt Marion 浮选厂与地下开发正式FID公告", "url": "https://clients3.weblink.com.au/pdf/MIN/03093542.pdf"}
        ],
        "images": [
            {
                "url": "img/marion_growth_timeline_official.png",
                "src": "MinRes《Lithium Investor Tour Presentation》2026-05-19，第36页",
                "cap": "Mt Marion Brownfields Growth Optionality：浮选厂18个月建设至爬坡、地下开发12个月至首矿，以及产能和资本开支框架（点击放大）"
            }
        ]
    },
    "Kathleen Valley": {
        "title": "Kathleen Valley 建设里程碑与项目历程",
        "document": "Liontown Investor Presentation – Offtake, Funding & Project Update",
        "date": "2022-06-30",
        "page": 11,
        "source_url": "https://www.liontown.com/wp-content/uploads/2023/06/61097709.pdf",
        "verification_sources": [
            {"label": "Liontown官网现行项目历程（用于核对实际完成节点）", "url": "https://www.liontown.com/project/kathleen-valley/#milestones"}
        ],
        "summary": "2022年官方建设计划图列示：Q4 2021完成DFS/NTA和A$463m融资，H1 2022签署三份基础承购，Q2 2022完成债务融资与FID，Q4 2022早期工程/设计，原计划Q4 2023完工、Q1/Q2 2024调试、Q2 2024投产。官网现行历程另覆盖2017首次钻探至2025地下生产启动。",
        "note": "官方PDF原图是2022年建设期计划，不是当前指引；图中Q2 2024投产目标后来调整，实际首批精矿于2024年7月产出。下方事件卡来自Liontown官网现行历程，并逐项链接公司原始公告。",
        "events": [
            {"year": 2017, "items": [
                {"label": "首次钻探计划启动", "url": "https://www.liontown.com/wp-content/uploads/2023/06/6810359.pdf"}
            ]},
            {"year": 2018, "items": [
                {"label": "定义矿产资源，确认一级锂矿床", "url": "https://www.liontown.com/wp-content/uploads/2023/06/6898063.pdf"}
            ]},
            {"year": 2021, "items": [
                {"label": "DFS完成", "url": "https://www.liontown.com/wp-content/uploads/2023/06/61062133.pdf"},
                {"label": "签署Native Title协议", "url": "https://www.liontown.com/wp-content/uploads/2023/06/61063303.pdf"}
            ]},
            {"year": 2022, "items": [
                {"label": "FID、与Tesla/Ford/LG Energy Solution签署承购协议并开工", "url": "https://www.liontown.com/wp-content/uploads/2023/06/61097709.pdf"}
            ]},
            {"year": 2023, "items": [
                {"label": "采矿作业启动", "url": "https://www.liontown.com/wp-content/uploads/2023/06/61134861.pdf"}
            ]},
            {"year": 2024, "items": [
                {"label": "混合能源电站启动", "url": "https://www.liontown.com/latest-news/renewables-power-up-kathleen-valley/"},
                {"label": "按计划实现首产", "url": "https://www.liontown.com/latest-news/first-production-delivered-on-schedule-at-kathleen-valley/"}
            ]},
            {"year": 2025, "items": [
                {"label": "地下生产按计划启动", "url": "https://www.liontown.com/latest-news/underground-production-commences-on-schedule-at-kathleen-valley-australias-first-underground-lithium-mine/"}
            ]}
        ],
        "images": [
            {
                "url": "img/kathleen_project_milestones_official.png",
                "src": "Liontown《Investor Presentation – Offtake, Funding & Project Update》2022-06-30，第11页",
                "cap": "2024 Production Target / Project Milestones on Schedule（2022年建设期历史计划，点击放大）"
            }
        ]
    },
    "Bald Hill": {
        "title": "Bald Hill 重启计划",
        "document": "Mineral Resources Lithium Investor Tour Presentation",
        "date": "2026-05-19",
        "page": 43,
        "source_url": "https://clients3.weblink.com.au/pdf/MIN/03091270.pdf",
        "summary": "公司重启计划显示：首批矿石装船目标Q1 FY27，Q2 FY27爬坡至满产；安装产能140ktpa SC6、产品品位5.1%，重启成本A$20M。",
        "note": "Q1/Q2 FY27是MinRes财季：分别对应日历2026Q3和2026Q4。该图是2026-05-19的公司重启计划，实际进度仍须用后续季报核验。",
        "updates": [
            {"label": "2026-05-18 Bald Hill 锂矿重启公告", "url": "https://clients3.weblink.com.au/pdf/MIN/03091219.pdf"}
        ],
        "images": [
            {
                "url": "img/baldhill_restart_timeline_official.png",
                "src": "MinRes《Lithium Investor Tour Presentation》2026-05-19，第43页",
                "cap": "Bald Hill Restart Plan：首矿装船、满产爬坡、重启成本、安装产能及剥采比路径（点击放大）"
            }
        ]
    },
    "Mt Cattlin": {
        "title": "Mt Cattlin 重启进度与计划里程碑（2016历史）",
        "document": "Galaxy Resources — MT CATTLIN PREPARES FOR PRODUCTION COMMENCEMENT",
        "date": "2016-11-01",
        "page": 2,
        "source_url": "https://announcements.asx.com.au/asxpdf/20161101/pdf/43ckdjcfb731f3.pdf",
        "summary": "Galaxy截至2016-10-29的进度包括DMS厂机械完工、DMS管线完成95%、反渗透装置安装、过滤区工程及回流分级楼湿调试；随后两周计划完成絮凝剂厂、调试各回路、引入硅铁介质并准备矿石调试。",
        "note": "这是Galaxy Resources 2016年重启阶段的历史进度，不代表当前复产计划。Mt Cattlin自2025年3月底起处于维护保养状态；截至2026-08，Rio Tinto尚未公布当前复产决定或时间表。",
        "updates": [
            {"label": "2016-11-16 矿石调试及首批锂精矿生产确认", "url": "https://announcements.asx.com.au/asxpdf/20161116/pdf/43cy0r8fkqs4wm.pdf"}
        ],
        "images": [
            {
                "url": "img/mtcattlin_2016_progress_official.png",
                "src": "Galaxy Resources《MT CATTLIN PREPARES FOR PRODUCTION COMMENCEMENT》2016-11-01，第2页",
                "cap": "截至2016-10-29已完成进展 + 截至2016-11-12计划里程碑（历史重启进度，点击放大）"
            }
        ]
    },
    "Finniss": {
        "title": "Finniss 分阶段重启时间表",
        "document": "Core Lithium Finniss Funding and Restart Presentation",
        "date": "2026-03-18",
        "page": 10,
        "source_url": "https://corelithium.com.au/announcements/7451204",
        "verification_sources": [
            {"label": "InvestorPA原ASX附件镜像（用于页面核验）", "url": "https://investorpa.com/announcement-pdf/20260318/270827.pdf"}
        ],
        "summary": "公司重启路径显示：Q1 2026融资与FID，Q2部署重启资本并启动Grants露天矿/BP33箱形切口，Q3-Q4选厂启动和首批精矿发运；BP33地下矿目标2027年中首矿、2028年中达到1.2Mtpa满产。",
        "note": "该图脚注明确说明时序仅供说明，基于当前完工估计，受对手方按时交付、关键风险及其他条件影响并可能变化。季度为日历季度；首批精矿发运目标Q4 2026应继续用后续季报核验。",
        "images": [
            {
                "url": "img/finniss_restart_timeline_official.png",
                "src": "Core Lithium《Finniss Funding and Restart Presentation》2026-03-18，第10页（官方落地页；InvestorPA原ASX附件镜像取回）",
                "cap": "RESTART TIMELINE：Grants露天矿、BP33地下开发、选厂启动、首批精矿发运及满产路径（点击放大）"
            }
        ]
    },
    "Mt Holland": {
        "title": "Mt Holland 建设进度表（2023历史官方图）",
        "document": "WesCEF Investor Briefing and Site Tours",
        "date": "2023-03-23",
        "page": "PDF第67页（页脚66）",
        "source_url": "https://www.wesfarmers.com.au/docs/default-source/asx-announcements/wescef-investor-briefing-and-site-tours.pdf?sfvrsn=5cea1ebb_0",
        "summary": "Wesfarmers项目更新表列出2023年3月时点的状态、当前时序和资本成本：2021年7月开工、2022年12月首矿、选矿厂完成度超过85%并开始早期调试，原计划2023年底选矿厂首产、2025上半年Kwinana炼厂首产。",
        "note": "这是原项目建设阶段的历史图，不是2026扩产时间表。2026-07-22最新FID为精矿产能约380ktpa扩至约760ktpa，二号选矿厂预计2027H2开工、2030H1首批扩产精矿；最新扩产披露为文字公告，未找到独立甘特图。",
        "updates": [
            {"label": "2026-07-22 Mt Holland扩产FID公告", "url": "https://www.wesfarmers.com.au/docs/default-source/asx-announcements/mt-holland-lithium-expansion-final-investment-decision-20260721222532.pdf?sfvrsn=f024a8bb_0"}
        ],
        "images": [
            {
                "url": "img/mtholland_project_update_official.png",
                "src": "Wesfarmers《WesCEF Investor Briefing and Site Tours》2023-03-23，PDF第67页（页脚66）",
                "cap": "Project update：选矿厂/炼厂建设状态、当前时序与资本成本（2023历史快照，点击放大）"
            }
        ]
    }
}

for _mine in MINES:
    if _mine["mine"] in MILESTONE_TIMELINES:
        _mine["milestone_timeline"] = MILESTONE_TIMELINES[_mine["mine"]]







# ============ 历史数据（从更新后的 Excel 提取） ============
wb = openpyxl.load_workbook(SRC, data_only=True)
ws = wb["季度生产数据"]

# 季度列映射：列14=17Q1 ... 列53=26Q4；数据展示起点 2019Q1（列22）
QCOLS = list(range(22, 54))
def qlabel(c):
    q = c - 14
    return f"{2017 + q // 4}Q{q % 4 + 1}"

QUARTERS = [qlabel(c) for c in QCOLS]

def series(row):
    return [ws.cell(row, c).value for c in QCOLS]

# ============ Pilgangoora（PLS）历史数据 ============
# 100% 资产口径。来源：
#  - 飞书看板（官方口径，3Q2024-2Q2026 产量/销量）
#  - PLS March 2026 Quarterly Activities Report（26Q1：产量 232.4kt、销量 195.7kt、均价 US$1,867/t、FOB A$520/t；25Q4：208.0/232.0/1,161/585）
#  - PLS December 2022 QAR（22Q4：162.2kt/148.6kt/US$5,668/A$579；22Q3：147.1/138.2）
#  - PLS March 2020 QAR（20Q1：20.3kt/33.7kt）
#  - PLS FY25 AR：FY25 产量 754.6kt、FOB 成本 A$627/t；FY24 ~726kt
# 季度粒度缺口（2019-2022 部分季度、2023-2024H1）标 N.D.，年度列以官方年报为准
PLS_QUARTERS_START = "2019Q1"  # 与 Greenbushes 同起点
# 季度索引：2019Q1=0, ..., 26Q4=31
def pls_qidx(q):
    y, qq = int(q[:4]), int(q[5])
    return (y - 2019) * 4 + (qq - 1)

pls_prod = [None] * 32
pls_sales = [None] * 32
pls_price = [None] * 32
pls_cost = [None] * 32
pls_cif = [None] * 32
pls_ratio = [None] * 32

def _set(arr, q, v):
    arr[pls_qidx(q)] = v

# 官方披露的季度数据（万吨）
for q, p, s in [
    ("2020Q1", 2.03, 3.37),     # PLS Mar2020 QAR: 20,251dmt / 33,729dmt
    ("2022Q3", 14.71, 13.82),   # PLS Dec2022 QAR 对比列
    ("2022Q4", 16.22, 14.86),   # PLS Dec2022 QAR
    ("2023Q3", 14.42, 14.64),   # PLS FY24Q1 (Sep2023): 144,184 / 146,353 dmt（H1 FY24 合计 320,153 推算；2023-08 复产）
    ("2023Q4", 17.60, 15.99),   # PLS FY24Q2 (Dec2023 QAR): 175,969 / 159,897 dmt（官方）
    ("2024Q1", 17.90, 16.51),   # PLS FY24Q3 (Mar2024 QAR): 179,006 / 165,121 dmt（官方）
    ("2024Q2", 22.62, 23.58),   # PLS FY24Q4 (Jun2024 QAR): 226,169 / 235,762 dmt（官方）
    ("2024Q3", 22.01, 21.45),   # PLS FY25Q1 (Sep2024 QAR): 220,120 / 214,513 dmt（官方 2025-01-29 QAR 核实；原 19.44 为 SC6 误存）
    ("2024Q4", 18.82, 20.41),   # PLS FY25Q2 (Dec2024 QAR): 188,214 / 204,125 dmt（官方；原 16.62 为 SC6 误存）
    ("2025Q1", 12.50, 12.55),   # PLS FY25Q3 (Mar2025 QAR): 124,978 / 125,468 dmt（官方；原 11.04 为 SC6 误存）
    ("2025Q2", 22.13, 21.60),   # PLS Jun2026 QAR 附表 Jun-25 列（修订后）：221.272kt / 215.982kt（2026-08-11 用户确认按修订列更新）
    ("2025Q3", 22.48, 21.40),   # PLS Sep2025 QAR: 224.757kt / 214.025kt（官方；审计修正 2026-08-07 原 198.6/189.0 错位）
    ("2025Q4", 20.80, 23.20),   # PLS Dec2025 QAR: 208.022kt / 231.971kt（官方；审计修正）
    ("2026Q1", 23.24, 19.57),   # PLS Mar2026 QAR: 232.4kt / 195.7kt
    ("2026Q2", 21.43, 24.99),   # PLS Jun2026 QAR: 214.3kt / 249.9kt（官方实际品位）
    # 预测季度（26Q3E/26Q4E = FY27 指引 1,030-1,100kt 中值 1,065kt/年 → 26.6 万吨/季；Ngungaju 已重启的双厂口径）
    ("2026Q3", 26.6, None),
    ("2026Q4", 26.6, None),
]:
    _set(pls_prod, q, p)
    _set(pls_sales, q, s)
    if p and s:
        _set(pls_ratio, q, round(s / p, 3))

for q, p, c in [
    ("2022Q4", 5668, 579),   # PLS Dec2022 QAR: US$5,668/dmt (SC5.4 CIF), A$579 FOB
    ("2025Q3", 672, None),   # PLS Sep2025 QAR (FY26Q1): US$672/t (SC5.2 CIF China)
    ("2025Q4", 1488, None),  # PLS Dec2025 QAR (FY26Q2): US$1,488/t (SC5.2 CIF China)
    ("2026Q1", 1867, 520),   # PLS Mar2026 QAR
    ("2026Q2", 2107, 616),   # PLS Jun2026 QAR: US$2,107/t (SC5.2 CIF), A$616 FOB
]:
    _set(pls_price, q, p)
    _set(pls_cost, q, c)

# PLS 披露的 CIF 单位成本（A$/t，CIF China）——June 2026 QAR Jun/Mar 对比列 + March 2026 QAR Dec 列
for q, c in [
    ("2025Q4", 717),
    ("2026Q1", 733),
    ("2026Q2", 845),
]:
    _set(pls_cif, q, c)

# 年度口径（官方年报/季报，万吨）——年度列在页面以 SUM/手动标注，此处备用
pls_yearly = {
    "2019": 8.0, "2020": 20.6, "2021": 32.6, "2022": 36.2,
    "2023": 62.0, "2024": 72.6, "2025": 75.5, "2026": 88.0,
}  # 2026 = FY26 实际 879.5kt（June 2026 QAR 确认，超指引上限）

# ============ Wodgina（MRL 50% / Albemarle 50%，MRL 运营）============
# 口径：产量/销量统一为 100% 资产口径（官方 50% attributable 值 ×2；销售 100% 为推算）
# 官方 50% 口径数据（k dmt / k dmt SC6）：来源 = MRL 官方季报（子任务提取 + 飞书看板交叉验证）
wod_prod = [None] * 32   # 精矿产量（万吨，混合品位）
wod_sales = [None] * 32  # 销量（万吨，混合品位）
wod_price = [None] * 32  # 均价（US$/t，CIF SC6）
wod_cost = [None] * 32   # FOB 成本（A$/t SC6）
wod_ratio = [None] * 32

def wod_set(arr, q, v):
    arr[pls_qidx(q)] = v

# 历史锚点（100% 口径；2022Q2 复产首批精矿）
for q, p, s in [
    ("2019Q3", 2.2, 0.3),        # Q1FY20: 历史首批精矿 22k wmt / 3k wmt（100%；选矿厂 2019 年建成）
    ("2020Q1", 0.0, 0.0),        # care & maintenance（2019-11 起）
    ("2022Q3", 6.4, 6.6),        # Q1FY23: 64k/66k（100%），Train 2 爬坡
    ("2022Q4", 9.2, 9.5),        # Q2FY23: 92k/95k（100%）
    ("2023Q1", 8.8, 9.8),        # Q3FY23: 44k→100%≈88k / 49k→100%≈98k
    ("2023Q2", 10.25, 9.25),     # Q4FY23: 41k(40%)→100%≈102.5k / 37k(40%)→100%≈92.5k
    ("2023Q3", 22.6, 12.4),      # Q1FY24: 113k(100%) / 62k(100%)——Train 1 重启
    ("2023Q4", 23.0, 28.4),      # Q2FY24: 115k(100%) / 142k(100%)（50% 口径 55/65）
    ("2024Q2", 12.6, 12.4),      # Q4FY24: 63k(50%)→100%≈126k / 62k→100%≈124k
    ("2024Q3", 10.2, 9.2),       # Q1FY25: 51k→100%≈102k / 46k→100%≈92k
    ("2024Q4", 10.8, 12.2),      # Q2FY25: 54k→100%≈108k / 61k→100%≈122k
    ("2025Q1", 12.6, 11.8),      # Q3FY25: 63k→100%≈126k / 59k→100%≈118k
    ("2025Q2", 16.6, 13.6),      # Q4FY25: 83k→100%≈166k / 68k→100%≈136k（Sold 67）
    ("2025Q3", 17.6, 19.4),      # Q1FY26: 88k→100%≈176k / 97k→100%≈194k
    ("2025Q4", 17.0, 16.8),      # Q2FY26: 85k→100%≈170k / 84k→100%≈168k
    ("2026Q1", 15.6, 13.8),      # Q3FY26: 78k→100%≈156k / 69k→100%≈138k
    ("2026Q2", 18.8, 20.0),      # Q4FY26: 94k→100%≈188k / 100k→100%≈200k
    # 预测（26Q3E/26Q4E = FY26 销量 317k SC6 年化 ~40 万吨/年 混合品位；三线 Q1FY27 全开）
    ("2026Q3", 21.0, None),
    ("2026Q4", 21.0, None),
]:
    wod_set(wod_prod, q, p)
    wod_set(wod_sales, q, s)
    if p and s:
        wod_set(wod_ratio, q, round(s / p, 3))

# ===== 官方 SC6 覆盖（2026-08-11 用户要求：MRL 季报明确披露 Produced SC6/Sales SC6，必须用官方值）=====
# Wodgina 表格 50% attributable → ×2 = 100% SC6；来源 MRL Q1-Q4 FY26 季报 LITHIUM 表（Q4: 2026-07-29, Q3: 2026-04-30, Q2: 2026-01-29, Q1: 2025-10）
# Produced SC6 / Sales SC6（k dmt, 50%）：2025Q3(Q1FY26)=83/88、2025Q4(Q2FY26)=80/76、2026Q1(Q3FY26)=71/62、2026Q2(Q4FY26)=83/91
# FY25 年度 231/214k SC6（50%）→ 2025Q1/Q2 按 FY25 SC6/dmt 比例 0.92 折算；2024 及更早同比例（MRL FY25 起披露 SC6）
# FY25 各季官方/倒推（来源：Q1-Q4 FY26 季报"上年同期"列 + FY25 年度 231/214k 闭合倒推）
# 产 SC6（50%）：Q1FY25 60.7（倒推）、Q2FY25 37.3（倒推）、Q3FY25 56（官方）、Q4FY25 77（官方）
# 销 SC6（50%）：Q1FY25 61、Q2FY25 42、Q3FY25 52、Q4FY25 61（官方上年同期列；合计 216≈官方 214）
for _q, _p, _s in [("2024Q3", 12.1, 12.2), ("2024Q4", 7.5, 8.4),
                   ("2025Q1", 11.2, 10.4), ("2025Q2", 15.4, 12.2),
                   ("2025Q3", 16.6, 17.6), ("2025Q4", 16.0, 15.2),
                   ("2026Q1", 14.2, 12.4), ("2026Q2", 16.6, 18.2)]:
    wod_set(wod_prod, _q, round(_p, 2))
    wod_set(wod_sales, _q, round(_s, 2))
for _i in range(0, 22):   # 2021Q3-2024Q2（FY25 之前无官方 SC6 季度数据）按 FY25 官方 SC6/dmt 比例 0.92 折算；2024Q3 起用官方/倒推值（见上）
    if wod_prod[_i] is not None: wod_prod[_i] = round(wod_prod[_i] * 0.92, 2)
    if wod_sales[_i] is not None: wod_sales[_i] = round(wod_sales[_i] * 0.92, 2)
# 26Q3E/26Q4E：三线 Q1 FY27 全开满产 SC6 ≈ 83k×2 季度（官方 Q4 趋势）→ 17.0/17.3
wod_set(wod_prod, "2026Q3", 17.0); wod_set(wod_prod, "2026Q4", 17.3)
wod_set(wod_sales, "2026Q3", 17.0); wod_set(wod_sales, "2026Q4", 17.3)

for q, pr, c in [
    ("2024Q2", 1243, 949),   # Q4FY24: US$1,243 SC6 / A$949 FOB（50%）
    ("2024Q3", 842, 1217),   # Q1FY25
    ("2024Q4", 834, 868),    # Q2FY25
    ("2025Q1", 846, 775),    # Q3FY25
    ("2025Q2", 674, 641),    # Q4FY25
    ("2025Q3", 881, 733),    # Q1FY26
    ("2025Q4", 1140, 717),   # Q2FY26（CIF）
    ("2026Q1", 2130, 805),   # Q3FY26（CIF）
    ("2026Q2", 2450, 714),   # Q4FY26（CIF）
]:
    wod_set(wod_price, q, pr)
    wod_set(wod_cost, q, c)

# ============ Mt Marion（MRL 50% / Ganfeng 50%，MRL 运营）============
# 口径：产量 100%（官方 50%×2）；销量 100% 为推算（官方 51% 包销份额 /0.51；2022Q3 前官方按 100% 报告）
mar_prod = [None] * 32
mar_sales = [None] * 32
mar_price = [None] * 32
mar_cost = [None] * 32
mar_ratio = [None] * 32

def mar_set(arr, q, v):
    arr[pls_qidx(q)] = v

for q, p, s in [
    ("2019Q4", 12.4, 9.9),       # Q2FY20: 124k wmt / 99k wmt（100%）
    ("2020Q1", 11.6, 11.0),      # Q4FY20: 146 wmt→116 dmt / 114 wmt→110 dmt
    ("2020Q3", 13.3, 11.8),      # Q1FY21: 133k / 118k（100%）
    ("2021Q2", 11.4, 15.5),      # Q4FY21: 114k / 155k（100%）
    ("2021Q3", 10.1, 3.6),       # Q1FY22: 101k(100%) / 36k(51%)
    ("2021Q4", 9.8, 6.9),        # Q2FY22: 98k(100%) / 69k(51%)
    ("2022Q2", 12.8, 7.2),       # Q4FY22: 128k(100%) / 72k(51%)
    ("2022Q3", 10.8, 11.1),      # Q1FY23: 108k(100%) / 111k(100%)
    ("2022Q4", 12.1, 11.6),      # Q2FY23: 121k(100%) / 116k(100%)
    ("2023Q1", 12.0, 12.4),      # Q3FY23: 60k(50%)→100%≈120k / 62k(50%)→100%≈124k
    ("2023Q2", 12.0, 12.2),      # Q4FY23: 60k(50%)→100% / 61k(50%)→100%
    ("2023Q3", 12.8, 12.8),      # Q1FY24: 64k(50%)→100% / 64k(50%)→100%
    ("2023Q4", 16.6, 17.2),      # Q2FY24: 83k(50%)→100%≈166k / 86k(50%)→100%≈172k
    ("2024Q2", 17.8, 19.0),      # Q4FY24: 89k→100%≈178k / 95k→100%≈190k
    ("2024Q3", 13.6, 22.2),      # Q1FY25: 68k→100%≈136k / 111k→100%≈222k
    ("2024Q4", 11.6, 11.2),      # Q2FY25: 58k→100%≈116k / 56k→100%≈112k
    ("2025Q1", 14.0, 13.8),      # Q3FY25: 70k→100%≈140k / 69k→100%≈138k
    ("2025Q2", 12.4, 13.4),      # Q4FY25: 62k→100%≈124k / 67k→100%≈134k
    ("2025Q3", 14.6, 14.2),      # Q1FY26: 73k→100%≈146k / 71k→100%≈142k
    ("2025Q4", 16.2, 17.8),      # Q2FY26: 81k→100%≈162k / 89k→100%≈178k
    ("2026Q1", 16.0, 13.92),   # MRL 51% 承购 71k÷0.51=139.2k（审计修正 2026-08-07 原 ×2=142 错误）      # Q3FY26: 80k→100%≈160k / 71k→100%≈142k
    ("2026Q2", 16.4, 18.43),     # Q4FY26: 82k→100%≈164k / 94k÷0.51=184.3k（51% 承购换算，非 ×2——审计修正）
    # 预测（26Q3E/26Q4E = FY26 销量 242k SC6 年化 ~30 万吨/年 混合品位；浮选厂在建 2027 投产）
    ("2026Q3", 16.5, None),
    ("2026Q4", 16.5, None),
]:
    mar_set(mar_prod, q, p)
    mar_set(mar_sales, q, s)
    if p and s:
        mar_set(mar_ratio, q, round(s / p, 3))

# ===== 官方 SC6 覆盖（2026-08-11：MRL 季报 Produced SC6/Sales SC6）=====
# Marion 产 50% → ×2；销 51% → ÷0.51；来源 MRL Q1-Q4 FY26 季报（产 SC6 k dmt：Q1FY26=52、Q2FY26=59、Q3FY26=57、Q4FY26=59；销 SC6(51%)：55/67/53/67）
# FY25 官方 SC6/dmt = 180/257 = 0.70 → 2025Q1/Q2 及更早 ×0.70
# FY25 各季官方/倒推（产 50%×2、销 51%÷0.51）
# 产 SC6（50%）：Q1FY25 39.6（倒推）、Q2FY25 43.4（倒推）、Q3FY25 52（官方）、Q4FY25 45（官方）
# 销 SC6（51%）：Q1FY25 54、Q3FY25 53、Q4FY25 54（Q1/Q3/Q4 FY26 上年同期列）；Q2FY25 = FY25 年度 223-161 = 62k 闭合倒推
for _q, _p, _s in [("2024Q3", 7.9, 10.6), ("2024Q4", 8.7, 12.2),
                   ("2025Q1", 10.4, 10.4), ("2025Q2", 9.0, 10.6),
                   ("2025Q3", 10.4, 10.8), ("2025Q4", 11.8, 13.1),
                   ("2026Q1", 11.4, 10.4), ("2026Q2", 11.8, 13.1)]:
    mar_set(mar_prod, _q, round(_p, 2))
    mar_set(mar_sales, _q, round(_s, 2))
for _i in range(0, 22):   # 2021Q3-2024Q2 按 FY25 官方 SC6/dmt 比例 0.70 折算；2024Q3 起用官方/倒推值（见上）
    if mar_prod[_i] is not None: mar_prod[_i] = round(mar_prod[_i] * 0.70, 2)
    if mar_sales[_i] is not None: mar_sales[_i] = round(mar_sales[_i] * 0.70, 2)
# 26Q3E/26Q4E：DMS 稳态满产 SC6（FY26 227k×2=45.4 万吨/年 → 季均 11.4；浮选 2027 中投产）→ 11.6/11.8
mar_set(mar_prod, "2026Q3", 11.6); mar_set(mar_prod, "2026Q4", 11.8)
mar_set(mar_sales, "2026Q3", 11.6); mar_set(mar_sales, "2026Q4", 11.8)

for q, pr, c in [
    ("2022Q3", 3262, None),  # Q1FY23（重述）
    ("2022Q4", 4151, None),  # Q2FY23
    ("2023Q2", 2589, None),  # Q4FY23
    ("2023Q4", 1060, 844),   # Q2FY24（1H24 成本）
    ("2024Q2", 1139, 683),   # Q4FY24
    ("2024Q3", 813, 1020),   # Q1FY25
    ("2024Q4", 816, 1176),   # Q2FY25
    ("2025Q1", 845, 708),    # Q3FY25
    ("2025Q2", 607, 717),    # Q4FY25
    ("2025Q3", 797, 796),    # Q1FY26
    ("2025Q4", 1042, 812),   # Q2FY26（CIF）
    ("2026Q1", 2076, 903),   # Q3FY26（CIF）
    ("2026Q2", 2392, 878),   # Q4FY26（CIF）
]:
    mar_set(mar_price, q, pr)
    mar_set(mar_cost, q, c)

# ============ Kathleen Valley（Liontown Resources，ASX: LTR）============
# 口径：100% 资产口径（Liontown 全资拥有运营）；官方按实际品位 dmt 披露，看板 SC6e 交叉验证
kv_prod = [None] * 32   # 精矿产量（万吨，实际品位 dmt）
kv_sales = [None] * 32  # 销量（万吨，实际品位 dmt）
kv_price = [None] * 32  # 均价（US$/t SC6e）
kv_cost = [None] * 32   # 单位成本 FOB（A$/t sold）
kv_ratio = [None] * 32

def kv_set(arr, q, v):
    arr[pls_qidx(q)] = v

# 历史数据（2024-07 投产；官方季报 + 飞书看板交叉验证）
for q, p, s in [
    ("2024Q3", 3.0, 1.0),       # 投产首季（2024-07 首产）：看板 25 kt SC6e → ~30kt dmt（SC~5.0）
    ("2024Q4", 9.2, 8.5),       # 看板 76.9 SC6e → ~92kt dmt / 销量 70.5 SC6e → ~85kt
    ("2025Q1", 9.6, 9.4),       # Q3 FY25 官方: 95,709 dmt / 93,940 dmt
    ("2025Q2", 8.6, 9.7),       # Q4 FY25 官方: 85,892 / 97,330
    ("2025Q3", 8.7, 7.7),       # Q1 FY26 官方: 87,172 / 77,474
    ("2025Q4", 10.5, 11.2),     # Q2 FY26 官方: 105,342 / 112,122
    ("2026Q1", 9.6, 8.4),       # Q3 FY26 官方: 96,367 / 83,912
    ("2026Q2", 10.3, 10.8),     # Q4 FY26 官方: 103,111 / 108,489
    # 预测（26Q3E/26Q4E = FY26 产量 392k dmt 年化 ~40 万吨，地下开发 2.8Mtpa 爬坡中）
    ("2026Q3", 10.8, None),
    ("2026Q4", 11.2, None),
]:
    kv_set(kv_prod, q, p)
    kv_set(kv_sales, q, s)
    if p and s:
        kv_set(kv_ratio, q, round(s / p, 3))

for q, pr, c in [
    ("2025Q1", 815, 702),    # Q3 FY25: US$815 SC6e / A$702 FOB
    ("2025Q2", 740, 898),    # Q4 FY25: US$740 / A$898
    ("2025Q3", 700, 1093),   # Q1 FY26: US$700 / A$1,093
    ("2025Q4", 900, 910),    # Q2 FY26: US$900 / A$910
    ("2026Q1", 1845, 981),   # Q3 FY26: US$1,845 / A$981
    ("2026Q2", 1880, 995),   # Q4 FY26: US$1,880 / A$995
]:
    kv_set(kv_price, q, pr)
    kv_set(kv_cost, q, c)

# ============ Bald Hill（MRL 100% 拥有，2026-05 复产）============
# 口径：100% 资产口径（MRL 全资）；产量按混合品位 dmt（MRL 披露 mixed + SC6 双值）
bh_prod = [None] * 32   # 精矿产量（万吨，混合品位 dmt）
bh_sales = [None] * 32  # 销量（万吨，混合品位 dmt）
bh_price = [None] * 32  # 均价（US$/t SC6）
bh_cost = [None] * 32   # 单位成本 FOB（A$/t SC6）
bh_ratio = [None] * 32

def bh_set(arr, q, v):
    arr[pls_qidx(q)] = v

# 历史数据（2024-11 C&M 前 MRL 运营期 FY25 估算 + 2026-05 复产）
# FY25 官方（2024Q3-2025Q2）：产 63k mixed / 销 70k（MRL FY25 Q1/Q2 QAR 可还原季度：产 38/25/0/0 kt、销 43/27/0/0 kt——审计修正 2026-08-07，原全年均分误作逐季实际）
for q, p, s in [
    ("2024Q3", 3.8, 4.3),       # FY25 Q1（MRL Q1 FY25 QAR：38k mixed / 43k）
    ("2024Q4", 2.5, 2.7),       # FY25 Q2（MRL Q2 FY25 QAR：25k / 27k）
    ("2025Q1", 0.0, 0.0),       # FY25 Q3：停产（MRL 披露 0）
    ("2025Q2", 0.0, 0.0),       # FY25 Q4：停产
    ("2025Q3", 0.0, 0.0),       # 2024-11 C&M 停产
    ("2025Q4", 0.0, 0.0),       # C&M
    ("2026Q1", 0.0, 0.0),       # C&M（2026-05-18 宣布复产）
    ("2026Q2", 0.1, 0.0),       # 2026-06 首产精矿 1k dmt；销量 0（2026-07 首批发运）
    # 预测：26Q3E 爬坡中（首批 Esperance 发运 Q1 FY27）、26Q4E 满产 140k SC6/年 = 3.5 万吨/季
    ("2026Q3", 2.0, 1.8),       # Q1 FY27 爬坡 + 首批发运
    ("2026Q4", 4.1, 4.0),       # Q2 FY27 满产 140k dmt SC6（≈165k mixed）目标
]:
    bh_set(bh_prod, q, p)
    bh_set(bh_sales, q, s)
    if p and s:
        bh_set(bh_ratio, q, round(s / p, 3))

# ===== 官方 SC6 覆盖（2026-08-11：MRL 季报 Produced SC6/Sales SC6，100% basis）=====
# BH FY25 产 SC6 54k（38/25k dmt → 3.3/2.2 万吨 SC6）；FY25 SC6/dmt = 54/63 = 0.86；2026Q2 产 1k SC6 ✓ 已对
bh_set(bh_prod, "2024Q3", 3.3); bh_set(bh_sales, "2024Q3", 3.7)   # FY25 销 SC6 59k 拆分（43×0.86）
bh_set(bh_prod, "2024Q4", 2.2); bh_set(bh_sales, "2024Q4", 2.3)   # 27×0.86
# 26Q3E/26Q4E：爬坡 → Q2 FY27 满产 140k SC6 = 3.5/季（原 4.1 dmt ≈ 3.5 SC6）
bh_set(bh_prod, "2026Q3", 1.7); bh_set(bh_sales, "2026Q3", 1.5)
bh_set(bh_prod, "2026Q4", 3.5); bh_set(bh_sales, "2026Q4", 3.5)

for q, pr, c in [
    ("2024Q3", 808, 1148),   # MRL Q1 FY25 QAR：US$808 SC6 / FOB A$1,148
    ("2024Q4", 808, 1148),   # MRL Q2 FY25 QAR（FY25 全年均价）
    # 2025Q1-2026Q2 停产/复产期无销售 → 无价格/成本
]:
    bh_set(bh_price, q, pr)
    bh_set(bh_cost, q, c)

# ============ Mt Cattlin（力拓 Rio Tinto 100%，2025 收购自 Arcadium）============
# 口径：100% 资产口径（力拓全资）；产量为锂辉石精矿（dmt，SC5.5-6%）
mc_prod = [None] * 32   # 精矿产量（万吨）
mc_sales = [None] * 32  # 销量（万吨）
mc_price = [None] * 32  # 均价（US$/t SC6）
mc_cost = [None] * 32   # 单位成本 FOB（A$/t）
mc_ratio = [None] * 32

def mc_set(arr, q, v):
    arr[pls_qidx(q)] = v

# 历史数据（2019-2025；Galaxy→Allkem→Arcadium→力拓；季度数据以官方季报为准，缺失标 N.D.）
# 年度锚点（NI 43-101 Table 6-1 + Allkem/Arcadium 季报）：2019=19.16、2020=10.87、2021=12.77、2022=10.74、FY23=13.20
for q, p, s in [
    ("2019Q1", 4.8, 4.8),       # Galaxy 季报估算（年度 191.6kt ÷ 4；实际季度有波动）
    ("2019Q2", 4.8, 4.8),
    ("2019Q3", 4.8, 4.8),
    ("2019Q4", 4.8, 4.8),
    ("2020Q1", 2.7, 2.7),       # 2020 年 108.7kt ÷ 4（估算）
    ("2020Q2", 2.7, 2.7),
    ("2020Q3", 2.7, 2.7),
    ("2020Q4", 2.7, 2.7),
    ("2021Q1", 3.2, 3.2),       # 2021 年 127.7kt ÷ 4（估算）
    ("2021Q2", 3.2, 3.2),
    ("2021Q3", 3.2, 3.2),
    ("2021Q4", 3.2, 3.2),
    ("2022Q1", 2.7, 2.7),       # 2022 年 107.4kt ÷ 4（估算）
    ("2022Q2", 2.7, 2.7),
    ("2022Q3", 2.7, 2.7),
    ("2022Q4", 2.7, 2.7),
    ("2023Q1", 3.3, 3.3),       # Allkem FY23 产量 131.99kt → 日历 2023 均分估算（无逐季披露）
    ("2023Q2", 3.3, 3.3),
    ("2023Q3", 3.3, 3.3),
    ("2023Q4", 3.3, 3.3),
    ("2024Q1", None, None),       # Arcadium FY2024 未披露季度产量；Q1+Q2 销量合计 53.5kt 未拆分（10-K）——不均分（审计修正 2026-08-07）
    ("2024Q2", None, None),
    ("2024Q3", None, 3.2),        # Arcadium 10-K 销量：2024Q3 ≈32.4kt（产量未披露 → N.D.，不得填销量入产量行）
    ("2024Q4", None, 5.4),        # Arcadium 10-K 销量：2024Q4 ≈54.1kt（产量未披露）
    # 2025 年：2025 H1 为 Rio 收购后合并期（Q2 2026 Operations Review 口径：H1 合计产 9.1kt、第三方发运 22.6kt——季度无法拆分，保留合并期 N.D. + 注记）；2025Q3 起 C&M
    ("2025Q3", 0.0, 0.0),       # 2025 年进入 C&M（力拓官网确认，因锂价下降）
    ("2025Q4", 0.0, 0.0),
    ("2026Q1", 0.0, 0.0),
    ("2026Q2", 0.0, 0.0),
    ("2026Q3", 0.0, 0.0),   # 26Q3E/26Q4E = 0（C&M 延续预估，用户规范 2026-08-07：季报未出的矿山也需预估；依据：力拓 C&M 无复产公告）
    ("2026Q4", 0.0, 0.0),
]:
    mc_set(mc_prod, q, p)
    mc_set(mc_sales, q, s)

# ============ Finniss（Core Lithium CXO 100%，2023 投产/2024 C&M/2026-05 重启）============
# 口径：100% 资产口径；产量为锂辉石精矿（dmt，SC6 等效）
fn_prod = [None] * 32   # 精矿产量（万吨）
fn_sales = [None] * 32  # 销量（万吨）
fn_price = [None] * 32  # 均价（US$/t SC6）
fn_cost = [None] * 32   # 单位成本 FOB（A$/t）
fn_ratio = [None] * 32

def fn_set(arr, q, v):
    arr[pls_qidx(q)] = v

# 历史数据（2023 投产起；2024 年中 C&M；2026-05 重启）
# 2023 年（投产年）：2023-02 首产、2023-05 首运；FY24（2023Q3-2024Q2）产 95,020 dmt → 季度估算
for q, p, s in [
    ("2023Q1", 0.3, 0.3),       # 2023-02/03 首产（Grants 爬坡初期，估算）
    ("2023Q2", 1.2, 1.0),       # 2023-05 首运（估算）
    ("2023Q3", 1.8, 1.8),       # FY24 H1 爬坡（估算）
    ("2023Q4", 2.2, 2.2),
    ("2024Q1", 1.8, 1.8),       # 2024 年锂价下跌、减产（估算）
    ("2024Q2", 1.3, 1.3),       # 2024 年中暂停采矿加工（估算，2024-09-08 最后一船）
    # 2024Q3 起 C&M（2024 年暂停；2024-09-08 Darwin 港最后一船后停产）
    ("2024Q3", 0.0, 0.0),
    ("2024Q4", 0.0, 0.0),
    ("2025Q1", 0.0, 0.0),       # C&M + 重启研究
    ("2025Q2", 0.0, 0.0),
    ("2025Q3", 0.0, 0.0),
    ("2025Q4", 0.0, 0.0),
    ("2026Q1", 0.0, 0.0),       # 2026-03-18 FID（重启准备）
    ("2026Q2", 0.0, 0.51),      # 新产精矿 0（Grants 5 月恢复采矿，26Q3 才处理）；销量 = 库存精矿发运 5.1kdmt（另 20kt 锂细粉）——审计修正 2026-08-07
]:
    fn_set(fn_prod, q, p)
    fn_set(fn_sales, q, s)
fn_set(fn_price, "2026Q2", 2023)  # 库存精矿成交 US$2,023/dmt SC6e CIF（Core stockpile concentrate sale 2026-02-26 公告；审计修正）

# ============ Manna（Global Lithium GL1 100%，未投产/开发阶段）============
# 口径：100% 资产口径；未投产——历史无产量，预测季度 2027 年起（DSO Q2 2027 + 精矿 mid-2027）
mn_prod = [None] * 32   # 精矿产量（万吨）
mn_sales = [None] * 32  # 销量（万吨）
mn_price = [None] * 32  # 均价（US$/t SC6）
mn_cost = [None] * 32   # 单位成本 FOB（A$/t）
mn_ratio = [None] * 32

def mn_set(arr, q, v):
    arr[pls_qidx(q)] = v

# 历史：未投产（2021-11 收购、2022-2024 勘探/DFS、2025 DFS/ML、2026 MDCP/FID 准备）——2026Q2 前全 N.D./0
# 预测：26Q3/26Q4 建设期（FID Q4 2026）→ 0；27Q1 建设 → 0；27Q2 DSO 首批（无精矿）；27Q3 起精矿爬坡
# 26Q1/26Q2 推测 = 0（用户规范 2026-08-07：未披露季度也按投产进度推测——Manna 未投产（MDCP 2026-08-04 批、FID Q4 2026、首产 mid-2027）→ 无精矿产出）
for q, p, s in [
    ("2026Q1", 0.0, 0.0),   # 推测 0：未投产（FID 未通过、无开采/选矿）
    ("2026Q2", 0.0, 0.0),   # 推测 0：未投产（MDCP 2026-08-04 才获批）
    ("2026Q3", 0.0, 0.0),   # FID 目标 Q4 2026——建设前
    ("2026Q4", 0.0, 0.0),   # FID + 建设启动
]:
    mn_set(mn_prod, q, p)
    mn_set(mn_sales, q, s)

# ============ Mt Holland（Covalent Lithium：SQM 50% + Wesfarmers 50%）============
# 口径（2026-08-07 审计修正）：产量行=官方季度产量（SQM 不披露 → 全 N.D.）；销量行=SQM 50% 份额 SC6 销量 ×2 = 100% 估算（已标注）
mh_prod = [None] * 32   # 产量（万吨，100% dmt SC5.5）——SQM 不披露季度产量，保持 None（N.D.）
mh_sales = [None] * 32  # 销量（万吨，SQM 50% 份额 SC6 ×2 = 100% 估算）
mh_price = [None] * 32  # 均价（US$/t SC6；FOB/CIF 未披露 → N.D.）
mh_cost = [None] * 32   # 单位成本 FOB（A$/t）——SQM 未披露 → 全 N.D.，页面已删除该行
mh_ratio = [None] * 32

def mh_set(arr, q, v):
    arr[pls_qidx(q)] = v

# 年度产量（SQM 20-F FY2025，官方 100% 项目口径，dmt SC5.5）：2023=15.0kt、2024=232.4kt、2025=329.6kt（2025 达名义产能 383ktpa 的 86%）——见 ④ 历史表年度注记
# 季度销量（SQM 美式季报披露 50% 份额 SC6 销量 ×2 = 100% 估算；⚠️ 不得填入产量行）：
for q, s in [
    ("2025Q1", 3.66),    # SQM 1Q2025 18.3kt（50%）×2
    # 2025Q2/Q3：SQM 未单独披露 SC 销量（标 N.D.）
    ("2025Q4", 13.46),  # SQM 4Q2025 67.3kt（50%）×2
    ("2026Q1", 7.62),    # SQM 1Q2026 38.1kt（50%）×2
]:
    mh_set(mh_sales, q, s)
mh_set(mh_price, "2026Q1", 1461)  # SQM 1Q2026 实现均价 US$1,461/t SC6（+72% yoy；FOB/CIF 未披露 → 标 N.D.）
# 26Q1-26Q4E 满产预估（用户规范 2026-08-07：季报未披露的矿山也需预估今年/明年产量并备注依据，同步总览汇总）
# 依据：SQM 2026Q1 确认矿山满产运营（'operating at full capacity'）+ 名义产能 383ktpa ÷ 4 ≈ 9.58 万吨/季（100% dmt SC5.5）+ 2026-07-21 扩产 FID 再确认满产状态
# 26Q1/26Q2 为推测（SQM 不披露季度产量，按满产推算）；26Q3E/26Q4E 为预测
for _q in ["2026Q1", "2026Q2", "2026Q3", "2026Q4"]:
    mh_set(mh_prod, _q, 9.5)

# ============ 资本开支（主页 capex 表；口径：矿山/项目级，财年 6/30 为主，100% 优先；2026E/2027E 为指引或 FID 计划）============
# 单位：亿澳元（A$100M = 1.0）；披露为份额/公司级时在 unit 标注
CAPEX = {
    "Greenbushes": {"2024": 8.96, "unit": "IGO 锂业务（GB+Kwinana）100% 口径，FY24 披露 $896M；GB 单矿 N.D."},
    "Pilgangoora": {"2023": 4.08, "2024": 8.65, "2025": 3.15, "2026E": 3.28, "2027E": 1.75,
                    "unit": "PLS 公司级（P680/P1000 建设 FY23-24 峰值）；2027E=P2000 pre-FID $175M（2026-06 批准）"},
    "Wodgina": {"2025": 1.35, "2026E": 1.60, "unit": "MRL 披露；2026E=1H26 $80M×2 年化；三线口径（MinRes 50% / Albemarle 50%）"},
    "Mt Marion": {"2025": 1.23, "2026E": 0.24, "2027E": 2.45,
                  "unit": "MRL 披露（2026E=1H26 $12M×2）；2027E=浮选+地下 FID $490M（2026-05-26，FY27-28 投入）"},
    "Kathleen Valley": {"2026E": 1.14, "unit": "Liontown；FY26 $114M（excl. $14M early works）；建设期 FY23-24 峰值后回落；2027E 指引待核实"},
    "Bald Hill": {"2025": 0.52, "2026E": 0.20, "unit": "MRL 披露（FY25 关停期维持）；2026E=重启 capex $20M（2026-05 公告）"},
    "Mt Cattlin": {"2025": 0.0, "2026E": 0.0, "unit": "力拓 2025-03 收购后 C&M——无资本开支；2022-24 为 Arcadium 披露（未提取）"},
    "Finniss": {"2024": 0.61, "2025": 0.0, "2026E": 0.0, "2027E": 1.0,
                "unit": "Core 年报（FY24 $60.6M 建设/投产期）；2025-26 C&M 无；2027E=重启 FID 后 pre-production 资本部署（研究性）"},
    "Manna": {"2026E": 0.10, "2027E": 2.20, "unit": "GL1 开发支出（季度现金流出）；2027E=DFS 计划 capex A$439.1M 的 FID 后首年部分（研究性拆分）"},
    "Mt Holland": {"2027E": 3.25, "unit": "Covalent 建设期 capex 在 SQM 20-F（份额口径，未逐季拆分）；2027E=扩产 FID 的 SQM 50% 份额 A$645-715M 首年部分（2027 H2 开工，研究性）"},
}

data = {
    "meta": {
        "title": "永安期货 · 澳洲锂矿季度汇总",
        "updated": "2026-08-05",
        "data_quarters": {"start": "2019Q1", "end_actual": "26Q2", "end_forecast": "26Q4"},
        "unit_note": "产量/销量/库存单位为万吨；均价 US$/t；成本 A$/t",
        "color_legend": "浅色柱/空心圆=预测季度（按官方 FY27 指引中值推算）；灰色 N.D.=官方未披露",
        "disclaimer": "本页面数据来自各矿山母公司官方季度报告，仅供研究参考，不构成投资建议。",
        "pages": [
            {"key": "Overview", "label": "总览", "file": "overview.html"},
            {"key": "Greenbushes", "label": "1 Greenbushes", "file": "index.html"},
            {"key": "Pilgangoora", "label": "2 Pilgangoora", "file": "pilgangoora.html"},
            {"key": "Wodgina", "label": "3 Wodgina", "file": "wodgina.html"},
            {"key": "Mt Marion", "label": "4 Mt Marion", "file": "marion.html"},
            {"key": "Kathleen Valley", "label": "5 Kathleen Valley", "file": "kathleenvalley.html"},
            {"key": "Bald Hill", "label": "6 Bald Hill", "file": "baldhill.html"},
            {"key": "Mt Cattlin", "label": "7 Mt Cattlin", "file": "mtcattlin.html"},
            {"key": "Finniss", "label": "8 Finniss", "file": "finniss.html"},
            {"key": "Manna", "label": "9 Manna", "file": "manna.html"},
            {"key": "Mt Holland", "label": "10 Mt Holland", "file": "mtholland.html"},
        ]
    },
    "mines": MINES,
    "capex": CAPEX,
    "quarters": QUARTERS,
    "history": {
        "production": series(9),
        "lce": series(10),
        "tech_grade": series(11),
        "chem_grade": series(12),
        "sales": series(13),
        "inv_change": series(14),
        "inventory": series(15),
        "prod_sales_ratio": series(16),
        "avg_price": series(17),
        "cost_with_royalty": series(18),
        "cost_no_royalty": series(19),
        "cash_cost": series(20),
    },
    "history_labels": [
        ("production", "精矿产量（万吨，SC6 折算 6% Li₂O）"),
        ("tech_grade", "技术级精矿产量（万吨，实际品位）"),
        ("chem_grade", "化学级精矿产量（万吨，实际品位）"),
        ("sales", "销量（万吨，SC6 折算 6% Li₂O）"),
        ("inv_change", "库存变动量（万吨）"),
        ("inventory", "库存（万吨）"),
        ("prod_sales_ratio", "产销比"),
        ("avg_price", "平均售价（US$/t，SC6）"),
        ("cost_with_royalty", "单位成本—含权益金（A$/t，FOB SC6）"),
        ("cost_no_royalty", "单位成本—不含权益金（A$/t，FOB SC6）"),
        ("cash_cost", "cash cost（A$/t，FOB SC6）"),
    ],
    "pilgangoora": {
        "quarters": QUARTERS,
        "history": {
            "production": pls_prod,
            "lce": [None] * 32,
            "tech_grade": [None] * 32,
            "chem_grade": [None] * 32,
            "sales": pls_sales,
            "inv_change": [None] * 32,
            "inventory": [None] * 32,
            "prod_sales_ratio": pls_ratio,
            "avg_price": pls_price,
            "cost_with_royalty": pls_cost,
            "cost_no_royalty": [None] * 32,
            "cash_cost": pls_cost,
            "cif_cost": pls_cif,
        },
        "yearly": pls_yearly,
    },
    "wodgina": {
        "quarters": QUARTERS,
        "history": {
            "production": wod_prod,
            "lce": [None] * 32,
            "tech_grade": [None] * 32,
            "chem_grade": [None] * 32,
            "sales": wod_sales,
            "inv_change": [None] * 32,
            "inventory": [None] * 32,
            "prod_sales_ratio": wod_ratio,
            "avg_price": wod_price,
            "cost_with_royalty": wod_cost,
            "cost_no_royalty": [None] * 32,
            "cash_cost": wod_cost,
            "cif_cost": [None] * 32,
        },
        "yearly": {"2020": 0.0, "2022": 16.2, "2023": 74.1, "2024": 64.4, "2025": 75.5, "2026": 68.7},
    },
    "marion": {
        "quarters": QUARTERS,
        "history": {
            "production": mar_prod,
            "lce": [None] * 32,
            "tech_grade": [None] * 32,
            "chem_grade": [None] * 32,
            "sales": mar_sales,
            "inv_change": [None] * 32,
            "inventory": [None] * 32,
            "prod_sales_ratio": mar_ratio,
            "avg_price": mar_price,
            "cost_with_royalty": mar_cost,
            "cost_no_royalty": [None] * 32,
            "cash_cost": mar_cost,
            "cif_cost": [None] * 32,
        },
        "yearly": {"2020": 42.4, "2021": 45.4, "2022": 48.6, "2023": 46.6, "2024": 54.2, "2025": 52.8, "2026": 61.0},
    },
    "kathleenvalley": {
        "quarters": QUARTERS,
        "history": {
            "production": kv_prod,
            "lce": [None] * 32,
            "tech_grade": [None] * 32,
            "chem_grade": [None] * 32,
            "sales": kv_sales,
            "inv_change": [None] * 32,
            "inventory": [None] * 32,
            "prod_sales_ratio": kv_ratio,
            "avg_price": kv_price,
            "cost_with_royalty": kv_cost,
            "cost_no_royalty": [None] * 32,
            "cash_cost": kv_cost,
            "cif_cost": [None] * 32,
        },
        "yearly": {"2024": 12.2, "2025": 29.5, "2026": 39.2},
    },
    "baldhill": {
        "quarters": QUARTERS,
        "history": {
            "production": bh_prod,
            "lce": [None] * 32,
            "tech_grade": [None] * 32,
            "chem_grade": [None] * 32,
            "sales": bh_sales,
            "inv_change": [None] * 32,
            "inventory": [None] * 32,
            "prod_sales_ratio": bh_ratio,
            "avg_price": bh_price,
            "cost_with_royalty": bh_cost,
            "cost_no_royalty": [None] * 32,
            "cash_cost": bh_cost,
            "cif_cost": [None] * 32,
        },
        "yearly": {"2024": 3.2, "2025": 6.3, "2026": 0.1},
    },
    "mtcattlin": {
        "quarters": QUARTERS,
        "history": {
            "production": mc_prod,
            "lce": [None] * 32,
            "tech_grade": [None] * 32,
            "chem_grade": [None] * 32,
            "sales": mc_sales,
            "inv_change": [None] * 32,
            "inventory": [None] * 32,
            "prod_sales_ratio": mc_ratio,
            "avg_price": mc_price,
            "cost_with_royalty": mc_cost,
            "cost_no_royalty": [None] * 32,
            "cash_cost": mc_cost,
            "cif_cost": [None] * 32,
        },
        "yearly": {"2019": 19.2, "2020": 10.9, "2021": 12.8, "2022": 10.7, "2023": 13.2, "2024": 14.0, "2025": 0.0, "2026": 0.0},
    },
    "finniss": {
        "quarters": QUARTERS,
        "history": {
            "production": fn_prod,
            "lce": [None] * 32,
            "tech_grade": [None] * 32,
            "chem_grade": [None] * 32,
            "sales": fn_sales,
            "inv_change": [None] * 32,
            "inventory": [None] * 32,
            "prod_sales_ratio": fn_ratio,
            "avg_price": fn_price,
            "cost_with_royalty": fn_cost,
            "cost_no_royalty": [None] * 32,
            "cash_cost": fn_cost,
            "cif_cost": [None] * 32,
        },
        "yearly": {"2023": 5.5, "2024": 3.1, "2025": 0.0, "2026": 0.0},
    },
    "manna": {
        "quarters": QUARTERS,
        "history": {
            "production": mn_prod,
            "lce": [None] * 32,
            "tech_grade": [None] * 32,
            "chem_grade": [None] * 32,
            "sales": mn_sales,
            "inv_change": [None] * 32,
            "inventory": [None] * 32,
            "prod_sales_ratio": mn_ratio,
            "avg_price": mn_price,
            "cost_with_royalty": mn_cost,
            "cost_no_royalty": [None] * 32,
            "cash_cost": mn_cost,
            "cif_cost": [None] * 32,
        },
        "yearly": {},
    },
    "mtholland": {
        "quarters": QUARTERS,
        "history": {
            "production": mh_prod,
            "lce": [None] * 32,
            "tech_grade": [None] * 32,
            "chem_grade": [None] * 32,
            "sales": mh_sales,
            "inv_change": [None] * 32,
            "inventory": [None] * 32,
            "prod_sales_ratio": mh_ratio,
            "avg_price": mh_price,
            "cost_with_royalty": mh_cost,
            "cost_no_royalty": [None] * 32,
            "cash_cost": mh_cost,
            "cif_cost": [None] * 32,
        },
        "yearly": {"2023": 1.50, "2024": 23.24, "2025": 32.96},  # 20-F 官方 100% 项目产量（dmt SC5.5）
    },
}

# ============ 线性增长预测覆写（用户规范 2026-08-06） ============
# 26Q3E/26Q4E：从 26Q2 实际（A）等差爬坡到 FY27 指引季均/满产季均（B），n 步等差（默认 2 步）
# 2027 年度预期：27Q1-27Q4 线性季度序列求和（27Q1/27Q2 = B（FY27 指引期），27Q3/27Q4 线性延至 cap）
LIN = {
    "history": {"A": 38.7, "B": 41.25, "cap": 43.5},   # GB：26Q2=38.7 → FY27 指引中值 165/4=41.25 → CGP 满产 43.5
    "pilgangoora": {"A": 23.24, "B": 26.6, "cap": 27.5},
    "wodgina": {"A": 16.6, "B": 17.3, "cap": 17.3},   # 2026-08-11 官方 SC6：Q4 产 83k×2=16.6 → 三线全开满产 ~17.3/季 SC6（原 dmt 18.75）
    "marion": {"A": 11.8, "B": 11.8, "cap": 11.8},   # 2026-08-11 官方 SC6：Q4 产 59k×2=11.8（原 dmt 16.4；Marion 实际品位 4.3-4.5% 非 5.5%）
    "kathleenvalley": {"A": 10.3, "B": 10.4, "cap": 10.6},
    "baldhill": {"A": 0.1, "B": 3.5, "cap": 3.5},
    "finniss": {"A": 0.5, "B": 4.0, "cap": 5.1, "steps": 4},   # 首产矿山：4 步等差爬坡
    "manna": None,        # 未投产：2026 年保持 0（FID Q4 26 → 首产 2027 年中）
    "mtholland": None,    # 26Q3E/26Q4E N.D.（SQM 美式财季 Q2 2026 报告未发布）
}
for key, p in LIN.items():
    if not p or p.get("A") is None:
        continue
    A, B, cap = p["A"], p["B"], p["cap"]
    n = p.get("steps", 2)
    h = data[key]["production"] if key == "history" else data[key]["history"]["production"]
    # 只有 26Q3E/26Q4E 两个预测位置：26Q3E = 第 1 步、26Q4E = 第 2 步（n 步等差爬坡）
    h[30] = round(A + (B - A) * 1 / n, 2)
    h[31] = round(A + (B - A) * 2 / n, 2)

# 2027 年度预期（线性）：悲观 = 爬坡慢 1 季（Q3E + 3×B）、基准 = 线性序列、乐观 = 提前满产（cap）
FC27 = {
    "history":         {"bear": 164, "base": 168, "bull": 173, "q": [41.25, 41.25, 42.5, 43.5]},
    "pilgangoora":     {"bear": 106, "base": 109.7, "bull": 112.5, "q": [26.6, 26.6, 28.25, 28.25]},   # 2026-08-11：27Q3/27Q4 上调至 28.25（FY28 双厂稳态 ~90%——Ngungaju 满产、爬坡拖累消失；用户指出年末可接近满产）；bull=90% 满产 112.5
    "wodgina":         {"bear": 64.0, "base": 67.0, "bull": 72.0, "q": [16.7, 16.7, 16.8, 16.8]},   # 2026-08-11 谨慎下调（用户）：基准=Q4 FY26 年化 66.4 贴近（83k×2×4）；铭牌 69 仅乐观；Stage 3 低品位+回收率 68% 是下行风险
    "marion":          {"bear": 45.0, "base": 47.0, "bull": 50.0, "q": [11.6, 11.6, 11.8, 12.0]},   # 2026-08-11 适度乐观（用户）：DMS 满产 45.4 + 浮选厂 2027H2 调试贡献 ~1.6（FID 装机 500→600ktpa SC6）；基准 47 SC6
    "kathleenvalley":  {"bear": 40,  "base": 41.9, "bull": 44, "q": [10.4, 10.4, 10.5, 10.6]},   # 基准统一 41.9（季度合计，审计修正）
    "baldhill":        {"bear": 12,  "base": 14,  "bull": 14,  "q": [3.5, 3.5, 3.5, 3.5]},
    "mtcattlin":       {"bear": 0,   "base": 0,   "bull": 8,   "q": [0.0, 0.0, 0.0, 0.0]},  # 审计修正：严谨基准=0（无复产决定）；3/8 仅列纯上行情景（q 按 0 基准）
    "finniss":         {"bear": 13,  "base": 15,  "bull": 16,  "q": [3.0, 4.0, 4.0, 4.0]},
    "manna":           {"bear": 4,   "base": 6,   "bull": 8,   "q": [0.0, 0.0, 2.0, 4.0]},   # 2026-08-11 谨慎下调（用户）：FID Q4 26 未定、Nova 收购 2026-11/12 才完成、改造+爬坡有延期风险——首产可能延至 2027H2/2028，基准保守 6 万吨 SC5.5（SC6 折算 5.5）
    "mtholland":       {"bear": 36,  "base": 38,  "bull": 40,  "q": [9.5, 9.5, 9.5, 9.5]},
}
_LABELMAP = {"悲观": "bear", "基准": "base", "乐观": "bull"}
_FC27_KEY = {"Greenbushes": "history", "Pilgangoora": "pilgangoora", "Wodgina": "wodgina",
             "Mt Marion": "marion", "Kathleen Valley": "kathleenvalley", "Bald Hill": "baldhill",
             "Mt Cattlin": "mtcattlin", "Finniss": "finniss", "Manna": "manna", "Mt Holland": "mtholland"}
for _mm in data["mines"]:  # fc 位于 mines[] 矿山对象内
    fc = FC27.get(_FC27_KEY.get(_mm["mine"]))
    if not fc:
        continue
    if "forecast_2027" in _mm and isinstance(_mm["forecast_2027"].get("scenarios"), dict):
        s = _mm["forecast_2027"]["scenarios"]
        s["bear"]["production_kt"] = fc["bear"] * 10
        s["base"]["production_kt"] = fc["base"] * 10
        s["bull"]["production_kt"] = fc["bull"] * 10
        _mm["forecast_2027"]["quarterly_base"] = {
            "27Q1": fc["q"][0], "27Q2": fc["q"][1], "27Q3": fc["q"][2], "27Q4": fc["q"][3],
            "total": round(sum(fc["q"]), 1),
        }
    elif isinstance(_mm.get("fc_2027"), list):
        for it in _mm["fc_2027"]:
            it["val"] = fc[_LABELMAP[it["label"]]]
        _mm["quarterly_base"] = {
            "27Q1": fc["q"][0], "27Q2": fc["q"][1], "27Q3": fc["q"][2], "27Q4": fc["q"][3],
            "total": round(sum(fc["q"]), 1),
        }

# ============ 预测依据增强（用户规范 2026-08-06） ============
# ② 各矿山 2027 预测详细依据（basis/assumptions，矿山页⑤与总览页共用，线性增长口径）
FC_BASIS = {
    "Greenbushes": {
        "basis": "FY27 官方指引 155-175 万吨（中值 165）→ 季均 41.25；26Q2 实际 38.7 万吨（CGP3 火灾后复产爬坡中）→ 按线性增长 26Q3E=40.0、26Q4E=41.25（等差 d=1.28）；27Q1/27Q2=41.25（FY27 指引期）、27Q3/27Q4 线性延至 CGP 满产 43.5；2027 基准≈168 万吨（线性覆写口径，页面统一值）。",
        "assumptions": ["CGP3 复产爬坡按线性：26Q4 达指引季均、2027 上半年爬满 52 万吨/年", "存量产线维持 FY26 实际 ~130 万吨/年水平", "CGP4 2027 年内不贡献（投资决策未定）", "悲观=爬坡延迟（164）、乐观=满产提前+回收率改善（173）"],
    },
    "Pilgangoora": {
        "basis": "FY27 指引（2026-07至2027-06 财年）1,030-1,100kt（中值 106.5）→ 季均 26.6，覆盖日历 26Q3-27Q2 四季；日历 2027 = FY27 后两季（27Q1/27Q2=26.6，指引覆盖——Ngungaju 已满产）+ FY28 前两季（27Q3/27Q4——FY28 无官方指引，Ngungaju 满产+爬坡拖累消失，按双厂稳态利用率 ~90%（31.25×0.90≈28.1）外推 28.25/季，接近满产但保留检修余量）→ 日历 2027 基准 109.7 万吨 dmt（指引覆盖 53.2 + 外推 56.5）→ SC6 折算 96.9（×0.883，品位 ~SC5.2）；26Q2 实际 23.24（FY26Q4）→ 26Q3E=24.0 线性爬坡。",
        "assumptions": ["Ngungaju 2026-10 前达目标产能（官方指引基础）", "Pilgan 维持 ~200-215kt/季高利用率", "FY28 前两季（27Q3/27Q4）双厂稳态利用率 ~90%——Ngungaju 满产、爬坡拖累消失（Pilgan 历史最高 88% 单厂记录为参照）", "P2000 2027 年内不贡献（可研 2026-12、FID+建设 >2 年）", "悲观=Ngungaju 爬坡慢（104）、乐观=双厂超产接近满产（112.5，90%）"],
    },
    "Wodgina": {
        "basis": "无年度指引（MRL 不发布季度/年度产量指引）；当前官网三线合计约 750ktpa、产品 5.5% Li₂O（即实际品位铭牌，不再换算 mixed）→ 季均 18.75；26Q2 实际 18.8（100% 推算 mixed）→ 26Q3E/26Q4E=18.75，CY2026E ≈ 71.9；2027 基准=67 万吨 SC6（2026-08-11 谨慎下调：≈Q4 FY26 年化 66.4，三线全开但 Stage 3 低品位+回收率 68% 压制；铭牌 69 仅乐观）。",
        "assumptions": ["三线 750ktpa SC5.5% 产能满负荷（Q1 FY27 起三线全开）", "Stage 4 预剥离 Q1 FY27 启动保障 3 年矿石供应", "悲观=利用率不足（72）、乐观=超铭牌（80）"],
    },
    "Mt Marion": {
        "basis": "无年度指引；2026 稳态 ~66 万吨/年（FY26 销量 242k SC6 100% 口径）→ 季均 16.5；26Q2 实际 16.4 → 线性 26Q3E=16.4、26Q4E=16.5；2027 基准=47 万吨 SC6（2026-08-11 适度乐观：DMS 满产 45.4 + 浮选厂 2027H2 调试贡献 ~1.6；FY26 官方 227k×2）。",
        "assumptions": ["浮选厂（FID 2026-05-26 $490M）2027 年中投产提升回收率", "N9→N11 矿坑过渡品位波动可控", "Ganfeng 合资运营稳定", "悲观=浮选延期品位波动（63）、乐观=提前投产+地下开发（69）"],
    },
    "Kathleen Valley": {
        "basis": "FY27 官方指引 390-440k dmt concentrate（2026-07-29 澄清非 SC6，中值 415k）→ 季均 10.4；26Q2 实际 10.3（dmt）→ 线性 26Q3E=10.3、26Q4E=10.4；27Q1/27Q2=10.4（FY27 指引期）、27Q3/27Q4 为 FY28 研究外推；2027 基准=34.9 万吨 SC6 折算（原 41.9 万吨实际精矿 dmt ×0.833）。",
        "assumptions": ["2.8Mtpa 原矿运行率 FY27 底达成（地下爬坡）", "回收率维持 ~63% 逐步改善", "悲观=地下爬坡不及预期（40）、乐观=回收率 70%+（44）"],
    },
    "Bald Hill": {
        "basis": "2026-05 复产重启（capex $20M）、目标 26Q4 满产 140k SC6/年 → 季均 3.5；26Q2 实际 0.1（首月）→ 线性 26Q3E=1.8、26Q4E=3.5；2027 基准=14 万吨（全年满产运行）。",
        "assumptions": ["Q2 FY27 达满产 140k dmt SC6/年（MRL 公告目标）", "存量尾矿+选矿厂重启改造完成", "悲观=爬坡延迟锂价回落（12）、乐观=扩建研究通过（14 满产 cap）"],
    },
    "Mt Cattlin": {
        "basis": "力拓 2025-03 收购后进入 C&M（无生产、无资本开支、无复产决定）；2027 严谨基准=0，3/8 万吨仅列纯上行情景（取决于锂价回升与力拓复产决策——审计修正）。",
        "assumptions": ["悲观/基准=持续 C&M（0-3 万吨，概率最高）", "乐观=力拓利用自有渠道有限复产（8 万吨）", "S-K1300 资源 6.48Mt@1.41% 支撑复产可能性"],
    },
    "Finniss": {
        "basis": "2026-05 恢复采矿（Grants）、26Q3 首产精矿目标；名称产能 214ktpa SC6e（2026 FID）→ 满产季均 5.35；首产 4 步线性爬坡：26Q3E=1.4、26Q4E=2.3 → 27Q1=3.0、27Q2=4.0 后持平；2027 基准=15 万吨（~70% 名铭牌，研究情景非公司指导——审计修正）。",
        "assumptions": ["FID 融资 US$120M（Glencore/InfraVia/Nebari）+ A$120M 股权已到位", "2028 年中爬坡至 1.2Mtpa 原矿吞吐", "BP33 地下储量 9.29Mt@1.31% 支撑 20 年寿命", "悲观=爬坡慢 50% 运行率（13）、乐观=年底达名称产能（16）"],
    },
    "Manna": {
        "basis": "未投产（MDCP 2026-08-04 批准、FID Q4 2026、首产精矿 2027 年中、Nova 1.8Mtpa 选矿厂路线）；2026 年产量为零；2027 年内首产爬坡：27Q3=2.0、27Q4=4.0（等差，谨慎下调）；2027 基准=6 万吨 SC5.5（SC6 折算 5.5；FID 未定+Nova 收购 2026-11/12 完成+改造爬坡延期风险，首产可能延至 2027H2/2028）。",
        "assumptions": ["Nova Operation（A$7m 收购）改造后 2027 年中加工 Manna 矿石", "Lopal 40% 包销 + US$75M 预付款（FID 后）+ Canmax 30% 包销", "DFS 参数：NPV A$472M、capex A$439.1M、首产 SC5.5 精矿", "悲观=FID 延后仅 DSO（6）、乐观=Nova 改造顺利（10）"],
    },
    "Mt Holland": {
        "basis": "MH 无官方 FY27 产量指引——按名义产能 383ktpa 利用率情景（非线性，非指引外推）：26Q1 满产运营（SQM 确认 'operating at full capacity'）；26Q2 美式财季报告未发布（N.D.，8 月下旬）；2027 基准=34.8 万吨 SC6 折算（原 38 万吨 SC5.5 ×0.917 ≈ 名义产能 99.2%），有 Wesfarmers FY27 项目口径约 380kt 依据；2027 扩产不贡献产量（第二选矿厂 2027 H2 才开工、扩产首产 H1 2030）。",
        "assumptions": ["悲观 36 万吨 = 名义产能 94.0%（36.0/38.3）——需求/发运节奏影响的保守运行", "基准 38 万吨 = 99.2%——满产稳定运行（Wesfarmers FY27 ~380kt 口径）", "乐观 40 万吨 = 104.4%——超名义产能的乐观假设（扩产前期/直接销售增加）", "Kwinana 精炼厂 2027 达名称产能（50ktpa LOH）；扩产 FID（2026-07-21）2027 H2 建设启动不影响存量产线"],
    },
}
for _mm in data["mines"]:
    _fb = FC_BASIS.get(_mm["mine"])
    if not _fb:
        continue
    if "forecast_2027" in _mm and isinstance(_mm["forecast_2027"], dict):
        _mm["forecast_2027"]["basis_detail"] = _fb["basis"]
        _mm["forecast_2027"]["assumptions_detail"] = _fb["assumptions"]
    elif isinstance(_mm.get("fc_2027"), list):
        _mm["basis_detail"] = _fb["basis"]
        _mm["assumptions_detail"] = _fb["assumptions"]

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    f.write("// 由 build_data.py 生成（永安期货-澳洲锂矿汇总格式）\n")
    f.write("const YONGAN_DATA = " + json.dumps(data, ensure_ascii=False, indent=1) + ";\n")

# 每次构建同步生成十个静态矿山页，避免 index.html 模板与单矿页漂移。
_DOCS_DIR = os.path.dirname(OUT)
_INDEX_HTML = os.path.join(_DOCS_DIR, "index.html")
_MINE_PAGES = {
    "greenbushes.html": "Greenbushes",
    "pilgangoora.html": "Pilgangoora",
    "wodgina.html": "Wodgina",
    "marion.html": "Mt Marion",
    "kathleenvalley.html": "Kathleen Valley",
    "baldhill.html": "Bald Hill",
    "mtcattlin.html": "Mt Cattlin",
    "finniss.html": "Finniss",
    "manna.html": "Manna",
    "mtholland.html": "Mt Holland",
}
_MINE_KEY_NEEDLE = "const MINE_KEY = urlParams.get('mine') || 'Greenbushes';"
with open(_INDEX_HTML, "r", encoding="utf-8") as f:
    _template = f.read()
if _template.count(_MINE_KEY_NEEDLE) != 1:
    raise RuntimeError("index.html 默认矿山键缺失或不唯一，停止生成静态矿山页")
for _filename, _mine_key in _MINE_PAGES.items():
    _page = _template.replace(
        _MINE_KEY_NEEDLE,
        f"const MINE_KEY = urlParams.get('mine') || '{_mine_key}';",
        1,
    )
    with open(os.path.join(_DOCS_DIR, _filename), "w", encoding="utf-8") as f:
        f.write(_page)

print("OK ->", OUT)
print("static pages:", len(_MINE_PAGES))
print("quarters:", QUARTERS[-4:], "... 共", len(QUARTERS))
print("production 21Q3-26Q4:", series(9)[18:])
print("sales 21Q3-26Q2:", [v for v in series(13)[18:26]])
print("mines:", [m["mine"] for m in MINES])
