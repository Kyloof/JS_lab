from datetime import datetime, date
from typing import List
from statistics import stdev

class TimeSeries:
    def __init__(self, measure_name:str, station_code:str, avg_time:str, unit:str, dates: List[datetime] = [], measures: List[float | None] = []):
        if len(dates) != len(measures):
            raise ValueError("Number of dates and measures don't match!")

        self.measure_name = measure_name
        self.station_code = station_code
        self.avg_time = avg_time
        self.unit = unit
        self.dates = dates if dates is not None else []
        self.measures = measures if measures is not None else []

    def __getitem__(self, key: int | slice | date | datetime):
        if isinstance(key,int):
            return self.dates[key], self.measures[key]

        elif isinstance(key, slice):
            return list(zip(self.dates[key], self.measures[key]))

        elif isinstance(key, date):
            for idx, dt in enumerate(self.dates):
                if dt.date() == date:
                    return self.measures[idx]
            raise KeyError

        elif isinstance(key, datetime):
            try:
                return self.measures[self.dates.index(key)]
            except ValueError:
                raise KeyError
        raise KeyError

    @property
    def mean(self):
        if self.measures is not None and self.measures != []:
            return sum(self.measures)/len(self.measures)

        return None

    @property
    def stddev(self):
        if self.measures is not None and self.measures != []:
            return stdev(self.measures)

        return None
