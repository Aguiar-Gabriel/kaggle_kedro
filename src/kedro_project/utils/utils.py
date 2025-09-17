import pandas as pd

def concatenate_excel_sheets(excel_data: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """
    Concatenates multiple DataFrames from different Excel sheets into a single DataFrame.

    Args:
        excel_data: A dictionary where keys are sheet names and values are DataFrames.

    Returns:
        A single DataFrame containing all concatenated data.
    """
    return pd.concat(excel_data.values(), ignore_index=True)
