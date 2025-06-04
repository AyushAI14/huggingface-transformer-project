import os
from pathlib import Path
from tabnanny import verbose
import yaml
from src.logging import logger
from box.exceptions import BoxValueError
from typing import Any
from box import config_box
from ensure import ensure_annotations

def read_yaml_file(filepath:str)->config_box:
    """
    This function extract yaml files from a given path
    return config_box type result 
    """
    try :
        with open(filepath,'w') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.debug("Yaml file sucessfully loaded")
            return config_box(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def createDirs(filepath_dirs:list):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """

    for filepaths in filepath_dirs:
        os.makedirs(filepaths,exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {Path}")
