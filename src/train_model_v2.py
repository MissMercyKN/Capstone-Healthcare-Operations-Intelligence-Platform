import pandas as pd
import joblib

from pathlib import Path

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    accuracy_score
)


DATA_PATH = (
    "data/processed/analytics_features_v3.csv"
)


MODEL_PATH = (
    "models/congestion_prediction_model.pkl"
)



# Load dataset

df = pd.read_csv(DATA_PATH)


# Remove non-feature columns

X = df.drop(
    columns=[
        "congestion_flag",
        "current_congestion_flag",
        "risk_score",
        "department",
        "date"
    ],
    errors="ignore"
)

y = df["congestion_flag"]


# Train/test split

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.2,

    random_state=42,

    stratify=y

)



# Baseline model

log_model = LogisticRegression(
    max_iter=1000
)


log_model.fit(
    X_train,
    y_train
)


log_predictions = log_model.predict(
    X_test
)


print(
    "Logistic Regression Results"
)

print(
    classification_report(
        y_test,
        log_predictions
    )
)



# Final model

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


rf_model.fit(
    X_train,
    y_train
)


rf_predictions = rf_model.predict(
    X_test
)



print(
    "Random Forest Results"
)


print(
    classification_report(
        y_test,
        rf_predictions
    )
)



# Confusion matrix

print(
    "Confusion Matrix:"
)

print(
    confusion_matrix(
        y_test,
        rf_predictions
    )
)



# Feature importance

importance = pd.DataFrame({

    "feature": X.columns,

    "importance":
    rf_model.feature_importances_

})


print(
    importance.sort_values(
        "importance",
        ascending=False
    )
)



# Save final model

Path(
    "models"
).mkdir(
    exist_ok=True
)


joblib.dump(
    rf_model,
    MODEL_PATH
)


print(
    "Model saved successfully"
)