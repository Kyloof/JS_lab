from datetime import datetime, date
from typing import List

class TimeSeries:
    def __init__(self, measure_name:str, station_code:str, avg_time:str, unit:str, dates: List[datetime] = [], measurements: List[float | None] = []):
        if len(dates) != len(measurements):
            raise ValueError("Number of dates and measurements don't match!")

        self.measure_name = measure_name
        self.station_code = station_code
        self.avg_time = avg_time
        self.unit = unit
        self.dates = dates if dates is not None else []
        self.measurements = measurements if measurements is not None else []

    def __getitem__(self, key: int | slice | date | datetime):
        if isinstance(key,int):
            return self.dates[key], self.measurements[key]

        elif isinstance(key, slice):
            return list(zip(self.dates[key], self.measurements[key]))

        elif isinstance(key, date):
            for idx, dt in enumerate(self.dates):
                if dt.date() == date:
                    return self.measurements[idx]
            raise KeyError

        elif isinstance(key, datetime):
            try:
                return self.measurements[self.dates.index(key)]
            except ValueError:
                raise KeyError
        raise KeyError

    @property
    def mean(self):
        if self.measurements is not None and self.measurements != []:
            # Can't use sum(self.measurements)/len(self.measurements) cuz of Nones :(
            sum_all = 0
            count = 0
            for measure in self.measurements:
                if measure is not None:
                    sum_all+=measure
                    count+=1

            if count>0:
                return round(sum_all/count,4)
            else:
                return None

        return None

    @property
    def stddev(self):
        if self.measurements is not None and self.measurements != []:
            mean = self.mean
            upper_sum = 0
            count = 0
            for measure in self.measurements:
                if measure is not None:
                    upper_sum += (measure-mean)**2
                    count+=1

            if count > 0:
                return round((upper_sum/count)**(1/2),4)
            else:
                return None

        return None
    
    def __str__(self):
        n = len(self.dates)
        return (
            f"TimeSeries for station '{self.station_code}' measuring '{self.measure_name}'\n"
            f"Average time: {self.avg_time}, Unit: {self.unit}\n"
            f"Total records: {n}\n"

        )