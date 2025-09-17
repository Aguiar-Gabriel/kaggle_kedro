from kedro.pipeline import Pipeline, node, pipeline

from .nodes import create_features


def create_pipeline(**kwargs) -> Pipeline:
    """Cria o pipeline de engenharia de features para os datasets de treino e teste."""
    nodes = []
    nodes.extend(
        [
            node(
                func=create_features,
                inputs=[f"preprocessed_train", "params:feature_engineering_params.linear_features"],
                outputs="feature_engineered_train_data",
                name="create_features_train_node",
            ),
            node(
                func=create_features,
                inputs=[f"preprocessed_test", "params:feature_engineering_params.linear_features"],
                outputs="feature_engineered_test_data",
                name="create_features_test_node",
            ),
        ]
    )
    return pipeline(nodes)
