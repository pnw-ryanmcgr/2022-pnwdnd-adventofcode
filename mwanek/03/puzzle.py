#!python
""" AOC 2022: Day 3 """
import pathlib
import string

def parse(puzzle_input: str) -> list[list[int]]:
    """ Parse input """
    priority = dict(zip(string.ascii_letters,range(1,53)))
    rucksacks = []
    for line in puzzle_input.splitlines():
        rucksacks.append([priority[c] for c in line])
    return rucksacks

def part1(rucksacks: list) -> int:
    """ Solve part 1 """
    priorities = 0
    for sack in rucksacks:
        half = len(sack)//2
        first_compartment = sack[:half]
        second_compartment = sack[half:]
        checked = {}
        for item in first_compartment:
            if item in checked:
                continue
            if item in second_compartment:
                priorities += item
                break
            checked[item] = True
    return priorities

def part2(rucksacks: list) -> int:
    """ Solve part 2 """
    priorities = 0
    for i in range(0,len(rucksacks),3):
        small_sack = min(range(i,i+3), key=lambda x: len(rucksacks[x]))
        second_sack, third_sack = (small_sack+1)%3+i, (small_sack+2)%3+i
        checked = {}
        for item in rucksacks[small_sack]:
            if item in checked:
                continue
            if item in rucksacks[second_sack] and item in rucksacks[third_sack]:
                priorities += item
                break
            checked[item]=True
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
