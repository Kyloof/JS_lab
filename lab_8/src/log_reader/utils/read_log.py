import datetime
from logs.log import Log


def read_log_from_file(filepath: str):
    log: list[Log] = []
    with open(filepath, "r", encoding="UTF-8") as f:
        for line in f:
            line = line.split("\t")
            elements = line[:15]
            ts = datetime.fromtimestamp(float(elements[0]))

            log_entry = Log(
                host_address=elements[2],
                target_address=elements[4],
                timestamp=ts,
                status_code=elements[14],
                method=elements[7])

            log.append(log_entry)

    return log
