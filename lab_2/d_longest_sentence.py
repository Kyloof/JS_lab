from utils import file_to_string, check_sentence_end, print_text

def longest_sentence():
    text = file_to_string()

    current = ""
    longest = ""

    #prevents counting the space after the '.'
    sentence_end = False

    for letter in text:
        if sentence_end:
            sentence_end = False
            continue

        if letter != '\n':
            current += letter

        if check_sentence_end(letter):
            if  len(current) > len(longest):
                longest = current
            current = ""
            sentence_end = True

    #check the last string sequence
    if len(current) > len(longest):
        longest = current

    return longest

if __name__ == '__main__':
    print_text( longest_sentence() )
