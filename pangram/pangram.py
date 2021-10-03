
def is_pangram(sentence):
    sentence = sentence.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(alphabet)):
        letter = alphabet[i]
        if sentence.find(letter) > -1:
            pass
        else:
            return False
    return True
