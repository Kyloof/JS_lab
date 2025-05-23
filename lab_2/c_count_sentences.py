from utils import file_to_string, print_text, check_sentence_end

def count_sentences():
    text = file_to_string()
    #text = "Raz rzekłem sobie. Co Ci mowie."

    sentences_amount = 0
    sentences_with_capital = 0
    length = 0

    is_first_alpha = True
    is_skipping = False

    for letter in text:
        if not is_skipping and not is_first_alpha and letter.isupper():
            sentences_with_capital += 1
            is_skipping = True
        if letter.isalpha():
            is_first_alpha = False

        if check_sentence_end(letter):
            sentences_amount += 1
            is_first_alpha = True
            is_skipping = False

    return sentences_with_capital/sentences_amount

if __name__ == '__main__':
    print_text(count_sentences())