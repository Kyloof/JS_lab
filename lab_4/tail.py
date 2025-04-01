from collections import deque
import argparse as ap
import sys

def tail():
    parser = ap.ArgumentParser()

    parser.add_argument('file', type=str, nargs='?')
    parser.add_argument('--lines','-l',  type=int, default=10)
    #parser.add_argument('--follow', action='store_true')

    args = parser.parse_args()

    if args.file is None:
        if not sys.stdin.isatty():
            from_stdin(args.lines)
    else:
        from_file(args.file, args.lines)

def from_file(filename, lines):
    stack = deque(maxlen=lines)

    with open(filename, "r") as file:
        file.seek(0)

        for line in file:
            stack.append(line)

    stdout_stack(stack)

def from_stdin(lines):
    stack = deque(maxlen=lines)

    for line in sys.stdin:
        stack.append(line)

    stdout_stack(stack)

def stdout_stack(stack):
    while stack:
        sys.stdout.write(stack.popleft())
        sys.stdout.flush()

if __name__ == "__main__":
    tail()