#!python
""" AOC 2022: Day 10 """
import pathlib
from collections import deque

def parse(puzzle_input: str):
    """ Parse input """
    signals = []
    for line in  puzzle_input.splitlines():
        if len(signal := line.split()) == 1:
            signals.append( tuple(signal + [None]) )
        else:
            signal, value = signal
            signals.append( (signal, int(value)) )
    return signals

def solve(puzzle_input: str):
    data = parse(puzzle_input)
    signals = deque(data)

    cycle = timer = signal_strengths = 0
    x = 1
    cycle_to_check = 20
    screen = ""

    while (cycle := cycle + 1) < 1000 and ( signals or timer ):
        pixel_position = (cycle-1)%40
        sprite_min, sprite_max = x-1, x+1

        if pixel_position == 0:
            screen += "\n"

        if sprite_min <= pixel_position <= sprite_max:
            screen += "#"
        else:
            screen += " "

        if cycle == cycle_to_check:
            cycle_to_check += 40
            signal_strengths += cycle * x

        if not timer:
            signal, value = signals.popleft()
            if signal == "noop":
                signal = None
                continue
            if signal == "addx":
                timer = 2

        if (timer := timer - 1) <= 0:
            if signal == "addx":
                x += value
            timer = 0

    return signal_strengths, screen

if __name__ == "__main__":
    puzzle_file = pathlib.Path(__file__).parent.joinpath("input.txt")
    puzzle_text = puzzle_file.read_text(encoding='utf-8').strip()
    answer1, answer2 = solve(puzzle_text)
    print(f"Part 1: {answer1}")
    print(f"Part 2: {answer2}")
