"""
    Load Data Module.
"""

from typing import Text
import argparse
import yaml
from sklearn.datasets import load_iris


def data_load(config_path: Text) -> None:
    """Create new features.
    Args:
        config_path {Text}: path to config
    """

    with open(config_path, 'r', encoding='utf-8') as configuration_path:
        config = yaml.safe_load(configuration_path)

    data = load_iris(as_frame=True)
    dataset = data.frame

    dataset.columns = [colname.strip(' (cm)').replace(' ', '_')
                       for colname in dataset.columns.tolist()]
    dataset.to_csv(config["data"]["raw_data_path"], index=False)
    print("Data Load Complete.")


if __name__ == "__main__":

    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("--config", dest='config', required=True)
    args = args_parser.parse_args()

    data_load(args.config)
