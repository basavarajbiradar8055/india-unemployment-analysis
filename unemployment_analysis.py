import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import statistics
from sklearn.linear_model import LinearRegression

# ── Problem Statement ─────────────────────────────────────────────────────────

print("=" * 55)
print("   INDIA UNEMPLOYMENT ANALYSIS (2015 - 2024)")
print("=" * 55)
print("""
PROBLEM STATEMENT:
  India is one of the fastest growing economies, yet
  unemployment remains a serious challenge. With a
  large youth population and education-jobs mismatch,
  unemployment affects millions of families every year.

  This project analyzes India's unemployment data from
  2015 to 2024 across gender, age, education, and
  state-wise groups to find key patterns and predict
  future trends using Machine Learning.

OBJECTIVE:
  1. Understand how unemployment changed over 10 years
  2. Identify which groups are most affected in India
  3. Predict unemployment rates for 2025, 2026, 2027

DATASET SOURCE:
  Centre for Monitoring Indian Economy (CMIE)
  Ministry of Statistics & PI (MOSPI), India
  Website: cmie.com / mospi.gov.in
""")

# ── India Data ────────────────────────────────────────────────────────────────

years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
rate  = [4.9,  5.4,  5.4,  6.1,  5.3,  8.0,  8.7,  7.3,  7.5,  7.8]

df = pd.DataFrame({"Year": years, "Rate": rate})

# ── Statistics ────────────────────────────────────────────────────────────────

print("STATISTICS SUMMARY")
print("Mean   :", statistics.mean(rate))
print("Median :", statistics.median(rate))
print("Std Dev:", round(statistics.stdev(rate), 2))
print("Max    :", max(rate), "(COVID 2020-21)")
print("Min    :", min(rate))

# ── ML Prediction ─────────────────────────────────────────────────────────────

df_clean = df[df["Year"] != 2020]
model = LinearRegression()
model.fit(df_clean[["Year"]], df_clean["Rate"])

future = pd.DataFrame({"Year": [2025, 2026, 2027]})
preds  = model.predict(future)

print("\nML PREDICTION (Linear Regression)")
print("2025 ->", round(preds[0], 2), "%")
print("2026 ->", round(preds[1], 2), "%")
print("2027 ->", round(preds[2], 2), "%")

# ── Chart 1: Line Chart + ML Prediction ──────────────────────────────────────

plt.figure(figsize=(11, 5))
plt.plot(df["Year"], df["Rate"], color="red", marker="o", linewidth=2, label="Actual Rate")
plt.plot([2024, 2025, 2026, 2027], [7.8] + list(preds), color="orange",
         marker="s", linestyle="--", linewidth=2, label="ML Prediction")
for x, y in zip(years, rate):
    plt.text(x, y + 0.2, f"{y}%", ha="center", fontsize=8, fontweight="bold")
