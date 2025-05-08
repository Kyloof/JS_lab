from abc import ABCMeta, abstractmethod
from typing import List
from TimeSeries import TimeSeries

class SeriesValidator(metaclass=ABCMeta):
    @abstractmethod
    def analyze(self, series: TimeSeries) -> List[str]:
        pass

    #for the composite validator
    @abstractmethod
    def _get_validated(self, series: TimeSeries)->list[int]:
        pass

class OutlierDetector(SeriesValidator):

    def __init__(self, k:float):
        self.k = k

    def analyze(self, series: TimeSeries) -> List[str]:

        validated = self._get_validated(series)

        result = []

        for idx, val in enumerate(validated):
            if val == 1:
                result.append(f"Outlier on {series.dates[idx]} with a value of {series.measurements[idx]}")

        return result

    def _get_validated(self, series: TimeSeries) -> list[int]:
        result = [0]*len(series.measurements)

        mean = series.mean
        std = series.stddev

        if mean is None:
            raise ValueError("Invalid TimeSeries")

        for idx,measurement in enumerate(series.measurements):
            if measurement is not None and (measurement > mean + self.k * std or measurement < mean - self.k*std):
                result[idx] = 1

        return result

class ZeroSpikeDetector(SeriesValidator):

    def analyze(self, series: TimeSeries) -> List[str]:

        validated = self._get_validated(series)

        result = []

        series_detected = False
        start_idx = 0
        end_idx = 0

        for idx, val in enumerate(validated):
            if val == 1:
                if series_detected:
                    end_idx+=1
                else:
                    series_detected = True
                    start_idx = idx
                    end_idx = start_idx
            else:
                if series_detected:
                    result.append(f"Missing Values streak of {end_idx-start_idx+1} {series.avg_time} from {series.dates[start_idx]} to {series.dates[end_idx]}")

                series_detected = False

        if series_detected:
            result.append(f"Missing Values streak of {end_idx-start_idx+1} {series.avg_time} from {series.dates[start_idx]} to {series.dates[end_idx]}")

        return result

    def _get_validated(self, series: TimeSeries) -> list[int]:
        result = [0]*len(series.measurements)

        null_count = 0

        for idx, measurement in enumerate(series.measurements):
            if measurement in [0, None]:
                null_count+=1
            else:
                if null_count >= 3:
                    result[idx-null_count:idx] = [1]* null_count
                null_count = 0

        if null_count >= 3:
            result[-null_count:] = [1] * null_count

        return result

class ThresholdDetector(SeriesValidator):

    def __init__(self, threshold:float):
        self.threshold = threshold

    def analyze(self, series: TimeSeries) -> List[str]:

        validated = self._get_validated(series)

        result = []

        for idx, val in enumerate(validated):
            if val == 1:
                result.append(f"Threshold exceeded on {series.dates[idx]} by { series.measurements[idx] - self.threshold}")

        return result

    def _get_validated(self, series: TimeSeries) -> list[int]:
        result = [0] * len(series.measurements)

        for idx, measurement in enumerate(series.measurements):
            if measurement is not None and measurement>self.threshold:
                result[idx] = 1

        return result

class CompositeValidator(SeriesValidator):

    def __init__(self,validators: list[SeriesValidator] ,mode: str):
        if mode.upper() not in ['OR', 'AND']:
            raise ValueError("Invalid mode (OR, AND)")

        self.mode = mode.upper()
        self.validators = validators

    def analyze(self, series: TimeSeries) -> List[str]:
        summary = self._get_validated(series)

        result = []

        if self.mode == 'OR':
            for idx, summ in enumerate(summary):
                if summ > 0:
                   result.append(f'Anomaly found on {series.dates[idx]} with a value of {series.measurements[idx]}')
        else:
            for idx, summ in enumerate(summary):
                if summ == len(self.validators):
                    result.append(f'Anomaly found on {series.dates[idx]} with a value of {series.measurements[idx]}')

        return result

    def _get_validated(self, series: TimeSeries) -> list[int]:

        result = [0]*len(series.measurements)

        for validator in self.validators:
            tmp = validator._get_validated(series)

            result = [sum(x) for x in zip(result, tmp)]

        return result