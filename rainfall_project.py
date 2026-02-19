# ==========================================================
# FULL RAINFALL EDA PROJECT
# Exploratory Analysis of Rainfall Data in India
# Runs directly in VS Code
# ==========================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os
import warnings

warnings.filterwarnings("ignore")

print("\n===========================================")
print("   RAINFALL DATA ANALYSIS PROJECT STARTED")
print("===========================================\n")

# Create output folder automatically
if not os.path.exists("outputs"):
    os.makedirs("outputs")

# Load Dataset
try:
    df = pd.read_csv("rainfall_data.csv")
    print("Dataset Loaded Successfully!\n")
except:
    print("ERROR: rainfall_data.csv not found in this folder.")
    exit()

print("---------- FIRST 5 ROWS ----------")
print(df.head())

print("\n---------- DATA INFO ----------")
print(df.info())

print("\n---------- STATISTICAL SUMMARY ----------")
print(df.describe())

print("\n---------- MISSING VALUES ----------")
print(df.isnull().sum())

df.fillna(df.mean(numeric_only=True), inplace=True)

# Annual Rainfall Trend
if "YEAR" in df.columns and "ANNUAL" in df.columns:
    plt.figure()
    plt.plot(df["YEAR"], df["ANNUAL"])
    plt.title("Annual Rainfall Trend")
    plt.xlabel("Year")
    plt.ylabel("Annual Rainfall (mm)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("outputs/annual_rainfall_trend.png")
    plt.show()

# Monthly Average Rainfall
months = ["JAN","FEB","MAR","APR","MAY","JUN",
          "JUL","AUG","SEP","OCT","NOV","DEC"]

available_months = [m for m in months if m in df.columns]

if len(available_months) > 0:
    monthly_avg = df[available_months].mean()
    plt.figure()
    monthly_avg.plot(kind="bar")
    plt.title("Average Monthly Rainfall")
    plt.xlabel("Month")
    plt.ylabel("Rainfall (mm)")
    plt.tight_layout()
    plt.savefig("outputs/monthly_average.png")
    plt.show()

# Correlation Heatmap
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("outputs/correlation_heatmap.png")
plt.show()

# Distribution of Annual Rainfall
if "ANNUAL" in df.columns:
    plt.figure()
    sns.histplot(df["ANNUAL"], kde=True)
    plt.title("Distribution of Annual Rainfall")
    plt.tight_layout()
    plt.savefig("outputs/annual_distribution.png")
    plt.show()

# Subdivision-wise Analysis
if "SUBDIVISION" in df.columns and "ANNUAL" in df.columns:
    subdivision_avg = df.groupby("SUBDIVISION")["ANNUAL"].mean().sort_values(ascending=False)
    plt.figure(figsize=(12,6))
    subdivision_avg.plot(kind="bar")
    plt.title("Average Annual Rainfall by Subdivision")
    plt.ylabel("Rainfall (mm)")
    plt.tight_layout()
    plt.savefig("outputs/subdivision_average.png")
    plt.show()

# Interactive Plot
if "YEAR" in df.columns and "ANNUAL" in df.columns:
    fig = px.line(df, x="YEAR", y="ANNUAL",
                  title="Interactive Annual Rainfall Trend")
    fig.write_html("outputs/interactive_rainfall_plot.html")

print("\n===========================================")
print("  EDA COMPLETED SUCCESSFULLY")
print("  All graphs saved in 'outputs' folder")
print("===========================================\n")
