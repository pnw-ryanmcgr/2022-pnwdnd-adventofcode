#!python
""" AOC 2022: Day 2 """
import pathlib

def parse(puzzle_input: str):
    """ Parse input """
    strategy_guide = []
    for line in puzzle_input.splitlines():
        a,b = line.split(' ')
        strategy_guide.append(('ABC'.index(a), 'XYZ'.index(b)))
    return strategy_guide

def part1(rps_rounds) -> int:
    """ Solve part 1 """
    total_score = 0
    for opponent_throw, my_throw in rps_rounds:
        my_throw += 1
        outcome = (my_throw - opponent_throw) % 3
        outcome_score = outcome * 3
        total_score += my_throw + outcome_score
    return total_score

def part2(strategy_guide):
    """ Solve part 2 """
    rounds = []
    for opponent_throw, goal in strategy_guide:
        my_throw = (opponent_throw + 2 + goal) % 3
        rounds.append((opponent_throw, my_throw))
    return part1(rounds)

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
