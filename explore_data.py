# explore_data.py

from db_utils import fetch_salaries

def explore():
    df = fetch_salaries()
    print("🧾 First 5 rows:")
    print(df.head())
    print("\n📐 Info:")
    print(df.info())
    print("\n📊 Summary:")
    print(df.describe(include='all'))
    print("\n🔍 Null values per column:")
    print(df.isnull().sum())

if __name__ == "__main__":
    explore()
