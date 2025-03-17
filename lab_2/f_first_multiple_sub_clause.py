from utils import *

def find_first_multiple_sub_clause():
    text = file_to_string()

    current = ""
    comma_count = 0

    sentence_end = False

    for letter in text:
        if sentence_end:
            sentence_end = False
            continue

        if letter != '\n':
            current += letter

        if letter == ',':
            comma_count+=1

        if check_sentence_end(letter):
            if comma_count > 1:
                return current
            else:
                current = ""
                comma_count = 0
            sentence_end = True

    if comma_count > 1:
       return current

print_text( find_first_multiple_sub_clause() )