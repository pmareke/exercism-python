"""
High Scores module.
"""


def latest(scores):
    """
    Returns the last score in the list.

    :param scores: list of int.
    :return int lastest score.
    """

    return scores[-1]


def personal_best(scores):
    """
    Returns the max score in the list.

    :param score: list of int.
    :return int Scores' maximum

    """

    return max(scores)


def personal_top_three(scores):
    """
    Returns the 3 highest scores in the list

    :param score: list of int.
    :return int Scores' maximum
    """

    return sorted(scores, reverse=True)[0:3]
