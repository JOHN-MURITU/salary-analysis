# visualization.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from db_utils import fetch_salaries

sns.set_theme(style="whitegrid", palette="deep")

def visualize():
    df = fetch_salaries()
    df['TotalPay'] = pd.to_numeric(df['TotalPay'], errors='coerce')
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

    top_jobs = df['JobTitle'].value_counts().head(10)
    yearly_avg = df.groupby("Year")["TotalPay"].mean().dropna()

    # Boxplot: TotalPay by Year
    plt.figure(figsize=(10,6))
    sns.boxplot(x="Year", y="TotalPay", data=df, palette="coolwarm")
    plt.title("💰 Total Pay Distribution by Year")
    plt.xlabel("Year")
    plt.ylabel("Total Pay")
    plt.tight_layout()
    plt.savefig("boxplot_total_pay_by_year.png")
    plt.show(block=False)

    # Barplot: Top 10 Job Titles
    plt.figure(figsize=(10,6))
    sns.barplot(y=top_jobs.index, x=top_jobs.values, palette="viridis")
    plt.title("👷 Top 10 Most Common Job Titles")
    plt.xlabel("Number of Employees")
    plt.ylabel("Job Title")
    plt.tight_layout()
    plt.savefig("top_10_job_titles.png")
    plt.show(block=False)

    # Lineplot: Average TotalPay per Year
    plt.figure(figsize=(10,6))
    sns.lineplot(x=yearly_avg.index, y=yearly_avg.values, marker='o', color="#1f77b4", linewidth=2.5)
    plt.title("📈 Average Total Pay per Year")
    plt.xlabel("Year")
    plt.ylabel("Average Total Pay")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("average_total_pay_per_year.png")
    plt.show(block=False)

    # Histogram: Distribution of TotalPay
    plt.figure(figsize=(10,6))
    sns.histplot(df['TotalPay'].dropna(), bins=30, kde=True, color='orange')
    plt.title("📦 Distribution of Total Pay")
    plt.xlabel("Total Pay")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("histogram_total_pay_distribution.png")
    plt.show(block=False)

    # Pause the script to keep all windows open
    input("\n✅ All plots displayed in separate windows.\nPress Enter to close them and exit...\n")

if __name__ == "__main__":
    visualize()
