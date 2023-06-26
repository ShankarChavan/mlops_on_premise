import pandas as pd
from sklearn.linear_model import LinearRegression
from typing import Dict

def select_feature(data: pd.DataFrame, params) -> pd.DataFrame:
    """Extracts the feature data from the model input

    Args:
        data: Data containing features and target.
        parameters: Parameters defined in parameters/data_science.yml.
    Returns:
        Split data.
    """
    X_test = data[params['features']]

    return X_test  # type: ignore

def generate_predictions(regressor:LinearRegression,X_test: pd.DataFrame)->pd.DataFrame:
    predictions=regressor.predict(X_test)
    X_test_copy=X_test.copy()
    X_test_copy['predictions']=predictions
    return X_test_copy
