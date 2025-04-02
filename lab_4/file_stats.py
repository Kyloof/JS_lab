import json
import sys
from collections import Counter

def file_stats(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = file.read()

        char_count = len(data)
        words_count = len(data.split())
        poem_count = data.count('\n')
        char_counter = Counter(data)
        words_counter = Counter(data.split())

    return {
        "path": file_path,
        "characters": char_count,
        "words": words_count,
        "verses": poem_count+1,
        "most common character": char_counter.most_common()[0],
        "most common word": words_counter.most_common()[0]
    }

if __name__ == "__main__":
    json.dump(file_stats(sys.argv[1]), sys.stdout)