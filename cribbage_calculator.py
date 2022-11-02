from functools import reduce
import operator
import itertools
import collections

class TooManyArgumentsException(Exception):
    pass

def limit_args(n):
    def limit_decorator(f):
        def new_f(*args, **kwargs):
            if len(args) > n:
                raise TooManyArgumentsException("%d args accepted at most, %d args passed" % (n, len(args)))
            return f(*args, **kwargs)
        return new_f
    return limit_decorator

# Points calculator
@limit_args(5)
def cribbage_points_calculator(card1,card2,card3,card4,*args):
    hand = [card1,card2,card3,card4] + [arg for arg in args]
    points = 0
    nums = [int(x[1]) if x[1].isdigit() else 10 for x in hand]
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
    sorted_nums = sorted(nums)
    run = []
    run_dict = {}
    for i in sorted_nums:
        run_dict[i] = 1
    for num in sorted_nums:
        if (len(run) == 0) or (run[-1] == num - 1):
            run.append(num)
        elif (run[-1] == num) and num in run:
            run_dict[num] += 1
        else:
            continue
    multiplier = 1
    for val in run_dict.values():
        multiplier *= val
    if len(run) >= 3:
        points += len(run) * multiplier
        print(f'{multiplier} runs of {len(run)} for {len(run) * multiplier}')
    
    # Calculate for Jack
    if len(hand) == 5:
        for i in range(4):
            if (hand[i][0] == hand[4][0]) and (hand[i][1] == 'J'):
                points += 1
                print('One for the nob.')
    
    print(f'Total points: {points}')

