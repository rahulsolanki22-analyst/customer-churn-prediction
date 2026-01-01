import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

def train_model(data_path, model_path):
    df = pd.read_csv(data_path)

    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    categorical_cols = X.select_dtypes(include="object").columns
    numerical_cols = X.select_dtypes(exclude="object").columns

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", "passthrough", numerical_cols),
            ("cat", OneHotEncoder(drop="first"), categorical_cols)
        ]
    )

    model = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("model", LogisticRegression(max_iter=1000))
    ])

    model.fit(X, y)

    joblib.dump(model, model_path)
    print(f"Model saved at: {model_path}")