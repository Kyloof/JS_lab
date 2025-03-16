from utils import print_text, file_to_string

def longest_sentence():
    text = file_to_string()

    current = ""
    longest = ""

    for letter in text:
        if letter != '.' and letter != '!' and letter != '?' and letter != '':
            # \n doesn't end a sentence but is not a part of one
            if letter != '\n':
                current += letter
        else:
            if  len(current) > len(longest):
                longest = current
            current = ""
    #check the last string sequence
    if len(current) > len(longest):
        longest = current

    return longest

print_text( longest_sentence() )
