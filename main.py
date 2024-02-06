import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
        random.shuffle(self.cards)

    def deal_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self, deck):
        card = deck.deal_card()
        if card:
            self.hand.append(card)
            print(f"{self.name} draws {card}")
        else:
            print("Deck is empty, cannot draw a card.")

    def show_hand(self):
        print(f"{self.name}'s hand:")
        for card in self.hand:
            print(card)


# Пример использования классов
if __name__ == "__main__":
    deck = Deck()

    player1 = Player("Alice")
    player2 = Player("Bob")

    for _ in range(5):
        player1.draw_card(deck)
        player2.draw_card(deck)

    player1.show_hand()
    player2.show_hand()
