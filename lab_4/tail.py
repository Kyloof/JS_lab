import os
import time
from collections import deque
import argparse as ap
import sys

def tail():
    parser = ap.ArgumentParser()

    parser.add_argument('file', type=str, nargs='?')
    parser.add_argument('--lines','-l',  type=int, default=10)
    parser.add_argument('--follow', '-f', action='store_true')

    args = parser.parse_args()

    if args.file is None:
        if not sys.stdin.isatty():
            from_stdin(args.lines)
    elif args.follow:
        last_pos = from_file(args.file, args.lines)
        follow(last_pos,args.file,args.lines)
    else:
        from_file(args.file, args.lines)

def from_file(filename, lines):
    stack = deque(maxlen=lines)

    with open(filename, "r", encoding="utf-8") as file:
        file.seek(0)

        for line in file:
            stack.append(line)
        last_pos = file.tell()

    stdout_stack(stack)

    return last_pos

def from_stdin(lines):
    stack = deque(maxlen=lines)

    for line in sys.stdin:
        stack.append(line)

    stdout_stack(stack)

def follow(pos, filename, n):
    with open(filename, "r", encoding="utf-8") as file:
        file.seek(pos)

        while True:
            current_pos = file.tell()
            line = file.readline()

            if not line:
                time.sleep(0.5)
                size = os.stat(filename).st_size


                if current_pos > size:
                    print(f"\nfile {filename} has been shortened")
                    file.seek(0)
            else:
                sys.stdout.write(line)
                sys.stdout.flush()

def stdout_stack(stack):
    while stack:
        sys.stdout.write(stack.popleft())
        sys.stdout.flush()

if __name__ == "__main__":
    tail()