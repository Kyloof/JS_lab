from datetime import datetime
from log_reader.logs.log import Log


def read_log_from_file(filepath: str) -> list[Log]:
    log_entries: list[Log] = []
    
    with open(filepath, "r", encoding="UTF-8") as f:
        for line in f:
            elements = line.strip().split("\t")
            try:
                ts = datetime.fromtimestamp(float(elements[0]))

                log_entry = Log(
                    host_address=elements[2],
                    target_address=elements[4],
                    timestamp=ts,
                    status_code=elements[14],
                    method=elements[7]
                )

                log_entries.append(log_entry)
            except (ValueError, IndexError) as e:
                continue

    return log_entries
