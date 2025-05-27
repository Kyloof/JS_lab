import sys
from datetime import datetime


def read_log():
    log = []

    for line in sys.stdin:
        line = line.split("\t")
        elements = line[:6] + line[7:10] + line[14:15]

        ts = datetime.fromtimestamp(float(elements[0]))
        orig_port = int(elements[3])
        resp_port = int(elements[5])

        log_entry = (
            ts,
            elements[1],
            elements[2],
            orig_port,
            elements[4],
            resp_port,
            elements[6],
            elements[7],
            elements[8],
            elements[9],
        )
        log.append(log_entry)

    return log


def read_log_from_file(filepath):
    log = []
    with open(filepath, "r", encoding="UTF-8") as f:
        for line in f:
            line = line.split("\t")
            elements = line[:6] + line[7:10] + line[14:15]

            ts = datetime.fromtimestamp(float(elements[0]))
            orig_port = int(elements[3])
            resp_port = int(elements[5])

            log_entry = (
                ts,
                elements[1],
                elements[2],
                orig_port,
                elements[4],
                resp_port,
                elements[6],
                elements[7],
                elements[8],
                elements[9],
            )
            log.append(log_entry)

    return log
