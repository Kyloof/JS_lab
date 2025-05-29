from Station import Station
import datetime


def test_eq_stations():
    station1 = Station(
        "code",
        "1",
        "1",
        "1",
        datetime.datetime.now(),
        datetime.datetime.now(),
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        0.5,
        0.5,
    )
    station2 = Station(
        "code",
        "1",
        "1",
        "1",
        datetime.datetime.now(),
        datetime.datetime.now(),
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        0.5,
        0.5,
    )
    station3 = Station(
        "another_code",
        "1",
        "1",
        "1",
        datetime.datetime.now(),
        datetime.datetime.now(),
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        0.5,
        0.5,
    )
    assert station1 == station2
    assert station2 != station3
