import json
import os
from pathlib import Path
from typing import List


def list_to_json(list_to_output: List, question_name: str):
    json_list = json.dumps(list_to_output)
    cwd = Path(os.getcwd())
    json_file_to_save = cwd.joinpath(f'{question_name}.json')

    with open(json_file_to_save, "w") as my_open_file:
        my_open_file.write(json_list)
