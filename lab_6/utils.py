from datetime import datetime
from TimeSeries import TimeSeries
import csv


def load_timeseries(csv_dict, keys, csv_path):
    with open(csv_path, mode="r", encoding="utf-8") as file:
        reader = list(csv.reader(file))

    station_codes = reader[1][1:]
    measure_names = reader[2][1:]
    avg_times = reader[3][1:]
    units = reader[4][1:]

    measurements = list(zip(*reader[6:]))
    timestamps = list(measurements[0])

    for i, timestamp in enumerate(timestamps):
        try:
            timestamps[i] = datetime.strptime(timestamp, "%d/%m/%y %H:%M")
        except ValueError:
            pass

    result = []
    measurements = measurements[1:]

    # some measurements are empty, in order to not crash out on them it needs to be done
    def safe_float(value):
        try:
            return float(value)
        except ValueError:
            return 0.0

    for i in range(len(station_codes)):
        result.append(
            TimeSeries(
                measure_names[i],
                station_codes[i],
                avg_times[i],
                units[i],
                timestamps,
                list(map(safe_float, measurements[i])),
            )
        )
    mark_as_loaded(csv_dict, keys, result)
    return result


def mark_as_loaded(csv_dict, keys, value):
    del csv_dict[False][keys]
    csv_dict[True][keys] = value
