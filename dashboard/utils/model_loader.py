import joblib
import pandas as pd


import joblib


MODEL_PATH = (
    "models/congestion_prediction_model.pkl"
)


def load_model():

    return joblib.load(
        MODEL_PATH
    )


def get_feature_importance(model, features):

    importance = pd.DataFrame({

        "Feature":
        features,

        "Importance":
        model.feature_importances_

    })


    return importance.sort_values(
        "Importance",
        ascending=False
    )