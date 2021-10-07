def find_anagrams(word, candidates):
    word = word.upper()
    return [x for x
            in candidates if sorted(word) == sorted(x.upper())
            and word != x.upper()]
