from re import sub


class Luhn:

    def __init__(self, card_num):
        self.card = sub(" ", "", card_num)

    def valid(self):
        if len(self.card) <= 1 or not self.card.isdigit():
            return False

        cards = []
        for index, num in enumerate(list(self.card[::-1])):
            if index % 2 != 0:
                double = int(num) * 2
                if double < 10:
                    cards.append(double)
                else:
                    cards.append(double - 9)
            else:
                cards.append(int(num))

        return sum(cards) % 10 == 0
