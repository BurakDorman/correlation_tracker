import sqlite3
import pandas as pd

conn = sqlite3.connect('crypto_prices.db')

def calculate_correlations():
    query = "SELECT * FROM prices"
    df = pd.read_sql_query(query, conn)
    pivot_df = df.pivot(index='timestamp', columns='symbol', values='price')
    correlations = pivot_df.corr()
    return correlations

correlations = calculate_correlations()
print(correlations)
