"""
Ryan McGregor, 02Dec2022
AOC2022:Day02
https://adventofcode.com/2022/day/2
"""

from pprint import pprint
from aocd import get_data, submit

# TEST_DATA = """A Y
# B X
# C X
# A Z
# B Y
# C X
# C X
# C X"""

### Legend
# a, x = rock
# b, y = paper
# c, z = scissors

COMBINATIONS_A = {
    'winning': [
        ('A', 'Y'),
        ('B', 'Z'),
        ('C', 'X')
    ],
    'losing': [
        ('A', 'Z'),
        ('B', 'X'),
        ('C', 'Y')
    ],
    'draw': [
        ('A', 'X'),
        ('B', 'Y'),
        ('C', 'Z')
    ]
}

## Part B Legend
## X = LOSE
## Y = DRAW
## Z = WIN

COMBINATIONS_B = {
    'X': {
        'A': 'Z',
        'B': 'X',
        'C': 'Y',
    },
    'Y': {
        'A': 'X',
        'B': 'Y',
        'C': 'Z',
    },
    'Z': {
        'A': 'Y',
        'B': 'Z',
        'C': 'X',
    }
}

## Score table for lose/draw/win
SCORES = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

## Score table for our choice
VALUES = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

def score_round_a(matchup):
    """(PART A) Checks score for a given round, given tuple of (opponent, self)"""
    # Set match score
    if matchup in COMBINATIONS_A['winning']:
        score = 6
    elif matchup in COMBINATIONS_A['losing']:
        score = 0
    else:
        score = 3
    # Add selection score
    return score + VALUES[matchup[1]]

def score_round_b(matchup):
    """(PART B) Checks score for a given round, given tuple of (opponent, self)"""
    # Determine match result and our choice
    return SCORES[matchup[1]] + VALUES[COMBINATIONS_B[matchup[1]][matchup[0]]]

if __name__ == '__main__':
    data = get_data(day=2, year=2022).split('\n')
    total_score_a = 0
    for line in data:
        total_score_a += score_round_a(tuple(line.split(' ')))
    print(f'Total Score: {total_score_a}')

    total_score_b = 0
    for line in data:
        total_score_b += score_round_b(tuple(line.split(' ')))
    print(f'Total Score: {total_score_b}')

    ## Submit Answer #1
    # submit(total_score_a, part="a", day=2, year=2022)
    # submit(total_score_b, part="b", day=2, year=2022)
