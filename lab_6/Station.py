from datetime import datetime


class Station:
    def __init__(self, code:str, international_code:str, name:str, old_code:str, start:datetime, end:datetime, station_type:str,
                 area_type:str, station_kind:str, voivodeship:str, city:str, address:str, latitude:float, longitude:float):
        self.code = code
        self.international_code = international_code
        self.name = name
        self.old_code = old_code
        self.start = start
        self.end = end
        self.station_type = station_type
        self.area_type = area_type
        self.station_kind = station_kind
        self.voivodeship = voivodeship
        self.city = city
        self.address = address
        self.latitude = latitude
        self.longitude = longitude

    def __eq__(self, other):
        return self.code == other.code

    def __str__(self):
        return (f"Station name: {self.name} \nStation code: {self.code} \nInternational station code: {self.international_code} \nOld station code: {self.old_code}\n"
                f"Opened in: {self.start} \nClosed in {self.end} \nStation type: {self.station_type} \nStation kind: {self.station_kind}\n"
                f"Surrounded area type: {self.area_type} \nVoivodeship: {self.voivodeship} \nCity: {self.city} \nAddres: {self.address}\n"
                f"Latitude: {self.latitude} Longitude: {self.longitude}")

    def __repr__(self):
        return f"{self.__class__.__name__}({vars(self)})"


if __name__ == "__main__":
    s = Station(
        code="001",
        international_code="PL001",
        name="Central Station",
        old_code="0001",
        start=datetime(2000, 1, 1),
        end=datetime(2100, 1, 1),
        station_type="Main",
        area_type="Urban",
        station_kind="Passenger",
        voivodeship="Mazowieckie",
        city="Warsaw",
        address="123 Main St",
        latitude=52.2297,
        longitude=21.0122
    )

    print(s)