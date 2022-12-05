#!python
""" AOC 2022: Day 5 """
import pathlib
from collections import deque
from copy import deepcopy

def parse(puzzle_input: str):
    """ Parse input """
    stacks, moves = [l.split('\n') for l in puzzle_input.split("\n\n")]

    pile_numbers = stacks[-1]
    crates = stacks[:-1]
    crate_piles = []
    for i,pile_number in enumerate(pile_numbers):
        crate_pile = deque()
        if pile_number.isdigit():
            for crate_layer in crates:
                crate = crate_layer[i]
                if crate.isalpha():
                    crate_pile.appendleft(crate)
            crate_piles.append(crate_pile)

    procedures = []
    for procedure in moves:
        numbers = ''.join([c for c in procedure if c.isdigit() or c.isspace()]).strip().split()
        procedures.append(tuple(map(int, numbers)))

    return crate_piles, procedures

def part1(data):
    """ Solve part 1 """
    crate_piles, procedures = deepcopy(data)
    for procedure in procedures:
        amount, origin, destination = procedure
        for _ in range(amount):
            crate_piles[destination-1].append(crate_piles[origin-1].pop())
    return ''.join([pile[-1] for pile in crate_piles])

def part2(data):
    """ Solve part 2 """
    crate_piles, procedures = deepcopy(data)
    for procedure in procedures:
        amount, origin, destination = procedure
        crates_to_move = deque()
        for _ in range(amount):
            crates_to_move.append(crate_piles[origin-1].pop())
        for _ in range(amount):
            crate_piles[destination-1].append(crates_to_move.pop())
    return ''.join([pile[-1] for pile in crate_piles])

def solve(puzzle_input: str) -> tuple:
    """ Parse, solve, return solutions """
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_file = pathlib.Path(__file__).parent.joinpath("input.txt")
    puzzle_text = puzzle_file.read_text(encoding='utf-8').strip()
    answer1, answer2 = solve(puzzle_text)
    print(f"Part 1: {answer1}")
    print(f"Part 2: {answer2}")
