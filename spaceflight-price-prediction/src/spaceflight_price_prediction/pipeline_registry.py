"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline

from spaceflight_price_prediction.pipelines import data_processing as dp
from spaceflight_price_prediction.pipelines import data_science as ds
from spaceflight_price_prediction.pipelines import inference_pipeline as infer


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.

    """
    data_processing_pipeline = dp.create_pipeline()
    data_science_pipeline = ds.create_pipeline()
    inference_pipeline=infer.create_pipeline()

    return {
        "dp": data_processing_pipeline,
        "ds": data_science_pipeline,
        "infer_pipe":inference_pipeline,
        "__default__": data_processing_pipeline + data_science_pipeline+inference_pipeline,
    }
