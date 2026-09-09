import pandas as pd
from pathlib import Path


MIMIC_PATH = Path(
    "data/raw/mimic_iv_demo"
)


def load_mimic_tables():

    patients = pd.read_csv(
        MIMIC_PATH /
        "hosp" /
        "patients.csv.gz"
    )

    admissions = pd.read_csv(
        MIMIC_PATH /
        "hosp" /
        "admissions.csv.gz"
    )

    transfers = pd.read_csv(
        MIMIC_PATH /
        "hosp" /
        "transfers.csv.gz"
    )

    icustays = pd.read_csv(
        MIMIC_PATH /
        "icu" /
        "icustays.csv.gz"
    )


    return {
        "patients": patients,
        "admissions": admissions,
        "transfers": transfers,
        "icustays": icustays
    }


if __name__ == "__main__":

    tables = load_mimic_tables()

    for name, df in tables.items():

        print(
            name,
            df.shape
        )