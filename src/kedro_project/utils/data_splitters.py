import pandas as pd
import numpy as np

def create_titanic_excel_with_sheets(output_filepath: str):
    """
    Simulates the Titanic dataset split into 5 parts and saves them into
    different sheets of an Excel file.
    """
    # Create a dummy Titanic-like dataset
    np.random.seed(42)
    num_rows = 1000
    data = {
        'PassengerId': np.arange(1, num_rows + 1),
        'Survived': np.random.randint(0, 2, num_rows),
        'Pclass': np.random.randint(1, 4, num_rows),
        'Name': [f'Name_{i}' for i in range(num_rows)],
        'Sex': np.random.choice(['male', 'female'], num_rows),
        'Age': np.random.randint(1, 80, num_rows),
        'SibSp': np.random.randint(0, 5, num_rows),
        'Parch': np.random.randint(0, 5, num_rows),
        'Ticket': [f'TICKET_{i}' for i in range(num_rows)],
        'Fare': np.random.uniform(10, 500, num_rows),
        'Cabin': [f'C{i}' if np.random.rand() > 0.5 else np.nan for i in range(num_rows)],
        'Embarked': np.random.choice(['S', 'C', 'Q'], num_rows),
    }
    df = pd.DataFrame(data)

    # Split the DataFrame into 5 parts
    df_parts = np.array_split(df, 5)

    with pd.ExcelWriter(output_filepath, engine='openpyxl') as writer:
        for i, part_df in enumerate(df_parts):
            sheet_name = f'titanic_part_{i+1}'
            part_df.to_excel(writer, sheet_name=sheet_name, index=False)

    print(f"Simulated Titanic dataset saved to {output_filepath} with 5 sheets.")

if __name__ == '__main__':
    # Example usage:
    create_titanic_excel_with_sheets('C:/Dev/curso_kedro/project_kedro/kedro-project/data/01_raw/titanic_parts.xlsx')
