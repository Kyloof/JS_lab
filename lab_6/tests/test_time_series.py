import pytest
from TimeSeries import TimeSeries
from datetime import datetime


@pytest.fixture
def time_series():
    dates = [
        datetime(2025, 5, 20, 8),
        datetime(2025, 5, 21, 8),
        datetime(2025, 5, 22, 8),
        datetime(2025, 5, 23, 8),
    ]
    measurements = [2.3, 2.5, 2.4, None]
    return TimeSeries(
        measure_name="name",
        station_code="ST456",
        avg_time="24g",
        unit="PM10",
        dates=dates,
        measurements=measurements,
    )


@pytest.fixture
def time_series_full():
    dates = [
        datetime(2025, 5, 20, 8),
        datetime(2025, 5, 21, 8),
        datetime(2025, 5, 22, 8),
    ]
    measurements = [2.3, 2.5, 2.4]
    return TimeSeries(
        measure_name="name",
        station_code="ST456",
        avg_time="24g",
        unit="PM10",
        dates=dates,
        measurements=measurements,
    )


def test_time_series_index(time_series):
    assert time_series[0] == (datetime(2025, 5, 20, 8), 2.3)


def test_time_series_slice(time_series):
    assert time_series[0:2] == [
        (datetime(2025, 5, 20, 8), 2.3),
        (datetime(2025, 5, 21, 8), 2.5),
    ]


def test_time_series_existing_date_key(time_series):
    assert time_series[datetime(2025, 5, 20, 8)] == 2.3


def test_time_series_non_existing_date_key(time_series):
    assert time_series[datetime(2025, 5, 10, 8)] == ValueError


def test_time_series_mean(time_series):
    assert time_series.mean == 2.4


def test_time_series_stddev(time_series):
    assert time_series.stddev == 0.0816


def test_time_series_mean_full(time_series_full):
    assert time_series_full.mean == 2.4


def test_time_series_stddev_full(time_series_full):
    assert time_series_full.stddev == 0.0816
