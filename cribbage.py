import itertools
import random
import cribbage_calculator

# Greet User
"""
player_name = input("Hello, what's your name? ")
print(f"Welcome, {player_name}. Let's play cribbage!")
"""
# Start of a new game, computer and player both start at 0 points. Setting up and shuffling card deck
cpu_score=0
player_score=0
score_tracker={} # example:  {round1:{cpu:120, player:93}, round2:{cpu:80, player:120}}
round_num = 0
suit = ['Club','Diamond','Heart','Spade']
number = ['1','2','3','4','5','6','7','8','9','10','J','Q','K']
new_card_deck = list(itertools.product(suit,number))
card_deck = new_card_deck.copy()
#print(f'{card_deck[0][1]} of {card_deck[0][0]}')
random.shuffle(card_deck)


# Draw for first crib, lower deals and gets first crib
## Rock paper scissor to decide first cut??
cpu_cut = 0
player_cut = 0
while cpu_cut == player_cut:
    cpu_cut_card = card_deck[random.randrange(52)]
    player_cut_card = [x for x in card_deck if x != cpu_cut][random.randrange(52)]
    if cpu_cut_card[1] in ('J','Q','K'):
        cpu_cut = '10'
    else:
        cpu_cut = cpu_cut_card[1]
    if player_cut_card[1] in ('J','Q','K'):
        player_cut = '10'
    else:
        player_cut = player_cut_card[1]
# Deal cards
if cpu_cut > player_cut:
    cpu_hand = card_deck[0:11:2]
    player_hand = card_deck[1:12:2]
else:
    player_hand = card_deck[0:11:2]
    cpu_hand = card_deck[1:12:2]

card_deck = card_deck[12:]

# Discard for crib

# Player discard
print(f'Your cards are:')
for i in range(len(player_hand)):
    print(f'[{i+1}]: {player_hand[i][1]} of {player_hand[i][0]}')
player_discard_1 = input('Please select the first card to discard:')
while player_discard_1 not in map(str, range(1,7)):
    player_discard_1=input('Selection invalid. Please reselect the first card to discard:')
player_discard_2 = input('Please select the second card to discard:')
while (player_discard_2 not in map(str,range(1,7))) or (player_discard_2 == player_discard_1):
    player_discard_2=input('Selection invalid. Please reselect the second card to discard:')

# Cpu discard





