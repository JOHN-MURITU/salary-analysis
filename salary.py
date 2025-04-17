
# ========================================
# Salary Data Analysis & Visualization
# Dataset Source: SQLite database
# ========================================

# Import required packages
import sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style for better aesthetics
sns.set()

# ----------------------------------------
# Step 1: Connect to SQLite database
# ----------------------------------------
db_path = "database.sqlite"  # Update if your DB is in a different location
conn = sqlite3.connect(db_path)

# ----------------------------------------
# Step 2: Display available tables
# ----------------------------------------
query = "SELECT name FROM sqlite_master WHERE type='table';"
tables = pd.read_sql(query, conn)
print("Tables in the database:")
print(tables)

# ----------------------------------------
# Step 3: Load data from 'Salaries' table
# ----------------------------------------
df = pd.read_sql_query("SELECT * FROM Salaries;", conn)

# ----------------------------------------
# Step 4: Basic Exploration
# ----------------------------------------
print("\nFirst 5 rows of the Salaries table:")
print(df.head())

print("\nDataFrame Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# ----------------------------------------
# Step 5: Visualization 1 - Histogram of Total Pay
# ----------------------------------------
plt.figure(figsize=(10, 5))
sns.histplot(df["TotalPay"], kde=True, bins=20)
plt.title("Distribution of Total Pay")
plt.xlabel("Total Pay")
plt.ylabel("Frequency")
plt.show()

# ----------------------------------------
# Visualization 2 - Top 10 Highest Paying Job Titles
# ----------------------------------------
top_jobs = df.groupby("JobTitle")["TotalPay"].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_jobs.values, y=top_jobs.index, palette="viridis")
plt.title("Top 10 Highest Paying Job Titles (Average Total Pay)")
plt.xlabel("Average Total Pay")
plt.ylabel("Job Title")
plt.show()

# ----------------------------------------
# Visualization 3 - Scatter: Base Pay vs Total Pay
# ----------------------------------------
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="BasePay", y="TotalPay", hue="Year", palette="coolwarm", alpha=0.7)
plt.title("Base Pay vs Total Pay")
plt.xlabel("Base Pay")
plt.ylabel("Total Pay")
plt.legend(title='Year')
plt.show()

# ----------------------------------------
# Visualization 4 - Most Common Job Titles
# ----------------------------------------


# ----------------------------------------
# Visualization 5 - Average Total Pay by Year
# ----------------------------------------
avg_pay_year = df.groupby("Year")["TotalPay"].mean()
plt.figure(figsize=(10, 5))
sns.lineplot(x=avg_pay_year.index, y=avg_pay_year.values, marker='o')
plt.title("Average Total Pay Over Years")
plt.xlabel("Year")
plt.ylabel("Average Total Pay")
plt.grid(True)
plt.show()

# ----------------------------------------
# Visualization 6 - Top 10 Earners: Pay Breakdown
# ----------------------------------------
top_earners = df.sort_values("TotalPayBenefits", ascending=False).head(10)
top_earners_plot = top_earners[["EmployeeName", "BasePay", "OvertimePay", "TotalPayBenefits"]].set_index("EmployeeName")
top_earners_plot.plot(kind="bar", figsize=(14, 7), colormap="Paired")
plt.title("Top 10 Employees: Base Pay vs Overtime Pay vs Benefits")
plt.xlabel("Employee Name")
plt.ylabel("Pay (in USD)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ----------------------------------------
# Visualization 7 - Correlation Heatmap of Pay Columns
# ----------------------------------------
pay_cols = df[["BasePay", "OvertimePay", "OtherPay", "TotalPay", "TotalPayBenefits"]]
plt.figure(figsize=(8, 6))
sns.heatmap(pay_cols.corr(), annot=True, cmap="YlGnBu", fmt=".2f")
plt.title("Correlation Heatmap of Salary Components")
plt.show()

# ----------------------------------------
# Close the connection to the database
# ----------------------------------------
conn.close()
