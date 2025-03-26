from read_log import read_log

def get_failed_reads(log: list[tuple], combined=False):

    start_4 = []
    start_5 = []

    for line in log:
        if line[-1][0] == '4':
            start_4.append(line)
        elif line[-1][0] == '5':
            start_5.append(line)

    if combined:
        return start_4 + start_5

    return start_4, start_5

print(get_failed_reads(read_log()))