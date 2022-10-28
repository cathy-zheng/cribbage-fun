from functools import reduce
import operator
import itertools
import collections

# Points calculator
def cribbage_points_calculator(card1,card2,card3,card4,*args):
    hand = [card1,card2,card3,card4] + [arg for arg in args]
    points = 0
    suits = [x[0] for x in hand]
    nums = [int(x[1]) for x in hand]
    num_dict = collections.Counter(nums)
    i = 2
    all_combo=[]
    all_combo_num = []
    while i <= len(hand):
        all_combo += list(itertools.combinations(hand,i))
        all_combo_num += list(itertools.combinations(nums,i))
        i += 1
    
    # calculate for 15
    for i in range(len(all_combo)):
        if reduce(operator.add,all_combo_num[i]) == 15:
            print(f'Fiften for two. {all_combo[i]}')
            points += 2
        else:
            continue
    
    # Calculate for pairs
    for key, value in num_dict.items():
        if value == 2:
            points += 2
            print(f'A Pair of {key} for two.')
        elif value == 3:
            points += 6
            print(f'Three {key}s for six.')
        elif value == 4:
            points += 12
            print(f'Four {key}s for twelve.')
        else:
            continue
    
    # Calculate for runs
    
    print(points)


cribbage_points_calculator(('Heart','5'),('Diamond','10'),('Heart','10'),('Club','10'))