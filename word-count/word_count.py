import re


def count_words(sentence):
    words = dict()
    pattern = re.compile("([0-9a-z']+)")
    for word in re.findall(pattern, sentence.lower()):
        if word.startswith("'") or word.endswith("''"):
            word = word.replace("'", "")
        words[word] = words.get(word, 0) + 1
    return words
