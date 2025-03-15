import sys
from utils import file_to_string, print_text

def sentences_in_fourth_quartile():
    text = file_to_string()
    
    sentence = ''
    max_length = -1
    min_length = sys.maxsize
    sentences_amount = 0
    sentence_length = 0

    for letter in text:
        sentence += letter
        if letter == '.' or letter == '!' or letter == '?' or letter == '': 
            sentence_length = len(sentence.strip())  

            max_length = max(max_length, sentence_length)
            min_length = min(min_length, sentence_length)

            sentence = ''
            sentences_amount += 1

    fourth_quartile_start = sentences_amount * 3 // 4

  
    sentence = ''
    for letter in text:
        if letter == '\n':
            sentence += ' '
        else:
            sentence += letter
        if letter == '.' or letter == '!' or letter == '?' or letter == '': 
            sentence_length = len(sentence.strip())
            if sentence_length >= max_length * 0.75:  
                print_text(sentence.strip(), '\n')
            sentence = ''

sentences_in_fourth_quartile()