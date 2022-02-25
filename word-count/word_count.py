from collections import defaultdict


def count_words(sentence):
    words = defaultdict(int)
    for word in sentence.split(" "):
        words[word] += 1
    return words
