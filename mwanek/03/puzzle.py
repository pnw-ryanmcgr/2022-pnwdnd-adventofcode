#!python
""" AOC 2022: Day 3 """
import pathlib
import string

def parse(puzzle_input: str) -> list[list[int]]:
    """ Parse input """
    priority = lambda x: string.ascii_letters.index(x) + 1
    rucksacks = []
    for rucksack_inventory in puzzle_input.splitlines():
        rucksacks.append([priority(item) for item in rucksack_inventory])
    return rucksacks

def part1(rucksacks: list) -> int:
    """ Solve part 1 """
    priorities = 0
    for sack in rucksacks:
        half = len(sack)//2
        common_item = set(sack[:half]) & set(sack[half:])
        if common_item:
            priorities += common_item.pop()
    return priorities

def part2(rucksacks: list) -> int:
    """ Solve part 2 """
    priorities = 0
    next_sack = lambda: set(rucksacks.pop())
    while rucksacks:
        common_item = next_sack() & next_sack() & next_sack()
        if common_item:
            priorities += common_item.pop()
    return priorities

def solve(puzzle_input: str) -> tuple:
    """ Parse, solve, return solutions """
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_file = pathlib.Path(__file__).parent.joinpath("input.txt")
    puzzle_text = puzzle_file.read_text(encoding='utf-8').strip()
    solution1, solution2 = solve(puzzle_text)
    print(f"Part 1: {solution1}")
    print(f"Part 2: {solution2}")
