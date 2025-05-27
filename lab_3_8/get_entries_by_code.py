from read_log import read_log

def get_entries_by_code(log: tuple, code: int):

    if not 100 <= code < 600:
        return []

    result = []

    for line in log:
        if line[-1] == str(code):
            result.append(line)

    return result

print(get_entries_by_code(read_log(), 99))
