from re import compile, match
import csv
from pprint import pprint

FILE_PATH = 'lab_5/data/stacje.csv'

def get_dates():
    date_pattern = compile(r'[0-9]{4}-[0-9]{2}-[0-9]{2}')
    result = []

    with open(FILE_PATH, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            start_date = row['Data uruchomienia']
            end_date = row['Data zamknięcia']
            start_date_match = date_pattern.match(start_date)
            end_date_match = date_pattern.match(end_date)

            if start_date_match:
                result.append(start_date)
            if end_date_match:
                result.append(end_date)

    return result

def get_position():
    pos_pattern = compile(r'[0-9]{2}\.[0-9]{6}')
    result = []

    with open(FILE_PATH, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            height = row['WGS84 φ N']
            width = row['WGS84 λ E']
            height_match = pos_pattern.match(height)
            width_match = pos_pattern.match(width)

            if height_match:
                result.append(height)
            if width_match:
                result.append(width)
    return result


def get_stations():
    pos_pattern = compile(r'[A-Za-z]+-[A-Za-z]+')
    result = []

    with open(FILE_PATH, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['Nazwa stacji']
            name_match = pos_pattern.match(name)

            if name_match:
                result.append(name)
    return result


def change_names():
    letters_dict = {
        'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n',
        'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z',
        'Ą': 'A', 'Ć': 'C', 'Ę': 'E', 'Ł': 'L', 'Ń': 'N',
        'Ó': 'O', 'Ś': 'S', 'Ź': 'Z', 'Ż': 'Z', ' ': '_'
    }
    pattern = compile('|'.join(k for k in letters_dict.keys()))
    result = []

    def fix_letters(name):
        def replace_letter(match):
            return letters_dict[match.group()]
        return pattern.sub(replace_letter, name)
    
    with open(FILE_PATH, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['Nazwa stacji']
            result.append(fix_letters(name))
    return result




def verify_stations():
    pattern = compile(r'.*MOB$')
    with open(FILE_PATH, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['Nazwa stacji']
            station_type = row['Typ stacji']
            if pattern.match(name) and station_type != 'mobilna':
                return False
        return True
    

def get_streets():
    pattern = compile(r'.*\b(ul\.|al\.).*')
    #                  coś,koniec slowa, ul. lub al., i cos dalej
    result = []
    with open(FILE_PATH, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['Nazwa stacji']
            if pattern.match(name):
                result.append(name)
    return result


pprint(get_dates())
pprint(get_position())
pprint(get_stations())
pprint(change_names())
print(verify_stations())
pprint(get_stations())
pprint(get_streets())
        
