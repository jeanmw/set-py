from itertools import combinations
import random

COLORS = ["red", "green", "purple"]
SHAPES = ["pill", "diamond", "toothpaste"]
NUMBERS = [1, 2, 3]
FILLS = ["solid", "fuzzy", "empty"]

class SetCard:
    def __init__(self, color, shape, number, fill):
        self.color = color
        self.shape = shape
        self.number = number
        self.fill = fill

def random_value(attributes):
    return attributes[random.randint(0,2)]

def random_card():
    card = SetCard(
        color=random_value(COLORS),
        shape=random_value(SHAPES),
        number=random_value(NUMBERS),
        fill=random_value(FILLS)
    )
    print(card)
    return card

def initialize_cards():
    cards = []
    while len(cards) < 8:
        cards.append(random_card())
    return cards

def is_attribute_match(a0, a1, a2):
    if (a0 == a1 == a2) or ((a0 != a1) and (a1 != a2)):
        return True
    return False

def is_set(c0, c1, c2):
    if not is_attribute_match(c0.color, c1.color, c2.color):
        return False
    if not is_attribute_match(c0.shape, c1.shape, c2.shape):
        return False
    if not is_attribute_match(c0.number, c1.number, c2.number):
        return False
    if not is_attribute_match(c0.fill, c1.fill, c2.fill):
        return False
    return True

def get_num_sets(cards):
    num_sets = 0
    comb = combinations(cards, 3)
    for c in comb:
        if is_set(c[0], c[1], c[2]):
            print("is set")
            print(c[0].__dict__, c[1].__dict__, c[2].__dict__)
            num_sets += 1
    print("Got " + str(num_sets) + " sets")
    return num_sets

def run_game():
    get_num_sets(initialize_cards())

run_game()
