"""
Ryan McGregor, 04Dec2022
AOC2022:Day04
https://adventofcode.com/2022/day/4
"""

from pprint import pprint
from aocd import get_data, submit

TEST_DATA = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

class ElfPair():
    """Basic object to handle pairs of elves"""
    def __init__(self, elf_pair):
        """
        Initializer
        Input: elf_pair (list(tuple,tuple))
        Output: none
        """
        self.pair = elf_pair
        self.elf_a = range(int(self.pair[0][0]), int(self.pair[0][1]) + 1)
        self.elf_b = range(int(self.pair[1][0]), int(self.pair[1][1]) + 1)

    @property
    def fully_contained(self):
        """Returns True if one set fully contains another"""
        if ((len([x for x in self.elf_a if x not in self.elf_b]) == 0) or
            (len([x for x in self.elf_b if x not in self.elf_a]) == 0)):
            return True
        return False

    @property
    def overlapping(self):
        """Returns True if sets overlap at all"""
        if len([x for x in self.elf_a if x in self.elf_b]) != 0:
            return True
        return False

if __name__ == '__main__':
    data = [x for x in get_data(day=4, year=2022).split('\n') if x]
    # data = [x for x in TEST_DATA.split('\n') if x]
    pairs = []
    answer_a, answer_b = 0, 0
    for line in data:
        pair = ElfPair([tuple(x.split('-')) for x in line.split(',')])
        pairs.append(pair)
        print('===========')
        print(f'Pair: {pair.pair}')
        # print(f'Elf A: {pair.elf_a}')
        # print(f'Elf B: {pair.elf_b}')
        print(f'Contained: {pair.fully_contained}')
        print(f'Overlapping: {pair.overlapping}')
        if pair.fully_contained:
            answer_a += 1
        if pair.overlapping:
            answer_b += 1
    print('=-=-=-=-=-=-=-=-=-=-=')
    print(f'Total Pairs: {len(pairs)}')
    print(f'Totally Contained: {answer_a}')
    print(f'Overlapping: {answer_b}')
    ## Submit Answer
    # submit(answer_a, part="a", day=4, year=2022)
    # submit(answer_b, part="b", day=4, year=2022)
