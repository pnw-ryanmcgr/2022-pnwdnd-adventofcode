#!python
""" AOC 2022: Day 4 """
import pathlib

def parse(puzzle_input: str) -> list[list[set]]:
    """ Parse input """
    pairs_of_cleaning_ranges = []
    for pair_of_elves in puzzle_input.splitlines():
        ranges_for_this_pair = []
        for cleaning_range in pair_of_elves.split(','):
            start, end = map(int, cleaning_range.split('-'))
            ranges_for_this_pair.append(set(range(start, end+1)))
        pairs_of_cleaning_ranges.append(ranges_for_this_pair)
    return pairs_of_cleaning_ranges

def part1(cleaning_ranges: list[list[set]]) -> int:
    """ Solve part 1 """
    fully_contained_ranges = 0
    for range1, range2 in cleaning_ranges:
        if range1 <= range2 or range1 >= range2:
            fully_contained_ranges += 1
    return fully_contained_ranges

def part2(cleaning_ranges: list[list[set]]) -> int:
    """ Solve part 2 """
    overlapping_ranges = 0
    for range1, range2 in cleaning_ranges:
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
