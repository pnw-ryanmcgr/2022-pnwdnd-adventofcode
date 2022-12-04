#!python
""" AOC 2022: Day 4 """
import pathlib

def parse(puzzle_input: str) -> list[list[set]]:
    """ Parse input """
    cleaning_pairs = []
    for elves in puzzle_input.splitlines():
        elf_pair = []
        for section_assignment in elves.split(','):
            start, end = map(int, section_assignment.split('-'))
            elf_pair.append(set(range(start, end+1)))
        cleaning_pairs.append(elf_pair)
    return cleaning_pairs

def part1(cleaning_pairs: list[list[set]]) -> int:
    """ Solve part 1 """
    fully_contained_ranges = 0
    for range1, range2 in cleaning_pairs:
        if range1.issubset(range2) or range2.issubset(range1):
            fully_contained_ranges += 1
    return fully_contained_ranges

def part2(cleaning_pairs: list[list[set]]) -> int:
    """ Solve part 2 """
    overlapping_ranges = 0
    for range1, range2 in cleaning_pairs:
        if range1 & range2:
            overlapping_ranges +=1
    return overlapping_ranges

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
