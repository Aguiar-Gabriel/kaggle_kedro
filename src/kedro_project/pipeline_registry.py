"""Project pipelines."""
from __future__ import annotations

from kedro.pipeline import Pipeline
from kedro_project.pipelines import data_processing, feature_engineering


def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    data_processing_pipeline = data_processing.create_pipeline()
    feature_engineering_pipeline = feature_engineering.create_pipeline()

    return {
        "__default__": data_processing_pipeline + feature_engineering_pipeline,
        "dp": data_processing_pipeline,
        "fe": feature_engineering_pipeline,
    }