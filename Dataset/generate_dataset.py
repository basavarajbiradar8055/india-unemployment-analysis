import pandas as pd
import random

random.seed(42)

states = {
    "Haryana":       27.0,
    "Rajasthan":     24.0,
    "Jharkhand":     19.0,
    "Bihar":         12.5,
    "Uttar Pradesh": 9.0,
    "Punjab":        8.0,
    "West Bengal":   7.5,
    "Kerala":        8.5,
    "Madhya Pradesh":6.0,
    "Telangana":     5.5,
    "Andhra Pradesh":5.0,
    "Tamil Nadu":    4.5,
    "Maharashtra":   4.0,
    "Karnataka":     3.5,
    "Gujarat":       2.2,
}

years      = list(range(2015, 2025))
genders    = ["Male", "Female"]
areas      = ["Rural", "Urban"]
age_groups = ["15-24", "25-34", "35-44", "45-54", "55+"]
educations = ["Illiterate", "Primary", "Secondary", "Graduate"]

# Multipliers to make data realistic
year_factor = {
    2015: 0.90, 2016: 0.95, 2017: 0.95, 2018: 1.05,
    2019: 0.92, 2020: 1.45, 2021: 1.55, 2022: 1.30,
    2023: 1.32, 2024: 1.35
}
gender_factor    = {"Male": 0.85, "Female": 1.55}
area_factor      = {"Rural": 0.75, "Urban": 1.30}
age_factor       = {"15-24": 2.8, "25-34": 1.4, "35-44": 0.7, "45-54": 0.5, "55+": 0.4}
education_factor = {"Illiterate": 0.15, "Primary": 0.30, "Secondary": 0.85, "Graduate": 2.80}

rows = []
for year in years:
    for state, base in states.items():
        for gender in genders:
            for area in areas:
                for age in age_groups:
                    for edu in educations:
                        rate = (base
                                * year_factor[year]
                                * gender_factor[gender]
                                * area_factor[area]
                                * age_factor[age]
                                * education_factor[edu])
                        noise = random.uniform(-0.5, 0.5)
                        rate  = round(max(0.5, min(rate + noise, 40.0)), 2)
                        rows.append({
                            "Year":         year,
                            "State":        state,
                            "Gender":       gender,
                            "Area":         area,
                            "AgeGroup":     age,
                            "Education":    edu,
                            "Unemployment": rate
                        })

df = pd.DataFrame(rows)
df.to_csv("india_unemployment_large.csv", index=False)
print(f"Dataset created: {len(df)} rows x {len(df.columns)} columns")
print(df.head(10))
