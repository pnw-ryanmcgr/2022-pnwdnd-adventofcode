"""
Ryan McGregor, 08Dec2022
AOC2022:Day07
https://adventofcode.com/2022/day/7
Note: Already falling behind....
"""

from pprint import pprint
from aocd import get_data, submit

TEST_DATA = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

class FileSystem():
    """
    Not-So-Basic object to handle filesystem metadata, built from a
    list of commands and responses from a directory crawl.
    """
    def __init__(self, command_history):
        """
        Processes a list of commands and their returns.
        Input: Big ol' list of commands and their associated response
        Output: None
        """
        for command in command_history:



if __name__ == '__main__':
    data = TEST_DATA.split('\n')
    # data = get_data(day=7, year=2022)

    # print(f'Answer_A: {answer_a}')
    # print(f'Answer_B: {answer_b}')

    # submit(answer_a, part="a", day=7, year=2022)
    # submit(answer_b, part="b", day=7, year=2022)
