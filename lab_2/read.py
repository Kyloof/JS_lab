import sys

idx = 0
preambule_acc = ""
is_text = False
prev_line_empty = False

for line in sys.stdin:
    line = line.lstrip().rstrip()
    line = ' '.join(line.split())
    if line == '-----':
        break
    elif (is_text):
        sys.stdout.write(line + '\n')
    else:
        idx += 1
        if line == '':
            if prev_line_empty:
                is_text = True
            else:
                prev_line_empty = True
        else:
            prev_line_empty = False
            preambule_acc += line + '\n'
        if idx == 10:
            sys.stdout.write(preambule_acc + '\n')
            is_text = True


'''ewentualnie zeby bez splita
    for i in range(len(line)):
        if line[i] == ' ' and i > 0 and line[i - 1] != ' ':
            print(' ')
        else:
            print(line[i])
    '''

'''#preambuła
starting_index = 0

for i in range(10):
    if data[i] == '' and data[i + 1] == '':
        starting_index = i + 2
        break

#tresc ksazki
for line in data[starting_index:]:
    if line == '':
        print()
    elif line == '-----':
        break
    else:
        #unikniecie >1 spacji miedzy wyrazami
        print(' '.join(line.split()).strip())

#wyraz = 'wyraz  z    trzema spacjami'
#print(' '.join(wyraz.split()))


'''