import sys
from utils import file_to_string, print_text, check_sentence_end

def sentences_in_fourth_quartile():
    text = file_to_string()
    
    sentence = ''
    sentences_amount = 0
    sentence_length = 0

 

    sentences = {}

    for letter in text:
        sentence += letter
        if check_sentence_end(letter): 
            sentences[sentence.lstrip().rstrip()] = len(sentence)
           
            sentence = ''
            sentences_amount += 1
    print(sentences)
    sentences = dict(sorted(sentences.items(), key=lambda item: item[1]))
    print(sentences)

    fourth_quartile_start = sentences_amount * 3 // 4

    return list(sentences.keys())[fourth_quartile_start:]
    
  
    

if __name__ == '__main__':
    print(sentences_in_fourth_quartile())