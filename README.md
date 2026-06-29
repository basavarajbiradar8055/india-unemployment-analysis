# India Unemployment Analysis (2015–2024)
**Tools:** Python | Pandas | Matplotlib | Seaborn | Scikit-learn | Git & GitHub

---

## Problem Statement
Despite being one of the fastest-growing economies, India faces a serious unemployment challenge. A large youth population, education-jobs mismatch, and gender gap affect millions of families every year.

This project analyzes India's unemployment data from 2015 to 2024 across gender, age, education, and state-wise groups to discover patterns and predict future trends using Machine Learning.

---

## Objectives
1. How has unemployment changed from 2015 to 2024?
2. Which gender is more affected?
3. Which age group faces the highest unemployment?
4. Does more education guarantee a job?
5. Which states have the highest and lowest unemployment?
6. Is urban or rural unemployment higher?
7. What will unemployment look like in 2025–2027?

---

## Dataset
| Detail | Info |
|---|---|
| Source | CMIE (cmie.com) & MOSPI (mospi.gov.in) |
| Rows | 10 (Year 2015 to 2024) |
| Columns | 16 (Overall, Gender, Age, Education, States) |
| Format | CSV |
| Limitation | State-level data is approximate/estimated |

---

## Tools & Technologies
- **Python** – Core programming language
- **Pandas** – Data loading and manipulation
- **Matplotlib** – Charts and visualizations
- **Seaborn** – Heatmap and styled charts
- **Scikit-learn** – Linear Regression ML model
- **Statistics** – Mean, Median, Std Dev
- **Git & GitHub** – Version control and portfolio

---

## Project Folder Structure
```
unemployment_dashboard/
├── Dataset/
│   └── india_unemployment.csv
├── Python/
│   └── unemployment_analysis.py
├── Images/
│   ├── 01_trend_prediction.png
│   ├── 02_gender_comparison.png
│   ├── 03_age_group.png
│   ├── 04_education_paradox.png
│   ├── 05_state_comparison.png
│   ├── 06_rural_urban.png
│   ├── 07_correlation_heatmap.png
│   └── 08_yoy_change.png
└── README.md
```

---

## Data Cleaning
- No missing values found
- No duplicate rows
- All data types are correct (numeric)
- COVID-19 spike in 2020–21 confirmed as real data, not an error
- Dataset is clean and ready for analysis

---

## EDA – Summary Statistics
| Metric | Value |
|---|---|
| Mean Rate | 6.64% |
| Median Rate | 6.70% |
| Std Deviation | 1.37% |
| Lowest Rate | 4.9% (2015) |
| Highest Rate | 8.7% (2021 – COVID) |

---

## Key Business Questions & Answers

| Question | Answer |
|---|---|
| Unemployment trend? | Steady rise, COVID spike in 2020–21, slow recovery |
| Gender most affected? | Women (10.5%) vs Men (6.8%) |
| Age group hardest hit? | Youth 15–24 at 23.2% |
| Education helps? | NO — Graduates face 18.4% (paradox!) |
| Worst state? | Haryana 26.7% |
| Best state? | Gujarat 2.1% |
| Rural vs Urban? | Urban (8.9%) > Rural (5.3%) |

---

## Visualizations

| Chart | Description |
|---|---|
| Trend + ML Prediction | Unemployment 2015–2024 with 2025–2027 forecast |
| Gender Comparison | Men vs Women unemployment gap |
| Age Group | Youth 15–24 hit hardest |
| Education Paradox | Graduates have highest unemployment |
| State Comparison | Haryana vs Gujarat — 12x difference |
| Rural vs Urban | Urban unemployment is higher |
| Correlation Heatmap | All groups correlation |
| Year-over-Year Change | Which years improved or worsened |

---

## Key Insights
1. **Education Paradox** – Graduates face 18.4% unemployment, 20x more than illiterates (0.9%). Skills mismatch is the root cause.
2. **Youth Crisis** – 1 in 4 young Indians (15–24) is unemployed. Biggest long-term risk.
3. **Gender Gap** – Women face 10.5% vs Men 6.8%. Low female workforce participation is a major issue.
4. **COVID Impact** – Rate jumped from 5.3% to 8.7% during COVID. Full recovery still pending.
5. **State Inequality** – Haryana (26.7%) vs Gujarat (2.1%) — 12x gap between states.
6. **Urban > Rural** – Urban unemployment is higher because urban workers actively seek and report unemployment.
7. **ML Forecast** – Unemployment predicted to reach ~9.2% by 2027 without major interventions.

---

## Conclusion
India's unemployment is a multi-layered problem. Despite strong GDP growth, jobs are not being created fast enough for the growing workforce. Youth, women, and graduates are the most vulnerable groups.

---

## Recommendations
1. Reform education system — focus on practical skills, not just degrees
2. Create manufacturing and startup hubs in high-unemployment northern states
3. Incentivize companies to hire women
4. Launch youth apprenticeship and internship programs at scale
5. Expand rural employment schemes (MGNREGA)

---

## Future Improvements
- Use real-time data from CMIE API
- Add district-level analysis
- Build an interactive Power BI dashboard
- Include GDP vs unemployment correlation analysis

---

*Author: Basavaraj Biradar*
*Data Source: CMIE & MOSPI India*
