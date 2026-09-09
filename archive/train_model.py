import pandas as pd
import joblib

from pathlib import Path

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import classification_report


# Load upgraded feature dataset

df = pd.read_csv(
    "data/processed/analytics_features_v2.csv"
)


# Define features and target

X = df.drop(
    columns=[
        "congestion_flag",
        "department"
    ]
)


y = df["congestion_flag"]


# Split data

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.25,

    random_state=42,

    stratify=y

)


# Train model

model = RandomForestClassifier(

    random_state=42

)


model.fit(

    X_train,

    y_train

)


# Evaluate model

predictions = model.predict(

    X_test

)


print(
    classification_report(
        y_test,
        predictions
    )
)


# Save model

Path(
    "models"
).mkdir(
    exist_ok=True
)


joblib.dump(

    model,

    "models/congestion_prediction_model.pkl"

)


print(
    "Model saved successfully"
)