from utils import file_to_string, print_text

def first_twenty_sentences():
    text = file_to_string()
    sentence = ''
    sentences_amount = 0
    for letter in text:
        if sentences_amount == 20:
            return
       
        if letter == '\n':
            sentence += ' '
        else:
            sentence += letter
        if letter == '.' or letter == '!' or letter == '?' or letter == '':
            sentences_amount += 1
            print_text(sentence.strip(), sentences_amount)
            sentence = ''
            
if __name__ == '__main__':
    first_twenty_sentences()