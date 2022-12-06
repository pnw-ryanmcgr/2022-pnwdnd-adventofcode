"""
Ryan McGregor, 06Dec2022
AOC2022:Day06
https://adventofcode.com/2022/day/6
"""

from pprint import pprint
from aocd import get_data, submit

TEST_DATA = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

def find_marker(msg, marker_len):
    """
    Finds the marker in a message
    Input:
        msg - message (str)
        marker_len - number of distinct characters identifying a marker (int)
    Output:
        idx - index of last item in marker set (int)
    """
    for idx, _ in enumerate(msg):
        if idx >= marker_len - 1:
            test_set = set(msg[idx-(marker_len-1):idx+1])
            if len(test_set) == marker_len:
                return int(idx)
    return None

if __name__ == '__main__':
    # data = TEST_DATA
    data = get_data(day=6, year=2022)
    answer_a = find_marker(data, 4) + 1
    answer_b = find_marker(data, 14) + 1

    print(f'Answer_A: {answer_a}')
    print(f'Answer_B: {answer_b}')

    # submit(answer_a, part="a", day=6, year=2022)
    # submit(answer_b, part="b", day=6, year=2022)
