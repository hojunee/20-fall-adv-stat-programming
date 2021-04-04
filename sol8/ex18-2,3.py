import random

class Card():
    """
    suit : clubs, diamonds, hearts, spades
    rank_names = None, Ace, 2, ...
    """

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                    'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "{} of {}".format(Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __repr__(self):
        return "{} of {}".format(Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank

        if t1[0] < t2[0]:
            return True
        if t1[0] > t2[0]:
            return False
        if t1[1] < t2[1]:
            return True
        if t1[1] > t2[1]:
            return False
        return False

class Deck():
    """

    """

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        return '\n'.join([str(card) for card in self.cards])    
    
    def add_card(self, card):
        self.cards.append(card)

    def pop_card(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)

    # Solution 18-2
    def sort(self):
        self.cards.sort()

    def move_cards(self, hand, num):
        for _ in range(num):
            hand.add_card(self.pop_card())

    # Solution 18-3
    def deal_hands(self, n_of_participant, n_of_cards):
        game = []
        for _ in range(n_of_participant):
            one_hand = Hand()
            self.move_cards(one_hand, n_of_cards)
            game.append(one_hand)
        return game                

class Hand(Deck):
    def __init__(self, label=''):
        self.cards = []
        self.label = label

    def __repr__(self):
        return "{}".format(self.cards)
    
deck = Deck()
deck.shuffle()
print("deck에서 뽑아내기 :", deck.deal_hands(7, 7), sep="\n")
print("남은 deck :", deck, sep="\n")