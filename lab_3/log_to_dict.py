from pprint import pprint

from entry_to_dict import entry_to_dict
from read_log import *

def log_to_dict(log: list[tuple]):
    result = {}

    for entry in log:
        result[entry[1]] = entry_to_dict(entry)

    return result