import json
import sys
from pathlib import Path
from subprocess import Popen, PIPE
from pprint import pprint

def get_text_files_data(paths):
    stats=[]

    for path in paths:
        process = Popen(["python","file_stats.py", path], stdout=PIPE, text=True)
        stats.append(json.load(process.stdout))

    return stats

def overall_stats(multiple_stats):

    result = {
        "files read": 0,
        "total characters count": 0,
        "total words count": 0,
        "total verses count": 0,
        "most common char": ['',0],
        "most common word": ['',0]
    }

    for stats in multiple_stats:
        result["files read"] += 1
        for k,v in stats.items():
            match k:
                case "characters":
                    result["total characters count"] += v
                case "words":
                    result["total words count"] += v
                case "verses":
                    result["total verses count"] += v
                case "most common character":
                    if v[1] > result["most common char"][1]:
                        result["most common char"] = v
                case "most common word":
                    if v[1] > result["most common word"][1]:
                        result["most common word"] = v

    pprint(result)

if __name__ == "__main__":
    path = Path(sys.argv[1])

    if not path.is_dir():
        raise Exception(f"Error {path} is not a directory")



    text_files = list(path.glob("*.txt"))
    overall_stats(get_text_files_data(text_files))