from utils import *
import locale

def sorted_sentences():
    text = file_to_string()

    locale.setlocale(locale.LC_COLLATE, "pl_PL.UTF-8")

    is_sorted = True

    result = ""

    previous_word = ""
    current_word = ""
    current_sentence = ""

    for letter in text:
        if letter != '\n':
            current_sentence += letter
            if letter != ' ' and letter != ',' and letter != ';':
                current_word += letter

        if letter == '\n' or letter == ' ':
            if previous_word != "":
                if locale.strcoll(previous_word.lower(), current_word.lower()) > 0:
                    is_sorted = False

            previous_word = current_word
            current_word = ""

        if check_sentence_end(letter):
            if previous_word != "":
                if locale.strcoll(previous_word.lower(),current_word[:-1].lower()) > 0:
                    is_sorted = False

            if is_sorted:
               result += current_sentence
            is_sorted = True
            current_sentence = ""
            current_word = ""
            previous_word = ""

    if is_sorted:
        result += current_sentence

    return result


print_text(sorted_sentences())