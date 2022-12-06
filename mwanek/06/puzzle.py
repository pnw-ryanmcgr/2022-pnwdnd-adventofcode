#!python
""" AOC 2022: Day 6 """
import pathlib
from collections import deque

def solve(data):
    start_packet_buffer = deque(maxlen=4)
    start_message_buffer = deque(maxlen=14)
    start_packet_index = None
    start_message_index = None

    for i,char in enumerate(data):

        if not start_packet_index:
            start_packet_buffer.append(char)
            if len(set(start_packet_buffer)) == 4:
                start_packet_index = i + 1

        if not start_message_index:
            start_message_buffer.append(char)
            if len(set(start_message_buffer)) == 14:
                start_message_index = i + 1

    return start_packet_index, start_message_index

if __name__ == "__main__":
    puzzle_file = pathlib.Path(__file__).parent.joinpath("input.txt")
    puzzle_text = puzzle_file.read_text(encoding='utf-8').strip()
    answer1, answer2 = solve(puzzle_text)
    print(f"Part 1: {answer1}")
    print(f"Part 2: {answer2}")
