def calculate_average_wait(df):

    return round(
        df["waiting_time"].mean(),
        2
    )


def calculate_risk_percentage(df):

    risk = (
        df["congestion_flag"]
        .mean()
        *100
    )

    return round(risk,2)