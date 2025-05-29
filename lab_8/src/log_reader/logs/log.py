from datetime import datetime

# timestamp - 0, uid - 1, hostip -2 , hostport -3, targetip-4, targetprt -5,
# metoda - 7, targetname-8, uri-9, statuscode-13/14


class Log:
    def __init__(
        self,
        host_address: str,
        target_address: str,
        timestamp: datetime,
        status_code: int,
        method: str,
    ):
        self._date = timestamp.date()
        self._time = timestamp.time()
        self._host_address = host_address
        self._target_address = target_address
        self._status_code = status_code
        self._method = method

    def __str__(self) -> str:
        return f"{self._host_address} \t {self._target_address} \t {self._date} \t {self._time} \t {self._status_code} \t {self._method}"

    @property
    def date(self):
        return self._date

    @property
    def time(self):
        return self._time

    @property
    def host_address(self):
        return self._host_address

    @property
    def target_address(self):
        return self._target_address

    @property
    def status_code(self):
        return self._status_code

    @property
    def method(self):
        return self._method

    def is_withing_bounds(self, lower_bound: date, upper_bound: date):
        return self._date >= lower_bound and self._date <= upper_bound
