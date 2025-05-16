import os
from pprint import pp, pprint
from pathlib import Path
from SeriesValidator import SeriesValidator
from utils import load_timeseries, mark_as_loaded
from SeriesValidator import (
    OutlierDetector,
    ZeroSpikeDetector,
    ThresholdDetector,
)
import csv


class Measurements:

    def __init__(self, path):
        # False - not loaded yet, True - loaded
        self.csv_metadata = {False: {}, True: {}}
        self.path = Path(path)
        """
        - load paths into a dictionary
        - if someone wants to use them, they can just give appriopariate data, eg. '2023', 'O3', '1g', 
        and then if such data is stored it will be read from the csv that is stored in a dictionary.
        - lazy load ✅💥💥💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯
        """
        for csv_path in self.path.glob("*.csv"):
            keys = tuple(os.path.split(csv_path)[1].replace(".csv", "").split("_"))
            if len(keys) == 3:
                self.csv_metadata[False][keys] = csv_path

    def __len__(self):
        count = 0
        for keys, path in self.csv_metadata[False].items():
            with open(path, "r", newline="") as f:
                reader = csv.reader(f)
                first_row = next(reader, None)
                if first_row:
                    count += len(first_row) - 1
        for keys, values in self.csv_metadata[True].items():
            count += len(values)
        return count

    def __contains__(self, parameter_name: str):
        for keys in self.csv_metadata[False].keys():
            if parameter_name == keys[2]:
                return True

        for keys in self.csv_metadata[True].keys():
            if parameter_name == keys[2]:
                return True

        return False

    def get_by_parameter(self, param_name: str):
        results = []

        for keys, values in self.csv_metadata[True].items():
            if param_name == keys[1]:
                results += values

        for keys, path in list(self.csv_metadata[False].items()):
            if param_name == keys[1]:
                results += load_timeseries(self.csv_metadata, keys, path)

        return results

    def get_by_station(self, station_code: str):
        results = []

        for keys, values in self.csv_metadata[True].items():
            for time_serie in values:
                if time_serie.station_code == station_code:
                    results.append(time_serie)

        for keys, path in list(self.csv_metadata[False].items()):
            timeseries = load_timeseries(self.csv_metadata, keys, path)
            for time_serie in timeseries:
                if time_serie.station_code == station_code:
                    results.append(time_serie)

        return results

    def detect_all_anomalies(
        self, validators: list[SeriesValidator], preload: bool = False
    ):
        if preload:
            for keys, path in list(self.csv_metadata[False].items()):
                load_timeseries(self.csv_metadata, keys, path)

        results = []
        for keys, values in self.csv_metadata[True].items():
            for time_serie in values:
                for validator in validators:
                    anomalies = validator.analyze(time_serie)
                    if anomalies != []:
                        results.append((time_serie, anomalies))

        return results

    def validate(self):
        results = {}
        validators = [
            OutlierDetector(5.00),
            ZeroSpikeDetector(),
            ThresholdDetector(threshold=70.0),
        ]

        for keys, values in self.csv_metadata[True].items():
            for time_serie in values:
                result = []
                for validator in validators:
                    validation = validator.analyze(time_serie)
                    if validation:
                        result.append(validation)
                results[time_serie] = result

        return results


if __name__ == "__main__":
    m1 = Measurements("lab_6/data/measurements/")
    print(len(m1))
    print("24g" in m1)
    print("2g" in m1)

    pprint(m1.get_by_parameter("PM10"))

    pprint(
        m1.detect_all_anomalies(
            [
                OutlierDetector(5),
                ZeroSpikeDetector(),
                ThresholdDetector(threshold=70.0),
            ],
            True,
        )
    )
    list1 = m1.get_by_station("DsOsieczow21")
    for el in list1:
        print(el)

    pprint(m1.validate())

    """

    pprint(
        m1.detect_all_anomalies(
            [OutlierDetector(5), ZeroSpikeDetector(), ThresholdDetector(threshold=70.0)]
        )
    )
    

"""
