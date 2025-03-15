from utils import file_to_string, print_text

def sentences_with_less_than_four_words():
    text = file_to_string()
    sentence = ''
    words_amount = 1
    for letter in text:
        if words_amount == 0:
            if letter != ' ' and letter != '-':
                words_amount += 1
                sentence += letter
        else:

            if letter == ' ':
                words_amount += 1
        
            sentence += letter

        if letter == '.' or letter == '!' or letter == '?' or letter == '':
            if (words_amount <= 4):
                print_text(sentence.strip())
            sentence = ''
            words_amount = 0

sentences_with_less_than_four_words()