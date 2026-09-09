import sqlite3
import pandas as pd
import numpy as np

from pathlib import Path


DB_PATH = (
    "data/database/hospital_operations.db"
)

OUTPUT_PATH = Path(
    "data/processed/analytics_features_v3.csv"
)


def build_features():

    conn = sqlite3.connect(DB_PATH)

    patient_flow = pd.read_sql(
        "SELECT * FROM patient_flow",
        conn
    )

    capacity = pd.read_sql(
        "SELECT * FROM capacity",
        conn
    )

    staffing = pd.read_sql(
        "SELECT * FROM staffing",
        conn
    )

    conn.close()


    # --------------------------------------------------
    # Create operational time-series observations
    # --------------------------------------------------

    np.random.seed(42)

    dates = pd.date_range(
        start="2026-01-01",
        periods=180,
        freq="D"
    )

    departments = (
        patient_flow["department"]
        .dropna()
        .unique()
    )

    records = []

    for date in dates:

        for department in departments:

            patient_volume = np.random.randint(
                50,
                250
            )

            avg_wait_time = np.random.randint(
                20,
                100
            )

            avg_treatment_time = np.random.randint(
                30,
                150
            )

            records.append(
                {
                    "date": date,
                    "department": department,
                    "patient_volume": patient_volume,
                    "avg_wait_time": avg_wait_time,
                    "avg_treatment_time": avg_treatment_time
                }
            )


    features = pd.DataFrame(records)


    # --------------------------------------------------
    # Add capacity information
    # --------------------------------------------------

    features = features.merge(
        capacity[
            [
                "department",
                "occupancy_rate"
            ]
        ],
        on="department",
        how="left"
    )


    # --------------------------------------------------
    # Add staffing information
    # --------------------------------------------------

    staffing["staff_available"] = (
        staffing["doctors"]
        +
        staffing["nurses"]
    )

    staffing_features = staffing[
        [
            "department",
            "staff_available"
        ]
    ].copy()

    features = features.merge(
        staffing_features,
        on="department",
        how="left"
    )


    # --------------------------------------------------
    # Calculate staffing pressure
    # --------------------------------------------------

    features["staff_ratio"] = (
        features["patient_volume"]
        /
        features["staff_available"]
    )


    # --------------------------------------------------
    # Validate operational fields
    # --------------------------------------------------

    required_columns = [
        "patient_volume",
        "avg_wait_time",
        "avg_treatment_time",
        "occupancy_rate",
        "staff_available",
        "staff_ratio"
    ]

    if features[required_columns].isnull().any().any():

        missing_summary = (
            features[required_columns]
            .isnull()
            .sum()
        )

        raise ValueError(
            f"Missing values detected in feature engineering:\n"
            f"{missing_summary}"
        )


    # --------------------------------------------------
    # Current-period operational risk score
    # --------------------------------------------------

    wait_score = (
        features["avg_wait_time"]
        /
        features["avg_wait_time"].max()
    )

    occupancy_score = (
        features["occupancy_rate"]
        /
        features["occupancy_rate"].max()
    )

    staff_score = (
        features["staff_ratio"]
        /
        features["staff_ratio"].max()
    )

    features["risk_score"] = (
        (wait_score * 0.40)
        +
        (occupancy_score * 0.35)
        +
        (staff_score * 0.25)
    ) * 100


    # --------------------------------------------------
    # Current-period congestion status
    # This is descriptive, not the final ML target
    # --------------------------------------------------

    features["current_congestion_flag"] = (
        features["risk_score"] >= 65
    ).astype(int)


    # --------------------------------------------------
    # Create leakage-free predictive target
    #
    # Current operational conditions are used to predict
    # the NEXT operational period's congestion status.
    # --------------------------------------------------

    features = (
        features
        .sort_values(
            [
                "department",
                "date"
            ]
        )
        .reset_index(drop=True)
    )

    features["congestion_flag"] = (
        features
        .groupby("department")
        ["current_congestion_flag"]
        .shift(-1)
    )


    # Final observation for each department has no
    # next-period outcome, so it cannot be used for training

    features = (
        features
        .dropna(
            subset=[
                "congestion_flag"
            ]
        )
        .copy()
    )

    features["congestion_flag"] = (
        features["congestion_flag"]
        .astype(int)
    )


    # --------------------------------------------------
    # Ensure date is stored consistently
    # --------------------------------------------------

    features["date"] = pd.to_datetime(
        features["date"]
    ).dt.strftime(
        "%Y-%m-%d"
    )


    # --------------------------------------------------
    # Save final feature dataset
    # --------------------------------------------------

    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    features.to_csv(
        OUTPUT_PATH,
        index=False
    )


    # --------------------------------------------------
    # Validation output
    # --------------------------------------------------

    print(
        "Created:",
        OUTPUT_PATH
    )

    print(
        "\nDataset shape:"
    )

    print(
        features.shape
    )

    print(
        "\nTarget distribution:"
    )

    print(
        features[
            "congestion_flag"
        ].value_counts()
    )

    print(
        "\nPreview:"
    )

    print(
        features.head()
    )


if __name__ == "__main__":

    build_features()