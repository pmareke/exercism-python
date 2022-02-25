from collections import Counter

# Score categories.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    counter = Counter(dice)
    if category == YACHT:
        if len(list(counter)) == 1:
            return 50
        return 0
    elif category in [ONES, TWOS, THREES, FOURS, FIVES, SIXES]:
        return category * counter.get(category, 0)
    elif category in [FULL_HOUSE]:
        result = 0
        values = sorted(counter.values())
        if values == [2, 3]:
            for item in counter:
                result += item * counter[item]
        return result
    elif category == FOUR_OF_A_KIND:
        result = 0
        if sorted(counter.values()) in ([1, 4], [5]):
            for item in counter:
                if counter[item] in (4, 5):
                    result = 4 * item
        return result
    elif category == LITTLE_STRAIGHT:
        if len(list(counter)) == 5 and min(counter.keys()) == 1 and max(
                counter.keys()) == 5:
            return 30
        return 0
    elif category == BIG_STRAIGHT:
        if len(list(counter)) == 5 and min(counter.keys()) == 2 and max(
                counter.keys()) == 6:
            return 30
        return 0
    elif category == CHOICE:
        result = 0
        for item in counter:
            result += item * counter[item]
        return result
