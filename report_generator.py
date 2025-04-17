# report_generator.py

from db_utils import fetch_salaries

def generate_report():
    df = fetch_salaries()
    df.to_csv("salaries_export.csv", index=False)
    print("📁 Exported database as 'salaries_export.csv'")

if __name__ == "__main__":
    generate_report()
