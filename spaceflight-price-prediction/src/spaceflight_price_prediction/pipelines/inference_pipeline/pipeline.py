from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline
from .nodes import select_feature,generate_predictions


def create_pipeline(**kwargs) -> Pipeline:

    pipeline_instance= pipeline(
        [
            node(
                func=select_feature,
                inputs=["model_input_table", "parameters"],
                outputs="inference_feature_table",
                name="selected_test_features",
            ),
            node(
                func=generate_predictions,
                inputs=["regressor","inference_feature_table"],
                outputs="predictions",
                name="prediction_node",

            ),
        ])
    return pipeline_instance
