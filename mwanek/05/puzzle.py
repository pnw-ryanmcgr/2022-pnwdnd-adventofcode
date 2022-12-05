#!python
""" AOC 2022: Day 5 """
import pathlib
from collections import deque
from copy import deepcopy

def parse(puzzle_input: str):
    """ Parse input """
    cargo, procedures = [l.split('\n') for l in puzzle_input.split("\n\n")]

    pile_number_string = cargo[-1]
    crate_strings = cargo[:-1]
    parsed_crate_piles = []
    for pile_index,pile_number in enumerate(pile_number_string):
        crate_pile = deque()
        if pile_number.isdigit():
            for layer_of_crates in crate_strings:
                crate = layer_of_crates[pile_index]
                if crate.isalpha():
                    crate_pile.appendleft(crate)
            parsed_crate_piles.append(crate_pile)

    parsed_procedures = []
    for procedure in procedures:
        digits_in_string = ''.join([c for c in procedure if c.isdigit() or c.isspace()]).strip().split()
        parsed_procedures.append(tuple(map(int, digits_in_string)))

    return parsed_crate_piles, parsed_procedures

def part1(data):
    """ Solve part 1 """
    crate_piles, procedures = deepcopy(data)
    for procedure in procedures:
        amount, source, target = procedure
        origin = crate_piles[source-1]
        destination = crate_piles[target-1]
        for _ in range(amount):
            destination.append(origin.pop())
    return ''.join([pile[-1] for pile in crate_piles])

def part2(data):
    """ Solve part 2 """
    crate_piles, procedures = deepcopy(data)
    for procedure in procedures:
        amount, source, target = procedure
        origin = crate_piles[source-1]
        destination = crate_piles[target-1]
        height = len(destination)
        for _ in range(amount):
            destination.insert(height, origin.pop())
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
