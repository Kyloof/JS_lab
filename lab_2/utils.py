import sys


sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

def file_to_string():
    idx = 0
    result = ""
    preambule_acc = ""
    is_text = False
    prev_line_empty = False
    
    for line in sys.stdin:
        line = line.lstrip().rstrip()
        line = ' '.join(line.split())
        if line == '-----':
            return result.rstrip()
        elif is_text:
            result += line + '\n'
        else:
            idx += 1
            if line == '':
                preambule_acc += '\n'
                if prev_line_empty:
                    is_text = True
                else:
                    prev_line_empty = True
            else:
                prev_line_empty = False
                preambule_acc += line + '\n'
            if idx == 10:
                result += preambule_acc + '\n'
                is_text = True
    return result.rstrip()



def print_text(*args):
    for el in args:
        try:
            sys.stdout.write(str(el) + '\n')
        except TypeError:
            sys.stdout.write("Wrong value type given")

def check_sentence_end(symbol):
    return symbol == '.' or symbol == '' or symbol == '!' or symbol == '?'
