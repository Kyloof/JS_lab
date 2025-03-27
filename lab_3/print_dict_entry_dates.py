from pprint import pprint

from read_log import read_log
from log_to_dict import log_to_dict
from collections import Counter

def print_dict_entry_dates(log: dict):
    """for k,v in log.items():
        ip = v["id.orig_h"]
        if ip not in result:
            result[ip] = {
                'sessions': 1,
                'first_request': v["ts"],
                'last_request': v["ts"],
                'method_count': Counter({v["method"]:1}),
                '2xx_count': 1 if v["status_code"][0] == '2' else 0
            }
        else:
            result[ip]['sessions'] += 1
            result[ip]['last_request'] = v["ts"]
            result[ip]['method_count'][v["method"]] += 1
            result[ip]['2xx_count'] += 1 if v["status_code"][0] == '2' else 0

    return result
    """

    hosts_info = {}

    method_counter = Counter()
    start_2_count = 0

    requests_count = 0
    for k,v in log.items():
        ip = v["id.orig_h"]
        if ip not in hosts_info:
            hosts_info[ip] = {
                'requests': 1,
                'first_request': v["ts"],
                'last_request': v["ts"],
            }
        else:
            hosts_info[ip]['requests'] += 1
            hosts_info[ip]['last_request'] = v["ts"]

        requests_count += 1
        method_counter[v["method"]] += 1

        start_2_count += 1 if v["status_code"][0] == '2' else 0


    pprint(hosts_info)

    for k,v in method_counter.items():
        print(f"{k}: {round(v*100/requests_count,3)} %")

    print(f"2xx ratio: {round(start_2_count*100/requests_count,3)} %")

print_dict_entry_dates(log_to_dict(read_log()))