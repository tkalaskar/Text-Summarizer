import os
from box.exceptions import BoxValueError
import yaml
from src.Text_Summarizer.logger import logger
try:
    from ensure import ensure_annotations
except Exception:
    def ensure_annotations(func):
        return func
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(file_path: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox object.

    Args:
        file_path (Path): The path to the YAML file.
    Raises:
        ValueError: If the file does not have a .yaml or .yml extension.

    Returns:
        ConfigBox: The contents of the YAML file as a ConfigBox object.
    """
    try:
        with open(file_path, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {file_path} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("The provided file is not a valid YAML file.")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates directories specified in the list.

    Args:
        path_to_directories (list): A list of directory paths to be created.
        verbose (bool): If True, logs the creation of each directory.

    Returns:
        None
    """
    if isinstance(path_to_directories, (str, Path)):
        path_to_directories = [path_to_directories]

    for path in path_to_directories:
        path = Path(path)
        path.mkdir(parents=True, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")