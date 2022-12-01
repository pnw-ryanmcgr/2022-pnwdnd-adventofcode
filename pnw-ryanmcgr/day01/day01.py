"""
Ryan McGregor, 01Dec2022
AOC2022:Day01
https://adventofcode.com/2022/day/1
"""

from pprint import pprint
from aocd import get_data, submit

data = get_data(day=1, year=2022)

# TEST_DATA = """1000
# 2000
# 3000

# 4000

# 5000
# 6000

# 7000
# 8000
# 9000

# 10000"""

elves = [0]

for line in data.split('\n'):
    if line == '':
        elves.append(0)
    else:
        elves[-1] += int(line)

elves = sorted(elves)

answer_1 = elves[-1]
print(f'Answer 1: {answer_1}')

answer_2 = sum([elves[-3], elves[-2], elves[-1]])
print(f'Answer 2: {answer_2}')

# submit(answer_1, part="a", day=1, year=2022)
# submit(answer_2, part="b", day=1, year=2022)
