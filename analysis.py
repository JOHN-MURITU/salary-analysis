# analysis.py

import pandas as pd
from db_utils import fetch_salaries

def perform_analysis():
    df = fetch_salaries()

    # Convert numeric columns to float
    for col in ['BasePay', 'OvertimePay', 'OtherPay', 'Benefits', 'TotalPay', 'TotalPayBenefits']:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    print("\n📅 Yearly Salary Averages:")
    print(df.groupby("Year")[["BasePay", "OvertimePay", "TotalPay"]].mean())

    print("\n👷 Top 10 Job Titles:")
    print(df["JobTitle"].value_counts().head(10))

    print("\n💰 Top Earners:")
    print(df.sort_values("TotalPayBenefits", ascending=False)[["EmployeeName", "TotalPayBenefits"]].head(10))

if __name__ == "__main__":
    perform_analysis()
