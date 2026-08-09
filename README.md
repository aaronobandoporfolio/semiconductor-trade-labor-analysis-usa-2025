# Uncovering 2025 Nearshoring Opportunities: A U.S. Semiconductor Trade & Labor Analysis

[![Dashboard](https://github.com/aaronobandoporfolio/semiconductor-trade-labor-analysis-usa-2025/blob/main/Images/86%20Semiconductor%20Sector%20ECI%20Analysis.png)](https://github.com/aaronobandoporfolio/semiconductor-trade-labor-analysis-usa-2025/blob/main/Data%20Visualization%20%26%20Dashboards/3%20Semiconductor%20Wage%20%26%20Skills%20Premium%20Dashboard.pbix)

## Project Overview

This project examines how U.S. semiconductor trade flows (HS Code 85423100) are being reshaped by inflationary pressures, labor costs, tariff structures, and global demand. By integrating official datasets from trade, labor, logistics, and market demand sources, the analysis highlights strategic insights relevant to executives, startups, recruiters, and policymakers.

The work is structured in phases, serving as a showcase of my professional approach to data analysis and business intelligence:  

- **Phase 1: Data Extraction** – Focused on locating and extracting data from authoritative legal and public sources. 
- **Phase 2: Data Preprocessing** – Involved cleaning, organizing, and preparing the datasets to ensure accuracy and reliability. 
- **Phase 3: Exploratory Data Analysis (EDA)** – The current stage, dedicated to uncovering patterns, relationships, and actionable insights. 
- **Phase 4: Data Visualization** – Will emphasize the development of a Power BI Dashboard designed to present insights interactively for executives, managers, and decision-makers.
- **Phase 5: Final Reporting** – Will consolidate findings into a comprehensive Report and PowerPoint Presentation, tailored to professionals, recruiters, CEOs, and policymakers seeking strategic clarity.

The emphasis is on understanding how nearshoring, tariff advantages, and employment trends are influencing the semiconductor supply chain. Mexico, South Korea and Malaysia stand out as critical hubs, while China faces structural disadvantages due to Section 301 tariffs.


## Objectives

- Compare U.S. semiconductor imports and exports by destination  
- Quantify tariff structures and trade barriers (MFN, Section 301) and their impact on competitiveness  
- Assess logistic efficiency and potential cost savings using rail and border data  
- Evaluate labor costs and employment trends in semiconductor-related industries (NAICS 334), including wage premium dynamics, real vs. nominal wage growth by subsector, skills compression, and the structural shift from headcount growth to value-per-worker retention  
- Project global demand growth and the rise of new hubs using OECD and SIA data


## Data Sources

### 1. USA TradeData Imports Dataset  
- [UN Comtrade – HS 854231 USA Imports](https://comtradeplus.un.org/TradeFlow?Frequency=A&Flows=M&CommodityCodes=854231&Partners=842&Reporters=156&period=2024&AggregateBy=none&BreakdownMode=plus)

### 2. HS 3542 UN Comtrade USA Exports Dataset  
- [UN Comtrade – HS 854231 USA Exports](https://comtradeplus.un.org/TradeFlow?Frequency=A&Flows=M&CommodityCodes=854231&Partners=842&Reporters=156&period=2024&AggregateBy=none&BreakdownMode=plus)

### 3. Semiconductor Demand Study  
- [OECD – Semiconductors Topic](https://www.oecd.org/en/topics/semiconductors.html)  
- [Semiconductor Industry Association (SIA) – Market Data](https://www.semiconductors.org/policies/tax/market-data/?type=post)

### 4. Tariff Analysis – HS Code 85423100  
- [WTO Tariff Data](https://ttd.wto.org/en/data/idb/applied-duties?member=C840&product=85423100&year=2025)  
- [USITC HTS Search](https://hts.usitc.gov/search?query=85423100)  
- [Ballast Markets – Section 301 Tariffs](https://content.ballastmarkets.com/blog/2025-11-08-section-301-tariffs-explained-complete-list/)

### 5. Rail Equipment & Logistics  
- [Rail Equipment Accident Data – Form 54](https://data.transportation.gov/Railroads/Rail-Equipment-Accident-Incident-Data-Form-54-/85tf-25kj/about_data)

### 6. Labor & Employment Data  
- [Quarterly Census of Employment and Wages (QCEW)](https://www.bls.gov/data/)  
- [Employment Cost Index (ECI)](https://www.bls.gov/news.release/eci.toc.htm)  
- [State and Metro Employment (SAE)](https://www.bls.gov/data/)  
- [Occupational Employment and Wage Statistics (OEWS)](https://www.bls.gov/data/)  
- [Company Census File – BLS CEW](https://www.bls.gov/cew/)


## Documentation and Power Bi Dashboard Links

### Phases 1 & 2 — Data Collection, Sourcing & Cleaning

> Every dataset used in this project is sourced from official public institutions
> (UN, BLS, WTO, OECD, U.S. DOT). The documents below cover where each dataset
> came from, why it was selected, and how it was cleaned and prepared for analysis.

- [Why These Datasets Were Selected and How They Were Collected](https://drive.google.com/file/d/1-3SQiZhzIkydtv6eWh92isykCIxGN_ef/view?usp=sharing)
- [U.S. Semiconductor Imports — Source Dataset (UN Comtrade)](https://drive.google.com/file/d/1u0P0rbN6ok3GJFVW5FBWn0qq2E11dxIC/view?usp=sharing)
- [U.S. Semiconductor Exports — Source Dataset (UN Comtrade)](https://drive.google.com/file/d/1YcdE62QwZrf7Y5lE99XZmv03Pfy_9w3L/view?usp=sharing)
- [Global Semiconductor Demand Study — Source Dataset (SIA & OECD)](https://drive.google.com/file/d/1Pr-jg3PHVlkSzI1eT4q0XfalV_hWEbnt/view?usp=sharing)
- [Tariff Structure — Source Dataset, HS Code 85423100 (2025)](https://drive.google.com/file/d/1E962Viu1xvghCLE5IfafTda5OaI2H55F/view?usp=sharing)
- [Logistics Risk — Source Dataset, Rail Equipment Incidents (U.S. DOT Form 54)](https://drive.google.com/file/d/1gRpTuLqjJvutQps7Xzc2dIEjD6iiViLE/view?usp=sharing)
- [U.S. Employment & Wages — Source Dataset, Quarterly Census (BLS QCEW)](https://drive.google.com/file/d/1Z56mXnFIui68kvf9GsmsriejWwQ0xH4k/view?usp=sharing)
- [Employment Cost Index — Source Dataset, ECI Tables (BLS)](https://drive.google.com/file/d/1mfsM_xQTCQX8xuWtivi6noqI7_OVqsP2/view?usp=sharing)
- [State & Metro Employment — Source Dataset, SAE Tables (BLS)](https://drive.google.com/file/d/1yg2FOCxXwXcJGXHD0iDUGf-KAXUJyPGD/view?usp=sharing)
- [Occupational Wages by Role — Source Dataset, OEWS (BLS)](https://drive.google.com/file/d/1EOsHBXyN1-5Zz7fYwIEZJ8tCwqgzge0A/view?usp=sharing)
- [Company Census File — Cleaning Process & Validation](https://drive.google.com/file/d/1MXG2djJDZ7_B_SEqY-peLbFJe2PlBUtK/view?usp=sharing)
  
---

### Dashboard 1 — U.S. Semiconductor Imports Overview

> Who is selling semiconductors to the U.S., at what price, and from where?

- [Loading Cleaned Imports into MySQL — Pipeline Documentation](https://drive.google.com/file/d/18xiokOF3ZzXAXeGOYf7EkMlt_fh0144Z/view?usp=sharing)
- [Imports EDA — Full Analysis & Findings](https://drive.google.com/file/d/1Sou0BtrLAZy2XEDGCnaHI_5MkLMjEHIB/view?usp=sharing)
- [SQL Validation & Extended Insights — Imports (2025)](https://drive.google.com/file/d/1lXmCQC2wlwdD64JHw5vW9hzP8Lr46GeH/view?usp=sharing)
- [Dashboard File — CIF Imports Overview (.pbix)](https://github.com/aaronobandoporfolio/semiconductor-trade-labor-analysis-usa-2025/blob/main/Data%20Visualization%20%26%20Dashboards/1%20US%20Semiconductors%20CIF%20Imports%20Overview.pbix)
- [Dashboard Documentation — Imports by Country (2025)](https://drive.google.com/file/d/1wntK7ip2EMJFM9lplSnfYG-LZQYUDoIi/view?usp=sharing)

---

### Dashboard 2 — U.S. Semiconductor Trade Balance: Exports vs. Imports

> How do U.S. export destinations compare to import sources — and where are the strategic gaps?

- [Exports EDA — Full Analysis & Findings](https://drive.google.com/file/d/1NcOpa9zuEkv0iVsBZMFj5n9lnR0o_cNq/view?usp=sharing)
- [SQL Validation & Extended Insights — Exports (2025)](https://drive.google.com/file/d/1srhp7MSJkPbx9LWRvAfKDYVgVojdoJGx/view?usp=sharing)
- [Dashboard File — Trade Overview (.pbix)](https://github.com/aaronobandoporfolio/semiconductor-trade-labor-analysis-usa-2025/blob/main/Data%20Visualization%20%26%20Dashboards/2%20U.S.%20Semiconductor%20Trade%20Overview%20(2025).pbix)
- [Dashboard Documentation — Imports & Exports Combined](https://drive.google.com/file/d/1Cmqq9XC17ByEmvI3GnvsH13GKSvvh6Eh/view?usp=sharing)

---

### Dashboard 3 — Semiconductor Workforce: Wages, Employment & the Skills Premium

> Why are semiconductor wages rising while headcount is falling — and what does that mean for hiring strategy?

- [BLS Earnings & ECI Analysis — Semiconductor Sector](https://drive.google.com/file/d/1uA-Y2eKHvb2NhIynn_gG8Z3Loyfd59oW/view?usp=sharing)
- [Dashboard File — Wage & Skills Premium (.pbix)](https://github.com/aaronobandoporfolio/semiconductor-trade-labor-analysis-usa-2025/blob/main/Data%20Visualization%20%26%20Dashboards/3%20Semiconductor%20Wage%20%26%20Skills%20Premium%20Dashboard.pbix)
- [Dashboard Documentation — Wage & Skills Premium](https://drive.google.com/file/d/1Py86BmphD81hzcrQlAP4qlySyd2uAFlV/view?usp=sharing)


## Process & Documentation Images

### Data Wrangling Process
During Phase 2, I worked with two windows simultaneously: one running Python scripts in Visual Studio Code and another displaying CSV files in Excel. This setup allowed me to check the accuracy of my data wrangling process step by step.  

- I verified data types across columns, which were all accurate.  
- My focus was on extracting what was relevant and dropping what was not.  
- After ensuring the wrangling met expectations, I documented the major steps and added comments to the code.  
- Some files contained millions of rows, which required longer debugging cycles to ensure accuracy.  


![Dual-Screen Data Wrangling](https://github.com/aaronobandoporfolio/semiconductor-trade-labor-analysis-usa-2025/blob/main/Images/Screenshot%202026-01-29%20191735.png)



### Cleaned Data Repository
The cleaned dataset now consists of **23 files in total**, covering trade, labor, logistics, and economic indicators. These include:  

1. Occupational Employment and Wage Statistics (OEWS).txt  
2. Rail_Equipment_Accident_Incident_Data_(Form_54)_20260121.csv  
3. Demand SIA_OECD.xlsx  
4. Imports USA.csv  
5. Quarterly Census of Employment and Wages.csv  
6. semiconductors_tariffs_2025.xlsx  
7. Company_Census_File_20260121.csv  
8. HS_3542_Un_Comtrade_USA_Exports.csv  
9. Employment and Earnings Table B-1a.pdf  
10. Employment and Earnings Table B-1b.pdf  
11. Employment and Earnings Table B-3a.pdf  
12. Employment and Earnings Table B-3b.pdf  
13. Employment and Earnings Table B-8a.pdf  
14. Employment and Earnings Table B-8b.pdf  
15. Export Price Indexes, by Harmonized System - 2025 M11 Results.pdf  
16. Ports by Commodities.pdf  
17. SAE table-2-employees-on-nonfarm-payrolls-by-states-selected-metropolitan-areas-and-metropolitan-divisions.pdf  
18. Table 1. Seasonally adjusted Employment Cost Index – 2025 Q03 Results.pdf  
19. Table 2. Seasonally adjusted Employment Cost Index – 2025 Q03 Results.pdf  
20. Table 3. Seasonally adjusted Employment Cost Index – 2025 Q03 Results.pdf  
21. Index for wages and salaries – 2025.pdf  
22. Table 13. Compensation and wages and salaries (not seasonally adjusted) – 2025 Q0.pdf  
23. Weekly_Traffic_Volume_20260121.csv  

All of these files will be analyzed thoroughly in **Phase 3 (EDA)** to uncover actionable insights.


![Project Folder Structure](https://github.com/aaronobandoporfolio/semiconductor-trade-labor-analysis-usa-2025/blob/main/Images/Screenshot%202026-01-29%20192358.png)

![Cleaned Data Repository](https://github.com/aaronobandoporfolio/semiconductor-trade-labor-analysis-usa-2025/blob/main/Images/Screenshot%202026-01-29%20191958.png)


## Insights & Use Cases

### Workforce & ECI Analysis

- **Workforce & ECI**:  
  Trade concentration is only half the story — the Employment Concentration Index (ECI) shows how semiconductor jobs are distributed across U.S. regions and industries. While total employment in NAICS 334 hovers around 3 million, the distribution is uneven.  
  - **Dashboard Insight**: Employment growth is clustered in electronics manufacturing (≈1M) and precision instruments (≈0.41M), while semiconductors hold steady at ≈0.38M with slight cooling (‑0.03%). Smaller sub‑industries like magnetic & optical media show sharper declines (‑1.8%), signaling structural shifts.

- **ECI Deep Dive — Semiconductor Wage & Employment Dynamics (NAICS 3344)**:  
  Beyond headcount distribution, a dedicated **ECI Employment Analytics Dashboard** drills into the wage dynamics of the U.S. semiconductor sector through December 2025. Built in **Power BI** with custom **DAX measures** and **HTML/CSS/JS** visual panels, and fed by a Python pipeline extracting eight BLS earnings tables, it surfaces six core findings:

  | # | Finding | Key Metric |
  |---|---------|------------|
  | 1 | **Employment contraction stabilizing** | 365.2K workers · ▼4.6% YoY · Q4 plateau confirmed at −100 jobs/month |
  | 2 | **Wage premium expanding** | +21.9% above manufacturing average · $21.8K/yr premium · widened +1.6 pp in 2025 |
  | 3 | **Wage growth accelerating** | +6.9% nominal full-year · Q4 sprint +0.56% · retention driving raises |
  | 4 | **Skill compression emerging** | Skills premium narrowed from 0.4% → 0.3% · possible oversupply of specialized talent |
  | 5 | **Subsector divergence** | Comms Gear **+8.52% real** vs. Electronic Parts **−3.54% real** · 12 pp spread within NAICS 334 |
  | 6 | **The Semiconductor Paradox confirmed** | Headcount fell while wages rose — the sector is concentrating talent, not growing it |

  **Analytical workflow:**
  1. **Data extraction** — Eight BLS CSV tables (weekly/hourly earnings, SA/NSA, all employees and production workers) processed through a six-function Python script.
  2. **Intermediary files** — Six CSV insight files and two Excel workbooks exported to a validated Findings layer.
  3. **Dashboard build** — Power BI report combining native visuals with custom HTML/CSS/JS panels and DAX-calculated KPIs.

  **Dashboard navigation** includes five interactive panels accessible from the control sidebar:
  - **Executive Summary** — headline KPIs, key findings, emerging risks, and a strategic recommendation
  - **Storytelling** — the "Semiconductor Paradox" narrative in three acts, with four tested hypotheses (2 confirmed, 2 rejected)
  - **Executive Walkthrough** — a 9-step guided tour explaining every visual in context
  - **Data Source** — direct link to the BLS ECI tables for full transparency and independent verification
  - **About This Dashboard** — methodology, technical stack, design philosophy, and known UI behaviors

  > **Strategic implication**: The sector is shifting from *growth by headcount* to *growth by value per worker*. Leaders must invest in advanced training, differentiated pay structures, and talent mobility programs to sustain competitiveness — especially given that 2 of 5 subsectors posted real wage losses in 2025.

[![Dashboard](https://github.com/aaronobandoporfolio/semiconductor-trade-labor-analysis-usa-2025/blob/main/Images/86%20Semiconductor%20Sector%20ECI%20Analysis.png)](https://github.com/aaronobandoporfolio/semiconductor-trade-labor-analysis-usa-2025/blob/main/Data%20Visualization%20%26%20Dashboards/3%20Semiconductor%20Wage%20%26%20Skills%20Premium%20Dashboard.pbix)

### Trade Analysis

- **Startups and CEOs**:  
  In 2025, the semiconductor trade tells two very different stories. On the export side, Mexico thrives under **USMCA's zero tariffs**, positioning itself as a competitive hub for electronics assembly. Meanwhile, China faces a **25% Section 301 tariff**, pushing U.S. firms to rethink sourcing strategies.  
  - **Dashboard Insight**: Exports show strength and diversification, with Mexico and China leading as destinations and Malaysia playing a secondary but strategic role. Imports, however, reveal extreme dependence on Malaysia (≈60%+), forcing CEOs to balance efficiency with resilience.

- **Recruiters**:  
  The talent race mirrors the trade race. U.S. hubs like **Phoenix, Austin, and Albany** are booming in semiconductor manufacturing and R&D, while external partners such as **Malaysia, Germany, and Japan** remain critical to global supply chains.  
  - **Dashboard Insight**: Exports are moderately concentrated (HHI ≈0.17), reflecting diverse demand. Imports are highly concentrated (HHI ≈0.70), signaling risk. Recruiters can align pipelines with domestic hotspots while keeping an eye on international partners that anchor supply chain resilience.

- **Policy Analysts**:  
  Behind the numbers lies systemic risk. OECD and USITC data show that **over 70% of semiconductor trade value is concentrated in just five countries**. Malaysia, a global powerhouse in assembly and testing (~13% of the market), dominates U.S. imports.  
  - **Dashboard Insight**: Malaysia's dominance reflects efficiency but also vulnerability. Analysts can model disruption scenarios — geopolitical shocks, natural disasters — and evaluate diversification toward **Brazil, India, and Israel**, which appear as emerging suppliers in the import dashboard.

- **Data Scientists**:  
  The duality of exports and imports offers fertile ground for modeling. Linking **UN Comtrade flows** with **transport modes (air vs. sea)** and **tariff regimes** enables predictive analytics for supply chain risk.  
  - **Dashboard Insight**: Exports highlight balanced partnerships across Asia and North America, while imports expose single‑partner dependency. This contrast can fuel models that quantify resilience, simulate shocks, and recommend diversification strategies.

**U.S. Semiconductor Trade Overview (2025)**
[![Page 1](https://github.com/aaronobandoporfolio/semiconductor-trade-labor-analysis-usa-2025/blob/main/Images/80%20Global%20Export%20Overview%20(2025)%20Page%201.png)](https://github.com/aaronobandoporfolio/semiconductor-trade-labor-analysis-usa-2025/blob/main/Data%20Visualization%20%26%20Dashboards/2%20U.S.%20Semiconductor%20Trade%20Overview%20(2025).pbix)
[![Page 2](https://github.com/aaronobandoporfolio/semiconductor-trade-labor-analysis-usa-2025/blob/main/Images/81%20Semiconductor%20Imports%20Concentration%20Page%202.png)](https://github.com/aaronobandoporfolio/semiconductor-trade-labor-analysis-usa-2025/blob/main/Data%20Visualization%20%26%20Dashboards/2%20U.S.%20Semiconductor%20Trade%20Overview%20(2025).pbix)
[![Page 3](https://github.com/aaronobandoporfolio/semiconductor-trade-labor-analysis-usa-2025/blob/main/Images/82%20Semiconductor%20Trade%20Trends%20%26%20Balance%20(Page%203).png)](https://github.com/aaronobandoporfolio/semiconductor-trade-labor-analysis-usa-2025/blob/main/Data%20Visualization%20%26%20Dashboards/2%20U.S.%20Semiconductor%20Trade%20Overview%20(2025).pbix)


### Complementary Narrative

Together, the dashboards reveal **two sides of U.S. semiconductor competitiveness in 2025**:

- **Workforce** → wages accelerating even as headcount contracts, with stark divergence between subsectors masking the aggregate headline.
- **Trade** → diversified exports with resilient allies, but highly concentrated imports vulnerable to Malaysia's dominance.

This contrast underscores both the **strengths** and the **fragilities** of the U.S. semiconductor ecosystem — and the urgent need for simultaneous diversification in supply chains **and** talent strategy.

  
## Disclaimer  
- **Data Privacy**: Due to privacy considerations, the cleaned datasets and intermediate files used in this project are not available for direct download. Documentation and methodological notes are provided instead to ensure transparency without compromising data security.  
- **Wrangling Steps**: During the data wrangling process, several repetitive but essential validation steps (such as `df.describe()`, `df.info()`, and checks on `dtypes`) were performed. In some cases, these commands were later deleted or commented out in the final code to streamline readability once validation was complete. Their absence in the published scripts does not mean they were skipped; rather, they were executed during the workflow and discarded only after confirming accuracy.  
- **Dataset Limitations**: Some official sources, such as **UN Comtrade** and the **U.S. Bureau of Labor Statistics (BLS)**, provide datasets that are incomplete or too brief for long‑term trend analysis — for example, BLS Employment Cost Index tables for NAICS 3344 are published at a fixed level of aggregation, with no granular breakdowns by state, occupation, or firm size available in the public release. This project acknowledges those gaps and works hard to complement them with additional context, validation, and careful interpretation. Every effort was made to ensure that the insights presented are as accurate and meaningful as possible, despite the constraints of the raw data.
- **Dashboard Design**: Not every dashboard in this project reaches the same level of visual polish. Data availability, source formatting constraints, and time limitations sometimes make it difficult to build the fully refined experience I aim for. That said, every dashboard — regardless of complexity — is built with the same core principles: clarity first, dynamic where possible, and always designed to make the data as easy to understand and navigate as possible. When richer data and more time allow, as with the ECI Employment Analytics Dashboard, the result reflects that investment in design — combining custom **DAX measures**, **HTML/CSS/JS** visual panels, interactive navigation, and a guided walkthrough to elevate the analytical experience beyond a standard report.

## Connect With Me

If you found this project interesting and would like to discuss insights, opportunities, or collaborations, feel free to reach out to me on [LinkedIn](https://www.linkedin.com/in/aaron-obando-55a098308/).  

You can also review my CV to learn more about my background and experience: [CV Link](https://drive.google.com/file/d/1mEmvdFMjBYZ2gHJWf0lr0sWNJrvNmQ6Z/view?usp=sharing).

Email: contact@obandoanalytics.com


## Author

**Aaron Eliseo Obando Gómez**  
Data analyst focused on bridging trade, labor, and logistics to deliver actionable insights and strategic storytelling.
