import sqlite3
import pandas as pd
from pathlib import Path


DB_PATH = (
    "data/database/hospital_operations.db"
)


OUTPUT_PATH = Path(
    "data/processed/analytics_features_v2.csv"
)


def build_features():

    conn = sqlite3.connect(DB_PATH)


    # Load operational tables

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


    inventory = pd.read_sql(
        "SELECT * FROM inventory",
        conn
    )


    incidents = pd.read_sql(
        "SELECT * FROM incidents",
        conn
    )


    conn.close()


    # Patient flow aggregation

    patient_features = (
        patient_flow
        .groupby("department")
        .agg(

            patient_volume=(
                "visit_id",
                "count"
            ),

            avg_wait_time=(
                "waiting_time",
                "mean"
            ),

            avg_treatment_time=(
                "treatment_time",
                "mean"
            )

        )
        .reset_index()
    )


    # Staffing integration

    staffing["staff_available"] = (
        staffing["doctors"]
        +
        staffing["nurses"]
    )


    staffing_features = (
        staffing
        .groupby("department")
        ["staff_available"]
        .mean()
        .reset_index()
    )


    # Merge capacity

    features = patient_features.merge(
        capacity[
            [
                "department",
                "occupancy_rate"
            ]
        ],
        on="department",
        how="left"
    )


    # Merge staffing

    features = features.merge(
        staffing_features,
        on="department",
        how="left"
    )


    # Staff pressure

    features["staff_ratio"] = (
        features["patient_volume"]
        /
        features["staff_available"]
    )


    # Incident count

    incident_counts = (
        incidents
        .groupby("incident_type")
        .size()
        .reset_index(
            name="incident_count"
        )
    )


    total_incidents = len(
        incidents
    )


    features["incident_count"] = (
        total_incidents
    )


    # Inventory risk

    inventory["stock_days_remaining"] = (
        inventory["current_stock"]
        /
        inventory["daily_usage"]
    )


    features["average_stock_days"] = (
        inventory[
            "stock_days_remaining"
        ]
        .mean()
    )


    # Congestion target


    # Operational Risk Score

    wait_score = (
        features["avg_wait_time"]
        /
        features["avg_wait_time"].max()
    )


    capacity_score = (
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

        (capacity_score * 0.35)

        +

        (staff_score * 0.25)

    ) * 100


    features["congestion_flag"] = (

        features["risk_score"] >= 85

    ).astype(int)


    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    features.to_csv(
        OUTPUT_PATH,
        index=False
    )


    print(
        "Feature dataset created:"
    )

    print(
        features.head()
    )

if __name__ == "__main__":

    build_features()