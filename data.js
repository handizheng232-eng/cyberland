// 由 build_data.py 生成（永安期货-澳洲锂矿汇总格式）
const YONGAN_DATA = {
 "meta": {
  "title": "永安期货 · 澳洲锂矿季度汇总",
  "updated": "2026-08-04",
  "data_quarters": {
   "start": "2019Q1",
   "end_actual": "26Q2",
   "end_forecast": "26Q4"
  },
  "unit_note": "产量/销量/库存单位为万吨；均价 US$/t；成本 A$/t",
  "color_legend": "橙色=预测值（26Q3E/26Q4E，按FY27指引中值）；灰色 N.D.=官方未披露",
  "disclaimer": "本页面数据来自各矿山母公司官方季度报告，仅供研究参考，不构成投资建议。"
 },
 "mines": [
  {
   "company": "IGO",
   "mine": "Greenbushes",
   "mine_cn": "Greenbushes（格林布什矿山）",
   "report": "IGO June 2026 Quarterly Activities Report（2026-07-28 发布，FY26 Q4 / 日历26Q2）",
   "source_url": "https://www.igo.com.au/site/investor-center/investor-center1",
   "equity_note": "100% 资产口径（Talison 运营）；IGO→TLEA 49%，TLEA/Windfield→Greenbushes 51%，Albemarle 49%",
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
      "url": "img/greenbushes_aerial_official.jpg",
      "src": "IGO 官网（Our Business）",
      "cap": "Greenbushes 矿山航拍实景——露天矿坑 + 选矿厂区（CGP1/CGP2/CGP3、TGP、TRP），可与卫星影像直接对照定位"
     },
     {
      "url": "img/greenbushes_ar2023_overview.jpg",
      "src": "IGO Annual Report 2023",
      "cap": "矿山全景照片（FY23 年报），展示露天开采区与选矿厂布局"
     },
     {
      "url": "img/slr_plants_aerial.jpg",
      "src": "SLR 技术报告 Fig 14-1/14-2",
      "cap": "选矿厂工艺流程总览 + 厂区航拍位置图（Fig 14-2 Aerial Image），标出各选矿厂相对位置"
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
       "url": "img/greenbushes_ar2023_mine.jpg",
       "src": "IGO Annual Report 2023",
       "cap": "Greenbushes 露天矿实景（FY23），主矿坑与采矿设备，可对照卫星影像识别矿坑轮廓"
      },
      {
       "url": "img/slr_location_plan.jpg",
       "src": "SLR 技术报告 Fig 3-1/3-2",
       "cap": "矿区位置图（含经纬度 33°51'24\"S 116°03'44\"E 与区域交通/港口关系）——卫星锁定第一参照"
      },
      {
       "url": "img/slr_site_layout.jpg",
       "src": "SLR 技术报告 Fig 3-3",
       "cap": "Greenbushes Mine Operation Layout——矿坑、选矿厂、尾矿库、废石堆整体布置"
      },
      {
       "url": "img/slr_pit_limit.jpg",
       "src": "SLR 技术报告 Fig 12-3/12-5",
       "cap": "矿坑境界优化壳与最终边坡设计图（含坐标网格），用于识别矿坑边界"
      },
      {
       "url": "img/slr_tsf.jpg",
       "src": "SLR 技术报告 Fig 15-7/15-8",
       "cap": "尾矿库 TSF1/2/4 布置图——TRP 原矿来源与尾矿设施卫星定位"
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
   "精矿产量（万吨）"
  ],
  [
   "lce",
   "精矿产量（6%,LCE）"
  ],
  [
   "tech_grade",
   "技术级精矿产量（万吨）"
  ],
  [
   "chem_grade",
   "化学级精矿产量（万吨）"
  ],
  [
   "sales",
   "销量（万吨）"
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
   "平均售价（US$/t）"
  ],
  [
   "cost_with_royalty",
   "单位成本—含权益金（A$/t）"
  ],
  [
   "cost_no_royalty",
   "单位成本—不含权益金（A$/t）"
  ],
  [
   "cash_cost",
   "cash cost（A$/t）"
  ]
 ]
};
