"""
Twelve Days module.
"""


def recite(start_verse, end_verse):
    """
    Create the song based on the starting and ending verses.

    :param str Starting verse.
    :param str Ending verse.
    """

    def build_verse(verse):
        verses = {
            'first': 'and a Partridge in a Pear Tree.',
            'second': 'two Turtle Doves, ',
            'third': 'three French Hens, ',
            'fourth': 'four Calling Birds, ',
            'fifth': 'five Gold Rings, ',
            'sixth': 'six Geese-a-Laying, ',
            'seventh': 'seven Swans-a-Swimming, ',
            'eighth': 'eight Maids-a-Milking, ',
            'ninth': 'nine Ladies Dancing, ',
            'tenth': 'ten Lords-a-Leaping, ',
            'eleventh': 'eleven Pipers Piping, ',
            'twelfth': 'twelve Drummers Drumming, '
        }
        days = list(verses)
        sentence = f'On the {days[verse-1]} day of Christmas my true love gave to me: '
        if verse == 1:
            sentence += "a Partridge in a Pear Tree."
            return sentence
        while verse >= 1:
            sentence += verses[days[verse - 1]]
            verse -= 1
        return sentence

    song = []
    for index in range(start_verse, end_verse + 1):
        song.append(build_verse(index))
    return song
