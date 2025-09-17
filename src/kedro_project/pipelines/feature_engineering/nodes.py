import pandas as pd
from typing import List, Dict, Any

def create_features(data: pd.DataFrame, params: List[Dict[str, Any]]) -> pd.DataFrame:

    for feature_def in params:
        input_col = feature_def["input_col"]
        output_col = feature_def["output_col"]
        operation = feature_def["operation"] # 'add' or 'subtract'

        # Determine the value to add or subtract
        if "value" in feature_def:
            value = feature_def["value"]
        elif "from_col" in feature_def:
            value = data[feature_def["from_col"]]

        # Apply the operation
        if operation == "add":
            data[output_col] = data[input_col] + value
        elif operation == "subtract":
            data[output_col] = data[input_col] - value

    return data