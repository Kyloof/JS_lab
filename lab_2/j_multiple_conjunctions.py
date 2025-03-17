from utils import *

def sentences_with_multiple_conjunctions():

    text = file_to_string()

    result = ""

    current_sentence = ""
    current_word = ""

    conjunctions_count = 0

    for letter in text:
        if letter != '\n':
            current_sentence += letter
            if letter != ' ' and letter != ',':
                current_word += letter

        if letter == '\n' or letter == ' ':
            conjunctions_count += check_word(current_word)
            current_word = ""

        if check_sentence_end(letter):
            conjunctions_count += check_word(current_word[-1])
            if conjunctions_count > 1:
                result += current_sentence + ' '

            current_word = ""
            current_sentence = ""
            conjunctions_count = 0

    if conjunctions_count > 1:
        result += current_sentence

    return result

def check_word(word):

    if word == "i" or word == "oraz" or word == "ale" or word == "że" or word == "lub":
        return 1
    return 0

print_text( sentences_with_multiple_conjunctions() )