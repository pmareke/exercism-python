"""
Hamming module.
"""


def distance(strand_a, strand_b):
    """
    Calculates the Hamming's distance between two strads.

    :param str Strand A.
    :param str Strand B.
    """
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands must be of equal length.')

    return sum(i != j for i, j in zip(strand_a, strand_b))
