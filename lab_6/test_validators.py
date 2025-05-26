import pytest
from datetime import datetime
from TimeSeries import TimeSeries
from SeriesValidator import OutlierDetector, ZeroSpikeDetector, ThresholdDetector
from SimpleReporter import SimpleReporter
from Measurements import Measurements


def test_outlier_detector_identifies_extreme_value():
    dates = [
        datetime(2025, 5, 20),
        datetime(2025, 5, 21),
        datetime(2025, 5, 22),
        datetime(2025, 5, 23),
        datetime(2025, 5, 24),
    ]

    measurements = [10.0, 10.5, 10.3, 100.0, 10.1]

    ts = TimeSeries(
        measure_name="Test",
        station_code="ST001",
        avg_time="Daily",
        unit="unit",
        dates=dates,
        measurements=measurements,
    )

    detector = OutlierDetector(k=1)
    result = detector.analyze(ts)

    print(result)

    assert len(result) == 1
    assert "100.0" in result[0]
    assert "2025-05-23" in result[0]


def test_zero_spike_detector_detects_streak_of_missing_values():
    dates = [
        datetime(2025, 5, 20),
        datetime(2025, 5, 21),
        datetime(2025, 5, 22),
        datetime(2025, 5, 23),
        datetime(2025, 5, 24),
        datetime(2025, 5, 25),
    ]

    measurements = [5.0, 0, None, 0, 6.0, 7.0]

    ts = TimeSeries(
        measure_name="Some Measure",
        station_code="ST999",
        avg_time="Daily",
        unit="unit",
        dates=dates,
        measurements=measurements,
    )

    detector = ZeroSpikeDetector()
    result = detector.analyze(ts)

    assert len(result) == 1
    assert "Missing Values streak of 3" in result[0]
    assert "2025-05-21" in result[0]
    assert "2025-05-23" in result[0]


def test_threshold_detector_detects_exceeding_values():
    dates = [
        datetime(2025, 5, 20),
        datetime(2025, 5, 21),
        datetime(2025, 5, 22),
        datetime(2025, 5, 23),
    ]

    measurements = [4.5, 7.0, 5.5, 8.5]

    ts = TimeSeries(
        measure_name="Water Level",
        station_code="ST888",
        avg_time="Daily",
        unit="m",
        dates=dates,
        measurements=measurements,
    )

    detector = ThresholdDetector(threshold=6.0)
    result = detector.analyze(ts)

    assert len(result) == 2
    assert "2025-05-21" in result[0]
    assert "1.0" in result[0]
    assert "2025-05-23" in result[1]
    assert "2.5" in result[1]


@pytest.fixture
def timeseries():
    dates = [
        datetime(2025, 5, 20),
        datetime(2025, 5, 21),
        datetime(2025, 5, 22),
        datetime(2025, 5, 23),
        datetime(2025, 5, 24),
    ]
    measurements = [10, 0, 0, None, 100]
    return TimeSeries(
        measure_name="Measure",
        station_code="ST1",
        avg_time="24g",
        unit="10PM",
        dates=dates,
        measurements=measurements,
    )


@pytest.fixture
def measurements(timeseries):
    measurements = Measurements("")
    measurements.csv_metadata = {
        True: {("ST1", "Measure"): [timeseries]},
        False: {},
    }
    return measurements


@pytest.mark.parametrize(
    "validators", [OutlierDetector(k=1), ZeroSpikeDetector(), SimpleReporter()]
)
def test_detect_all_anomalies_returns_messages_for_validators(measurements, validators):
    results = measurements.detect_all_anomalies(validators=[validators], preload=False)

    assert hasattr(results, "__iter__")
    assert len(results) > 0

    for ts, messages in results:
        assert hasattr(messages, "__iter__")
        messages_list = list(messages)
        assert all(hasattr(msg, "strip") for msg in messages_list)
        assert len(messages_list) > 0
        assert hasattr(ts, "dates")
        assert hasattr(ts, "measurements")
