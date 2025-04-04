import sys
from os import environ

def is_in_args(envar: str):
    if len(sys.argv) == 1:
        return True

    for argv in sys.argv[1:]:
        if argv in envar:
            return True

    return False

if __name__ == "__main__":
    for env in environ:
        if is_in_args(env):
            print(f"{env} = {environ[env]}")