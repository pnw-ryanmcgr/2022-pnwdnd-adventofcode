#!python
""" AOC 2022: Day X """
import pathlib
from copy import deepcopy

def parse(puzzle_input: str):
    """ Parse input """
    #section1, section2 = [l.split('\n') for l in puzzle_input.split("\n\n")]
    #for line in  puzzle_input.splitlines():

def part1(data):
    """ Solve part 1 """
    #d = deepcopy(data)

def part2(data):
    """ Solve part 2 """

def solve(puzzle_input: str) -> tuple:
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
