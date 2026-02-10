# Semiconductor Trade & Labor Analysis – USA 2025

## Project Overview

This project examines how U.S. semiconductor trade flows (HS Code 85423100) are being reshaped by inflationary pressures, labor costs, tariff structures, and global demand. By integrating official datasets from trade, labor, logistics, and market demand sources, the analysis highlights strategic insights relevant to executives, startups, recruiters, and policymakers.

The work is structured in phases, serving as a showcase of my professional approach to data analysis and business intelligence:  
- **Phase 1** focused on locating and extracting data from authoritative legal and public sources.  
- **Phase 2** involved cleaning, organizing, and preparing the datasets to ensure accuracy and reliability.  
- **Phase 3**, the current stage, is dedicated to Exploratory Data Analysis (EDA), where patterns, relationships, and actionable insights are uncovered. 
- **Phase 4** will emphasize Data Visualization, including the development of a Power BI Dashboard designed to present insights interactively for executives, managers, and decision-makers.  
- **Phase 5** will consolidate findings into a comprehensive Report and PowerPoint Presentation, tailored to professionals, recruiters, CEOs, and policymakers seeking strategic clarity and actionable recommendations.  

The emphasis is on understanding how nearshoring, tariff advantages, and employment trends are influencing the semiconductor supply chain. Mexico and South Korea stand out as critical hubs, while China faces structural disadvantages due to Section 301 tariffs.


## Objectives

- Compare U.S. semiconductor imports and exports by destination (Mexico, China, Malaysia, South Korea, Taiwan)  
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


## Documentation and Power Bi Dashboard Links

