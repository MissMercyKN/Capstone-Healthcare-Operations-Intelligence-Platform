from pathlib import Path
import pandas as pd
import numpy as np


def generate_capacity():

    output = Path(
        "data/raw/synthetic"
    )

    output.mkdir(
        parents=True,
        exist_ok=True
    )

    departments = [
        "Emergency",
        "ICU",
        "Radiology",
        "Surgery",
        "Outpatient"
    ]


    capacity = pd.DataFrame({

        "department": departments,

        "total_beds": [
            50,
            30,
            20,
            40,
            60
        ],

       "occupied_beds": [
            45,
            24,
            10,
            22,
            35
        ]

    })


    capacity["occupancy_rate"] = (
        capacity["occupied_beds"]
        /
        capacity["total_beds"]
    ) * 100


    capacity.to_csv(
        output / "capacity.csv",
        index=False
    )



def generate_staffing():

    output = Path(
        "data/raw/synthetic"
    )


    staffing = pd.DataFrame({

        "department": [
            "Emergency",
            "ICU",
            "Radiology",
            "Surgery",
            "Outpatient"
        ],

        "doctors": [
            4,
            5,
            6,
            8,
            10
        ],

        "nurses": [
            10,
            15,
            12,
            20,
            25
        ]

    })


    staffing["total_staff"] = (
        staffing["doctors"]
        +
        staffing["nurses"]
    )


    staffing.to_csv(
        output / "staffing.csv",
        index=False
    )



def generate_inventory():

    output = Path(
        "data/raw/synthetic"
    )


    inventory = pd.DataFrame({

        "item_name": [
            "Surgical Gloves",
            "Masks",
            "Syringes",
            "IV Fluids"
        ],

        "current_stock": [
            3000,
            5000,
            2500,
            1800
        ],

        "daily_usage": [
            400,
            600,
            300,
            250
        ]

    })


    inventory["stock_days_remaining"] = (
        inventory["current_stock"]
        /
        inventory["daily_usage"]
    )


    inventory.to_csv(
        output / "inventory.csv",
        index=False
    )



def generate_incidents():

    output = Path(
        "data/raw/synthetic"
    )


    incidents = pd.DataFrame({

        "incident_type": [
            "Overcrowding",
            "Staff Shortage",
            "Supply Delay"
        ],

        "severity": [
            "High",
            "Medium",
            "High"
        ]

    })


    incidents.to_csv(
        output / "incidents.csv",
        index=False
    )



if __name__ == "__main__":

    generate_capacity()

    generate_staffing()

    generate_inventory()

    generate_incidents()

    print(
        "Operational datasets generated"
    )