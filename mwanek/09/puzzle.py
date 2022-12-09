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
    delta_x, delta_y = head_x-tail_x, head_y-tail_y
    abs_x, abs_y = diff = (abs(delta_x), abs(delta_y))
    if 2 in diff:
        if abs_x == 2:
            delta_x //= 2
        if abs_y == 2:
            delta_y //= 2
        return (tail_x+delta_x, tail_y+delta_y)
    return tail

def solve(puzzle_input):
    data = parse(puzzle_input)

    tail = [(0,0) for _ in range(9)]
    head = (0,0)

    first_tail_visits = set()
    first_tail_visits.add(tail[0])
    last_tail_visits = set()
    last_tail_visits.add(tail[-1])

    for delta_x, delta_y in data:
        head_x, head_y = head
        head = (head_x + delta_x, head_y + delta_y)
        tail[0] = move(head, tail[0])
        for i in range(1,9):
            tail[i] = move(tail[i-1], tail[i])
        first_tail_visits.add(tail[0])
        last_tail_visits.add(tail[-1])

    return len(first_tail_visits), len(last_tail_visits)

if __name__ == "__main__":
    puzzle_file = pathlib.Path(__file__).parent.joinpath("input.txt")
    puzzle_text = puzzle_file.read_text(encoding='utf-8').strip()
    answer1, answer2 = solve(puzzle_text)
    print(f"Part 1: {answer1}")
    print(f"Part 2: {answer2}")
