import numpy as np
import random
import itertools


NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

directions = [NORTH, EAST, SOUTH, WEST]

cardstates = [True, False]

def set_up_cards():
    cards = []
    for i in range(4):
        cards.append(np.random.choice(cardstates))
    if check_win(cards):
        cards = set_up_cards()
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

def rotate_to_the_left(cards):
    temp = cards[1:]
    temp.append(cards[0])
    return temp

def flip_card(cards, direction):
    cards[direction] = not cards[direction]


def flip_n_cards(cards, n):
    choices = random.sample(directions, n)
    for choice in choices:
        flip_card(cards, choice)    


def compute_method_stats(all_attempts, max_attempts, fewest_attempts):
    print("Average till win: {0}".format(np.mean(all_attempts)))
    print("Median value: {0}".format(np.median(all_attempts)))
    print("Largest number flips neaded: {0}".format(max_attempts))
    print("Fewest number flips neaded: {0}".format(fewest_attempts))


def list_all_possible_card_states():
    # https://stackoverflow.com/questions/54059917/generate-all-length-n-permutations-of-true-false
    return [list(i) for i in itertools.product(cardstates, repeat=4)]


def list_all_flip_combos():
    # https://blog.enterprisedna.co/how-to-generate-all-combinations-of-a-list-in-python/
    # there is also a helpful stackoverflow which shows the same thing
    combos = []
    for i in range(1,5):
        combos.append(list(itertools.combinations(directions, i)))
    return combos


# Takes around 17 flips
# def only_flip_north(cards):
#     iterations=0
#     while check_win(cards) == False:
#         flip_card(cards, NORTH)
#         cards = rotate_table(cards)
#         iterations = iterations+1
#     return iterations



# # Takes around 17 flips
# def random_flip_cards(cards):
#     iterations=0
#     while check_win(cards) == False:
#         choice = np.random.choice(directions)
#         flip_card(cards, choice)
#         cards = rotate_table(cards)
#         iterations = iterations+1
#     return iterations




def test_theory():
    all_attempts = []
    max_attempts = 0
    fewest_attempts = math.inf
    for i in range(10000):
        cards = set_up_cards()
        test = flip_three_then_four_repeating(cards)
        if test > max_attempts:
            max_attempts = test
        if test < fewest_attempts:
            fewest_attempts = test
        all_attempts.append(test)
    compute_method_stats(all_attempts, max_attempts, fewest_attempts)



# test_theory()

# print(list_all_possible_card_states())
print(list_all_flip_combos())
