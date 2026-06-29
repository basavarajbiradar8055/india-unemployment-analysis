import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import statistics
from sklearn.linear_model import LinearRegression
import os

os.makedirs("../Images", exist_ok=True)

# ── Load Real Dataset ─────────────────────────────────────────────────────────
df = pd.read_csv("../Dataset/india_unemployment_real.csv")
print("=" * 55)
print("  INDIA UNEMPLOYMENT ANALYSIS")
print("  Source: World Bank Open Data (real data)")
print("=" * 55)
print(f"\n  Rows    : {df.shape[0]}")
print(f"  Columns : {df.shape[1]}")
print(f"  Years   : {df['Year'].min()} to {df['Year'].max()}")
print(f"\n{df.to_string(index=False)}\n")

# ── Statistics ────────────────────────────────────────────────────────────────
rate = list(df["Overall_Rate"])
print("STATISTICS")
print(f"  Mean   : {round(statistics.mean(rate), 2)}%")
print(f"  Median : {round(statistics.median(rate), 2)}%")
print(f"  Std Dev: {round(statistics.stdev(rate), 2)}%")
print(f"  Max    : {max(rate)}%  ({df.loc[df['Overall_Rate'].idxmax(), 'Year']})")
print(f"  Min    : {min(rate)}%  ({df.loc[df['Overall_Rate'].idxmin(), 'Year']})")

# ── ML Prediction ─────────────────────────────────────────────────────────────
model = LinearRegression()
model.fit(df[["Year"]], df["Overall_Rate"])
future = pd.DataFrame({"Year": [2025, 2026, 2027]})
preds  = model.predict(future)
print(f"\nML PREDICTION")
print(f"  2025 -> {round(preds[0], 2)}%")
print(f"  2026 -> {round(preds[1], 2)}%")
print(f"  2027 -> {round(preds[2], 2)}%")

# ── Chart 1: Unemployment Trend + ML ─────────────────────────────────────────
plt.figure(figsize=(12, 5))
plt.plot(df["Year"], df["Overall_Rate"], color="red", marker="o", linewidth=2, label="Actual")
plt.fill_between(df["Year"], df["Overall_Rate"], alpha=0.15, color="red")
plt.plot([2024, 2025, 2026, 2027], [df["Overall_Rate"].iloc[-1]] + list(preds),
         color="orange", marker="s", linestyle="--", linewidth=2, label="ML Prediction")
for x, y in zip(df["Year"], df["Overall_Rate"]):
    plt.text(x, y + 0.15, f"{y}%", ha="center", fontsize=7, fontweight="bold")
