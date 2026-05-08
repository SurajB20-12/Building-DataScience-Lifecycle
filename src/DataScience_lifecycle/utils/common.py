import os
from src.DataScience_lifecycle import logger
import yaml
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_ymal: Path) -> ConfigBox:
    """
    the function do 3 things:
    does 3 things:
        1.Reads a YAML file
        2.Converts data into an easy-to-access object (ConfigBox)
        3.Handles errors safely

    ConfigBox is a class from the box library that allows you to access dictionary keys as attributes.
    ensure_annotations is a decorator from the ensure library that checks the types of function arguments and return values at runtime.
    BoxValueError is an exception from the box library that is raised when you try to access
    """
    try:
        with open(path_to_ymal) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_ymal} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise BoxValueError(f"yaml file: {path_to_ymal} is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    it create a list of directories and also log the process of creating directories
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    it saves a dictionary as a json file and also log the process of saving json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    it loads a json file and returns it as a ConfigBox object and also log the process of loading json file
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    it saves any data as a binary file using joblib and also log the process of saving binary file
    """
    joblib.dump(data, path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    it loads a binary file using joblib and also log the process of loading binary file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data
