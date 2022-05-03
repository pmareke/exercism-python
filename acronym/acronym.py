import re


def abbreviate(words):
    letters = []
    for word in filter(lambda word: word, re.split(" |-", words)):
        letters.append(word[0] if word[0].isalpha() else word[1])
    return "".join(letters).upper()