- [Why These Datasets, Why This
Analysis, and How They Were Collected](https://drive.google.com/file/d/1B-DoWoTZz46CbGMlxdyh96ooA5mH0ddv/view?usp=sharing)
- [USA TradeData Imports Dataset.pdf](https://drive.google.com/file/d/15XfoNXVKj7G0hJE2CGBGGT3rYNSSqkAt/view?usp=sharing)  
- [HS 3542 UN Comtrade USA Exports Dataset.pdf](https://drive.google.com/file/d/1pRShU9XRMA1dkyWN9p54PP8MGv50_hOh/view?usp=sharing)  
- [Semiconductor Demand Study (SIA & OECD Sources).pdf](https://drive.google.com/file/d/1niSpH__EBZdBA8a-gGmgplcgDxt7jDTM/view?usp=sharing)  
- [Semiconductor Tariff Analysis – HS Code 85423100 (2025).pdf](https://drive.google.com/file/d/15FI1PaNU9tcyD6-j4nQEbEvy2xff--ym/view?usp=sharing)  
- [Rail Equipment Accident Incident Data (Form 54).pdf](https://drive.google.com/file/d/1mOiZihihsxE3XrSKQwqxSErUZ8Y7CH7f/view?usp=sharing)  
- [Quarterly Census of Employment and Wages.pdf](https://drive.google.com/file/d/1HlZ5APMSZj7GxU3De_NxVm7ft1BYHM1a/view?usp=sharing)  
- [ECI Tables Downloaded for Analysis.pdf](https://drive.google.com/file/d/1Pj5ZDTAeu8sL2FTPo6mOxnFPI-Jayala/view?usp=sharing)  
- [SAE Tables Downloaded for State and Metro Analysis.pdf](https://drive.google.com/file/d/1xIlwAIftNFx8QVGm7WVKNOGulA6somkl/view?usp=sharing)  
- [Occupational Employment and Wage Statistics (OEWS).pdf](https://drive.google.com/file/d/1Dm9Se3QDwJh-OBzt4PCSUI3vox_0qd6E/view?usp=sharing)  
- [Cleaning Company Census File (20260121).pdf](https://drive.google.com/file/d/1_-K7h0vSKHO36TBgNEFuYoEpLDlO0Unp/view?usp=sharing)
- [Saving Cleaned Imports USA.csv
into MySQL for Semiconductor Trade Analysis](https://drive.google.com/file/d/1EYzP69Kc7IlzDihOQ4pEbZuh5kAtRrj7/view?usp=sharing)
- [U.S. Semiconductor Imports Analysis: Comprehensive EDA Documentation](https://drive.google.com/file/d/1k2RcVabMy0CW8YUx8hM-jBAmBMXw85Md/view?usp=sharing)
- [SQL Validation and Extended Insights on U.S. Semiconductor Imports (2025)](https://drive.google.com/file/d/11WCcobP-a0hK_gwzbrXkYfblGfZ_rIWB/view?usp=sharing)
- [CIF Imports Overview by Country 
(2025) Dashboard Insights](https://drive.google.com/file/d/1sh7wzO63HLhjtmA6VAYC2tJR2sVIRa-b/view?usp=sharing)
- [1 US Semiconductors CIF Imports Overview.pbix](https://drive.google.com/file/d/1mbQUYXKKl5IAuiRkpYCiW4bcPqYXsULt/view?usp=sharing)
- [An Exploratory Data Analysis of HS Code 3542 (USA Exportations)](https://drive.google.com/file/d/1fYur07R_3y9E-j08jG05jtHyKeOS0rqu/view?usp=sharing)



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

- **Startups and CEOs**: Identify more cost-effective trade routes and regions with labor efficiency. For example, Mexico benefits from **zero MFN tariffs under USMCA**, making it a competitive hub for **electronics assembly and semiconductor-related activities**. In contrast, China faces a **25% penalty under Section 301**, which significantly raises import costs and motivates U.S. companies to diversify sourcing toward allies and nearshoring partners.  

- **Recruiters**: Detect metropolitan areas where semiconductor employment is growing. Recent reports show that U.S. hubs such as **Phoenix, Austin, and Albany** are experiencing rapid growth in manufacturing and R&D jobs, while **Malaysia, Germany, and Japan** remain critical external partners. Aligning talent pipelines with these hotspots ensures workforce readiness for both domestic production and international supply chain management.  

- **Policy Analysts**: Assess how tariff structures and concentrated value chains affect resilience. OECD data shows that **75% of semiconductor trade value is concentrated in just five countries**, highlighting systemic risk. Malaysia’s dominance in U.S. imports (55–65% in 2025) reflects efficiency but also vulnerability. Analysts can use this insight to model scenarios of geopolitical disruption or natural disasters, and evaluate how diversification toward **Brazil, India, and Israel** could mitigate exposure.  

- **Data Scientists**: Explore multidomain modeling opportunities by linking trade flows, labor costs, and logistics data. For example, combining **UN Comtrade import values** with **transport mode data (air vs. sea)** and **tariff schemes** enables the construction of predictive models for supply chain risks. This can anticipate bottlenecks, identify cost-optimized sourcing strategies, and quantify resilience under different trade policy regimes.  

**US Semiconductors CIF Imports Overview (Without Malaysia)**
![Page 1](https://github.com/aaronobandoporfolio/semiconductor-trade-labor-analysis-usa-2025/blob/main/Images/66%20KPI%20Imports%20Dashboard%20Without%20Malaysia%20page%201.png)

![Page 2](https://github.com/aaronobandoporfolio/semiconductor-trade-labor-analysis-usa-2025/blob/main/Images/68%20KPI%20Imports%20Dashboard%20Without%20Malaysia%20page%202.png)

  
## Disclaimer

- **Data Privacy**: Due to privacy considerations, the cleaned datasets and intermediate files used in this project are not available for direct download. Documentation and methodological notes are provided instead to ensure transparency without compromising data security.
- **Wrangling Steps**: During the data wrangling process, several repetitive but essential validation steps (such as df.describe(), df.info(), and checks on dtypes) were performed. In some cases, these commands were later deleted or commented out in the final code to streamline readability once validation was complete. Their absence in the published scripts does not mean they were skipped; rather, they were executed during the workflow and discarded only after confirming accuracy.


## Connect With Me

If you found this project interesting and would like to discuss insights, opportunities, or collaborations, feel free to reach out to me on [LinkedIn](https://www.linkedin.com/in/aaron-obando-55a098308/).  

You can also review my CV to learn more about my background and experience: [CV Link](https://drive.google.com/file/d/1eGT9nxJvH_wlA_xEE3MSumNMo90Nqzi6/view?usp=sharing).


## Support This Project

This project represents my debut in strategic data analysis, connecting trade, labor, and logistics to actionable insights for professionals, startups, and decision-makers.  

If you found value in this work and would like to support further research and development, you can contribute here:  

[Support via PayPal](https://paypal.me/AaronObando505?locale.x=en_US&country.x=CR)  

Your support helps me dedicate more time to expanding the analysis, improving documentation, and sharing insights with the community.



## Author

**Aaron Eliseo Obando Gómez**  
Data analyst focused on bridging trade, labor, and logistics to deliver actionable insights and strategic storytelling.
