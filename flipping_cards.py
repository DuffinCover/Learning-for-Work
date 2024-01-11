import numpy as np
import random



NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

directions = [NORTH, EAST, SOUTH, WEST]

def set_up_cards():
    cards = []
    for i in range(4):
        cards.append(np.random.choice([False,True]))
    return cards


def check_win(cards):
    return sum(cards) == 4

def rotate_table(cards):
    np.random.shuffle(cards)
    return cards

def flip_card(cards, direction):
    cards[direction] = not cards[direction]


def compute_method_stats(all_attempts):
    print("Average till win: {0}".format(np.mean(all_attempts)))
    print("Median value: {0}".format(np.median(all_attempts)))

# Takes around 17 flips
def only_flip_north(cards):
    iterations=0
    while check_win(cards) == False:
        flip_card(cards, NORTH)
        cards = rotate_table(cards)
        iterations = iterations+1
    return iterations



# Takes around 17 flips
def random_flip_cards(cards):
    iterations=0
    while check_win(cards) == False:
        choice = np.random.choice(directions)
        flip_card(cards, choice)
        cards = rotate_table(cards)
        iterations = iterations+1
    return iterations


# takes around 4.5 flips
def if_flip(cards):
    iterations=0
    while not check_win(cards):
        if(cards[NORTH] == False):
            flip_card(cards, NORTH)
        else:
            flip_card(cards, SOUTH) 
        cards = rotate_table(cards)
        iterations = iterations+1
    return iterations



def test_theory():
    all_attempts = []
    for i in range(10000):
        cards = set_up_cards()
        test = if_flip(cards)
        
        all_attempts.append(test)
    compute_method_stats(all_attempts)



test_theory()