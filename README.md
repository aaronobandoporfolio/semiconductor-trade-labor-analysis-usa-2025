# Semiconductor Trade & Labor Analysis – USA 2025

## Project Overview

This project examines how U.S. semiconductor trade flows (HS Code 85423100) are being reshaped by inflationary pressures, labor costs, tariff structures, and global demand. By integrating official datasets from trade, labor, logistics, and market demand sources, the analysis highlights strategic insights relevant to executives, startups, recruiters, and policymakers.

The work is structured in phases:  
- **Phase 1** focused on locating and extracting data from legal and public sources.  
- **Phase 2** involved cleaning, organizing, and preparing the datasets for analysis.  
- **Phase 3**, the current stage, is dedicated to Exploratory Data Analysis (EDA), where patterns, relationships, and actionable insights are uncovered.  

The emphasis is on understanding how nearshoring, tariff advantages, and employment trends are influencing the semiconductor supply chain. Mexico and South Korea stand out as critical hubs, while China faces structural disadvantages due to Section 301 tariffs.


## Objectives

- Compare U.S. semiconductor imports and exports by destination (Mexico, China, South Korea, Taiwan)  
- Quantify tariff structures and trade barriers (MFN, Section 301) and their impact on competitiveness  
- Assess logistic efficiency and potential cost savings using rail and border data  
- Evaluate labor costs and employment trends in semiconductor-related industries (NAICS 334)  
- Project global demand growth and the rise of new hubs using OECD and SIA data  


## Data Sources

### 1. USA TradeData Imports Dataset  
- [UN Comtrade – HS 854231 USA Imports](https://comtradeplus.un.org/TradeFlow?Frequency=A&Flows=M&CommodityCodes=854231&Partners=842&Reporters=156&period=2024&AggregateBy=none&BreakdownMode=plus)

### 2. HS 3542 UN Comtrade USA Exports Dataset  
- [UN Comtrade – HS 854231 USA Exports](https://comtradeplus.un.org/TradeFlow?Frequency=A&Flows=M&CommodityCodes=854231&Partners=842&Reporters=156&period=2024&AggregateBy=none&BreakdownMode=plus)

### 3. Semiconductor Demand Study  
- [OECD – Semiconductors Topic](https://www.oecd.org/en/topics/semiconductors.html)  
- [SEMI.org – Market Data](https://www.semiconductors.org/policies/tax/market-data/?type=post)

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


## Documentation Links

- [https://drive.google.com/file/d/19-W453X8x7ObEjlr15hCc0Rgo8kl877T/view?usp=sharing] `Cleaned_TradeData_Imports.csv`  
- [ ] `Cleaned_HS3542_Exports.csv`  
- [ ] `Semiconductor_Tariff_Analysis_2025.xlsx`  
- [ ] `Demand_SIA_OECD.xlsx`  
- [ ] `Employment_Trends_QCEW_OEWS.pdf`  
- [ ] `Logistics_Costs_Rail_Form54.csv`


## Insights & Use Cases

- **Startups and CEOs**: Identify cost-saving trade routes and labor-efficient regions. For example, Mexico shows strong import/export volumes with zero MFN tariffs, while China faces a 25% Section 301 penalty.  
- **Recruiters**: Pinpoint metro areas where semiconductor employment is expanding, aligning talent pipelines with industry growth.  
- **Policy Analysts**: Evaluate how tariff structures and concentrated value chains (75% in five countries per OECD) affect U.S. resilience.  
- **Data Scientists**: Explore cross-domain modeling opportunities by linking trade flows, labor costs, and logistics data to forecast supply chain risks.  


## Author

**Aaron Eliseo Obando Gómez**  
Data analyst focused on bridging trade, labor, and logistics to deliver actionable insights and strategic storytelling.
