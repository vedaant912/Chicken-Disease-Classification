import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64
import joblib

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read YAML file and return ConfigBox.
    Args:
        path_to_yaml (Path): Path to the YAML file.
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    Returns:
        ConfigBox: ConfigBox type
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Successfully loaded YAML file: {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"Invalid YAML file: {path_to_yaml}")
    except Exception as e:
        raise e
@ensure_annotations 
def create_directories(path_to_directories: list, verbose=True):
    """Creates list of directory
    Args:
        path_to_directory (list): List of directories to create.
        ignore_log (bool,optional): ignore if multiple directories is to be created. Defaults to False.
    
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save dictionary data into JSON file.
    Args:
        path (Path): Path to the JSON file.
        data (dict): Dictionary to save.
    """

    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
        logger.info(f"Saved JSON data to: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load JSON file and return ConfigBox.
    Args:
        path (Path): Path to the JSON file.
    Returns:
        ConfigBox: ConfigBox type
    """

    with open(path) as f:
        content = json.load(f)
    
    logger.info(f"Successfully loaded JSON file: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save binary data into a file.
    Args:
        data (Any): Binary data to save.
        path (Path): Path to the file.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary File save to: {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get size in KB
    Args: 
        path (Path): Path to the file.

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"{size_in_kb} KB"

def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as image_file:
        return base64.b64encode(image_file.read())