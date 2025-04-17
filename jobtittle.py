import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

sns.set()


db_path ="database.sqlite"

Conn= sqlite3.connect(db_path)

query="SELECT name FROM sqlite_master WHERE type='table'"


tables= pd.read_sql(query, conn)

print("Tables in the database")
print(tables)

top_jobs_count = df["JobTitle"].value_counts().head(15)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_jobs_count.values, y=top_jobs_count.index, palette="magma")
plt.title("Top 15 Most Common Job Titles")
plt.xlabel("Number of Employees")
plt.ylabel("Job Title")
plt.show()


