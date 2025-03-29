from os import environ,  listdir

def print_path():
    for dir_path in environ["Path"].split(";"):
        if (dir_path != ''):
            print(dir_path)

def print_path_with_exe():
    for dir_path in environ["Path"].split(";"):
        if (dir_path != ''):
            print(dir_path)
            files = listdir(dir_path)
            exe_files = []
            for file in files:
                if file.endswith(".exe"):
                    exe_files.append(file)
            print(exe_files, '\n')

print_path_with_exe()