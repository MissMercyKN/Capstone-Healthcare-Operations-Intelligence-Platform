import pandas as pd
from pathlib import Path
import sqlite3


FEATURE_PATH = Path(
    "data/processed/analytics_features_v3.csv"
)


DATABASE_PATH = (
    "data/database/hospital_operations.db"
)


def load_features():

    return pd.read_csv(
        FEATURE_PATH
    )



def load_table(table_name):

    conn = sqlite3.connect(
        DATABASE_PATH
    )

    df = pd.read_sql(
        f"SELECT * FROM {table_name}",
        conn
    )

    conn.close()

    return df