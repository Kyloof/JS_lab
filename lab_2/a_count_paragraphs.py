import sys

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')


def count_paragraphs():
    is_text = False
    prev_line_empty = False
    preambule_acc = 0
    result = 0
    idx = 0

    for line in sys.stdin:
        line = line.lstrip().rstrip()
        if line == '-----':
            return result
        elif is_text:
            if line == '':
                result += 1
        else:
            idx += 1
            if line == '':
                if prev_line_empty:
                    is_text = True
                else:
                    prev_line_empty = True
                    preambule_acc += 1
            else:
                prev_line_empty = False
            if idx == 10:
                result += preambule_acc
                is_text = True
    return result

if __name__ == '__main__':
    print(count_paragraphs())