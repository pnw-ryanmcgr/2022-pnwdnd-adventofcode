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

def get_pixel(cycle: int, x: int) -> str:
    pixel_position = (cycle-1)%40
    sprite_min, sprite_max = x-1, x+1

    pixel = "\n" if (pixel_position == 0) else ""

    if sprite_min <= pixel_position <= sprite_max:
        pixel += "#"
    else:
        pixel += " "

    return pixel

def solve(puzzle_input: str):
    data = parse(puzzle_input)
    signals = deque(data)
    cycles_to_complete = { "noop": 1, "addx": 2 }

    cycle = timer = signal_strength = 0
    x = 1
    screen = ""

    while (cycle := cycle + 1) < 1000 and (signals or timer):
        screen += get_pixel(cycle, x)
        signal_strength += 0 if ((cycle - 20) % 40) else cycle * x

        if not timer:
            signal, value = signals.popleft()
            timer = cycles_to_complete[signal]

        if (timer := timer - 1) <= 0:
            if signal == "addx":
                x += value

    return signal_strength, screen

if __name__ == "__main__":
    puzzle_file = pathlib.Path(__file__).parent.joinpath("input.txt")
    puzzle_text = puzzle_file.read_text(encoding='utf-8').strip()
    answer1, answer2 = solve(puzzle_text)
    print(f"Part 1: {answer1}")
    print(f"Part 2: {answer2}")
