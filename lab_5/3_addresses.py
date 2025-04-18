from pathlib import Path
from re import compile, match
import csv
from pprint import pprint

ADDRESS_PATTERN = compile(r'(?:[a-z]*\.\s*)?([\.*\w\s()]+?)(?:\s+(\d+\w*(?:/\d+)?))?$')

def get_addresses(path: Path, city: str):
    result = []

    with open(path, newline='', encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['Miejscowość'].strip().lower() == city.strip().lower():
                voivo = row['Województwo']
                address = row['Adres'].strip()

                addr_match = match(ADDRESS_PATTERN, address)

                street = ''
                number = ''

                if addr_match:
                    street = addr_match.group(1)
                    number = addr_match.group(2) if addr_match.group(2) else ''

                result.append(
                    (
                        voivo,
                        city,
                        street,
                        number
                    )
                )

        return result

if __name__ == "__main__":
    pprint(
        get_addresses(Path('data/stacje.csv'), 'Nowa Sól')
    )
