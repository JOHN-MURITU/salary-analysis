# db_utils.py

import sqlite3
import pandas as pd
from config import DB_PATH

def get_connection():
    return sqlite3.connect(DB_PATH)

def fetch_salaries():
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM Salaries", conn)
    conn.close()
    return df
