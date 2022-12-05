#!python
""" AOC 2022: Day 5 """
import pathlib
from collections import deque
from copy import deepcopy

def parse(puzzle_input: str) -> tuple[list]:
    """ Parse input """
    cargo_diagram, raw_procedures = [l.split('\n') for l in puzzle_input.split("\n\n")]

    pile_number_string = cargo_diagram[-1]
    crate_strings = cargo_diagram[:-1]
    pile_indexes = [i for i,c in enumerate(pile_number_string) if c.isdigit()]

    parsed_crate_piles = []
    for i in pile_indexes:
        crates_at_index = [s[i] for s in reversed(crate_strings) if s[i].isalpha()]
        parsed_crate_piles.append(deque(crates_at_index))

    parsed_procedures = []
    for procedure_string in raw_procedures:
        digits_and_spaces = ''.join([c for c in procedure_string if c.isdigit() or c.isspace()])
        procedure_as_integers = tuple(int(s) for s in digits_and_spaces.split())
        procedure_with_piles_as_indexes = tuple(sum(i) for i in zip((0,-1,-1), procedure_as_integers))
        parsed_procedures.append(procedure_with_piles_as_indexes)

    return parsed_crate_piles, parsed_procedures

def part1(data: tuple[list]) -> str:
    """ Solve part 1 """
    crate_piles, procedures = deepcopy(data)

    for amount, source, target in procedures:
        origin = crate_piles[source]
        destination = crate_piles[target]
        for _ in range(amount):
            destination.append(origin.pop())

    crates_on_top = [pile[-1] for pile in crate_piles]
    return ''.join(crates_on_top)

def part2(data: tuple[list]) -> str:
    """ Solve part 2 """
    crate_piles, procedures = deepcopy(data)

    for amount, source, target in procedures:
        origin = crate_piles[source]
        destination = crate_piles[target]
        height = len(destination)
        for _ in range(amount):
            destination.insert(height, origin.pop())

    crates_on_top = [pile[-1] for pile in crate_piles]
    return ''.join(crates_on_top)

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
