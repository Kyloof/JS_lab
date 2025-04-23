import argparse
from datetime import datetime
import random
from pprint import pprint
from statistics import mean, stdev
from data_parser import parse
from pathlib import Path
import logging
import sys



def configure_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG) 
    stdout_handler.addFilter(lambda record: record.levelno < logging.ERROR)    #everything below error goes to stdout
    stdout_handler.setFormatter(formatter)

    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setLevel(logging.ERROR)
    stderr_handler.setFormatter(formatter)

    logger.addHandler(stdout_handler)
    logger.addHandler(stderr_handler)



def get_random_station(start_date: datetime, end_date: datetime, stations_dict: dict, measure_type: str):
    logger = logging.getLogger()

    def is_in_date_range(station_start, station_end):
        return station_start <= end_date and (station_end is None or station_end >= start_date)

    filtered_stations = []
    for station_key in stations_dict:
        station = stations_dict[station_key]

        try:
            station_start = datetime.strptime(station["Data uruchomienia"], "%Y-%m-%d")
        except Exception as e:
            logger.warning(f"Invalid start date for station {station_key}")
            continue        
        
        station_end = None
        if station.get("Data zamknięcia"):
            try:
                station_end = datetime.strptime(station["Data zamknięcia"], "%Y-%m-%d")
            except Exception as e:
                logger.warning(f"Invalid end date for station {station_key}")

        if is_in_date_range(station_start, station_end):
            if "Pomiary" in station.keys():
                for code in station["Pomiary"]:
                    if measure_type in code:
                        filtered_stations.append((station["Nazwa stacji"], station["Adres"]))
                        break

    if not filtered_stations:
        logger.warning(f"No stations found for measurement type '{measure_type}' in the given date range.")
    return random.choice(filtered_stations) if filtered_stations else None


def calculate_stats_for_station(station_name, start_date, end_date, measure_type, stations_dict):
    logger = logging.getLogger()
    filtered_values = []
    for station in stations_dict.values():
        if station["Nazwa stacji"] == station_name:
            measurements = station.get("Pomiary", {})
            for code in measurements:
                if measure_type in code:
                    found_measure = True
                    for date_val in measurements.values():
                        for date_str, val in date_val.items():
                            if date_str == "Jednostka":
                                continue
                        try:
                            if start_date <= datetime.strptime(date_str, "%m/%d/%y %H:%M") <= end_date:
                                filtered_values.append(val)
                        except ValueError:
                            continue
            if not found_measure:
                logger.warning(f"Station '{station_name}' does not support measurement type '{measure_type}'.")
            if not filtered_values:
                logger.warning(f"No available meausurements for station '{station_name}', measurement type '{measure_type}', and date range.")
                return None, None
            filtered_values = list(map(float,filtered_values))
    if len(filtered_values) > 1:
        return mean(filtered_values), stdev(filtered_values)         
    logger.warning(f"Station '{station_name}' not found.")
    return None, None



def main():
    configure_logging()
    logger = logging.getLogger()
    parser = argparse.ArgumentParser(
        prog='Air Quality CLI',
        description='Analyze air quality measurements from stations',
    )

    try:
        logger.info("Opening csv file and measurements folder...")
        stations_dict = parse(Path("lab_5/data/stacje1.csv"), Path("lab_5/data/measurements"))
        logger.info("Successfully opened data files.")
    except FileNotFoundError as e:
        logger.error(f"Critical error: {e}")
        return
    
    parser.add_argument('-o', '--object', help="Specify the object being tested (e.g., 'PM2.5', 'NO')")
    parser.add_argument("-f", '--frequency', help="Frequency of the measurements (e.g., 1g/24g)")
    parser.add_argument('-s', '--start', help="start of the measurements (yyyy-mm-dd)")
    parser.add_argument('-e', '--end', help="end of the measurements (yyyy-mm-dd)")
  

    subparsers = parser.add_subparsers(dest="command")

    station_parser = subparsers.add_parser("station", help="Get a random station active in the given time range")
    #station_parser.add_argument('-s', '--start', required=True, help="Start date (yyyy-mm-dd)")
    #station_parser.add_argument('-e', '--end', required=True, help="End date (yyyy-mm-dd)")
    #station_parser.add_argument('-o', '--object', help="Measurement type (e.g., PM2.5, NO)")

    measure_parser = subparsers.add_parser("measure", help="Calculate average and standard deviation of a measurement")
    #measure_parser.add_argument('-s', '--start', required=True, help="Start date (yyyy-mm-dd)")
    #measure_parser.add_argument('-e', '--end', required=True, help="End date (yyyy-mm-dd)")
    #measure_parser.add_argument('-o', '--object', required=True, help="Measurement type (e.g., PM2.5, NO)")
    measure_parser.add_argument('--station', required=True, help="Station name for which to perform the analysis")

    args = parser.parse_args()

    try:
        start_date = datetime.strptime(args.start, "%Y-%m-%d")
        end_date = datetime.strptime(args.end, "%Y-%m-%d")
    except ValueError:
        logger.error("Invalid date format. Use yyyy-mm-dd.")
        return

    if args.command == "station":
        station = get_random_station(start_date, end_date, stations_dict, args.object)
        if station:
            print(f"Random station: {station[0]}\n Address: {station[1]}")
        else:
            print("No station found active in the given date range.")

    elif args.command == "measure":
        avg, std = calculate_stats_for_station(args.station, start_date, end_date, args.object, stations_dict)
        if avg is not None:
            print(f"Average {args.object}: {avg:.2f}")
            print(f"Standard deviation: {std:.2f}")
        else:
            print("No data found for the given station, measurement type, or date range.")

    else:
        parser.print_help()
    
    logger.info("Program execution finished.")


if __name__ == "__main__":
    main()
    #v1 - ta zakomentowa
    #python lab_5/air_quality.py measure --start 2020-01-01 --end 2024-01-31 --object PM2.5 --station "Warszawa, ul. Wokalna"
    #python lab_5/air_quality.py station --start 2020-01-01 --end 2023-01-10 --object PM2.5

    #v2
    #python lab_5/air_quality.py --start 2020-01-01 --end 2023-01-01 --object PM2.5 station
    #python lab_5/air_quality.py --start 2020-01-01 --end 2025-01-01 --object PM2.5 measure --station "Warszawa, ul. Wokalna"
    #python lab_5/air_quality.py --start 2024-01-01 --end 2025-01-01 --object PM2.5 measure --station "Warszawa, ul. Wokalna" # wynik bedzie sie roznil bo zmiana daty