plt.title("India Unemployment Rate 2015-2024 + ML Prediction")
plt.xlabel("Year")
plt.ylabel("Rate (%)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("line_chart.png")
plt.close()
print("\nSaved: line_chart.png")

# ── Chart 2: Bar Chart by Year ────────────────────────────────────────────────

plt.figure(figsize=(11, 5))
colors = ["green" if r < 6 else "orange" if r < 8 else "red" for r in rate]
plt.bar(df["Year"], df["Rate"], color=colors)
for i, (yr, r) in enumerate(zip(years, rate)):
    plt.text(yr, r + 0.1, f"{r}%", ha="center", fontsize=8, fontweight="bold")
plt.title("India Unemployment Rate by Year")
plt.xlabel("Year")
plt.ylabel("Rate (%)")
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.close()
print("Saved: bar_chart.png")

# ── Chart 3: Men vs Women ─────────────────────────────────────────────────────

gender = pd.DataFrame({
    "Year":  [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    "Men":   [3.2,  3.5,  3.8,  5.8,  4.7,  6.5,  7.3,  6.2,  6.5,  6.8],
    "Women": [8.7,  9.2,  9.0,  7.5,  7.0,  13.0, 13.5, 10.2, 9.8,  10.5]
})

plt.figure(figsize=(11, 5))
plt.plot(gender["Year"], gender["Men"],   color="blue", marker="o", linewidth=2, label="Men")
plt.plot(gender["Year"], gender["Women"], color="red",  marker="o", linewidth=2, label="Women")
plt.fill_between(gender["Year"], gender["Men"], gender["Women"], alpha=0.1, color="purple")
plt.title("India Unemployment: Men vs Women (2015-2024)")
plt.xlabel("Year")
plt.ylabel("Rate (%)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("gender_chart.png")
plt.close()
print("Saved: gender_chart.png")

# ── Chart 4: Education Level (India Paradox) ──────────────────────────────────

edu = pd.DataFrame({
    "Education":    ["Illiterate", "Primary", "Secondary", "Graduate+"],
    "Unemployment": [0.9,          1.8,        5.2,         18.4]
})

plt.figure(figsize=(9, 5))
plt.barh(edu["Education"], edu["Unemployment"],
         color=["green", "blue", "orange", "red"])
for i, val in enumerate(edu["Unemployment"]):
    plt.text(val + 0.2, i, f"{val}%", va="center", fontsize=11, fontweight="bold")
plt.title("India Unemployment by Education Level\n(Higher Education = Higher Unemployment Paradox)")
plt.xlabel("Rate (%)")
plt.grid(axis="x")
plt.tight_layout()
plt.savefig("education_chart.png")
plt.close()
print("Saved: education_chart.png")

# ── Chart 5: State-wise Bar Chart ────────────────────────────────────────────

states = pd.DataFrame({
    "State":        ["Haryana", "Rajasthan", "Bihar", "Kerala", "Gujarat", "Karnataka"],
    "Unemployment": [26.7,      24.5,        12.4,    8.3,      2.1,       3.5]
})

plt.figure(figsize=(10, 5))
plt.bar(states["State"], states["Unemployment"],
        color=["red", "red", "orange", "orange", "green", "green"])
for i, val in enumerate(states["Unemployment"]):
    plt.text(i, val + 0.3, f"{val}%", ha="center", fontsize=10, fontweight="bold")
plt.title("Unemployment by State in India (2024)")
plt.xlabel("State")
plt.ylabel("Rate (%)")
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("state_chart.png")
plt.close()
print("Saved: state_chart.png")

# ── Chart 6: Rural vs Urban ───────────────────────────────────────────────────

area = pd.DataFrame({
    "Area":         ["Rural", "Urban"],
    "Unemployment": [5.3,     8.9]
})

plt.figure(figsize=(7, 5))
plt.bar(area["Area"], area["Unemployment"], color=["green", "steelblue"], width=0.4)
for i, val in enumerate(area["Unemployment"]):
    plt.text(i, val + 0.2, f"{val}%", ha="center", fontsize=13, fontweight="bold")
plt.title("India Unemployment: Rural vs Urban (2024)")
plt.xlabel("Area")
plt.ylabel("Rate (%)")
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("rural_urban_chart.png")
plt.close()
print("Saved: rural_urban_chart.png")

# ── Chart 7: Age Group ────────────────────────────────────────────────────────

age = pd.DataFrame({
    "Age Group": ["15-24", "25-29", "30-44", "45-59", "60+"],
    "Rate":      [23.2,    13.4,    5.6,     2.9,     1.4]
})

plt.figure(figsize=(9, 5))
plt.bar(age["Age Group"], age["Rate"],
        color=["red", "orange", "blue", "green", "purple"])
for i, val in enumerate(age["Rate"]):
    plt.text(i, val + 0.3, f"{val}%", ha="center", fontsize=10, fontweight="bold")
plt.title("India Unemployment by Age Group (2024)")
plt.xlabel("Age Group")
plt.ylabel("Rate (%)")
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("age_chart.png")
plt.close()
print("Saved: age_chart.png")

# ── Chart 8: Seaborn Heatmap ──────────────────────────────────────────────────

heat = pd.DataFrame({
    "Overall":  rate,
    "Youth":    [20.1, 21.3, 22.0, 23.5, 22.8, 30.2, 31.5, 24.0, 23.5, 23.2],
    "Women":    [8.7,  9.2,  9.0,  7.5,  7.0,  13.0, 13.5, 10.2, 9.8,  10.5],
    "Urban":    [6.5,  7.0,  7.2,  8.0,  7.3,  10.5, 11.0, 9.2,  9.0,  8.9]
})

plt.figure(figsize=(8, 5))
sns.heatmap(heat.corr(), annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap - India Unemployment Groups")
plt.tight_layout()
plt.savefig("heatmap.png")
plt.close()
print("Saved: heatmap.png")

print("\nALL 8 CHARTS SAVED!")

# ── Key Insights ──────────────────────────────────────────────────────────────

print("\n" + "=" * 55)
print("   KEY INSIGHTS")
print("=" * 55)
print("""
  1. EDUCATION PARADOX:
     Graduates face 18.4% unemployment - 20x more than
     illiterates (0.9%). More education does NOT guarantee
     a job in India. Skills mismatch is a big problem.

  2. WOMEN ARE HARDEST HIT:
     Women face 10.5% unemployment vs 6.8% for men.
     India has one of the lowest female labor force
     participation rates in the world.

  3. YOUTH CRISIS:
     15-24 age group faces 23.2% unemployment.
     1 in 4 young Indians cannot find a job.

  4. COVID-19 IMPACT (2020-21):
     Unemployment jumped to 8.7% in 2021, the highest
     in 10 years due to lockdowns and job losses.

  5. STATE INEQUALITY:
     Haryana (26.7%) vs Gujarat (2.1%) - huge gap.
     Southern states perform much better than Northern.

  6. URBAN vs RURAL:
     Urban unemployment (8.9%) is higher than rural (5.3%)
     because urban workers are more likely to report
     themselves as unemployed.

  7. ML PREDICTION (2025-2027):
     If current trends continue, India's unemployment
     rate may hover around 7-8% through 2027.
     Policy intervention is needed to bring it down.
""")

# ── Conclusion ────────────────────────────────────────────────────────────────

print("=" * 55)
print("   CONCLUSION")
print("=" * 55)
print("""
  India's unemployment challenge is unique and complex.
  Despite strong GDP growth, jobs are not being created
  fast enough for the growing working-age population.

  Key groups needing immediate attention:
  - Youth (15-24) facing 23% unemployment
  - Women with low workforce participation
  - Graduates with no matching job opportunities
  - High-unemployment states like Haryana & Rajasthan

  RECOMMENDATIONS:
  1. Invest in vocational & skill-based education
  2. Create more manufacturing & startup jobs
  3. Support women re-entering the workforce
  4. Focus job creation in high-unemployment states

  Data Source : CMIE (cmie.com), MOSPI (mospi.gov.in)
  Tools Used  : Python, Pandas, Matplotlib, Seaborn,
                Scikit-learn, Statistics
""")
print("=" * 55)
