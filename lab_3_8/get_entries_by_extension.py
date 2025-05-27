from read_log import *

def format_extension(extension):
    if extension[0] != '.':
        return '.' + extension

    return extension

def get_entries_by_extension(log, extension):

    formated_ext = format_extension(extension)

    result = []

    for line in log:
        if line[-2][-len(formated_ext):] == formated_ext:
            result.append(line)
    return result

print(*get_entries_by_extension(read_log(),"pdf"),sep='\n')