from datetime import datetime
from random import randint
from TimeSeries import TimeSeries
from SeriesValidator import OutlierDetector, ZeroSpikeDetector, ThresholdDetector


class SimpleReporter:
    def analyze(self, series):
        s = 0
        for measurement in series.measurements:
            if measurement:
                s += measurement
        mean = s / len(series.measurements)

        return [
            f"Info: {series.measure_name} at {series.station_code} has mean = {mean}"
        ]


if __name__ == "__main__":

    dates = [datetime(2025, 5, i + 1) for i in range(10)]
    measurements = [randint(10, 100) for i in range(10)]
    time_series = TimeSeries(
        measure_name="PM10",
        station_code="stacja1",
        avg_time="1g",
        unit="ng/m3",
        dates=dates,
        measurements=measurements,
    )

    simple_reporter = SimpleReporter()
    outlier_detector = OutlierDetector(k=0.0)
    zero_spike_detector = ZeroSpikeDetector()
    threshold_detector = ThresholdDetector(threshold=70.0)
    analysis_objects = [
        simple_reporter,
        outlier_detector,
        zero_spike_detector,
        threshold_detector,
    ]

    for obj in analysis_objects:
        print(f"Analysis results from {obj.__class__.__name__}:")
        results = obj.analyze(time_series)
        for result in results:
            print(result)
        print("\n---\n")
