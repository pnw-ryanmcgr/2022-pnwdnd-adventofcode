
"""
Ryan McGregor, 11Dec2022
AOC2022:Day10
https://adventofcode.com/2022/day/10
Note: And another one goes....
"""

from pprint import pprint
from aocd import get_data, submit
import numpy as np

TEST_DATA ="""
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""

def retrieve_active_value(command_list, number_retrieved):
    """
    Retrieves active value for X at a given iteration.
    Input:
        command_list (list): sequence of commands
        number_retrieved (int): the cycle which is to be retrieved
    Output:
        (int): Value of X on cycle provided
    """
    current_idx, current_cycle, rolling_sum = 0, 1, 1
    while True:
        # print('======================')
        # print(f'Current Cycle: {current_cycle}')
        # print(f'Current Index: {current_idx}')
        # print(f'Rolling Sum (Start): {rolling_sum}')
        # print(f'Current Op: {command_list[current_idx]}')
        if current_cycle >= number_retrieved - 1:
            return rolling_sum
        if 'addx' in command_list[current_idx]:
            rolling_sum += int(command_list[current_idx].replace('addx ', ''))
            current_cycle += 2
        else:
            current_cycle += 1
        # print(f'Rolling Sum (Finish): {rolling_sum}')
        current_idx += 1


if __name__ == '__main__':
    # data = [x for x in TEST_DATA.split('\n') if x != '']
    data = [x for x in get_data(day=10, year=2022).split('\n') if x != '']

    # Part A
    answer_a = []
    for cycle_number in [20, 60, 100, 140, 180, 220]:
        answer_a.append(retrieve_active_value(data, cycle_number) * cycle_number)
    answer_a = sum(answer_a)
    print(f'Answer_A: {answer_a}')
    submit(str(answer_a), part="a", day=10, year=2022)

    # Part B
    # screen = np.zeros((40,6), dtype=bool)
    # pprint(screen)


    # print(f'Answer_B: {answer_b}')

    # submit(answer_b, part="b", day=7, year=2022)