plt.title("India Unemployment Rate 2010-2024 + ML Prediction (World Bank Data)")
plt.xlabel("Year")
plt.ylabel("Rate (%)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("../Images/01_trend.png", dpi=150)
plt.close()
print("\n  Saved: 01_trend.png")

# ── Chart 2: Men vs Women ─────────────────────────────────────────────────────
plt.figure(figsize=(12, 5))
plt.plot(df["Year"], df["Male_Rate"],   color="steelblue", marker="o", linewidth=2, label="Male")
plt.plot(df["Year"], df["Female_Rate"], color="crimson",   marker="o", linewidth=2, label="Female")
plt.fill_between(df["Year"], df["Male_Rate"], df["Female_Rate"], alpha=0.1, color="purple")
plt.title("India Unemployment: Male vs Female (World Bank Real Data)")
plt.xlabel("Year")
plt.ylabel("Rate (%)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("../Images/02_gender.png", dpi=150)
plt.close()
print("  Saved: 02_gender.png")

# ── Chart 3: Overall vs Youth ─────────────────────────────────────────────────
plt.figure(figsize=(12, 5))
plt.plot(df["Year"], df["Overall_Rate"], color="green",  marker="o", linewidth=2, label="Overall")
plt.plot(df["Year"], df["Youth_Rate"],   color="red",    marker="o", linewidth=2, label="Youth (15-24)")
plt.fill_between(df["Year"], df["Overall_Rate"], df["Youth_Rate"], alpha=0.1, color="orange")
plt.title("Overall vs Youth Unemployment in India (World Bank Real Data)")
plt.xlabel("Year")
plt.ylabel("Rate (%)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("../Images/03_youth_vs_overall.png", dpi=150)
plt.close()
print("  Saved: 03_youth_vs_overall.png")

# ── Chart 4: Seaborn Bar – All Groups in 2024 ─────────────────────────────────
latest = df[df["Year"] == 2024][["Overall_Rate", "Male_Rate", "Female_Rate", "Youth_Rate"]].T.reset_index()
latest.columns = ["Group", "Rate"]
latest["Group"] = ["Overall", "Male", "Female", "Youth (15-24)"]

plt.figure(figsize=(9, 5))
sns.barplot(x="Group", y="Rate", data=latest, palette=["steelblue", "green", "crimson", "orange"])
for i, row in latest.iterrows():
    plt.text(i, row["Rate"] + 0.2, f"{row['Rate']}%", ha="center", fontsize=11, fontweight="bold")
plt.title("India Unemployment by Group – 2024 (World Bank Real Data)")
plt.xlabel("")
plt.ylabel("Rate (%)")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("../Images/04_groups_2024.png", dpi=150)
plt.close()
print("  Saved: 04_groups_2024.png")

# ── Chart 5: Seaborn Heatmap ──────────────────────────────────────────────────
plt.figure(figsize=(8, 5))
sns.heatmap(df[["Overall_Rate", "Male_Rate", "Female_Rate", "Youth_Rate"]].corr(),
            annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap – India Unemployment Groups")
plt.tight_layout()
plt.savefig("../Images/05_heatmap.png", dpi=150)
plt.close()
print("  Saved: 05_heatmap.png")

# ── Chart 6: Year-over-Year Change ────────────────────────────────────────────
df["YoY"] = df["Overall_Rate"].diff()
colors = ["green" if v < 0 else "red" for v in df["YoY"].fillna(0)]

plt.figure(figsize=(12, 5))
plt.bar(df["Year"], df["YoY"].fillna(0), color=colors, width=0.6)
plt.axhline(0, color="black", linewidth=0.8)
plt.title("Year-over-Year Change (Green = Improved, Red = Worsened)")
plt.xlabel("Year")
plt.ylabel("Change (%)")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("../Images/06_yoy_change.png", dpi=150)
plt.close()
print("  Saved: 06_yoy_change.png")

# ── Chart 7: State-wise Bar (CMIE 2024 published data) ────────────────────────
states = pd.DataFrame({
    "State":  ["Haryana", "Rajasthan", "Jharkhand", "Bihar", "UP", "Punjab",
               "West Bengal", "Kerala", "Telangana", "Tamil Nadu", "Maharashtra", "Gujarat"],
    "Rate":   [26.7, 24.5, 17.8, 12.4, 8.9, 7.8, 6.5, 8.3, 5.5, 4.5, 4.0, 2.1]
})
colors_s = ["#e74c3c" if r > 15 else "#e67e22" if r > 8 else "#27ae60" for r in states["Rate"]]

plt.figure(figsize=(13, 5))
bars = plt.bar(states["State"], states["Rate"], color=colors_s, width=0.6)
for bar, val in zip(bars, states["Rate"]):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
             f"{val}%", ha="center", fontsize=9, fontweight="bold")
plt.title("State-wise Unemployment Rate in India 2024 (CMIE Data)")
plt.xlabel("State")
plt.ylabel("Rate (%)")
plt.xticks(rotation=20)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("../Images/07_state_wise.png", dpi=150)
plt.close()
print("  Saved: 07_state_wise.png")

# ── Chart 8: Education Paradox ────────────────────────────────────────────────
edu = pd.DataFrame({
    "Education":    ["Illiterate", "Primary", "Secondary", "Graduate+"],
    "Rate":         [0.9, 1.8, 5.2, 18.4]
})

plt.figure(figsize=(9, 5))
bars = plt.barh(edu["Education"], edu["Rate"],
                color=["#27ae60", "#3498db", "#e67e22", "#e74c3c"], height=0.45)
for bar, val in zip(bars, edu["Rate"]):
    plt.text(val + 0.2, bar.get_y() + bar.get_height()/2,
             f"{val}%", va="center", fontsize=12, fontweight="bold")
plt.title("Education Paradox – Graduates Face Highest Unemployment (CMIE 2024)")
plt.xlabel("Rate (%)")
plt.grid(axis="x", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("../Images/08_education.png", dpi=150)
plt.close()
print("  Saved: 08_education.png")

print("\n  ALL 8 CHARTS SAVED!")

# ── Insights & Conclusion ─────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("  KEY INSIGHTS (from real World Bank data)")
print("=" * 55)
print("""
  1. Peak unemployment was in 2020 at 7.86% due to COVID
  2. Fastest recovery: 2022-2023, dropped to 4.17%
  3. Youth unemployment (15-24) is 15.75% - nearly 4x overall
  4. Female rate has been consistently close to male rate
  5. Haryana has 12x higher unemployment than Gujarat
  6. Graduate unemployment paradox persists across years
  7. ML predicts unemployment to stabilize below 4% by 2027
""")
print("=" * 55)
print("  Data: World Bank API + CMIE India (real data)")
print("  Author: Basavaraj Biradar")
print("=" * 55)
