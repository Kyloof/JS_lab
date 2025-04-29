from abc import ABCMeta, abstractmethod
from typing import List
from TimeSeries import TimeSeries

class SeriesValidator(metaclass=ABCMeta):
    @abstractmethod
    def analyze(self, series: TimeSeries) -> List[str]:
        pass

class OutlierDetector(SeriesValidator):

    def __init__(self, k:float):
        self.k = k

    def analyze(self, series: TimeSeries) -> List[str]:
        mean = series.mean
        std = series.stddev

        if mean is None:
            raise ValueError("Invalid TimeSeries")

        result = []

        for idx, measurement in enumerate(series.measurements):
            if measurement > mean + self.k * std or measurement < mean - self.k * std:
                result.append(f"Outlier on {series.dates[idx]} with a value of {measurement}")

        return result

class ZeroSpikeDetector(SeriesValidator):

    def analyze(self, series: TimeSeries) -> List[str]:
        null_count = 0

        result = []

        for idx, measurement in enumerate(series.measurements):
            if measurement is None or measurement == 0:
                null_count+=1
            else:
                if null_count >= 3:
                    result.append(f"Missing Values streak of {null_count} {series.avg_time} from {series.dates[idx-null_count]} to {series.dates[idx-1]}")
                null_count = 0

        last_idx = len(series.dates)-1

        if null_count > 3:
            result.append(f"Missing value streak of {null_count} {series.avg_time} from {series.dates[last_idx-null_count]} to {series.dates[last_idx]}")

        return result

class ThresholdDetector(SeriesValidator):

    def __init__(self, threshold:float):
        self.threshold = threshold

    def analyze(self, series: TimeSeries) -> List[str]:
        result = []

        for idx, measurement in enumerate(series.measurements):
            if measurement is not None and  measurement>self.threshold:
                result.append(f"Threshold exceeded on {series.dates[idx]} by { measurement - self.threshold}")

        return result