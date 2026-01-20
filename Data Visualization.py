# ==========================================
# Data Visualization Internship Project
# AI Jobs Dataset Analysis
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------
# Global Visualization Settings
# ------------------------------------------
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# ------------------------------------------
# Load Dataset
# ------------------------------------------
try:
    df = pd.read_csv("ai_jobs.csv")   # CSV must be in same folder
    print("Dataset loaded successfully!\n")
except FileNotFoundError:
    print("Error: ai_jobs.csv file not found.")
    exit()

# ------------------------------------------
# Dataset Overview
# ------------------------------------------
print("First 5 rows of dataset:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nColumn Names:")
print(df.columns)

# ------------------------------------------
# 1. Top 10 Countries Offering AI Jobs
# (Safe column detection to avoid KeyError)
# ------------------------------------------
country_column = None
possible_columns = [
    "employee_residence",
    "company_location",
    "work_country",
    "location"
]

for col in possible_columns:
    if col in df.columns:
        country_column = col
        break

if country_column:
    top_countries = df[country_column].value_counts().head(10)

    plt.figure()
    sns.barplot(
        x=top_countries.values,
        y=top_countries.index
    )
    plt.title("Top 10 Countries Offering AI Jobs")
    plt.xlabel("Number of Jobs")
    plt.ylabel("Country")
    plt.tight_layout()
    plt.show()
else:
    print("No country-related column found in dataset.")

# ------------------------------------------
# 2. Experience Level Distribution
# ------------------------------------------
if "experience_level" in df.columns:
    plt.figure()
    sns.countplot(
        x="experience_level",
        data=df
    )
    plt.title("Experience Level Distribution")
    plt.xlabel("Experience Level")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()
else:
    print("Column 'experience_level' not found.")

# ------------------------------------------
# 3. Employment Type Distribution
# ------------------------------------------
if "employment_type" in df.columns:
    plt.figure()
    sns.countplot(
        x="employment_type",
        data=df
    )
    plt.title("Employment Type Distribution")
    plt.xlabel("Employment Type")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()
else:
    print("Column 'employment_type' not found.")

# ------------------------------------------
# 4. Remote Work Distribution
# ------------------------------------------
remote_column = None
for col in ["remote_type", "remote_ratio"]:
    if col in df.columns:
        remote_column = col
        break

if remote_column:
    plt.figure()
    sns.countplot(
        x=remote_column,
        data=df
    )
    plt.title("Remote Work Distribution")
    plt.xlabel("Remote Type")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()
else:
    print("No remote work column found.")

# ------------------------------------------
# 5. Salary Distribution
# ------------------------------------------
salary_column = None
for col in ["salary_in_usd", "salary_max_usd", "salary_min_usd"]:
    if col in df.columns:
        salary_column = col
        break

if salary_column:
    plt.figure()
    sns.histplot(
        df[salary_column],
        bins=30,
        kde=True
    )
    plt.title("Salary Distribution (USD)")
    plt.xlabel("Salary in USD")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()
else:
    print("No salary column found.")

# ------------------------------------------
# End of Program
# ------------------------------------------
print("\nData Visualization completed successfully!")
