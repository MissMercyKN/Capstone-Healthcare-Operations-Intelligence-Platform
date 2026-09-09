import sqlite3
from pathlib import Path
import pandas as pd


DATABASE_PATH = Path(
    "data/database/hospital_operations.db"
)


def load_csv_to_database(
    connection,
    file_path,
    table_name
):

    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        connection,
        if_exists="replace",
        index=False
    )


def load_mimic_tables(connection):

    mimic = Path(
        "data/raw/mimic_iv_demo"
    )


    tables = {

        "patients":
        mimic / "hosp/patients.csv.gz",

        "admissions":
        mimic / "hosp/admissions.csv.gz",

        "transfers":
        mimic / "hosp/transfers.csv.gz",

        "icustays":
        mimic / "icu/icustays.csv.gz"

    }


    for name, path in tables.items():

        df = pd.read_csv(path)

        df.to_sql(
            name,
            connection,
            if_exists="replace",
            index=False
        )



def load_operational_tables(connection):

    operational = Path(
        "data/raw/synthetic"
    )


    tables = {

        "patient_flow":
        operational / "patient_flow.csv",

        "capacity":
        operational / "capacity.csv",

        "staffing":
        operational / "staffing.csv",

        "inventory":
        operational / "inventory.csv",

        "incidents":
        operational / "incidents.csv"

    }


    for name, path in tables.items():

        df = pd.read_csv(path)

        df.to_sql(
            name,
            connection,
            if_exists="replace",
            index=False
        )



def build_database():

    DATABASE_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    connection = sqlite3.connect(
        DATABASE_PATH
    )


    load_mimic_tables(connection)

    load_operational_tables(connection)


    connection.close()


if __name__ == "__main__":

    build_database()

    print(
        "Database rebuilt successfully"
    )