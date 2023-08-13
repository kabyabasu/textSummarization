import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format ='[%(asctime)s] %(message)s:')

project_name = "textSumarization"

list_files = [

    ".github/workflows/.gitkeep",
    f"src/(project_name)/__init__.py",
    f"src/(project_name)/components/__init__.py",
    f"src/(project_name)/utils/__init__.py",
    f"src/(project_name)/utils/common.py",
    f"src/(project_name)/logging/__init__.py",
    f"src/(project_name)/config/__init__.py",
    f"src/(project_name)/config/configration.py",
    f"src/(project_name)/piplexec/__init__.py",
    f"src/(project_name)/entitys/__init__.py",
    f"src/(project_name)/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "reserach/traials.ipynb"

]

for filepath in list_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Created directory {filedir} for file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getatime(filepath) == 0):
        logging.info(f"Creating file {filepath}")
        with open(filepath, "w") as f:
            pass

    else:
        logging.info(f"File {filename} already exists")

