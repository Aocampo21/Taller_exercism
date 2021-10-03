
def is_isogram(word):
    clean_word = [i for i in word.lower() if i.isalpha()]
    return len(set(clean_word)) == len(clean_word)
