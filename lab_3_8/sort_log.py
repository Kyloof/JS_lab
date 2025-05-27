from read_log import *

def sort_log(log, index):
    #don't know how else to handle it
    try:
        return sorted(log, key= lambda x: x[index])
    except IndexError:
        return None

print(sort_log(read_log()[:5],2))
