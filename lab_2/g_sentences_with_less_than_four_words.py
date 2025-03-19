from utils import file_to_string, print_text, check_sentence_end

def sentences_with_less_than_four_words():
    text = file_to_string()
    sentence = ''
    words_amount = 1
    result = ''

    for letter in text:
        if words_amount == 0:
            if letter != ' ' and letter != '-':
                words_amount += 1
                sentence += letter
        else:

            if letter == ' ':
                words_amount += 1
        
            sentence += letter

        if check_sentence_end(letter):
            if (words_amount <= 4):
                result += sentence.strip() + '\n'
                print_text(sentence.strip())
            sentence = ''
            words_amount = 0
    
    return result


if __name__ == '__main__':
    sentences_with_less_than_four_words()