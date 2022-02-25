"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

ACES = ['10', 'J', 'Q', 'K', 'A']


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    """

    if card == 'A':
        return 1
    elif card in ['J', 'Q', 'K']:
        return 10
    return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    :return: higher value card - str. Tuple of both cards if they are of equal value.
    """
    one = value_of_card(card_one)
    two = value_of_card(card_two)
    if one == two:
        return card_one, card_two
    elif one > two:
        return card_one
    return card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. 'J', 'Q', 'K' = 10;
           'A' = 11 (if already in hand); numerical value otherwise.

    :return: int - value of the upcoming ace card (either 1 or 11).
    """
    one = value_of_card(card_one)
    two = value_of_card(card_two)
    return 1 if card_one in ACES or card_two in ACES or one + two > 10 else 11


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 11; numerical value otherwise.
    :return: bool - if the hand is a blackjack (two cards worth 21).
    """

    return card_one in ACES[0:-1] and card_two == 'A' or card_one == 'A' and card_two in ACES[0:-1]


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - if the hand can be split into two pairs (i.e. cards are of the same value).
    """

    return card_one and card_two in ['J', 'Q', 'K'] or card_one == card_two


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - if the hand can be doubled down (i.e. totals 9, 10 or 11 points).
    """

    one = value_of_card(card_one)
    two = value_of_card(card_two)

    return one + two in [9, 10, 11]
