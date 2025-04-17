# Importing required packages
import sqlite3  # for connecting to SQLite databases
import numpy as np  # for numerical operations (optional here but useful in general)
import pandas as pd  # for data manipulation and analysis
import matplotlib.pyplot as plt  # for basic plotting
import seaborn as sns  # for enhanced statistical plotting

# Set seaborn as the default style for plots
sns.set()

# Path to the SQLite database file
db_path = "database.sqlite"
# Establish a connection to the database
conn = sqlite3.connect(db_path)


# Fetch all table names in the database
query = "SELECT name FROM sqlite_master WHERE type='table';"
tables = pd.read_sql(query, conn)


# Display the available tables
print("Tables in the database:")
print(tables)

# Load first 5 rows from the 'Salaries' table
df = pd.read_sql_query("SELECT * FROM Salaries;", conn)

# Display the first few rows of the DataFrame
print("\nFirst 5 rows of the Salaries table:")
print(df.head())

# Display column information, non-null values, and data types
print("\nDataFrame Info:")
print(df.info())

# Display summary statistics for numerical columns
print("\nSummary Statistics:")
print(df.describe())

# Plot histogram to visualize the distribution of Total Pay
plt.figure(figsize=(10, 5))
sns.histplot(df["TotalPay"], kde=True, bins=20)  # Corrected column name (case sensitive)
plt.title("Distribution of Total Pay")
plt.xlabel("Total Pay")
plt.ylabel("Frequency")
plt.show()

# type: ignore # Optional: Close the connection to the database when done
# conn.close()
