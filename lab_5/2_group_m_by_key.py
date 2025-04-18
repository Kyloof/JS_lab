from os import listdir
from pathlib import Path
from re import compile
from pprint import pprint

def group_measurement_files_by_key(path: Path):

    result = {}

    pattern = compile(r"^([0-9]+)_(.+)_([a-zA-Z0-9]+)\.([a-zA-Z0-9]+)$")

    if path.exists() and path.is_dir():
        files = listdir(path)

        for file in files:
            file_path = Path(f"{path}/{file}")
            tmp = pattern.match(file)

            if file_path.is_file() and tmp:
                result[(tmp.group(1),tmp.group(2),tmp.group(3))] = file_path

    return result


if __name__ == "__main__":
    pprint(group_measurement_files_by_key(Path("data/measurements")))