from utils import file_to_string, print_text

def count_characters():
    text = file_to_string()

    count = 0

    whitespace_characters = " \n\t\r\v\f"

    for character in text:
        if character not in whitespace_characters:
            count+=1

    return count

print_text(count_characters())