import csv, datetime
from os import path, getenv, makedirs
from dotenv import load_dotenv

load_dotenv()

def save_log(input_path, output_path, format, program):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H")
    log_file = f"{getenv("CONVERTED_DIR","converted/")}history.csv"

    with open(log_file, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, input_path, format, output_path, program])

def get_filename(input_path):
    file_name, _ = path.splitext(path.basename(input_path))
    return file_name

def create_output_path(directory, file_name, convert_format):
    ts = datetime.datetime.now().strftime("%Y%m%d")
    return directory+ts+'-'+file_name+'.'+convert_format

def get_path_env(path, default):
    directory = getenv(path, default) #check for the left PATH variable, if it doesnt exist save to right arg
    makedirs(directory, exist_ok=True) #if folder doesnt exist, create it
    return directory