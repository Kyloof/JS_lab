from log_reader.logs.log import Log
from datetime import date


def get_logs_by_date(log_list: list[Log], lower_bound: date, upper_bound: date):
    log_list_by_date: list[Log] = []

    for log in log_list:
        if log.is_within_bounds(lower_bound, upper_bound):
            log_list_by_date.append(log)

    return log_list_by_date
