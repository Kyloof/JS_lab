from subprocess import run
import filetype
from utils import save_log, get_filename, create_output_path, get_path_env

def mediaconvert(input_path, convert_format):

    file_name = get_filename(input_path)
    directory = get_path_env("CONVERTED_DIR", "lab_4/converted/")
    output = create_output_path(directory, file_name, convert_format)
    
    if filetype.is_image(input_path):
        try:
            program = "magick"
            run(["magick", input_path, output])
        except RuntimeError:
            print("Failed to convert the image")
    else:
        try:
            program = "ffmpeg"
            run(["ffmpeg", "-i", input_path, output])
        except RuntimeError:
            print("Failed to convert the video")
    
    save_log(input_path, output, convert_format, program)

    
 
#export CONVERTED_DIR="sciezka"

if __name__ == "__main__":
    mediaconvert("lab_4/image.png", "heic")
    #mediaconvert("lab_4/video1.mp4", "avi")