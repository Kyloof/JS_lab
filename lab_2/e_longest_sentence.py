from utils import file_to_string, print_text, check_sentence_end

def longest_sequence():
    text = file_to_string()
    #text = "do da122. cha he."

    sentence = ''
    first_letter_1 = ''
    first_letter_2 = ''
    word_length = 0
    is_skipping = False

    max_word_length = -1
    result = ''

    
    for i in range(len(text)):
        letter = text[i]
        
        if word_length == 0:
            first_letter_1 = letter  
        elif word_length > 0 and is_skipping == False:
            if text[i - 1] == ' ':
                first_letter_2 = first_letter_1
                first_letter_1 = letter
                if first_letter_1 == first_letter_2:
                    is_skipping = True

        if letter != '':
            word_length += 1
            sentence += letter

        if check_sentence_end(letter):
            if not is_skipping:
                if word_length > max_word_length:
                    max_word_length = word_length
                    result = sentence

            sentence = ''
            first_letter_1 = ''
            first_letter_2 = ''
            word_length = 0
            is_skipping = False
            
    return result

if __name__ == '__main__':
    print_text(longest_sequence())