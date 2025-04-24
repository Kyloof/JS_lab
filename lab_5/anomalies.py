from re import compile, match
from data_parser import *
import argparse as ap

def find_anomalies(data: dict, alarm_threshold, delta_threshold, none_threshold):

    code_pattern = compile(r"^([A-Za-z]+)-([A-Za-z0-9()]+)-(\d+g)$")

    for station, data in data.items():

        print(f'\nStacja: {station}', sep=', ')

        pomiary = data.get('Pomiary') or {}

        for code, measurements in pomiary.items():
            m = match(code_pattern, code)

            if m:
                _, param, _ = m.groups()
                print(f'\tParametr: {param}')

            invalid_counter = 0
            prev_measure = None

            for date, val in measurements.items():
                if date == 'Jednostka':
                    continue

                #Rapid jumps in measurements
                if prev_measure is not None and val != '' and abs(prev_measure - float(val)) > delta_threshold:
                    print(f"\t\t{date} : Nagły skok wartości = {abs(prev_measure - float(val))}")

                #Invalid measurements counter
                if val == '' or float(val)<0:
                    invalid_counter+=1

                #Over the alarm threshold
                if val != '' and float(val) > alarm_threshold:
                    print(f"\t\t{date}: Wartość powyżej progu alarmowego = {val}")

                prev_measure = float(val) if val!='' else None

            invalid_ratio = invalid_counter/(len(measurements)-1)

            if invalid_ratio > none_threshold:
                print(f"\t\tBardzo duża ilość niepoprawnych danych: {invalid_ratio}")

if __name__ == "__main__":

    parser = ap.ArgumentParser()
    parser.add_argument('--delta', '-d', type=int ,default=200)
    parser.add_argument('--nones', '-n', type=float, default=0.2)
    parser.add_argument('--alarm', '-a', type=int, default=600)

    args = parser.parse_args()

    info = parse(Path("data/stacje.csv"),Path("data/measurements"))

    find_anomalies(info, args.alarm, args.delta, args.nones)