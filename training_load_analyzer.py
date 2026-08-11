# ==========================================
# Athlete Training Load Analyzer
# Author: Abhishek Tomar
# ==========================================

import pandas as pd


print("=" * 70)
print("             ATHLETE TRAINING LOAD ANALYZER")
print("=" * 70)


# ------------------------------------------
# Load Data
# ------------------------------------------

data = pd.read_csv("training_data.csv")

data["Date"] = pd.to_datetime(data["Date"])


# ------------------------------------------
# Calculate Session Training Load
# ------------------------------------------

data["Training_Load"] = (
    data["Duration_min"] * data["sRPE"]
)


# ------------------------------------------
# Display Session Data
# ------------------------------------------

print("\nTRAINING SESSION DATA")
print("=" * 70)

print(data.to_string(index=False))


# ------------------------------------------
# Team-Level Statistics
# ------------------------------------------

total_load = data["Training_Load"].sum()

average_load = data["Training_Load"].mean()

highest_load = data.loc[
    data["Training_Load"].idxmax()
]


print("\n" + "=" * 70)
print("TEAM TRAINING LOAD SUMMARY")
print("=" * 70)

print(f"Total Training Load  : {total_load:.0f} AU")
print(f"Average Session Load : {average_load:.1f} AU")

print(
    f"Highest Load Session : "
    f"{highest_load['Athlete']} - "
    f"{highest_load['Training_Load']:.0f} AU"
)


# ------------------------------------------
# Athlete-Level Analysis
# ------------------------------------------

athlete_summary = (
    data.groupby("Athlete")
    .agg(
        Sessions=("Athlete", "count"),
        Total_Load=("Training_Load", "sum"),
        Average_Load=("Training_Load", "mean"),
        Average_RPE=("sRPE", "mean"),
        Total_Duration=("Duration_min", "sum")
    )
    .reset_index()
)


print("\n" + "=" * 70)
print("ATHLETE TRAINING LOAD SUMMARY")
print("=" * 70)

print(
    athlete_summary.to_string(
        index=False,
        formatters={
            "Total_Load": "{:.0f}".format,
            "Average_Load": "{:.1f}".format,
            "Average_RPE": "{:.1f}".format
        }
    )
)


# ------------------------------------------
# Athlete Ranking
# ------------------------------------------

ranking = athlete_summary.sort_values(
    "Total_Load",
    ascending=False
)


print("\n" + "=" * 70)
print("ATHLETE LOAD RANKING")
print("=" * 70)

for position, (_, athlete) in enumerate(
    ranking.iterrows(),
    start=1
):

    print(
        f"{position}. "
        f"{athlete['Athlete']:<10} "
        f"{athlete['Total_Load']:.0f} AU"
    )


# ------------------------------------------
# Session Type Analysis
# ------------------------------------------

session_summary = (
    data.groupby("Session_Type")["Training_Load"]
    .agg(["count", "mean", "sum"])
    .reset_index()
)


print("\n" + "=" * 70)
print("SESSION TYPE ANALYSIS")
print("=" * 70)

print(
    session_summary.to_string(
        index=False,
        formatters={
            "mean": "{:.1f}".format,
            "sum": "{:.0f}".format
        }
    )
)


# ------------------------------------------
# Daily Team Load
# ------------------------------------------

daily_load = (
    data.groupby("Date")["Training_Load"]
    .sum()
    .reset_index()
)


print("\n" + "=" * 70)
print("DAILY TEAM TRAINING LOAD")
print("=" * 70)

for _, row in daily_load.iterrows():

    print(
        f"{row['Date'].date()} : "
        f"{row['Training_Load']:.0f} AU"
    )


print("\n" + "=" * 70)
print("ANALYSIS COMPLETE")
print("=" * 70)