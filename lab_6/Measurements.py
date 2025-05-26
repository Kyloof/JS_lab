import os
from pprint import pprint
from pathlib import Path
from typing import Tuple, List, Dict, Iterator
from SeriesValidator import SeriesValidator
from TimeSeries import TimeSeries
from utils import load_timeseries, mark_as_loaded
from SeriesValidator import (
    OutlierDetector,
    ZeroSpikeDetector,
    ThresholdDetector,
)
import csv


class Measurements:

    def __init__(self, path: str) -> None:
        # False - not loaded yet, True - loaded
        self.csv_metadata: Dict[bool, Dict[ Tuple[str, ...] , Path | List[TimeSeries]]] = {False: {}, True: {}}
        self.path = Path(path)
        """
        - load paths into a dictionary
        - if someone wants to use them, they can just give appropriate data, eg. '2023', 'O3', '1g', 
        and then if such data is stored it will be read from the csv that is stored in a dictionary.
        - lazy load ✅💥💥💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯
        """
        for csv_path in self.path.glob("*.csv"):
            keys: Tuple[str, ...] = tuple(os.path.split(csv_path)[1].replace(".csv", "").split("_"))
            if len(keys) == 3:
                self.csv_metadata[False][keys] = csv_path

    def __len__(self) -> int:
        count: int = 0
        for keys, path in self.csv_metadata[False].items():

            if not isinstance(path, (str, Path)):
                raise TypeError(f"Invalid path type: {type(path)}")

            with open(path, "r", newline="") as f:
                reader: Iterator[List[str]] = csv.reader(f)
                first_row: list[str] | None = next(reader, None)
                if first_row:
                    count += len(first_row) - 1
        for keys, values in self.csv_metadata[True].items():
            if not isinstance(values, list):
                raise TypeError(f'Invalid values type: {type(values)}')

            count += len(values)
        return count

    def __contains__(self, parameter_name: str) -> bool:
        for keys in self.csv_metadata[False].keys():
            if parameter_name == keys[2]:
                return True

        for keys in self.csv_metadata[True].keys():
            if parameter_name == keys[2]:
                return True

        return False

    def get_by_parameter(self, param_name: str) -> List[TimeSeries]:
        results: List[TimeSeries] = []

        for keys, values in self.csv_metadata[True].items():
            if param_name == keys[1]:
                if not isinstance(values, list):
                    raise ValueError(f'Invalid values type: {type(values)}')
                results += values

        for keys, path in list(self.csv_metadata[False].items()):
            if param_name == keys[1]:
                results += load_timeseries(self.csv_metadata, keys, path)

        return results

    def get_by_station(self, station_code: str) -> List[TimeSeries]:
        results: List[TimeSeries] = []

        for keys, values in self.csv_metadata[True].items():
            if not isinstance(values, list):
                raise ValueError(f'Invalid values type: {type(values)}')

            for time_serie in values:
                if time_serie.station_code == station_code:
                    results.append(time_serie)

        for keys, path in list(self.csv_metadata[False].items()):
            timeseries: List[TimeSeries] = load_timeseries(self.csv_metadata, keys, path)
            for time_serie in timeseries:
                if time_serie.station_code == station_code:
                    results.append(time_serie)

        return results

    def detect_all_anomalies(
        self, validators: list[SeriesValidator], preload: bool = False
    ) -> list[tuple[TimeSeries, list[str]]]:
        if preload:
            for keys, path in list(self.csv_metadata[False].items()):
                load_timeseries(self.csv_metadata, keys, path)

        results: List[Tuple[TimeSeries, List[str]]] = []
        for keys, values in self.csv_metadata[True].items():
            if not isinstance(values, list):
                raise ValueError(f'Invalid values type: {type(values)}')

            for time_serie in values:
                for validator in validators:
                    anomalies: List[str] = validator.analyze(time_serie)
                    if anomalies != []:
                        results.append((time_serie, anomalies))

        return results

    def validate(self) -> Dict[TimeSeries, List[List[str]]]:
        results: Dict[TimeSeries, List[List[str]]] = {}
        validators: List[SeriesValidator] = [
            OutlierDetector(5.00),
            ZeroSpikeDetector(),
            ThresholdDetector(threshold=70.0),
        ]

        for keys, values in self.csv_metadata[True].items():
            if not isinstance(values, list):
                raise ValueError(f'Invalid values type: {type(values)}')

            for time_serie in values:
                result: List[List[str]] = []
                for validator in validators:
                    validation: List[str] = validator.analyze(time_serie)
                    if validation:
                        result.append(validation)
                results[time_serie] = result

        return results


if __name__ == "__main__":
    m1: Measurements = Measurements("lab_6/data/measurements/")
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
    list1: List[TimeSeries] = m1.get_by_station("DsOsieczow21")
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
