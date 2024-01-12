import numpy as np
import random
import math


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
    new_start = np.random.choice(directions)
    temp = cards[new_start:]
    for i in range(new_start):
        temp.append(cards[i])
    cards = temp
    return cards

def flip_card(cards, direction):
    cards[direction] = not cards[direction]


def compute_method_stats(all_attempts, max_attempts, fewest_attempts):
    print("Average till win: {0}".format(np.mean(all_attempts)))
    print("Median value: {0}".format(np.median(all_attempts)))
    print("Largest number flips neaded: {0}".format(max_attempts))
    print("Fewest number flips neaded: {0}".format(fewest_attempts))





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



def flip_three_then_four_repeating(cards):
    iterations=0
    while not check_win(cards):
        # keeps the cards in the same group, just "inverses" them
        flip_four(cards)
        if not check_win(cards):
            iterations = iterations +1
            cards = rotate_table(cards)
            # flip three will almost always put the cards into the "off by one" group. Otherwise it puts them in win/lose
            flip_three(cards)
        
        cards = rotate_table(cards)
        iterations = iterations+1
    return iterations


def flip_three(cards):
    choices = random.sample(directions, 3)
    for choice in choices:
        cards[choice] = not cards[choice]


def flip_four(cards):
    for direction in directions:
        cards[direction] = not cards[direction]


def test_theory():
    all_attempts = []
    max_attempts = 0
    fewest_attempts = math.inf
    for i in range(10000):
        cards = set_up_cards()
        test = random_flip_cards(cards)
        if test > max_attempts:
            max_attempts = test
        if test < fewest_attempts:
            fewest_attempts = test
        all_attempts.append(test)
    compute_method_stats(all_attempts, max_attempts, fewest_attempts)



test_theory()
