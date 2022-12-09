#!python
""" AOC 2022: Day 9  """
import pathlib

def parse(puzzle_input: str):
    movements = []
    movement = {
            "L": (-1, 0),
            "R": (1, 0),
            "U": (0, 1),
            "D": (0, -1)
        }
    for line in puzzle_input.splitlines():
        direction, steps = line.split()
        for _ in range(int(steps)):
            movements.append(movement[direction])
    return movements

def move(head, tail):
    head_x, head_y = head
    tail_x, tail_y = tail
    delta_x, delta_y = diff = (head_x - tail_x, head_y - tail_y)
    if 2 in diff or -2 in diff:
        if delta_x in (2, -2):
            delta_x //= 2
        if delta_y in (2, -2):
            delta_y //= 2
        return (tail_x + delta_x, tail_y + delta_y)
    return tail

def solve(puzzle_input):
    head_movements = parse(puzzle_input)
    starting_point = (0,0)
    head_x, head_y = starting_point
    tail_knots = [starting_point for _ in range(9)]

    first_tail_visits = {starting_point}
    last_tail_visits = {starting_point}

    for delta_x, delta_y in head_movements:
        head_x, head_y = last_knot = (head_x + delta_x, head_y + delta_y)
        for number, knot in enumerate(tail_knots):
            tail_knots[number] = last_knot = move(last_knot, knot)
        first_tail_visits.add(tail_knots[0])
        last_tail_visits.add(tail_knots[-1])

    return len(first_tail_visits), len(last_tail_visits)

if __name__ == "__main__":
    puzzle_file = pathlib.Path(__file__).parent.joinpath("input.txt")
    puzzle_text = puzzle_file.read_text(encoding='utf-8').strip()
    answer1, answer2 = solve(puzzle_text)
    print(f"Part 1: {answer1}")
    print(f"Part 2: {answer2}")
