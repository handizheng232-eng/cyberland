// 由 build_data.py 生成（永安期货-澳洲锂矿汇总格式）
const YONGAN_DATA = {
 "meta": {
  "title": "永安期货 · 澳洲锂矿季度汇总",
  "updated": "2026-08-05",
  "data_quarters": {
   "start": "2019Q1",
   "end_actual": "26Q2",
   "end_forecast": "26Q4"
  },
  "unit_note": "产量/销量/库存单位为万吨；均价 US$/t；成本 A$/t",
  "color_legend": "浅色柱/空心圆=预测季度（按官方 FY27 指引中值推算）；灰色 N.D.=官方未披露",
  "disclaimer": "本页面数据来自各矿山母公司官方季度报告，仅供研究参考，不构成投资建议。",
  "pages": [
   {
    "key": "Overview",
    "label": "矿山总览",
    "file": "overview.html"
   },
   {
    "key": "Greenbushes",
    "label": "Greenbushes（第一页）",
    "file": "index.html"
   },
   {
    "key": "Pilgangoora",
    "label": "Pilgangoora（第二页）",
    "file": "pilgangoora.html"
   },
   {
    "key": "Wodgina",
    "label": "Wodgina（第三页）",
    "file": "wodgina.html"
   },
   {
    "key": "Mt Marion",
    "label": "Mt Marion（第四页）",
    "file": "marion.html"
   },
   {
    "key": "Kathleen Valley",
    "label": "Kathleen Valley（第五页）",
    "file": "kathleenvalley.html"
   },
   {
    "key": "Bald Hill",
    "label": "Bald Hill（第六页）",
    "file": "baldhill.html"
   }
  ]
 },
 "mines": [
  {
   "company": "IGO",
   "mine": "Greenbushes",
   "current_q": "26Q2",
   "prev_q": "26Q1",
   "current_q_date": "2026年4-6月",
   "mine_cn": "Greenbushes（格林布什矿山）",
   "report": "IGO June 2026 Quarterly Activities Report（2026-07-28 发布，FY26 Q4 / 日历26Q2）",
   "source_url": "https://www.igo.com.au/site/investor-center/investor-center1",
   "equity_note": "100% 资产口径（Talison 运营）；IGO→TLEA 49%，TLEA/Windfield→Greenbushes 51%，Albemarle 49%",
   "history_labels": [
    [
     "production",
     "精矿产量（万吨，SC6 折算 6% Li₂O）"
    ],
    [
     "lce",
     "精矿产量（6%,LCE）"
    ],
    [
     "tech_grade",
     "技术级精矿产量（万吨，实际品位）"
    ],
    [
     "chem_grade",
     "化学级精矿产量（万吨，实际品位）"
    ],
    [
     "sales",
     "销量（万吨，SC6 折算 6% Li₂O）"
    ],
    [
     "inv_change",
     "库存变动量（万吨）"
    ],
    [
     "inventory",
     "库存（万吨）"
    ],
    [
     "prod_sales_ratio",
     "产销比"
    ],
    [
     "avg_price",
     "平均售价（US$/t，SC6）"
    ],
    [
     "cost_with_royalty",
     "单位成本—含权益金（A$/t，FOB SC6）"
    ],
    [
     "cost_no_royalty",
     "单位成本—不含权益金（A$/t，FOB SC6）"
    ],
    [
     "cash_cost",
     "cash cost（A$/t，FOB SC6）"
    ]
   ],
   "status_26q2": {
    "existing_lines": [
     {
      "name": "已有产能1：技术级锂精矿工厂 — 14万吨",
      "q26q2": "未单独披露运行数据（IGO 自 1Q25 起不再拆分技术级/化学级产量，并入总量披露）。26Q2 矿山总产量 387kt 含技术级与化学级全部产线。",
      "q26q1": "同样未单独披露（并入总量披露），26Q1 矿山总产量 351kt。",
      "compare": "两季均无单独口径，无实质变化。"
     },
     {
      "name": "已有产能2：化学级锂精矿工厂 1号（CGP1）— 60万吨",
      "q26q2": "26Q2 Talison 重点提升 CGP1 性能，特别是可靠性、停机合规性和回收率，已引入外部专家团队制定综合回收率改善计划。本季回收率下降与工厂停机部分抵消了品位上升带来的产量增益（采矿转向高品位矿体）。",
      "q26q1": "26Q1 受入选品位下降、回收率下降及维护停机增加影响，运营结果偏弱；季度内为优先推进安全整改实施两次安全停工。",
      "compare": "本季采矿品位改善（转向高品位矿体）是环比亮点，但回收率与停机问题延续，改善措施落地仍需时间——改善方向超预期，兑现进度未超预期。"
     },
     {
      "name": "已有产能3：化学级锂精矿工厂 2号（CGP2）— 60万吨",
      "q26q2": "26Q2 同 CGP1：重点改善可靠性、停机合规性和回收率；外部专家支持的综合回收率改善计划推进中。",
      "q26q1": "26Q1 同 CGP1：品位、回收率、停机三重拖累，运营偏弱。",
      "compare": "两季表述一致：CGP2 回收率持续低于 CGP1（此前报告披露 CGP1 回收率稳定在 80% 以上、CGP2 约 70%），提升 CGP2 回收率仍是主要看点。"
     },
     {
      "name": "已有产能4：尾矿再处理厂 — 28万吨",
      "q26q2": "26Q2 维持性+增长性+资本化剥离支出合计 A$42M，主要用于尾矿设施（TSF）工程。",
      "q26q1": "26Q1 支出合计 A$75M，主要投向 CGP3 与尾矿库工程。",
      "compare": "本季资本开支环比下降 44%（A$75M→A$42M），主因 CGP3 建设高峰已过、投入转向尾矿设施——资本开支节奏符合投产后的正常回落。"
     },
     {
      "name": "已有产能5：化学级锂精矿工厂 3号（CGP3）— 52万吨【2025年新增投产】",
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
     "operation_changes": "26Q2 产量 387kt，环比 +10%（26Q1：351kt），增量主要来自 CGP3 贡献提升（71kt vs 33kt）；采矿品位改善，但回收率下降与工厂停机抵消了部分预期产量增益；销量 391kt，环比 +12%（含上季因港口拥堵延迟至本季的装运）；平均实现价 US$2,286/t，环比 +37%，反映锂市场持续走强；现金成本（production 口径）A$448/t，环比基本持平；EBITDA 利润率 80%（FY26 全年 73%）；6 月 CGP3 火灾停产约 7 周，预计近日复产；Windfield 期末现金 A$183.8M，有息负债 A$1,965.4M，本季向股东分红 A$390.0M。",
     "operation_changes_prev": "26Q1 产量 351kt，环比持平（25Q4：352kt），CGP3 贡献约 33kt；运营受入选品位下降、回收率下降及维护停机增加拖累，季度内实施两次安全停工；销量 349kt，环比 +6%，一船因港口拥堵延迟至 4 月装运；平均实现价 US$1,668/t，环比近翻倍（25Q4：US$850/t）；现金成本 A$446/t，环比 +20%（CGP3 运营成本自 2 月起计入、维护成本增加、剥离资本化减少）；EBITDA 利润率 75%；资本开支 A$75M，主要投向 CGP3 与尾矿库。",
     "future_outlook": "FY27 指引：精矿产量 155-175 万吨，现金成本 A$380-440/t，资本开支 A$250-300M；FY26 全年实际：产量 141.0 万吨（1,410kt），销量 136.8 万吨，现金成本 A$415/t，均价 US$1,443/t；26Q3/26Q4 按指引中值 165 万吨/年 ÷ 4 = 41.25 万吨/季预测；注意 CGP3 火灾后复产爬坡进度或影响 26Q3 初期产量。",
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
    "title": "2027 年产量预测（日历年度 · 100% 资产口径）",
    "basis": "官方指引：IGO FY27 精矿产量指引 155-175 万吨（FY27 = 2026年7月-2027年6月，即日历 26Q3-27Q2）。产能基础：存量产线铭牌 162 万吨/年（CGP1 60 + CGP2 60 + 技术级 14 + 尾矿再处理 28），CGP3 铭牌 52 万吨/年，CGP4 铭牌 52 万吨/年（规划 2027 建成投产，投资决策未定）。FY26 全年实际产量 141 万吨，其中 CGP3 贡献约 10.4 万吨（33+71kt），即存量产线 FY26 实际约 130 万吨/年（利用率约 80%）。",
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
      "note": "CGP3 复产推迟至 26Q4、2027 年中才达满产，全年贡献仅 ~35 万吨；存量产线回收率改善不及预期；日历 2027 ≈ 160 万吨。"
     },
     "base": {
      "label": "基准（CGP3 按计划爬满 + 存量小幅改善）",
      "production_kt": 1740,
      "note": "CGP3 2027 年初爬至 ~85% 利用率、年中满产，全年贡献 ~47 万吨；存量 ~130 万吨；合计 ≈ 174 万吨。口径说明：日历 2027 = FY27 后两季（27Q1-27Q2，落在公司 FY27 指引 155-175 万吨区间）+ FY28 前两季（27Q3-27Q4，满产稳态），故略高于 FY27 财年指引中枢 165 万吨是合理的。"
     },
     "bull": {
      "label": "乐观（CGP3 快速满产 + CGP4 提前 FID 带来增量）",
      "production_kt": 1850,
      "note": "CGP3 2027 年初即满产（~50 万吨/年贡献）；回收率改善兑现；CGP4 若 2027 年末提前投产可加 ~5 万吨；日历 2027 ≈ 185 万吨。"
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
      "excel_capacity": "60 万吨精矿/年",
      "verified": "⚠️ 多来源矿石口径交叉确认，精矿口径为推算",
      "sources": [
       {
        "src": "SLR 技术报告 (2026-02)",
        "data": "矿石处理能力 1.8 Mtpa；2025 实际年处理 ~1.7-1.8Mt、入选品位 ~2.7% Li₂O"
       },
       {
        "src": "IGO 官网",
        "data": "计入存量四厂合计 6.5Mtpa 矿石 → 精矿 up to 1.5Mtpa"
       },
       {
        "src": "IGO 年报",
        "data": "未单独披露；仅描述为四座处理厂之一"
       },
       {
        "src": "推算",
        "data": "按官方产率 ~23-33%，1.8Mtpa 矿石对应精矿约 42-60 万吨/年——Excel 60 万吨处于上限"
       }
      ],
      "status": "warn"
     },
     {
      "line": "CGP2（化学级2号）",
      "excel_capacity": "60 万吨精矿/年",
      "verified": "⚠️ 多来源矿石口径交叉确认，精矿口径为推算",
      "sources": [
       {
        "src": "SLR 技术报告 (2026-02)",
        "data": "矿石处理能力 2.4 Mtpa（设计）；实际仅 ~2.0 Mt（品位 2.0% Li₂O 偏低，未达设计）"
       },
       {
        "src": "IGO 官网",
        "data": "计入存量合计 6.5Mtpa 矿石 → 1.5Mtpa 精矿"
       },
       {
        "src": "IGO 年报 2022",
        "data": "CGP3 设计基于 CGP2、名义矿石处理量 2.4Mtpa（佐证 CGP2=2.4）"
       },
       {
        "src": "推算",
        "data": "2.4Mtpa 矿石 × ~25% 产率 ≈ 60 万吨精矿——与 Excel 一致，但实际品位下降后产率或走低"
       }
      ],
      "status": "warn"
     },
     {
      "line": "TGP（技术级）",
      "excel_capacity": "14 万吨精矿/年",
      "verified": "⚠️ 官方矿石口径远低于 Excel 精矿口径",
      "sources": [
       {
        "src": "SLR 技术报告 (2026-02)",
        "data": "矿石处理能力仅 0.35 Mtpa——按 40% 产率推算精矿约 14 万吨/年，与 Excel 一致；但近年技术级占比已降至 1% 以下（IGO 不再单独披露）"
       },
       {
        "src": "IGO 官网",
        "data": "四厂之一，未单独披露产能"
       },
       {
        "src": "Albemarle 10-K",
        "data": "技术级精矿厂在产"
       }
      ],
      "status": "warn"
     },
     {
      "line": "TRP（尾矿再处理厂）",
      "excel_capacity": "28 万吨精矿/年",
      "verified": "✓ 官方精矿口径确认（280ktpa）",
      "sources": [
       {
        "src": "IGO 年报 2022",
        "data": "'Nominal production from the TRP is expected to be 280ktpa...nameplate capacity expected FY23'——28 万吨精矿/年官方确认"
       },
       {
        "src": "SLR 技术报告 (2026-02)",
        "data": "矿石处理能力 2.0 Mtpa（处理 TSF1 旧钽尾矿，平均品位 1.4% Li₂O）"
       },
       {
        "src": "IGO 官网",
        "data": "计入存量合计 6.5Mtpa → 1.5Mtpa 精矿"
       }
      ],
      "status": "ok"
     },
     {
      "line": "CGP3（化学级3号）",
      "excel_capacity": "52 万吨精矿/年",
      "verified": "✓ 官方精矿口径确认（520ktpa）",
      "sources": [
       {
        "src": "IGO 年报 2022/2023",
        "data": "'contribute an additional 520ktpa'；'designed to deliver approximately 0.52Mtpa'"
       },
       {
        "src": "IGO 官网",
        "data": "处理能力 2.4Mtpa 矿石 → up to 500ktpa 精矿"
       },
       {
        "src": "SLR 技术报告 (2026-02)",
        "data": "矿石处理能力 2.4 Mtpa；CGP3 后 LOM 合计 8.95 Mtpa、精矿 up to 1.8 Mtpa"
       },
       {
        "src": "Albemarle 10-K",
        "data": "第三座化学级厂建成，商业化生产预计 2026 年；2026-06-10 火灾公告确认 CGP1/CGP2 不受影响"
       }
      ],
      "status": "ok"
     },
     {
      "line": "CGP4（化学级4号）",
      "excel_capacity": "52 万吨精矿/年（规划）",
      "verified": "⚠️ 规划未定，多来源均无最新进展",
      "sources": [
       {
        "src": "IGO 年报 2023",
        "data": "'IGO expects a decision on the FID on CGP4 during FY24'——FY24 已过，截至 2026 年中无 FID 公告，项目实际推迟"
       },
       {
        "src": "SLR 技术报告 (2026-02)",
        "data": "LOM 计划（表 14-1）未含 CGP4——第三方技术评估亦按无 CGP4 处理"
       },
       {
        "src": "IGO 官网 / Albemarle 10-K",
        "data": "均无 CGP4 进展披露"
       }
      ],
      "status": "warn"
     },
     {
      "line": "全矿合计",
      "excel_capacity": "214 万吨精矿/年（162 存量 + 52 CGP3）",
      "verified": "⚠️ 官方矿石口径 6.55→8.95 Mtpa；精矿口径 1.5→1.8 Mtpa",
      "sources": [
       {
        "src": "IGO 官网 + SLR",
        "data": "存量四厂 6.55 Mtpa 矿石 → 精矿 up to 1.5 Mtpa；含 CGP3 后 8.95 Mtpa → 精矿 up to 1.8 Mtpa——官方精矿上限（150-180 万吨/年）低于 Excel 的 214 万吨"
       },
       {
        "src": "IGO 年报 2023",
        "data": "'~2.5Mtpa by FY27'——该口径显著高于官网/SLR 的 1.8Mtpa，疑含 CGP4 或更高有效产能假设，未被第三方技术报告支持"
       },
       {
        "src": "SLR 技术报告 (2026-02)",
        "data": "2025 实际：5.85 Mtpa 矿石 → ~1.4 Mtpa SC6.0（作为可兑现基准）"
       }
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
     {
      "url": "img/sat_greenbushes.jpg",
      "src": "卫星影像（Yandex Maps，坐标 -33.8567,116.0622）",
      "cap": "Greenbushes 矿区卫星影像（Zoom 14）——露天矿坑与选矿厂区在卫星影像上的实际形态，卫星追踪第一参照"
     },
     {
      "url": "img/slr_plants_aerial.jpg",
      "src": "SLR 技术报告 Fig 14-1/14-2",
      "cap": "选矿厂工艺流程总览 + 厂区航拍位置图（Fig 14-2 Aerial Image），标出 CGP1/CGP2/CGP3/TGP/TRP 各厂相对位置"
     },
     {
      "url": "img/slr_overall_layout.jpg",
      "src": "SLR 技术报告 Fig 15-1",
      "cap": "Greenbushes 整体场地布局图（含选矿厂/尾矿库/储水设施位置）——技术报告项目总览图"
     },
     {
      "url": "img/greenbushes_aerial_official.jpg",
      "src": "IGO 官网（Our Business）",
      "cap": "Greenbushes 矿山官方航拍实景——露天矿坑 + 选矿厂区，可与卫星影像直接对照定位"
     }
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
        {
         "src": "Albemarle 10-K",
         "data": "大型露天矿（南纬33°52′、珀斯以南约250km）；主矿体 Central Lode + 东侧平行 Kapanga 矿体；开采区约 3,500 公顷、三个采矿租约"
        },
        {
         "src": "SLR 技术报告",
         "data": "Central Lode 走向 3km、厚度数十至 300m、倾角 40-60°SW，连续性优于 Kapanga；Kapanga 近六年新增钻探为主（DD 占 75%）"
        }
       ]
      },
      {
       "item": "采矿方法与产能",
       "built_plan": "✅ 建成（传统露天开采）",
       "status": "ok",
       "sources": [
        {
         "src": "SLR 技术报告",
         "data": "传统露天金属矿开采（卡车+铲运），10m 工作台阶（5m 分段）；全部 ROM 矿石运往四座选矿厂；LOM 年物料总移动量 2034 年起升至 ~53Mt、废石移动 2033-2040 年 >40Mt（峰值 46Mt/2039）；剥采比（ROM）3.4:1"
        }
       ]
      },
      {
       "item": "矿坑规划（露天境界）",
       "built_plan": "⚠️ 规划中（LOM 24 年）",
       "status": "warn",
       "sources": [
        {
         "src": "SLR 技术报告",
         "data": "LOM 计划假设矿山寿命 24 年：采矿至 2048、堆存矿石 2049 处理完毕；矿坑境界基于资源模型（Indicated 资源仅在露天境界内、距钻孔外推 50m 内分类）；矿坑内排土（in-pit dumping）为优化项"
        }
       ]
      },
      {
       "item": "尾矿库 TSF1-TSF4（TRP 原矿来源）",
       "built_plan": "✅ 建成（TSF1-4）；⚠️ TSF5 规划中",
       "status": "warn",
       "sources": [
        {
         "src": "SLR 技术报告",
         "data": "TSF4 按当前 LOM 容量可用至 2034 年；之后需加高 TSF4 并新建 TSF5（拟建于场外、设计容量待确认）；TRP 处理 TSF1 旧钽尾矿（品位 1.4% Li₂O、2.0Mtpa）"
        },
        {
         "src": "IGO 年报 2022",
         "data": "TRP 设计再处理 2Mtpa 旧钽选矿尾矿（TSF1），名义产出 280ktpa 精矿五年期"
        }
       ]
      },
      {
       "item": "废石堆 S1（Floyds）及后续规划",
       "built_plan": "✅ 建成（S1 Floyds）；⚠️ 后续废石堆规划中",
       "status": "warn",
       "sources": [
        {
         "src": "SLR 技术报告",
         "data": "目前唯一运行废石堆 S1（Floyds），容量 77Mbcm、预计 2034 年达容；之后需新建多个废石堆支撑 LOM 废石需求（需逐项取得审批）"
        },
        {
         "src": "Albemarle 10-K",
         "data": "废石堆与尾矿库均位于三个采矿租约+两个通用租约范围内"
        }
       ]
      },
      {
       "item": "地下开采研究（未来原矿来源）",
       "built_plan": "⚠️ 概念研究阶段（无建成）",
       "status": "warn",
       "sources": [
        {
         "src": "SLR 技术报告",
         "data": "地下开采研究含露天-地下切换（open pit underground trade-off）研究，目前概念级；未来若实施地下开采，可通过膏体充填（paste fill）减少废石与尾矿需求；Central Lode 北部历史地下采空区已按实测形态从资源中扣除"
        },
        {
         "src": "IGO 年报 2023",
         "data": "评估 Greenbushes 地下开采及潜在卫星矿供矿机会"
        }
       ]
      },
      {
       "item": "卫星矿 / 外围供矿",
       "built_plan": "⚠️ 评估阶段（无建成）",
       "status": "warn",
       "sources": [
        {
         "src": "IGO 年报 2023",
         "data": "额外研究将评估潜在卫星矿（satellite feed）供矿机会，以延长矿山服务年限"
        },
        {
         "src": "Albemarle 10-K",
         "data": "矿权区约 10,000 公顷，含历史锡/钽/锂采区；Talison 持有全部锂矿采矿权"
        }
       ]
      },
      {
       "item": "矿石堆存（库存矿石）",
       "built_plan": "✅ 建成（堆场）",
       "status": "ok",
       "sources": [
        {
         "src": "SLR 技术报告",
         "data": "LOM 计划利用现有矿石堆存 0.9Mt；未处理矿石堆存另有 30.5Mt（含尾矿再处理 2.8Mt）；选矿厂总给矿 164.5Mt、平均品位 1.90% Li₂O"
        }
       ]
      }
     ],
     "note": "核实时间：2026-08-04。采矿侧要点：① 单一露天矿（Central Lode 主矿体）服务全部选矿厂，矿体禀赋为全球最高品位硬岩锂矿之一；② TSF4 尾矿库 2034 年达容后需新建 TSF5（场外、容量待定）——长期原矿/尾矿处理能力的审批是关键风险；③ 地下开采仅概念研究，若实施可缓解废石/尾矿压力并延长矿山寿命；④ LOM 按 22.5% 回收率、1.90% 平均品位测算，产出精矿 37.0Mt——该回收率假设与 26Q2 实际回收率走低趋势存在张力，后续需跟踪。",
     "images": [
      {
       "url": "img/slr_location_plan.jpg",
       "src": "SLR 技术报告 Fig 3-1/3-2",
       "cap": "矿区位置图（含经纬度 33°51'24\"S 116°03'44\"E 与区域交通/港口关系）——卫星锁定第一参照"
      },
      {
       "url": "img/slr_site_layout.jpg",
       "src": "SLR 技术报告 Fig 3-3",
       "cap": "Greenbushes Mine Operation Layout——矿坑、选矿厂、尾矿库、废石堆整体布置（技术报告项目总览图）"
      },
      {
       "url": "img/slr_pit_limit.jpg",
       "src": "SLR 技术报告 Fig 12-3/12-5",
       "cap": "矿坑境界优化壳与最终边坡设计图（含坐标网格），用于识别矿坑边界"
      },
      {
       "url": "img/slr_geo_map.jpg",
       "src": "SLR 技术报告 Fig 6-1/6-2",
       "cap": "Greenbushes 区域地质图与矿体剖面——矿体分布与矿坑位置的地质背景"
      },
      {
       "url": "img/slr_tsf.jpg",
       "src": "SLR 技术报告 Fig 15-7/15-8",
       "cap": "尾矿库 TSF1/2/4 布置图——TRP 原矿来源与尾矿设施卫星定位"
      },
      {
       "url": "img/greenbushes_ar2023_mine.jpg",
       "src": "IGO Annual Report 2023",
       "cap": "Greenbushes 露天矿实景（FY23），主矿坑与采矿设备，可对照卫星影像识别矿坑轮廓"
      }
     ]
    }
   }
  },
  {
   "company": "PLS（Pilbara Minerals）",
   "mine": "Pilgangoora",
   "current_q": "26Q2",
   "prev_q": "26Q1",
   "current_q_date": "2026年4-6月",
   "mine_cn": "Pilgangoora（皮尔甘古拉矿山）",
   "report": "PLS June 2026 Quarterly Activities Report（2026-07-30 发布，FY26 Q4 / 日历26Q2）；FY25 Annual Report",
   "source_url": "https://www.pls.com/invest/asx-announcements",
   "equity_note": "100% 资产口径（PLS 全资拥有并运营）；Pilgangoora 为世界最大独立拥有的硬岩锂矿",
   "history_labels": [
    [
     "production",
     "精矿产量（万吨，dmt 实际品位 ~5.2% SC）"
    ],
    [
     "sales",
     "销量（万吨，dmt 实际品位 ~5.2% SC）"
    ],
    [
     "prod_sales_ratio",
     "产销比"
    ],
    [
     "avg_price",
     "平均售价（US$/t，CIF China ~SC5.2）"
    ],
    [
     "cash_cost",
     "单位成本 FOB（A$/t，dmt）"
    ],
    [
     "cif_cost",
     "单位成本 CIF（A$/t，dmt）"
    ]
   ],
   "status_26q2": {
    "existing_lines": [
     {
      "name": "已有产能1：Pilgan 选矿厂（Pilgan Plant）— 铭牌 ~1.0Mtpa（P1000 后）",
      "q26q2": "26Q2（Jun Q）产量 214.3kt（环比 -8%，主因上季创纪录高基数）；回收率小幅升至 76.8%；矿石分选机（世界最大）性能改善提供运营灵活性；FY26 全年 879.5kt 超指引上限",
      "q26q1": "26Q1（Mar Q）创纪录产量 232.4kt，回收率 ~75%；P1000 扩建（2025年1月完成）使 Pilgan 产能达 ~1.0Mtpa 基础",
      "compare": "产量环比 -8% 属高基数回落（232.4→214.3kt），但 FY26 全年 879.5kt 超指引上限 ~10kt；回收率 76.8% 创改善——全年表现超预期"
     },
     {
      "name": "已有产能2：Ngungaju 选矿厂（Ngungaju Plant）— 目标产能（2026年7月重启）",
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
   "forecast_unit": "万吨 dmt（实际品位 ~5.2% SC；FY27 指引 1,030-1,100kt 对应）",
   "forecast_2027": {
    "basis": "PLS FY27 官方指引已发布（2026-07-30 June QAR）：产量 1,030-1,100kt（财年口径 = 2026年7月-2027年6月，中值 ~1,065kt）；日历 2027 = FY27 后两季（含 Ngungaju 满产）+ FY28 前两季（满产稳态），预计落在指引区间上沿附近；产能基础：Pilgan ~1.0Mtpa（P1000 后）+ Ngungaju 重启后目标产能 → 双厂合计 ~1.25Mtpa；P2000 可研 2026-12 出结果、FID 若通过则 2028H2 起贡献（2027 年内不纳入）。",
    "assumptions": [
     "Ngungaju 2026年7月重启，FY27 前 4 个月（2026年10月底前）达目标产能——2027 年全年双厂运行",
     "Pilgan 维持 ~200-215kt/季（FY26 后两季实际 205.3/214.3kt，利用率高）",
     "P2000 2027 年内不贡献产量（可研 2026-12 出结果、FID+建设周期 >2 年）",
     "FY27 指引 1,030-1,100kt 为官方锚；日历 2027 因跨 FY27/FY28 两财年，按指引上沿 + Ngungaju 满产推算"
    ],
    "scenarios": {
     "bear": {
      "label": "悲观（Ngungaju 爬坡慢于计划 + 锂价回落压缩产量）",
      "production_kt": 950,
      "note": "Ngungaju 2027 年中才达产、Pilgan 利用率回落；全年 ~95 万吨"
     },
     "base": {
      "label": "基准（双厂满产，FY27 指引兑现）",
      "production_kt": 1080,
      "note": "Pilgan ~210kt/季×4 + Ngungaju 达产后 ~55-60kt/季×4 → ~108 万吨（对应 FY27 指引上沿）"
     },
     "bull": {
      "label": "乐观（锂价大涨 + P2000 提前 FID 动工）",
      "production_kt": 1180,
      "note": "双厂超产 ~110 万吨 + P2000 建设期效率提升 → ~118 万吨"
     }
    },
    "quarterly_base": {
     "27Q1": 26,
     "27Q2": 27,
     "27Q3": 28,
     "27Q4": 28,
     "total": 109
    },
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
      "excel_capacity": "~1.0Mtpa（P1000 后）",
      "verified": "✓ 官方确认（合计口径）",
      "sources": [
       {
        "src": "PLS 官网（2026-06 存档）",
        "data": "'Following completion of the P1000 Expansion Project in 2025, Pilgangoora has the capacity to produce up to one million tonnes of spodumene concentrate per annum'——1.0Mtpa 官方确认"
       },
       {
        "src": "FY25 年报",
        "data": "P1000 完成于 FY25，'adding ~320kt to the nameplate capacity'；Pilgan+Ngungaju 合计铭牌 ~580ktpa（P1000 前）；P680 于 2024年8月交付矿石分选机+HIMS"
       },
       {
        "src": "FY25 年报",
        "data": "P1000 资本支出 $560M，2025-01-31 首矿、3月季度完成爬坡"
       }
      ],
      "status": "ok"
     },
     {
      "line": "Ngungaju 选矿厂",
      "excel_capacity": "目标产能（2026年7月重启）",
      "verified": "⚠️ 铭牌为推算（官方未单独披露精矿口径）",
      "sources": [
       {
        "src": "June 2026 QAR",
        "data": "2026年7月1日按计划重启（季报后事件），预计 FY27 前 4 个月（2026年10月底前）达目标产能；26Q2 FOB 成本 +18% 含重启成本"
       },
       {
        "src": "FY25 年报",
        "data": "2024年12月转入临时维护（P850 单厂模式）；FY25 产量 754.6kt 全部来自 Pilgan"
       }
      ],
      "status": "warn"
     },
     {
      "line": "P2000 扩建项目",
      "excel_capacity": "2.0Mtpa（规划）",
      "verified": "⚠️ 可研阶段（2026-12 出结果，预FID $175M 已批）",
      "sources": [
       {
        "src": "June 2026 QAR",
        "data": "可研结果 2026 年 12 月季度发布；2026年6月批准 ~$175M 预 FID 资本支出；新建选矿厂紧邻 Pilgan 设施，全矿浮选流程；FID 取决于可研/融资/市场"
       },
       {
        "src": "PLS 官网",
        "data": "'potential to increase production capacity to two million tonnes per annum'"
       }
      ],
      "status": "warn"
     },
     {
      "line": "全矿合计（双厂）",
      "excel_capacity": "~1.25Mtpa",
      "verified": "⚠️ 官方 FY27 指引 1.03-1.10Mtpa（双厂口径）",
      "sources": [
       {
        "src": "June 2026 QAR",
        "data": "FY27 指引产量 1,030-1,100kt——首次含 Ngungaju 重启后的双厂口径；FY26 实际 879.5kt 超指引上限"
       },
       {
        "src": "PLS 官网",
        "data": "P1000 后 1.0Mtpa（Pilgan 单厂口径）"
       }
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
     {
      "url": "img/sat_pilgangoora.jpg",
      "src": "卫星影像（Yandex Maps，坐标 -21.7939,119.6346）",
      "cap": "Pilgangoora 矿区卫星影像（Zoom 13）——露天矿坑与 Pilgan/Ngungaju 选矿厂在卫星影像上的实际形态，卫星追踪第一参照"
     },
     {
      "url": "img/pilgangoora_overlook.jpg",
      "src": "PLS FY25 年报",
      "cap": "勘探队俯瞰 Pilgangoora 全景——露天矿坑与选矿厂区，可对照卫星影像识别"
     },
     {
      "url": "img/pilgangoora_p1000.jpg",
      "src": "PLS FY25 年报",
      "cap": "P1000 扩建项目完成图（Pilgan 选矿厂升级后）——项目总览展示图"
     },
     {
      "url": "img/pilgangoora_ops.jpg",
      "src": "PLS FY25 年报",
      "cap": "Pilgangoora 运营配图（选矿厂与堆场）"
     }
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
        {
         "src": "PLS 官网",
         "data": "位于 Port Hedland 东南 ~140km，Pilbara 地区；'First production 2018'；31 年矿山寿命"
        },
        {
         "src": "FY25 年报",
         "data": "FY25 采矿 5.2Mt @ 1.4% Li₂O；~32 年矿山寿命；Mineral Resource 445Mt、Ore Reserve 207.2Mt（官网口径）"
        }
       ]
      },
      {
       "item": "矿段与矿体（Central / South）",
       "built_plan": "✅ 建成（多矿段露天开采）",
       "status": "ok",
       "sources": [
        {
         "src": "FY25 年报",
         "data": "FY25 勘探：109 个钻孔 48,194m；900m 深金刚石钻孔（政府共助）发现北部延伸多个伟晶岩域；矿权区为世界最大 LCT 伟晶岩省之一"
        }
       ]
      },
      {
       "item": "采矿方法与产能",
       "built_plan": "✅ 建成（传统露天开采）",
       "status": "ok",
       "sources": [
        {
         "src": "June 2026 QAR",
         "data": "26Q2 总物料移动 10.2Mt（26Q1: 9.9Mt）、矿石 1.7Mt（26Q1: 1.3Mt）——增加采矿与剥离为 Ngungaju 重启与未来生产铺路"
        }
       ]
      },
      {
       "item": "尾矿库（TSF）",
       "built_plan": "✅ 建成；⚠️ 扩展规划中",
       "status": "warn",
       "sources": [
        {
         "src": "FY25 年报",
         "data": "Pilgan+Ngungaju 尾矿设施持续运营；年报提及尾矿管理政策与扩展计划（未披露具体容量）"
        }
       ]
      },
      {
       "item": "P2000 新选矿厂选址（未来）",
       "built_plan": "⚠️ 可研阶段",
       "status": "warn",
       "sources": [
        {
         "src": "March 2026 QAR",
         "data": "P2000 拟新建选矿厂紧邻现有 Pilgan/Ngungaju 设施"
        }
       ]
      }
     ],
     "note": "核实时间：2026-08-05（已更新至 June 2026 QAR）。采矿侧要点：① 单一露天矿服务两座选矿厂（Pilgan + Ngungaju）；② 31-32 年矿山寿命、资源 445Mt/储量 207.2Mt 支撑长期产能；③ PLS 未披露逐坑/逐尾矿库的详细技术参数（无 S-K1300 类 QP 报告），采矿侧细节不及 Greenbushes 丰富；④ 26Q2 总物料移动 10.2Mt、矿石 1.7Mt 创新高，为 Ngungaju 重启铺路。",
     "images": [
      {
       "url": "img/pilgangoora_tenure.jpg",
       "src": "PLS FY25 年报",
       "cap": "Pilgangoora 矿权地图（consolidated tenure，~51,000 公顷）——卫星锁定矿区范围参照"
      },
      {
       "url": "img/sat_pilgangoora.jpg",
       "src": "卫星影像（Yandex Maps，坐标 -21.7939,119.6346）",
       "cap": "Pilgangoora 矿区卫星影像（Zoom 13）——矿坑与选矿厂相对位置，与矿权图对照定位"
      },
      {
       "url": "img/pilgangoora_stockpile.jpg",
       "src": "PLS 官网",
       "cap": "Pilgangoora 精矿堆场实景（堆场在卫星影像上通常呈浅色矩形区域）"
      }
     ]
    }
   }
  },
  {
   "company": "MRL（Mineral Resources）",
   "mine": "Wodgina",
   "current_q": "26Q2",
   "prev_q": "26Q1",
   "current_q_date": "2026年4-6月",
   "mine_cn": "Wodgina（沃吉纳矿山）",
   "report": "MRL Quarterly Activity Report Q4 FY26（2026-07-29 发布，FY26 Q4 / 日历26Q2）；MRL 官网资产页（2025-10 快照）",
   "source_url": "https://www.mineralresources.com.au/our-business/lithium/wodgina/",
   "equity_note": "100% 资产口径为推算（官方披露 50% attributable；MARBL JV = MinRes 50% / Albemarle 50%，MinRes 运营）；销售 100% 为 50%×2 估算",
   "history_labels": [
    [
     "production",
     "精矿产量（万吨，100% 推算 · 混合品位 dmt）"
    ],
    [
     "sales",
     "销量（万吨，100% 推算 · 混合品位 dmt）"
    ],
    [
     "prod_sales_ratio",
     "产销比"
    ],
    [
     "avg_price",
     "平均售价（US$/t，CIF SC6）"
    ],
    [
     "cash_cost",
     "单位成本 FOB（A$/t SC6）"
    ]
   ],
   "status_26q2": {
    "existing_lines": [
     {
      "name": "已有产能1：选矿厂 Train 1（A1 产线）— 设计 ~250ktpa",
      "q26q2": "26Q2 三线利用率提升（产 94k dmt，+21% qoq）；2026-05-19 投资者现场会披露 Q1 FY27 起三线全开；回收率 68%（Stage 2 耗尽、全面转 Stage 3 矿石）；FY26 销量 317k dmt SC6 超指引上限（270-290k）",
      "q26q1": "26Q1 产 78k dmt（-8% qoq），高品位 Stage 2 矿石减少、更多 Stage 3 低品位矿石入厂，回收率约 69%",
      "compare": "产量环比 +21% 超预期（94 vs 78k dmt），三线利用改善；但回收率降至 68%——Stage 2 高品位矿石枯竭、Stage 3 全面供矿是中期观察点"
     },
     {
      "name": "已有产能2：选矿厂 Train 2 / Train 3（A2/A3 产线）— 设计各 ~250ktpa",
      "q26q2": "与 Train 1 同为三线运行的一部分；Q1 FY27 起三线全开（此前部分产线间歇运行）；矿石来自 Stage 3 与库存矿石混合",
      "q26q1": "26Q1 亦在三线运行框架内，但产量受 Stage 2/3 矿石切换影响",
      "compare": "三线全开是 Q1 FY27 明确指引（2026-05-19 现场会），Q4 已为三线运行铺路——产能利用率提升超预期"
     },
     {
      "name": "选矿厂配套：破碎 + 浮选 + 尾矿设施",
      "q26q2": "选矿厂含球磨、脱泥旋流器、磁选、浮选与精矿/尾矿脱水；细尾矿泵送至湿式尾矿库，粗尾矿与废石混合回填",
      "q26q1": "同口径（尾矿设施持续运行）",
      "compare": "无实质变化"
     }
    ],
    "future_lines": [
     {
      "name": "Stage 4 矿坑预剥离（2026-07 起）",
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
   "fc_unit": "万吨/年（100% 推算 · 混合品位 dmt）",
   "fc_2027": [
    {
     "label": "悲观",
     "val": 70,
     "note": "三线利用率不足 + Stage 3 品位走低（年化低于当前 ~72 万吨）"
    },
    {
     "label": "基准",
     "val": 80,
     "note": "三线满产 + Stage 4 按时供矿（750ktpa SC5.5% 产能 → 混合品位 ~80 万吨/年）"
    },
    {
     "label": "乐观",
     "val": 90,
     "note": "三线超产 + 品位回升 + 价格上行释放库存"
    }
   ],
   "capacity_verification": {
    "title": "选矿产能核实（多来源交叉印证）",
    "method": "以 MRL 官网资产页（2025-10 快照）、MRL 年报、季度报告为来源，逐条核对选矿产能；官方未单独披露的标 ⚠️，官方确认的标 ✓。",
    "summary": "Wodgina 三列选矿列车（Train 1/2/3）总产能约 750ktpa SC5.5%（官网原文）或 820ktpa（官网 PDF 另一处表述），采用保守值 ~750ktpa；每列车为球磨+脱泥+磁选+浮选流程。",
    "items": [
     {
      "line": "选矿厂 Train 1/2/3（A1-A3）",
      "excel_capacity": "~250ktpa × 3 = 750ktpa",
      "verified": "✓ 官方确认（总产能口径）",
      "sources": [
       {
        "src": "MRL 官网资产页（2025-10 快照）",
        "data": "three processing trains with a total annual production capacity of approximately 820,000 tonnes of spodumene concentrate at a grade of 5.5% Li2O——三列列车总产能官方确认；每列车含球磨机+脱泥旋流器+磁选+浮选"
       },
       {
        "src": "MRL 官网（2026-08 抓取）",
        "data": "总设计产能约 750,000 t/a SC @ 5.5% Li2O（≈3×250ktpa）——官网另一处表述，取保守值"
       },
       {
        "src": "Q4 FY26 季报",
        "data": "三线利用率提升、Q1 FY27 起三线全开；Q4 产量 94k dmt 为三线运行成果——实际产能利用率验证"
       }
      ]
     },
     {
      "line": "破碎厂（CSI Mining Services 运营）",
      "excel_capacity": "配套选矿厂",
      "verified": "✓ 官方确认",
      "sources": [
       {
        "src": "MRL 官网资产页",
        "data": "破碎厂由 CSI Mining Services（MinRes 子公司）运营，压碎后进入选矿厂"
       },
       {
        "src": "Q4 FY26 季报",
        "data": "TMM 10,100k wmt（100%）、矿石开采 1,118k dmt——采矿+破碎系统满负荷运行"
       }
      ]
     },
     {
      "line": "全矿合计（100% 口径）",
      "excel_capacity": "~750-820ktpa SC5.5%",
      "verified": "✓ 官网双表述（750/820）",
      "sources": [
       {
        "src": "MRL 官网",
        "data": "三列列车总产能 750-820ktpa（官网两处表述差异）——页面取 750ktpa 保守值"
       },
       {
        "src": "FY26 实际",
        "data": "FY26 销量 317k dmt SC6（50%）→ 100% 约 634k——产能利用率约 85%（含爬坡期）"
       }
      ]
     }
    ],
    "note": "核实时间：2026-08-05。关键结论：① 三列选矿列车总产能 750-820ktpa SC5.5%（官网确认）；② 无 Train 4 计划（官网未提及），产能扩张靠矿坑 Stage 4；③ 2023-10-18 起 MRL 权益从 40% 升至 50%（此前 Wodgina 按 40% 披露）。",
    "sources_index": {
     "公司官网": "MRL 资产页（2025-10 快照）+ 官网抓取",
     "公司季报": "MRL 季度活动报告（Q4 FY26 等）",
     "公司公告": "JORC 资源储量更新（2022/2023）、2026-05 FID 公告",
     "数据站": "USGS/Wikipedia/OSM 坐标验证",
     "券商咨询": "本轮未引用（公开数据充分）"
    },
    "images": [
     {
      "url": "img/sat_wodgina.jpg",
      "src": "卫星影像（Yandex Maps，坐标 -21.1746,118.6764）",
      "cap": "Wodgina 矿区卫星影像（Zoom 13）——露天矿坑与选矿厂区在卫星影像上的实际形态，卫星追踪第一参照"
     },
     {
      "url": "img/wodgina_location.jpg",
      "src": "MRL 官网资产页",
      "cap": "Wodgina 位置图——矿区相对 Port Hedland / Marble Bar / Karratha 的位置"
     },
     {
      "url": "img/wa_lithium_map.jpg",
      "src": "MRL 官网",
      "cap": "西澳锂矿分布图（Wodgina/Mt Marion/其他锂矿位置总览）"
     },
     {
      "url": "img/wodgina_processing.jpg",
      "src": "MRL 官网资产页",
      "cap": "Wodgina 选矿厂（三列浮选列车）——项目展示图"
     },
     {
      "url": "img/wodgina_aerial.jpg",
      "src": "MRL 官方媒体库",
      "cap": "Wodgina 矿区航拍全景——露天矿坑与选矿厂布局"
     }
    ],
    "mining_side": {
     "title": "原矿产能核实（矿坑 / 矿体 / 尾矿库）",
     "method": "以 MRL 官网资产页、JORC 资源储量公告（2022/2023）、季报运营描述为来源。",
     "items": [
      {
       "line": "原矿矿山：Wodgina 露天矿",
       "status": "✅ 建成（2019 年前 DSO 时代已开采）",
       "sources": [
        {
         "src": "MRL 官网资产页",
         "data": "露天开采（钻爆-装载-运输循环）；上部 20-50m 强风化、下部坚硬岩石；矿石堆存于 ROM pad"
        },
        {
         "src": "Q4 FY26 季报",
         "data": "26Q2 总物料移动 10,100k wmt（100%）、矿石 1,118k dmt"
        }
       ]
      },
      {
       "line": "矿体与品位（Stage 1-4）",
       "status": "✅ 多阶段矿坑",
       "sources": [
        {
         "src": "MRL 2023 资源储量更新",
         "data": "资源 217.4 Mt @ 1.15% Li₂O（2023-06-30）；储量 164.6 Mt @ 1.15%"
        },
        {
         "src": "Q4 FY26 季报",
         "data": "Stage 2 矿石耗尽、全面转 Stage 3；Stage 4 预剥离 2026 年 7 月启动——多阶段开采规划"
        }
       ]
      },
      {
       "line": "地下开采（未来）",
       "status": "⚠️ 评估中",
       "sources": [
        {
         "src": "MRL 官网资产页",
         "data": "future opportunities to mine ore at depth via underground mining methods which are being assessed——地下开采评估中"
        }
       ]
      },
      {
       "line": "尾矿库（TSF）",
       "status": "✅ 建成",
       "sources": [
        {
         "src": "MRL 官网资产页",
         "data": "细尾矿泵送至湿式尾矿库，粗尾矿与废石混合回填——现场有尾矿储存设施"
        }
       ]
      },
      {
       "line": "废石堆 / ROM pad",
       "status": "✅ 建成",
       "sources": [
        {
         "src": "MRL 官网资产页",
         "data": "废石堆、ROM pad、破碎站为现场基础设施"
        }
       ]
      }
     ],
     "note": "核实时间：2026-08-05。采矿侧要点：① Wodgina 为世界最大已知硬岩锂矿床之一，多阶段露天开采（Stage 1-4）；② 地下开采评估中（官网确认）；③ 2022 年资源 259.2 Mt @ 1.17% → 2023 年 217.4 Mt @ 1.15%（采矿消耗+边界调整），储量 164.6 Mt 支撑多年开采。",
     "images": [
      {
       "url": "img/sat_wodgina.jpg",
       "src": "卫星影像（Yandex Maps）",
       "cap": "Wodgina 矿区卫星影像——矿坑轮廓与选矿厂相对位置"
      },
      {
       "url": "img/wodgina_location.jpg",
       "src": "MRL 官网",
       "cap": "Wodgina 位置图（含 Port Hedland 关系）"
      },
      {
       "url": "img/wodgina_mining.jpg",
       "src": "MRL 官网资产页",
       "cap": "Wodgina 露天采矿（钻爆-装载-运输）实景"
      }
     ]
    }
   }
  },
  {
   "company": "MRL（Mineral Resources）",
   "mine": "Mt Marion",
   "current_q": "26Q2",
   "prev_q": "26Q1",
   "current_q_date": "2026年4-6月",
   "mine_cn": "Mt Marion（马里恩矿山）",
   "report": "MRL Quarterly Activity Report Q4 FY26（2026-07-29 发布，FY26 Q4 / 日历26Q2）；MRL 官网资产页",
   "source_url": "https://www.mineralresources.com.au/our-business/lithium/mt-marion/",
   "equity_note": "100% 资产口径为推算（官方披露 50% attributable 产量、51% 包销份额销量；JV = MinRes 50% / Ganfeng 50%，MinRes 运营）；销量 100% 为 51%÷0.51 估算",
   "history_labels": [
    [
     "production",
     "精矿产量（万吨，100% 推算 · 混合品位 dmt）"
    ],
    [
     "sales",
     "销量（万吨，100% 推算 · 混合品位 dmt）"
    ],
    [
     "prod_sales_ratio",
     "产销比"
    ],
    [
     "avg_price",
     "平均售价（US$/t，CIF SC6）"
    ],
    [
     "cash_cost",
     "单位成本 FOB（A$/t SC6）"
    ]
   ],
   "status_26q2": {
    "existing_lines": [
     {
      "name": "已有产能1：DMS 重介质选矿厂（主回路）— 设计 ~500ktpa SC（5%/3.5% 双品位）",
      "q26q2": "26Q2 产 82k dmt（+3% qoq）；回收率 59%（26Q1: 60%）；矿石分选机（ore sorting）已投产，FY27 处理低品位接触矿堆；矿石来源 N9（N4 完成开采）；DMS 回路按粒度分 3 个产品流",
      "q26q1": "26Q1 产 80k dmt（-1% qoq），回收率 60%；矿石来自 N9/N4；预剥离在 N11 推进",
      "compare": "产量温和 +3%，回收率 59-60% 稳定；ore sorting 投产是 FY27 低品位矿石处理的关键变量——技术升级超预期"
     },
     {
      "name": "已有产能2：浮选厂（在建，FID 2026-05-26）",
      "q26q2": "浮选厂建设推进中（FID 2026-05-26，$240M 100% 口径）；建筑团队已进场早期工程、长周期设备采购已启动；投产后处理 DMS 细粒/低品位产品提升综合回收率",
      "q26q1": "26Q1 浮选厂处于 FID 前评估",
      "compare": "FID 2026-05-26 正式通过（投资 $490M 含浮选+地下+基建）——扩建项目进入执行期，超预期"
     },
     {
      "name": "地下开发（预生产开发）",
      "q26q2": "地下预生产开发 FID（$220M）；2026-07-15 任命 Macmahon 为地下采矿合同伙伴；North/Central 坑内 portal 支护工程 7 月开工；此前 2024 年曾建 exploration decline、2024-12 因市场进入维护，现重启",
      "q26q1": "26Q1 地下开发处于评估/重启准备",
      "compare": "Macmahon 任命（2026-07-15）标志地下开发重启进入执行——重大进展"
     }
    ],
    "future_lines": [
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
   "fc_unit": "万吨/年（100% 推算 · 混合品位 dmt）",
   "fc_2027": [
    {
     "label": "悲观",
     "val": 58,
     "note": "浮选厂延期 + N9→N11 过渡品位波动 + 回收率维持 59%（年化低于当前 ~66 万吨）"
    },
    {
     "label": "基准",
     "val": 66,
     "note": "DMS 满产 + 浮选厂 2027 年中投产（FY26 销量 242k SC6 100% 口径 → 年化 ~66 万吨混合品位）"
    },
    {
     "label": "乐观",
     "val": 76,
     "note": "浮选厂提前投产 + 地下开发贡献 + 回收率升至 63%+"
    }
   ],
   "capacity_verification": {
    "title": "选矿产能核实（多来源交叉印证）",
    "method": "以 MRL 官网资产页、季度报告、FID 公告为来源，逐条核对选矿产能；官方未单独披露的标 ⚠️，官方确认的标 ✓。",
    "summary": "Mt Marion DMS 选矿厂设计年产能约 500,000 t SC（5%/3.5% 双品位）；浮选厂在建（$240M）投产后处理 DMS 细粒产品；地下开发与浮选厂为 FY27-28 主要扩建。",
    "items": [
     {
      "line": "DMS 重介质选矿厂",
      "excel_capacity": "~500ktpa SC（双品位）",
      "verified": "✓ 官网确认（总产能口径）",
      "sources": [
       {
        "src": "MRL 官网资产页",
        "data": "DMS 回路按粒度分 3 个产品流；设计年产能约 500,000 t spodumene concentrate（典型 5% 与 3.5% Li₂O 两种品位）"
       },
       {
        "src": "Q4 FY26 季报",
        "data": "26Q2 产量 82k dmt、回收率 59%；ore sorting 投产——产能利用率与技术进步验证"
       }
      ]
     },
     {
      "line": "浮选厂（在建）",
      "excel_capacity": "处理 DMS 细粒（不新增精矿铭牌）",
      "verified": "✓ FID 确认",
      "sources": [
       {
        "src": "FID 公告 2026-05-26",
        "data": "浮选厂 $240M（100% 口径）；投产后处理 DMS 细粒/低品位产品、提升综合回收率；建筑团队已进场、长周期采购启动"
       },
       {
        "src": "MRL 官网新闻",
        "data": "2024-03 曾宣布锂加工枢纽计划——浮选厂前身"
       }
      ]
     },
     {
      "line": "地下开发（预生产）",
      "excel_capacity": "地下预生产开发 $220M",
      "verified": "✓ FID 确认",
      "sources": [
       {
        "src": "FID 公告 2026-05-26",
        "data": "地下预生产开发 $220M；Macmahon 任命（2026-07-15）；North/Central portal 支护开工"
       },
       {
        "src": "2024-02 资源更新",
        "data": "地下资源 19.3 Mt @ 1.22%（+111%）；North Pit 地下矿体 500m 走向、30-60m 厚、1.2km 深"
       }
      ]
     }
    ],
    "note": "核实时间：2026-08-05。关键结论：① DMS 选矿厂 ~500ktpa（官网确认）；② 浮选厂 FID 2026-05-26（$240M）在建；③ 地下开发 FID 同步通过（$220M）；④ FY27-28 为浮选+地下双项目执行期。",
    "sources_index": {
     "公司官网": "MRL 资产页",
     "公司季报": "MRL 季度活动报告（Q4 FY26 等）",
     "公司公告": "JORC 资源储量更新（2018/2022/2023）、2024-02 地下资源更新、2026-05 FID 公告",
     "数据站": "USGS/Wikipedia/OSM 坐标验证",
     "券商咨询": "本轮未引用（公开数据充分）"
    },
    "images": [
     {
      "url": "img/sat_marion.jpg",
      "src": "卫星影像（Yandex Maps，坐标 -31.0738,121.4611）",
      "cap": "Mt Marion 矿区卫星影像（Zoom 13）——露天矿坑与选矿厂区在卫星影像上的实际形态，卫星追踪第一参照"
     },
     {
      "url": "img/marion_location.jpg",
      "src": "MRL 官网资产页",
      "cap": "Mt Marion 位置图——Kalgoorlie 以北 70km，Goldfields 地区"
     },
     {
      "url": "img/wa_lithium_map.jpg",
      "src": "MRL 官网",
      "cap": "西澳锂矿分布图（Wodgina/Mt Marion/其他锂矿位置总览）"
     },
     {
      "url": "img/marion_processing.jpg",
      "src": "MRL 官网资产页",
      "cap": "Mt Marion DMS 选矿厂——项目展示图"
     },
     {
      "url": "img/marion_drone_fid.jpg",
      "src": "MRL 官网（FID 新闻头图）",
      "cap": "Mt Marion 浮选厂/地下开发 FID 无人机航拍"
     }
    ],
    "mining_side": {
     "title": "原矿产能核实（矿坑 / 矿体 / 尾矿库）",
     "method": "以 MRL 官网资产页、JORC 资源储量公告（2018/2022/2023）、地下资源更新（2024）、季报运营描述为来源。",
     "items": [
      {
       "line": "原矿矿山：Mt Marion 露天矿（北坑 N9/N11 + 南坑）",
       "status": "✅ 建成（2016 年投产）",
       "sources": [
        {
         "src": "MRL 官网资产页",
         "data": "露天锂矿，世界第二大高品位锂资源（约 71 Mt spodumene）；上部 15-40m 风化；新鲜废石密度接近锂辉石，DMS 需控制贫化"
        },
        {
         "src": "Q4 FY26 季报",
         "data": "26Q2 矿石来源 N9（N4 完成）；N11 预剥离推进；TMM 9,578k wmt（+81% qoq）"
        }
       ]
      },
      {
       "line": "矿体与品位（N4/N9/N10/N11 + Central/C2）",
       "status": "✅ 多矿坑多阶段",
       "sources": [
        {
         "src": "MRL 2023 资源储量更新",
         "data": "资源 64.8 Mt @ 1.42%（2023-06-30）；储量 35.7 Mt @ 1.42%（+107%）"
        },
        {
         "src": "2024-02 地下资源更新",
         "data": "地下资源 19.3 Mt @ 1.22%（+111%）；露天 46.8 Mt @ 1.42%——合计 66.1 Mt；North Pit 地下矿体 500m 走向、30-60m 厚、1.2km 深"
        }
       ]
      },
      {
       "line": "地下开发（North/Central portal）",
       "status": "⚠️ 预生产开发（FID 2026-05）",
       "sources": [
        {
         "src": "FID 公告 + Macmahon 任命",
         "data": "地下预生产开发 $220M；2026-07-15 Macmahon 为合同伙伴；portal 支护工程 7 月开工；此前 exploration decline 2024-12 因市场进入维护"
        },
        {
         "src": "2024-02 资源更新",
         "data": "地下资源 19.3 Mt @ 1.22%"
        }
       ]
      },
      {
       "line": "尾矿库（TSF）",
       "status": "✅ 建成",
       "sources": [
        {
         "src": "MRL 官网资产页",
         "data": "现场含尾矿设施（DMS 回路尾矿）"
        }
       ]
      },
      {
       "line": "废石堆 / ROM pad",
       "status": "✅ 建成",
       "sources": [
        {
         "src": "MRL 官网资产页",
         "data": "多个露天矿坑、废石堆、ROM pad 为现场基础设施"
        }
       ]
      }
     ],
     "note": "核实时间：2026-08-05。采矿侧要点：① 露天多坑开采（N4/N9/N11 + Central/C2），北坑为主；② 地下资源 19.3 Mt 支撑地下开发 FID；③ 资源储量：2018 年 71.3 Mt → 2023 年 64.8 Mt 露天 + 19.3 Mt 地下（口径变化+消耗）。",
     "images": [
      {
       "url": "img/sat_marion.jpg",
       "src": "卫星影像（Yandex Maps）",
       "cap": "Mt Marion 矿区卫星影像——矿坑轮廓与选矿厂相对位置"
      },
      {
       "url": "img/marion_location.jpg",
       "src": "MRL 官网",
       "cap": "Mt Marion 位置图（Kalgoorlie 以北 70km）"
      },
      {
       "url": "img/marion_mining.jpg",
       "src": "MRL 官网资产页",
       "cap": "Mt Marion 露天采矿实景（多矿坑）"
      }
     ]
    }
   }
  },
  {
   "company": "Liontown（Liontown Resources）",
   "mine": "Kathleen Valley",
   "current_q": "26Q2",
   "prev_q": "26Q1",
   "current_q_date": "2026年4-6月",
   "mine_cn": "Kathleen Valley（凯瑟琳谷矿山）",
   "report": "Liontown Quarterly Activities Report June 2026（2026-07-29 发布，FY26 Q4 / 日历26Q2）；June Quarter FY26 Results Presentation",
   "source_url": "https://www.liontown.com/project/kathleen-valley/",
   "equity_note": "100% 资产口径（Liontown 全资拥有并运营）；历史承购方含 LG Energy Solution / Tesla / Ford / Canmax；LGES 可转债 2026-01 转股",
   "history_labels": [
    [
     "production",
     "精矿产量（万吨，dmt 实际品位 ~5.0% SC）"
    ],
    [
     "sales",
     "销量（万吨，dmt 实际品位 ~5.0% SC）"
    ],
    [
     "prod_sales_ratio",
     "产销比"
    ],
    [
     "avg_price",
     "平均售价（US$/t，SC6e）"
    ],
    [
     "cash_cost",
     "单位成本 FOB（A$/t sold）"
    ]
   ],
   "status_26q2": {
    "existing_lines": [
     {
      "name": "已有产能1：选矿厂（第四代浮选流程）— 设计 ~500ktpa SC6（2.5Mtpa 原矿）",
      "q26q2": "26Q2 产 103,111 dmt（+7% qoq）、销 108,489 dmt（+29%）；平均品位 5.0%；回收率 ~63%（纯净地下矿时 70%）；工厂可用率 92%；55% 地下矿 + 45% 露天矿入厂",
      "q26q1": "26Q1 产 96,367 dmt（-9% qoq，高基数）；回收率受入料混合影响；露天矿接近收尾（2025-12 完成）",
      "compare": "产量 +7%、销量 +29% 超预期；回收率 63% 仍受露天矿污染拖累——2026 转纯地下后回收率有望升至 70%"
     },
     {
      "name": "已有产能2：地下矿（澳洲首个地下锂矿）",
      "q26q2": "地下开发创纪录 3,316m（+35% qoq）；采出地下矿 356kt；向 2.8Mtpa 原矿运行率（FY27 底）推进；长孔空场采矿+膏体充填（南半球最大膏体厂）",
      "q26q1": "26Q1 地下开发 2,450m（+X%）；地下/露天混合供矿",
      "compare": "开发米数创纪录 +35% 是核心超预期——为 Q2 FY27 起的产量跃升铺路"
     },
     {
      "name": "选矿厂配套：矿石分选（ore sorting）+ 钽副产",
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
   "fc_unit": "万吨 SC6（FY27 指引 390-440k SC6 对应）",
   "fc_2027": [
    {
     "label": "悲观",
     "val": 40,
     "note": "地下爬坡不及预期 + 回收率维持 63%（FY27 指引下沿 390k SC6）"
    },
    {
     "label": "基准",
     "val": 44,
     "note": "FY27 指引中值 415k SC6（390-440k）+ 2.8Mtpa 原矿运行率 FY27 底达成"
    },
    {
     "label": "乐观",
     "val": 50,
     "note": "扩建 FID 后加速 + 纯地下矿回收率 70%+ 提前兑现"
    }
   ],
   "capacity_verification": {
    "title": "选矿产能核实（多来源交叉印证）",
    "method": "以 DFS 2021（ASX 公告 02450567）、2025-09 资源储量更新（61285782）、Liontown 官网、季度报告为来源，逐条核对选矿产能；官方未单独披露的标 ⚠️，官方确认的标 ✓。",
    "summary": "Kathleen Valley 选矿厂（第四代流程：破碎+矿石分选+浮选）设计产能 2.5Mtpa 原矿 → ~500ktpa SC6.0（DFS 2021）；实际爬坡目标 2.8Mtpa 原矿（FY27 底，约 550-560ktpa 精矿）；扩建（球磨机 5.5MW + NW Flats）FID 预计 Q1 FY27 底。",
    "items": [
     {
      "line": "选矿厂（第四代浮选流程）",
      "excel_capacity": "~500ktpa SC6（2.5Mtpa 原矿）",
      "verified": "✓ DFS 官方确认（设计口径）",
      "sources": [
       {
        "src": "DFS 2021-11-11（ASX 02450567）",
        "data": "基准产能 2.5Mtpa 原矿 → ~500ktpa SC6.0；第 6 年扩至 4Mtpa → ~700ktpa；建厂 Q3 2022-Q4 2023、投产 Q2 2024"
       },
       {
        "src": "Liontown 官网资产页",
        "data": "爬坡至 2.8Mtpa 原矿（FY27 底）；第四代选矿厂；南半球最大膏体充填厂"
       },
       {
        "src": "2025-09 资源储量更新",
        "data": "地下矿设计 ~2.8Mtpa（FY2031 前），NW 开发后 3.0Mtpa（FY2031-2046）"
       }
      ]
     },
     {
      "line": "矿石分选（ore sorting）",
      "excel_capacity": "2 列 Steinert（20ktpm 上限）",
      "verified": "✓ 官方确认",
      "sources": [
       {
        "src": "2025-09 资源储量更新",
        "data": "Steinert ore sorting trains 2 列，处理上限 20ktpm；分选精矿计入储量"
       },
       {
        "src": "Q4 FY26 季报",
        "data": "26Q2 55% 地下矿 + 45% 露天矿入厂，矿石分选持续运行"
       }
      ]
     },
     {
      "line": "扩建（FID Q1 FY27 底）",
      "excel_capacity": "球磨机 5.5MW + NW Flats",
      "verified": "✓ 官方公告（2026-04-29）",
      "sources": [
       {
        "src": "June FY26 Results Presentation",
        "data": "FID 预计 Q1 FY27 底；球磨机 5.5MW 采购为关键路径；NW Flats 地下开发从 Kathleen's Corner 露天坑进入；MSA Stage 1 建设"
       },
       {
        "src": "新闻 2026-04-29",
        "data": "early works + long-lead procurement 已启动；FY26 early works $14M、FID 前最高 $77M"
       }
      ]
     }
    ],
    "note": "核实时间：2026-08-05。关键结论：① DFS 设计 500ktpa SC6（2.5Mtpa 原矿），2024-11 战略调整至 2.8Mtpa 运行率（FY27 底），工厂设计产能 3.0Mtpa；② 扩建 FID 锁定 Q1 FY27 底（球磨机+NW Flats+MSA），4Mtpa 扩建路径保留；③ FY26 产 392k dmt 达指引中段；④ FY27 指引：精矿 390-440k SC6、FOB A$1,050-1,250、资本开支 A$320-370M；⑤ 2026 转纯地下开采（露天 2025-12 完成）。",
    "sources_index": {
     "公司公告": "DFS 2021、2025-09 资源储量更新、2026-04 扩建公告、季度报告",
     "公司官网": "Kathleen Valley 资产页（含 Google Earth 位置图）",
     "公司展示": "June Quarter FY26 Results（2026-07-29）",
     "数据站": "USGS/Wikipedia/OSM 坐标验证",
     "券商咨询": "本轮未引用（公开数据充分）"
    },
    "images": [
     {
      "url": "img/kv_google_earth.jpg",
      "src": "Liontown 官网（Google Earth 图）",
      "cap": "Kathleen Valley 位置图（Google Earth 底图）——Leinster 以北 60km、Geraldton 港出口，卫星追踪区域参照"
     },
     {
      "url": "img/sat_kathleen_z13.jpg",
      "src": "卫星影像（Yandex Maps，坐标 -27.4678,120.7047）",
      "cap": "Kathleen Valley 矿区卫星影像（Zoom 13）——地下矿/露天坑/选矿厂在卫星影像上的实际形态，卫星追踪第一参照"
     },
     {
      "url": "img/kv_main_overview.jpg",
      "src": "Liontown 官网（2026-05-19）",
      "cap": "Kathleen Valley 主视图（2026-05）——选矿厂与矿区布局总览"
     },
     {
      "url": "img/kv_process_plant.jpg",
      "src": "Liontown 官网",
      "cap": "Kathleen Valley 选矿厂（第四代浮选流程）——项目展示图"
     },
     {
      "url": "img/kv_ore_circuit.jpg",
      "src": "Liontown 官网",
      "cap": "全矿石浮选回路——选矿工艺项目图"
     }
    ],
    "mining_side": {
     "title": "原矿产能核实（矿坑 / 矿体 / 尾矿库）",
     "method": "以 DFS 2021、2025-09 资源储量更新、Liontown 官网、季度报告为来源。",
     "items": [
      {
       "line": "原矿矿山：露天矿（Kathleen's Corner / Mt Mann）",
       "status": "✅ 建成（2024-07 投产）；⚠️ 2025-12 完成开采",
       "sources": [
        {
         "src": "2025-09 资源储量更新",
         "data": "露天开采 2025 年 12 月完成，之后转纯地下；露天矿体 Kathleen's Corner 与 Mt Mann"
        },
        {
         "src": "Q4 FY26 季报",
         "data": "26Q2 45% 露天矿入厂（收尾阶段）"
        }
       ]
      },
      {
       "line": "地下矿（澳洲首个地下锂矿）",
       "status": "✅ 建成（2024 起开发）",
       "sources": [
        {
         "src": "Liontown 官网",
         "data": "澳洲首个地下锂矿、全球首批之一；长孔空场采矿+膏体充填；地下矿减少环境足迹、瞄准高品位矿"
        },
        {
         "src": "Q4 FY26 季报",
         "data": "地下开发 3,316m 创纪录（+35% qoq）；26Q2 采出地下矿 356kt；2.8Mtpa 目标 FY27 底"
        }
       ]
      },
      {
       "line": "矿体与品位（Kathleen's Corner / Mt Mann / NW Flats）",
       "status": "✅ 多矿体",
       "sources": [
        {
         "src": "2025-09 资源储量更新",
         "data": "资源 150Mt @ 1.33% Li₂O（2025-09）；储量 71.7Mt @ 1.32%；2024-06 资源 155Mt @ 1.34%"
        },
        {
         "src": "DFS 2021",
         "data": "Ore Reserve 68.5Mt @ 1.34%（2021）；生产库存 82.7Mt @ 1.30%；品位 1.3-1.4% Li₂O"
        }
       ]
      },
      {
       "line": "膏体充填厂（paste plant）",
       "status": "✅ 建成（南半球最大）",
       "sources": [
        {
         "src": "Liontown 官网",
         "data": "南半球最大膏体充填厂——尾矿回填地下采空区，减少地表尾矿库"
        },
        {
         "src": "DFS 2021",
         "data": "地下开采产生 ~7Mt 废石回填露天坑/地表堆场"
        }
       ]
      },
      {
       "line": "尾矿设施（TSF）",
       "status": "✅ 建成",
       "sources": [
        {
         "src": "Liontown 官网",
         "data": "尾矿管理含膏体回填与地表储存（Tailings and Waste Rock Policy 2025-10）"
        }
       ]
      }
     ],
     "note": "核实时间：2026-08-05。采矿侧要点：① 露天+地下双模式，2026 起转纯地下（露天 2025-12 完成）；② 地下矿为全球首批之一，膏体充填减少地表尾矿；③ 资源 150Mt @ 1.33% 支撑长寿命（矿山寿命 >20 年）；④ NW Flats 为下一开发区域（扩建 FID 范围）。",
     "images": [
      {
       "url": "img/sat_kathleen_z13.jpg",
       "src": "卫星影像（Yandex Maps）",
       "cap": "Kathleen Valley 矿区卫星影像——露天坑/地下矿口/选矿厂相对位置"
      },
      {
       "url": "img/kv_google_earth.jpg",
       "src": "Liontown 官网",
       "cap": "Kathleen Valley 位置图（Google Earth 底图，含 Geraldton 港关系）"
      },
      {
       "url": "img/kv_underground.jpg",
       "src": "Liontown 官网",
       "cap": "澳洲首个地下锂矿——地下开采实景"
      }
     ]
    }
   }
  },
  {
   "company": "MRL（Mineral Resources）",
   "mine": "Bald Hill",
   "current_q": "26Q2",
   "prev_q": "26Q1",
   "current_q_date": "2026年4-6月",
   "mine_cn": "Bald Hill（秃山矿山）",
   "report": "MRL Quarterly Activity Report Q4 FY26（2026-07-29 发布）；Bald Hill lithium mine restart 公告（2026-05-18）；Bald Hill Operations and Mineral Resources Update（2024-11-13）",
   "source_url": "https://www.mineralresources.com.au/our-business/lithium/bald-hill/",
   "equity_note": "100% 资产口径（MinRes 全资拥有并运营）；原属 Tawana Resources/Alliance Mineral Assets（后合并为 Alita Resources），Alita 2019-08-29 自愿托管（KordaMentha）、2024-04-04 清算终止；MinRes 2023-09-04 签约收购、2023-11-01 生效；2024-11 C&M、2026-05 复产",
   "history_labels": [
    [
     "production",
     "精矿产量（万吨，100% · 混合品位 dmt）"
    ],
    [
     "sales",
     "销量（万吨，100% · 混合品位 dmt）"
    ],
    [
     "prod_sales_ratio",
     "产销比"
    ],
    [
     "avg_price",
     "平均售价（US$/t，SC6）"
    ],
    [
     "cash_cost",
     "单位成本 FOB（A$/t，SC6）"
    ]
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
      "name": "已有产能2：露天矿（采矿服务全内部）",
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
   "fc_unit": "万吨 SC6（满产 140k dmt SC6/年对应）",
   "fc_2027": [
    {
     "label": "悲观",
     "val": 12,
     "note": "满产爬坡延迟（Q2 FY27 未达 140k）+ 锂价回落影响销售节奏"
    },
    {
     "label": "基准",
     "val": 14,
     "note": "Q2 FY27 满产 140k dmt SC6/年兑现，2027 年全年满产运行（= 14 万吨 SC6）"
    },
    {
     "label": "乐观",
     "val": 17,
     "note": "选矿厂扩建研究通过 + 2027 年内新增产能释放"
    }
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
       {
        "src": "MRL 官网资产页",
        "data": "annual production capacity of approximately 165,000 tonnes of spodumene concentrate at a grade of 5.1% Li2O；破碎厂 2024 年新建、DMS/spirals 厂 2018 年建（2019 C&M、2022 重启）"
       },
       {
        "src": "Bald Hill restart 公告（2026-05-18）",
        "data": "production capacity of circa 165,000 dmt per annum of 5.1% spodumene concentrate, equivalent to 140,000 dmt SC6 per annum——165kt SC5.1% = 140kt SC6 换算自洽"
       },
       {
        "src": "Q4 FY26 季报",
        "data": "ramp-up to full capacity of 140k dmt SC6 is on track for Q2 FY27；MinRes studying plant expansion options"
       },
       {
        "src": "2023-11 收购公告（MinRes 官网新闻）",
        "data": "收购时口径 circa 150,000 tpa @ 5.5% 精矿——产能表述沿革（150kt SC5.5% → 165kt SC5.1%）"
       }
      ]
     },
     {
      "line": "加工流程",
      "excel_capacity": "DMS 重介质 + spirals（2018）+ 新破碎厂（2024）",
      "verified": "✓ 官方确认",
      "sources": [
       {
        "src": "MRL 官网资产页",
        "data": "crushing and processing plant via Dense Media Separation (DMS) concentrator；crushing plant – a new plant was commissioned in 2024"
       },
       {
        "src": "2017-07 PFS（Tawana，被收购前时代）",
        "data": "1,200 ktpa 锂辉石 DMS 回路 + 独立钽厂 350 ktpa；capex A$42M（全澳最低）、IRR 185%、12 个月回本、~155,000 tpa SC + 260,000 lbs/yr Ta₂O₅；包销 US$880/t（6% Li₂O，FOB Esperance）"
       },
       {
        "src": "2024-11-13 更新公告",
        "data": "spodumene concentrate plant 在 C&M 期间保养，复产爬坡 4-6 周（公告口径）"
       }
      ]
     },
     {
      "line": "全矿合计（满产）",
      "excel_capacity": "140kt SC6/年",
      "verified": "✓ 官方目标（Q2 FY27）",
      "sources": [
       {
        "src": "Q4 FY26 季报",
        "data": "Ramp-up to full capacity of 140k dmt SC6 is on track for Q2 FY27——官方满产目标"
       },
       {
        "src": "锂业现场会（2026-05-19）",
        "data": "Bald Hill 100% internal 服务链（采矿/破碎/加工/运输全自营）；MinRes 将成全球唯一运营三个硬岩锂矿的公司"
       }
      ]
     }
    ],
    "note": "核实时间：2026-08-05。关键结论：① 选矿产能 165ktpa SC5.1% = 140kt SC6/年（官网+公告双确认）；② 2026-05 复产、6 月首产、7 月首运、Q2 FY27 满产——复产时间线按计划兑现；③ 选矿厂扩建研究启动（增产+延长寿命）；④ 重启成本 ~$20M、~370 岗位；⑤ FY27 指引（销量/FOB/capex）2026 年 8 月发布。",
    "sources_index": {
     "公司公告": "2026-05-18 重启公告、2024-11-13 资源储量更新、Q4 FY26 季报",
     "公司官网": "Bald Hill 资产页（含位置图）",
     "公司展示": "2026-05-19 锂业现场会展示",
     "历史公告": "Tawana 2018-06-06（被收购前）",
     "数据站": "WA MINEDEX（登记号 87101）、Wikipedia"
    },
    "images": [
     {
      "url": "img/sat_baldhill_z13.jpg",
      "src": "卫星影像（Yandex Maps，坐标 ≈-31.52,121.97 推算）",
      "cap": "Bald Hill 矿区卫星影像（Zoom 13）——Kambalda 东南 50km，卫星追踪第一参照"
     },
     {
      "url": "img/baldhill_map.png",
      "src": "MRL 官网",
      "cap": "Bald Hill 位置图（西澳全州示意）——Kalgoorlie/Mt Marion/Esperance 港关系，卫星追踪区域参照"
     },
     {
      "url": "img/baldhill_processing.jpg",
      "src": "MRL 官网",
      "cap": "Bald Hill 选矿厂（DMS + spirals + 2024 新破碎厂）"
     },
     {
      "url": "img/baldhill_ops.jpg",
      "src": "MRL 官网",
      "cap": "Bald Hill 矿区运营总览（露天矿 + 选矿厂）"
     },
     {
      "url": "img/baldhill_drone.jpg",
      "src": "MRL 官网（无人机航拍）",
      "cap": "Bald Hill 矿区无人机航拍——复产后的现场实景"
     }
    ],
    "mining_side": {
     "title": "原矿产能核实（矿坑 / 矿体 / 尾矿库 · 复产阶段矿山）",
     "method": "以 2024-11-13 资源储量更新、Tawana 2018 历史公告、MRL 官网、Q4 FY26 季报为来源。",
     "items": [
      {
       "line": "原矿矿山：Bald Hill 露天矿",
       "status": "✅ 建成（钽矿时代已开采；2019 起锂生产）",
       "sources": [
        {
         "src": "MRL 官网资产页",
         "data": "originally mined for tantalum, before commencing spodumene production in 2019；open pit mine, waste dumps, ROM pad and tailings storage facility"
        },
        {
         "src": "Q4 FY26 季报",
         "data": "2026-05 复产：pit was dewatered, enabling mining operations to ramp up（坑内抽水完成）；26Q2 TMM 426k wmt、矿石 15k dmt"
        }
       ]
      },
      {
       "line": "矿体与资源（多伟晶岩脉）",
       "status": "✅ 资源确认；⚠️ 储量未更新",
       "sources": [
        {
         "src": "2024-11-13 资源储量更新",
         "data": "Mineral Resources 58.1Mt @ 0.94% Li₂O（2024-06-30，>0.3% 边界，扣开采）：Indicated 17.2Mt @ 0.91% + Inferred 40.9Mt @ 0.95%（无 Measured）；较 2018-06 的 21.7Mt +168%（777 解释孔+599 估算孔）；矿权 M15/400（501 公顷）；权利金 5%"
        },
        {
         "src": "Tawana 2018-06-06 公告",
         "data": "资源 26.5Mt @ 0.96% Li₂O（149ppm Ta₂O₅）；储量 11.3Mt @ 1.01% Li₂O + 160ppm Ta₂O₅；钽储量 2.0Mt @ 313ppm——矿山寿命 9 年 @ 1.2Mtpa（被收购前时代）"
        },
        {
         "src": "MRL Resources & Reserves 页面",
         "data": "仅列 Bald Hill Resources（2024-11-13），无 Reserves 条目——MRL 未发布最新储量"
        }
       ]
      },
      {
       "line": "环评与许可（WA 政府）",
       "status": "✅ 已获批（DMP/DWER 体系）",
       "sources": [
        {
         "src": "2017-07-24 公告（Tawana+AMAL）",
         "data": "ENVIRONMENTAL APPROVALS FINALISED：DWER 修订运营许可（1.2Mtpa DMS 建设运营）+ DMP 更新 Environmental Mining Proposal 批准"
        },
        {
         "src": "MINEDEX 环境登记 #87101",
         "data": "Bald Hill Tantalum-Lithium Project：Mining Proposal + Mine Closure Plan，V4 Rev1 2020-08；矿权 M15/400、G15/28、L15/348、L15/384、L15/366、L15/365、M15/1305、M15/1308"
        },
        {
         "src": "EPA 检索",
         "data": "EPA（西澳环保局）正式评估：未检索到——项目通过 DMP Mining Proposal + DWER 运营许可体系监管（诚实标注：未找到）"
        }
       ]
      },
      {
       "line": "尾矿库（TSF）",
       "status": "✅ 建成",
       "sources": [
        {
         "src": "MRL 官网资产页",
         "data": "tailings storage facility 为现场基础设施之一；C&M 期间保养"
        }
       ]
      },
      {
       "line": "基础设施（营地/发电/供水）",
       "status": "✅ 建成（FIFO 营地 300 人）",
       "sources": [
        {
         "src": "MRL 官网资产页",
         "data": "workshops, offices, diesel power generation and bore fields；FIFO camp accommodation up to 300 people"
        },
        {
         "src": "2024-11-13 公告",
         "data": "C&M 时 ~300 员工受影响；复产新增 ~370 岗位"
        }
       ]
      }
     ],
     "note": "核实时间：2026-08-05。采矿侧要点：① 露天矿（钽矿转型锂矿 2019 首产）；② 资源 58.1Mt @ 0.94%（2024-06，Indicated 17.2 + Inferred 40.9，无 Measured），历史储量 11.3Mt @ 1.01%（2018，Tawana 时代）——MRL 未发布最新储量；③ 2017-07 PFS：1.2Mtpa DMS 回路、capex A$42M、矿山寿命 9 年（@1.2Mtpa）；④ 环评经 DMP Mining Proposal + DWER 运营许可（2017-07-24 批准），MINEDEX 登记 #87101；EPA 正式评估未检索到；⑤ 2026-05 复产坑抽水完成、采矿爬坡；⑥ Alita 时代产量轨迹：2018-03 投产、CY2018 产 51k wmt SC6、2019 指引 180k SC6/年。",
     "images": [
      {
       "url": "img/sat_baldhill_z13.jpg",
       "src": "卫星影像（Yandex Maps）",
       "cap": "Bald Hill 露天矿/选矿厂卫星影像——复产现场相对位置"
      },
      {
       "url": "img/baldhill_mining.jpg",
       "src": "MRL 官网",
       "cap": "Bald Hill 露天开采作业（钻爆-装载-运输循环）"
      },
      {
       "url": "img/baldhill_tsf.jpg",
       "src": "MRL 官网",
       "cap": "Bald Hill 尾矿库与矿区设施"
      }
     ]
    }
   }
  }
 ],
 "quarters": [
  "2019Q1",
  "2019Q2",
  "2019Q3",
  "2019Q4",
  "2020Q1",
  "2020Q2",
  "2020Q3",
  "2020Q4",
  "2021Q1",
  "2021Q2",
  "2021Q3",
  "2021Q4",
  "2022Q1",
  "2022Q2",
  "2022Q3",
  "2022Q4",
  "2023Q1",
  "2023Q2",
  "2023Q3",
  "2023Q4",
  "2024Q1",
  "2024Q2",
  "2024Q3",
  "2024Q4",
  "2025Q1",
  "2025Q2",
  "2025Q3",
  "2025Q4",
  "2026Q1",
  "2026Q2",
  "2026Q3",
  "2026Q4"
 ],
 "history": {
  "production": [
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   26.799999999999997,
   25.8,
   27.1,
   33.8,
   36.1,
   37.9,
   35.599999999999994,
   39.5,
   41.37,
   35.77,
   28,
   33.2,
   40.6,
   39.2,
   34.1,
   34,
   32,
   35.2,
   35.1,
   38.7,
   41.25,
   41.25
  ],
  "lce": [
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   3.3499999999999996,
   3.225,
   3.3875,
   4.225,
   4.5125,
   4.7375,
   4.449999999999999,
   4.9375,
   5.17125,
   4.47125,
   3.5,
   4.15,
   5.075,
   4.9,
   4.2625,
   4.25,
   4,
   4.4,
   4.3875,
   4.8375,
   5.15625,
   5.15625
  ],
  "tech_grade": [
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   3.9,
   4,
   4.1,
   3.3,
   3,
   3,
   2.8,
   2.1,
   0.73,
   1.88,
   1.9,
   0.2,
   null,
   3.3,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null
  ],
  "chem_grade": [
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   22.9,
   21.8,
   23,
   30.5,
   33.1,
   34.9,
   32.8,
   37.4,
   40.64,
   33.89,
   26.1,
   33,
   null,
   35.9,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null
  ],
  "sales": [
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   27,
   35.5,
   33.8,
   38.6,
   33.6,
   42.9,
   39.2,
   27.5,
   18.3,
   53,
   39.2,
   31.2,
   36.6,
   41.2,
   30.1,
   32.8,
   34.9,
   39.1,
   null,
   null
  ],
  "inv_change": [
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   0.10000000000000142,
   -1.7000000000000028,
   2.3000000000000043,
   -0.7000000000000028,
   1.999999999999993,
   -3.3999999999999986,
   2.1699999999999946,
   8.270000000000003,
   9.7,
   -19.799999999999997,
   1.3999999999999986,
   8.000000000000004,
   -2.5,
   -7.200000000000003,
   1.8999999999999986,
   2.4000000000000057,
   0.20000000000000284,
   -0.3999999999999986,
   null,
   null
  ],
  "inventory": [
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   29.6,
   31.599999999999987,
   28.199999999999996,
   30.36999999999999,
   38.639999999999986,
   48.33999999999999,
   28.539999999999992,
   29.939999999999984,
   37.93999999999998,
   35.43999999999999,
   28.239999999999995,
   30.139999999999993,
   32.540000000000006,
   32.740000000000016,
   32.340000000000025,
   null,
   null
  ],
  "prod_sales_ratio": [
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   1.0502958579881658,
   0.9362880886426591,
   1.0184696569920846,
   0.9438202247191013,
   1.0860759493670886,
   0.9475465313028766,
   0.7688006709533127,
   0.6535714285714286,
   1.5963855421686746,
   0.9655172413793104,
   0.7959183673469387,
   1.0733137829912023,
   1.211764705882353,
   0.940625,
   0.9318181818181817,
   0.9943019943019942,
   1.0103359173126614,
   null,
   null
  ],
  "avg_price": [
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   592,
   592,
   1770,
   1755,
   3729,
   3984,
   5783,
   5431,
   3740,
   3016,
   1034,
   1020,
   872,
   736,
   791,
   725,
   730,
   850,
   1668,
   2286,
   null,
   null
  ],
  "cost_with_royalty": [
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   310,
   388,
   476,
   618,
   660,
   757,
   690,
   585,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null
  ],
  "cost_no_royalty": [
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   219,
   242,
   235,
   254,
   253,
   263,
   292,
   304,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null
  ],
  "cash_cost": [
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   null,
   224,
   226,
   253,
   271,
   262,
   357,
   386,
   338,
   277,
   324,
   341,
   366,
   388,
   373,
   446,
   448,
   null,
   null
  ]
 },
 "history_labels": [
  [
   "production",
   "精矿产量（万吨，SC6 折算 6% Li₂O）"
  ],
  [
   "lce",
   "精矿产量（6%,LCE）"
  ],
  [
   "tech_grade",
   "技术级精矿产量（万吨，实际品位）"
  ],
  [
   "chem_grade",
   "化学级精矿产量（万吨，实际品位）"
  ],
  [
   "sales",
   "销量（万吨，SC6 折算 6% Li₂O）"
  ],
  [
   "inv_change",
   "库存变动量（万吨）"
  ],
  [
   "inventory",
   "库存（万吨）"
  ],
  [
   "prod_sales_ratio",
   "产销比"
  ],
  [
   "avg_price",
   "平均售价（US$/t，SC6）"
  ],
  [
   "cost_with_royalty",
   "单位成本—含权益金（A$/t，FOB SC6）"
  ],
  [
   "cost_no_royalty",
   "单位成本—不含权益金（A$/t，FOB SC6）"
  ],
  [
   "cash_cost",
   "cash cost（A$/t，FOB SC6）"
  ]
 ],
 "pilgangoora": {
  "quarters": [
   "2019Q1",
   "2019Q2",
   "2019Q3",
   "2019Q4",
   "2020Q1",
   "2020Q2",
   "2020Q3",
   "2020Q4",
   "2021Q1",
   "2021Q2",
   "2021Q3",
   "2021Q4",
   "2022Q1",
   "2022Q2",
   "2022Q3",
   "2022Q4",
   "2023Q1",
   "2023Q2",
   "2023Q3",
   "2023Q4",
   "2024Q1",
   "2024Q2",
   "2024Q3",
   "2024Q4",
   "2025Q1",
   "2025Q2",
   "2025Q3",
   "2025Q4",
   "2026Q1",
   "2026Q2",
   "2026Q3",
   "2026Q4"
  ],
  "history": {
   "production": [
    null,
    null,
    null,
    null,
    2.03,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    14.71,
    16.22,
    null,
    null,
    null,
    null,
    null,
    null,
    19.44,
    16.62,
    11.04,
    18.81,
    19.86,
    18.03,
    23.24,
    21.43,
    26.6,
    26.6
   ],
   "lce": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
   ],
   "tech_grade": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
   ],
   "chem_grade": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
   ],
   "sales": [
    null,
    null,
    null,
    null,
    3.37,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    13.82,
    14.86,
    null,
    null,
    null,
    null,
    null,
    null,
    18.95,
    18.03,
    11.09,
    18.36,
    18.9,
    20.11,
    19.57,
    24.99,
    null,
    null
   ],
   "inv_change": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
   ],
   "inventory": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
   ],
   "prod_sales_ratio": [
    null,
    null,
    null,
    null,
    1.66,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    0.939,
    0.916,
    null,
    null,
    null,
    null,
    null,
    null,
    0.975,
    1.085,
    1.005,
    0.976,
    0.952,
    1.115,
    0.842,
    1.166,
    null,
    null
   ],
   "avg_price": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    5668,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    1161,
    1867,
    2107,
    null,
    null
   ],
   "cost_with_royalty": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    579,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    585,
    520,
    616,
    null,
    null
   ],
   "cost_no_royalty": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
   ],
   "cash_cost": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    579,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    585,
    520,
    616,
    null,
    null
   ],
   "cif_cost": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    717,
    733,
    845,
    null,
    null
   ]
  },
  "yearly": {
   "2019": 8.0,
   "2020": 20.6,
   "2021": 32.6,
   "2022": 36.2,
   "2023": 62.0,
   "2024": 72.6,
   "2025": 75.5,
   "2026": 88.0
  }
 },
 "wodgina": {
  "quarters": [
   "2019Q1",
   "2019Q2",
   "2019Q3",
   "2019Q4",
   "2020Q1",
   "2020Q2",
   "2020Q3",
   "2020Q4",
   "2021Q1",
   "2021Q2",
   "2021Q3",
   "2021Q4",
   "2022Q1",
   "2022Q2",
   "2022Q3",
   "2022Q4",
   "2023Q1",
   "2023Q2",
   "2023Q3",
   "2023Q4",
   "2024Q1",
   "2024Q2",
   "2024Q3",
   "2024Q4",
   "2025Q1",
   "2025Q2",
   "2025Q3",
   "2025Q4",
   "2026Q1",
   "2026Q2",
   "2026Q3",
   "2026Q4"
  ],
  "history": {
   "production": [
    null,
    null,
    2.2,
    null,
    0.0,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    6.4,
    9.2,
    8.8,
    10.25,
    22.6,
    23.0,
    null,
    12.6,
    10.2,
    10.8,
    12.6,
    16.6,
    17.6,
    17.0,
    15.6,
    18.8,
    21.0,
    21.0
   ],
   "lce": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
   ],
   "tech_grade": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
   ],
   "chem_grade": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
   ],
   "sales": [
    null,
    null,
    0.3,
    null,
    0.0,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    6.6,
    9.5,
    9.8,
    9.25,
    12.4,
    28.4,
    null,
    12.4,
    9.2,
    12.2,
    11.8,
    13.6,
    19.4,
    16.8,
    13.8,
    20.0,
    null,
    null
   ],
   "inv_change": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
   ],
   "inventory": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
   ],
   "prod_sales_ratio": [
    null,
    null,
    0.136,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    1.031,
    1.033,
    1.114,
    0.902,
    0.549,
    1.235,
    null,
    0.984,
    0.902,
    1.13,
    0.937,
    0.819,
    1.102,
    0.988,
    0.885,
    1.064,
    null,
    null
   ],
   "avg_price": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    1243,
    842,
    834,
    846,
    674,
    881,
    1140,
    2130,
    2450,
    null,
    null
   ],
   "cost_with_royalty": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    949,
    1217,
    868,
    775,
    641,
    733,
    717,
    805,
    714,
    null,
    null
   ],
   "cost_no_royalty": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
   ],
   "cash_cost": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    949,
    1217,
    868,
    775,
    641,
    733,
    717,
    805,
    714,
    null,
    null
   ],
   "cif_cost": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
   ]
  },
  "yearly": {
   "2020": 0.0,
   "2022": 16.2,
   "2023": 74.1,
   "2024": 64.4,
   "2025": 75.5,
   "2026": 68.7
  }
 },
 "marion": {
  "quarters": [
   "2019Q1",
   "2019Q2",
   "2019Q3",
   "2019Q4",
   "2020Q1",
   "2020Q2",
   "2020Q3",
   "2020Q4",
   "2021Q1",
   "2021Q2",
   "2021Q3",
   "2021Q4",
   "2022Q1",
   "2022Q2",
   "2022Q3",
   "2022Q4",
   "2023Q1",
   "2023Q2",
   "2023Q3",
   "2023Q4",
   "2024Q1",
   "2024Q2",
   "2024Q3",
   "2024Q4",
   "2025Q1",
   "2025Q2",
   "2025Q3",
   "2025Q4",
   "2026Q1",
   "2026Q2",
   "2026Q3",
   "2026Q4"
  ],
  "history": {
   "production": [
    null,
    null,
    null,
    12.4,
    11.6,
    null,
    13.3,
    null,
    null,
    11.4,
    10.1,
    9.8,
    null,
    12.8,
    10.8,
    12.1,
    12.0,
    12.0,
    12.8,
    16.6,
    null,
    17.8,
    13.6,
    11.6,
    14.0,
    12.4,
    14.6,
    16.2,
    16.0,
    16.4,
    16.5,
    16.5
   ],
   "lce": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
   ],
   "tech_grade": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
   ],
   "chem_grade": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
   ],
   "sales": [
    null,
    null,
    null,
    9.9,
    11.0,
    null,
    11.8,
    null,
    null,
    15.5,
    3.6,
    6.9,
    null,
    7.2,
    11.1,
    11.6,
    12.4,
    12.2,
    12.8,
    17.2,
    null,
    19.0,
    22.2,
    11.2,
    13.8,
    13.4,
    14.2,
    17.8,
    14.2,
    18.8,
    null,
    null
   ],
   "inv_change": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
   ],
   "inventory": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
   ],
   "prod_sales_ratio": [
    null,
    null,
    null,
    0.798,
    0.948,
    null,
    0.887,
    null,
    null,
    1.36,
    0.356,
    0.704,
    null,
    0.562,
    1.028,
    0.959,
    1.033,
    1.017,
    1.0,
    1.036,
    null,
    1.067,
    1.632,
    0.966,
    0.986,
    1.081,
    0.973,
    1.099,
    0.887,
    1.146,
    null,
    null
   ],
   "avg_price": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    3262,
    4151,
    null,
    2589,
    null,
    1060,
    null,
    1139,
    813,
    816,
    845,
    607,
    797,
    1042,
    2076,
    2392,
    null,
    null
   ],
   "cost_with_royalty": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    844,
    null,
    683,
    1020,
    1176,
    708,
    717,
    796,
    812,
    903,
    878,
    null,
    null
   ],
   "cost_no_royalty": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
   ],
   "cash_cost": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    844,
    null,
    683,
    1020,
    1176,
    708,
    717,
    796,
    812,
    903,
    878,
    null,
    null
   ],
   "cif_cost": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
   ]
  },
  "yearly": {
   "2020": 42.4,
   "2021": 45.4,
   "2022": 48.6,
   "2023": 46.6,
   "2024": 54.2,
   "2025": 52.8,
   "2026": 61.0
  }
 },
 "kathleenvalley": {
  "quarters": [
   "2019Q1",
   "2019Q2",
   "2019Q3",
   "2019Q4",
   "2020Q1",
   "2020Q2",
   "2020Q3",
   "2020Q4",
   "2021Q1",
   "2021Q2",
   "2021Q3",
   "2021Q4",
   "2022Q1",
   "2022Q2",
   "2022Q3",
   "2022Q4",
   "2023Q1",
   "2023Q2",
   "2023Q3",
   "2023Q4",
   "2024Q1",
   "2024Q2",
   "2024Q3",
   "2024Q4",
   "2025Q1",
   "2025Q2",
   "2025Q3",
   "2025Q4",
   "2026Q1",
   "2026Q2",
   "2026Q3",
   "2026Q4"
  ],
  "history": {
   "production": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    3.0,
    9.2,
    9.6,
    8.6,
    8.7,
    10.5,
    9.6,
    10.3,
    10.8,
    11.2
   ],
   "lce": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
   ],
   "tech_grade": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
   ],
   "chem_grade": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
   ],
   "sales": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    1.0,
    8.5,
    9.4,
    9.7,
    7.7,
    11.2,
    8.4,
    10.8,
    null,
    null
   ],
   "inv_change": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
   ],
   "inventory": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
   ],
   "prod_sales_ratio": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    0.333,
    0.924,
    0.979,
    1.128,
    0.885,
    1.067,
    0.875,
    1.049,
    null,
    null
   ],
   "avg_price": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    815,
    740,
    700,
    900,
    1845,
    1880,
    null,
    null
   ],
   "cost_with_royalty": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    702,
    898,
    1093,
    910,
    981,
    995,
    null,
    null
   ],
   "cost_no_royalty": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
   ],
   "cash_cost": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    702,
    898,
    1093,
    910,
    981,
    995,
    null,
    null
   ],
   "cif_cost": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
   ]
  },
  "yearly": {
   "2024": 12.2,
   "2025": 29.5,
   "2026": 39.2
  }
 },
 "baldhill": {
  "quarters": [
   "2019Q1",
   "2019Q2",
   "2019Q3",
   "2019Q4",
   "2020Q1",
   "2020Q2",
   "2020Q3",
   "2020Q4",
   "2021Q1",
   "2021Q2",
   "2021Q3",
   "2021Q4",
   "2022Q1",
   "2022Q2",
   "2022Q3",
   "2022Q4",
   "2023Q1",
   "2023Q2",
   "2023Q3",
   "2023Q4",
   "2024Q1",
   "2024Q2",
   "2024Q3",
   "2024Q4",
   "2025Q1",
   "2025Q2",
   "2025Q3",
   "2025Q4",
   "2026Q1",
   "2026Q2",
   "2026Q3",
   "2026Q4"
  ],
  "history": {
   "production": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    1.6,
    1.6,
    1.6,
    1.6,
    0.0,
    0.0,
    0.0,
    0.1,
    2.0,
    4.1
   ],
   "lce": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
   ],
   "tech_grade": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
   ],
   "chem_grade": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
   ],
   "sales": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    1.8,
    1.8,
    1.8,
    1.8,
    0.0,
    0.0,
    0.0,
    0.0,
    1.8,
    4.0
   ],
   "inv_change": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
   ],
   "inventory": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
   ],
   "prod_sales_ratio": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    1.125,
    1.125,
    1.125,
    1.125,
    null,
    null,
    null,
    null,
    0.9,
    0.976
   ],
   "avg_price": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    808,
    808,
    808,
    808,
    null,
    null,
    null,
    null,
    null,
    null
   ],
   "cost_with_royalty": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    1148,
    1148,
    1148,
    1148,
    null,
    null,
    null,
    null,
    null,
    null
   ],
   "cost_no_royalty": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
   ],
   "cash_cost": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    1148,
    1148,
    1148,
    1148,
    null,
    null,
    null,
    null,
    null,
    null
   ],
   "cif_cost": [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
   ]
  },
  "yearly": {
   "2024": 3.2,
   "2025": 6.3,
   "2026": 0.1
  }
 }
};
