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
    def __init__(self, rucksack_line):
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
        items = list({x for x in self.compartment_1 if x in self.compartment_2})
        value = [x[0] + 1 for x in enumerate(list(VALID_ITEMS)) if x[1] in items]
        return [(items[x], value[x]) for x in range(len(items))]

class ElfGroup():
    """Basic object to handle a group of elves"""
    def __init__(self, group_members):
        """
        Initializer
        Input: group_members (list(str))
        Output: none
        """
        self.members = []
        for _member in group_members:
            self.members.append(Rucksack(_member))

    @property
    def badge(self):
        """Interpret/provide the group's badge"""
        badge = [x for x in self.members[0].rucksack_line
                 if x in self.members[1].rucksack_line and
                    x in self.members[2].rucksack_line]
        badge_value = [x[0] + 1 for x in enumerate(list(VALID_ITEMS)) if x[1] in badge]
        return (badge[0], badge_value[0])

if __name__ == '__main__':
    data = get_data(day=3, year=2022).split('\n')
    all_elves = data.copy()
    answer_a, answer_b = 0, 0
    elf_groups = []
    for group in [all_elves[i:i + 3] for i in range(0, len(all_elves), 3)]:
        elf_groups.append(ElfGroup(group))
    for group in elf_groups:
        print('======================')
        print(f'Group members: {[x.rucksack_line for x in group.members]}')
        print(f'Badge: {group.badge}')
        answer_b += group.badge[1]
        for member in group.members:
            print('===========')
            print(f'Whole Line: {member.rucksack_line}')
            print(f'Chunk A: {member.compartment_1}')
            print(f'Chunk B: {member.compartment_2}')
            print(f'Shared Items/ Value: {member.shared_items}')
            for item in member.shared_items:
                answer_a += item[1]
    ## Submit Answer
    # submit(answer_a, part="a", day=3, year=2022)
    # submit(answer_b, part="b", day=3, year=2022)
