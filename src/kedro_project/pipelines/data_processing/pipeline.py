from kedro.pipeline import Pipeline, node, pipeline

from .nodes import preprocess_data
from kedro_project.utils.utils import concatenate_excel_sheets

def create_pipeline(**kwargs) -> Pipeline:
    nodes = []
    nodes.extend(
        [
            node(
                func=preprocess_data,
                inputs="train",
                outputs="preprocessed_train",
                name="preprocess_train_data_node",
            ),
            node(
                func=preprocess_data,
                inputs="test",
                outputs="preprocessed_test",
                name="preprocess_test_data_node",
            ),            
            # node(
            #     func=concatenate_excel_sheets,
            #     inputs="titanic_full",
            #     outputs="concatenated_titanic_data",
            #     name="concatenate_titanic_sheets_node",
            # ),
        ]
    )
    return pipeline(nodes)