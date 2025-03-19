from utils import file_to_string, print_text, check_sentence_end

def first_twenty_sentences():
    text = file_to_string()
    sentence = ''
    sentences_amount = 0
    result = ''

    for letter in text:
        if sentences_amount == 20:
            return result
       
        if letter == '\n':
            sentence += ' '
        else:
            sentence += letter

        if check_sentence_end(letter):
            sentences_amount += 1
            result += sentence.strip() + '\n'
            sentence = ''

    return result

if __name__ == '__main__':
    print(first_twenty_sentences())