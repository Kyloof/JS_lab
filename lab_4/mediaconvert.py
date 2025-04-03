from subprocess import run
from os import path, getenv, makedirs
import datetime
import filetype
import csv

#python3 -m pip install filetype



def mediaconvert(path_name, convert_format):
    file_name, file_ext = path.splitext(path.basename(path_name))
    directory = getenv("CONVERTED_DIR","lab_4/converted/") #check for the left PATH variable, if it doesnt exist save to right arg
    makedirs(directory, exist_ok=True) #if folder doesnt exist, create it
    ts = datetime.datetime.now().strftime("%Y%m%d")
    output = directory+ts+'-'+file_name+'.'+convert_format
    if filetype.is_image(path_name):
        try:
            program = "magick"
            run(["magick", path_name, output])
        except RuntimeError:
            print("Failed to convert the image")
    else:
        try:
            program = "ffmpeg"
            run(["ffmpeg", "-i", path_name, output])
        except RuntimeError:
            print("Failed to convert the video")
    
    with open ("lab_4/history.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ts", "path_name", "convert_format", "output", "program"])  
        writer.writerow([ts + str(datetime.datetime.now().hour), path_name, convert_format, output, program])


    
 


mediaconvert("/Users/janku/Desktop/JS/JS_lab/lab_4/image.png", "heic")

#export CONVERTED_DIR="sciezka"