import csv
from os import listdir
from pathlib import Path
from pprint import pprint
import io
import logging


def parse(metadata: Path, measurements:Path):
    logger = logging.getLogger()

    result = parse_meta(metadata)

    files = listdir(measurements)

    files_blacklist = ['2023_Depozycja_1m.csv']
    keys_blacklist = ['Nr', 'Wskaźnik', 'Czas uśredniania', 'Kod stanowiska','Kod stacji']

    for file in files:
        if file in files_blacklist:
            continue

        reader = transposed_reader(f"{measurements}/{file}")

        for row in reader:
            #logger.debug(f"Read {len(str(row).encode('utf-8'))} bytes from line: {str(row).strip()}")
            station_code = row['Kod stacji']
            stanowisko_code = row['Kod stanowiska']

            # Ensure that 'Pomiary' dicts exist
            result[station_code].setdefault('Pomiary', {})

            result[station_code]['Pomiary'][stanowisko_code] = {
                k: v for k, v in row.items() if k not in keys_blacklist
            }

    return result

def parse_meta(metadata:Path):
    result = {}

    with open(metadata, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        skip_keys = ['Nr', 'Kod stacji']

        for row in reader:
            result[row['Kod stacji']] = {k: v for k, v in row.items() if k not in skip_keys}

    return result

def transposed_reader(input_path):
    with open(input_path, newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        rows = list(reader)

    transposed = zip(*rows)
    transposed_rows = list(transposed)

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerows(transposed_rows)
    output.seek(0)

    dict_reader = csv.DictReader(output)

    return dict_reader

if __name__ == "__main__":
    pprint(
        parse(Path("lab_5/data/stacje.csv"),Path("lab_5/data/measurements"))['DsGlogWiStwo']
    )
