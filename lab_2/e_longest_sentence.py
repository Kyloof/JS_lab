from utils import file_to_string, print_text

def longest_sequence():
    text = file_to_string()
    #text = "do da122. cha he."
    sentence = ''
    first_letter_1 = ''
    first_letter_2 = ''
    max_length = -1
    length = 0
    result = ''
    is_skipping = False
    for i in range(len(text)):
        letter = text[i]
        if length == 0:
            first_letter_1 = letter
        elif length > 0 and is_skipping == False:
            if text[i - 1] == ' ':
                first_letter_2 = first_letter_1
                first_letter_1 = letter
                if first_letter_1 == first_letter_2:
                    is_skipping = True
        if letter != '':
            length += 1
            sentence += letter

        if letter == '.' or letter == '!' or letter == '?' or letter == '':
            if not is_skipping:
                if length > max_length:
                    max_length = length
                    result = sentence
            sentence = ''
            first_letter_1 = ''
            first_letter_2 = ''
            length = 0
            is_skipping = False
    return result

if __name__ == '__main__':
    print_text(longest_sequence())