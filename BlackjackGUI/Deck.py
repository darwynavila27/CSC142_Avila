from Card import Card

class Deck:
    def __init__(self):
        self.cards = []

        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
                  "Jack", "Queen", "King", "Ace"]

        for suit in suits:
            for value in values:
                image_path = f"{value} of {suit}.png"
                self.cards.append(Card(value, suit, image_path))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def dealCard(self):
        return self.cards.pop()
