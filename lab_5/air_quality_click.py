import click
from datetime import datetime
import random
from pprint import pprint
from statistics import mean, stdev
from data_parser import parse
from pathlib import Path
import logging
import sys


def logging_config():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.addFilter(lambda record: record.levelno < logging.ERROR)     #everything below error goes to stdout
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
        except Exception:
            logger.warning(f"Invalid start date for station {station_key}")
            continue

        station_end = None
        if station.get("Data zamknięcia"):
            try:
                station_end = datetime.strptime(station["Data zamknięcia"], "%Y-%m-%d")
            except Exception:
                logger.warning(f"Invalid end date for station {station_key}")

        if is_in_date_range(station_start, station_end):
            if "Pomiary" in station:
                for code in station["Pomiary"]:
                    if measure_type in code:
                        filtered_stations.append((station["Nazwa stacji"], station["Adres"]))
                        break

    if not filtered_stations:
        logger.warning(f"No stations found with measurement type '{measure_type}' in the given date range.")
    return random.choice(filtered_stations) if filtered_stations else None


def calculate_stats_for_station(station_name, start_date, end_date, measure_type, stations_dict):
    logger = logging.getLogger()
    filtered_values = []
    found_measure = False

    for station in stations_dict.values():
        if station["Nazwa stacji"] == station_name:
            measurements = station.get("Pomiary", {})
            for code in measurements:
                if measure_type in code:
                    found_measure = True
                    for date_str, val in measurements[code].items():
                        if date_str == "Jednostka":
                            continue
                        try:
                            if start_date <= datetime.strptime(date_str, "%m/%d/%y %H:%M") <= end_date:
                                filtered_values.append(float(val))
                        except ValueError:
                            continue

    if not found_measure:
        logger.warning(f"Station '{station_name}' doesn't support measurement type '{measure_type}'.")
    if not filtered_values:
        logger.warning(f"No available meausurements for station '{station_name}', meausurement type '{measure_type}', and date range.")
        return None, None

    return mean(filtered_values), stdev(filtered_values) if len(filtered_values) > 1 else (None, None)

#allow subcommands
@click.group()
@click.option('--start', required=True, help='Start date (yyyy-mm-dd)')
@click.option('--end', required=True, help='End date (yyyy-mm-dd)')
@click.option('--object', 'measure_type', required=True, help='Measurement type (e.g., PM2.5, NO)')
@click.pass_context #use this for storing data across the script in the ctx object (you can save data here and then use it elsewhere)
def cli(ctx, start, end, measure_type):
    logging_config()
    logger = logging.getLogger()
    try:
        #check if ctx obj is a dict
        ctx.ensure_object(dict)
        ctx.obj['start_date'] = datetime.strptime(start, "%Y-%m-%d")
        ctx.obj['end_date'] = datetime.strptime(end, "%Y-%m-%d")
        ctx.obj['measure_type'] = measure_type
    except ValueError:
        logger.error("Invalid date format. Use yyyy-mm-dd.")
        sys.exit(1)

    try:
        logger.info("Opening stacje.csv file and measurements folder...")
        ctx.obj['stations_dict'] = parse(Path("lab_5/data/stacje.csv"), Path("lab_5/data/measurements"))
        logger.info("Successfully opened data files.")
    except FileNotFoundError as e:
        logger.error(f"Critical error: {e}")
        sys.exit(1)


@cli.command()
@click.pass_context
def station(ctx):
    station = get_random_station(ctx.obj['start_date'], ctx.obj['end_date'], ctx.obj['stations_dict'], ctx.obj['measure_type'])
    if station:
        click.echo(f"Random station: {station[0]}\nAddress: {station[1]}")
    else:
        click.echo("No station found active in the given date range.")


@cli.command()
@click.option('--station', 'station_name', required=True, help='Station name to perform the analysis')
@click.pass_context
def measure(ctx, station_name):
    avg, std = calculate_stats_for_station(
        station_name,
        ctx.obj['start_date'],
        ctx.obj['end_date'],
        ctx.obj['measure_type'],
        ctx.obj['stations_dict']
    )
    if avg is not None:
        click.echo(f"Average {ctx.obj['measure_type']}: {avg:.2f}")
        click.echo(f"Standard deviation: {std:.2f}")
    else:
        click.echo("No data found for the given station, measurement type, or date range.")


if __name__ == "__main__":
    cli()


#python lab_5/air_quality_click.py --start 2020-01-01 --end 2023-01-01 --object PM2.5 station
#python lab_5/air_quality_click.py --start 2020-01-01 --end 2025-01-01 --object PM2.5 measure --station "Warszawa, ul. Wokalna"
