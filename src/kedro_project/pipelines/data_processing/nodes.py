import pandas as pd

def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses the input data (train or test).

    Args:
        data: The raw input data.

    Returns:
        The preprocessed data with missing age values filled.
    """
    print(data["Age"].isnull().sum(), "missing values in Age column")
    data["Age"] = data["Age"].fillna(data["Age"].mean())
    return data

