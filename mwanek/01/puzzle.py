#!python
""" AOC 2022: Day 1 """
import pathlib

def parse(puzzle_input: str) -> list[int]:
    """ Parse input """
    calories_carried_per_elf = []
    for single_elf_data in puzzle_input.split('\n\n'):
        meals = single_elf_data.split('\n')
        total_calories = sum(map(int, meals))
        calories_carried_per_elf.append(total_calories)
    return sorted(calories_carried_per_elf)

def part1(sorted_calories_per_elf: list) -> int:
    """ Solve part 1 """
    return sorted_calories_per_elf[-1]

def part2(sorted_calories_per_elf: list) -> int:
    """ Solve part 2 """
    return sum(sorted_calories_per_elf[-3:])

def solve(puzzle_input: str) -> tuple:
    """ Parse, solve, return solutions """
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    input_file = pathlib.Path(__file__).parent.joinpath("input.txt")
    puzzle_input = input_file.read_text(encoding='utf-8').strip()
    answer1, answer2 = solve(puzzle_input)
    print(f"Part 1: {answer1}")
    print(f"Part 2: {answer2}")
