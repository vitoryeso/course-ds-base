"""
    Data Features Module.
"""

from typing import Text
import argparse
import yaml
import pandas as pd


def data_load(config_path: Text) -> None:
    """
        This function download the data and save it in a specified path.
    """

    with open(config_path, 'r', encoding='utf-8') as configuration_path:
        config = yaml.safe_load(configuration_path)

    dataset = pd.read_csv(config["data"]["raw_data_path"])

    dataset['sepal_length_to_sepal_width'] = dataset['sepal_length'] / dataset['sepal_width']
    dataset['petal_length_to_petal_width'] = dataset['petal_length'] / dataset['petal_width']

    dataset = dataset[[
        'sepal_length', 'sepal_width', 'petal_length', 'petal_width',
        'sepal_length_to_sepal_width', 'petal_length_to_petal_width',
        'target'
    ]]
    dataset.to_csv(config["data"]["features_data_path"], index=False)

    print("Data Features Extracted.")


if __name__ == "__main__":

    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("--config", dest='config', required=True)
    args = args_parser.parse_args()

    data_load(args.config)
