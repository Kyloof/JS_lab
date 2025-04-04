from os import environ, listdir, path, pathsep, access, X_OK
import argparse as ap

def print_path():
    for dir_path in environ["PATH"].split(";"):
        if dir_path != '':
            print(dir_path)

def print_path_with_exe():
    for dir_path in environ["PATH"].split(pathsep):
        if path.exists(dir_path) and path.isdir(dir_path):
            print(dir_path) #directory
            files = listdir(dir_path)
            exe_files = []
            for file in files:
                full_path = path.join(dir_path, file)
                if access(full_path, X_OK):
                    exe_files.append(file)
            print(exe_files, '\n')


if __name__ == "__main__":
    parser = ap.ArgumentParser()
    parser.add_argument('--executable', '-e', action='store_true')

    args = parser.parse_args()

    if args.executable:
        print_path_with_exe()
    else:
        print_path()
