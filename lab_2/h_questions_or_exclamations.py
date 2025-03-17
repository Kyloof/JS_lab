from utils import *

def questions_or_exclamations():
    text = file_to_string()

    current = ""
    result = ""

    sentence_end = False

    for letter in text:
        if sentence_end:
            sentence_end = False
            continue

        if letter != '\n':
            current+=letter

        if letter == '.':
            current = ""
            sentence_end = True

        if letter == '?' or letter == '!':
            result+= current + " "
            current = ""
            sentence_end = True

    print_text(result)
    return result

if __name__ == '__main__':
    questions_or_exclamations()