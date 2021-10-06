import re


def abbreviate(words):
    words = re.sub(r'[^A-Z\s\']+', ' ', words.upper()).split()
    return ''.join([x[0] for x in words])
