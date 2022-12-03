"""
Ryan McGregor, 03Dec2022
AOC2022:Day03
https://adventofcode.com/2022/day/3
"""

from pprint import pprint
from aocd import get_data, submit

TEST_DATA = """GwrhJPDJCZFRcwfZWV
LjnQlqNpjjmpmQlLlqNfZRvQcTWcTSTTZcSQcZ
nNqjdspspngnmjmslqmjjjCDGrHPHMGddGCMCGPPPJWC
GwmVZmPWWFFmBbVbZVwmbPsTCnlgQgnQfhlffffZnlQh
DqVDSqqSMzLLDDNSHHLdqSdSllCQjsTlClhlflnTlhjgfgfM
VHJztNLHGtcbvvPG
bjrPrNCtNrjdcCPpptfpTVspDtfTtB"""

VALID_ITEMS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Rucksack():
    """Basic object to handle a single rucksack"""
    def __init__(self,rucksack_line):
        """
        Initializer
        Input: rucksack_line (str)
        Output: none
        """
        self.rucksack_line = rucksack_line ## May not need
        self.compartment_1 = list(rucksack_line[:int(len(rucksack_line)/2)])
        self.compartment_2 = list(rucksack_line[int(len(rucksack_line)/2):])

    @property
    def shared_items(self):
        """Provide the items shared between both compartments"""
        items = list(set([x for x in self.compartment_1 if x in self.compartment_2]))
        value = [x[0] + 1 for x in enumerate(list(VALID_ITEMS)) if x[1] in items ]
        return [(items[x], value[x]) for x in range(len(items))]

if __name__ == '__main__':
    data = get_data(day=3, year=2022).split('\n')
    answer_a = 0
    for line in data:
        rucksack = Rucksack(line)
        print('===========')
        print(f'Whole Line: {rucksack.rucksack_line}')
        print(f'Chunk A: {rucksack.compartment_1}')
        print(f'Chunk B: {rucksack.compartment_2}')
        print(f'Shared Items/ Value: {rucksack.shared_items}')
        for item in rucksack.shared_items:
            answer_a += item[1]
    print(f'Total: {answer_a}')

    ## Submit Answer
    # submit(answer_a, part="a", day=3, year=2022)
    # submit(total_score_b, part="b", day=3, year=2022)
