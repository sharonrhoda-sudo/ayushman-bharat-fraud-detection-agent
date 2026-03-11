import sqlite3
import pandas as pd


DB_PATH = "database/claims.db"


def save_to_db(df: pd.DataFrame, table_name="claims"):
    conn = sqlite3.connect(DB_PATH)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()


def load_from_db(table_name="claims"):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
    conn.close()
    return df