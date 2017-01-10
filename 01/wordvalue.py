from data import DICTIONARY, LETTER_SCORES                                                                                                                                                     

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as f:
        dict_words = [line.strip() for line in f]
    return dict_words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    calc = 0 
    word = word.upper()
    for char in word:
        for key in LETTER_SCORES.items():
            if char == key[0]:
                calc += int(key[1])
    return calc

def max_word_value(max_word=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    return max(max_word, key=calc_word_value)

if __name__ == "__main__":
    pass # run unittests to validate
