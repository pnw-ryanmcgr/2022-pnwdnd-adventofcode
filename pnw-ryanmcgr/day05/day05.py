"""
Ryan McGregor, 05Dec2022
AOC2022:Day05
https://adventofcode.com/2022/day/5
"""

from pprint import pprint
import yaml
from aocd import get_data, submit

## Data manually cleaned for sanity sake.

class ContainerStack:
    """Basic object to handle a stack of containers"""
    def __init__(self, initial_stacks):
        """
        Initializer
        Input: initial_stack ([[A],[B,C]])
        Output: None
        """
        self.stacks = initial_stacks

    def move_container_sequential(self, command):
        """
        Move a set of containers from one stack to another, one at a time
        Input: command [num_boxes, from_stack, to_stack]
        Output: updated self.stack
        """
        for container in range(0, int(command[0])):
            self.stacks[command[2] - 1].append(self.stacks[command[1] - 1].pop())
        return self.stacks

    def move_container_bundle(self, command):
        """
        Move a set of containers from one stack to another, one at a time
        Input: command [num_boxes, from_stack, to_stack]
        Output: updated self.stack
        """
        quantity = -1 * command[0]
        # print(quantity)
        # print(f'from: {self.stacks[command[1] - 1]}')
        # print(f'to: {self.stacks[command[2] - 1]}')
        self.stacks[command[2] - 1] = self.stacks[command[2] - 1] + self.stacks[command[1] - 1][quantity:]
        del self.stacks[command[1] - 1][quantity:]
        # print(f'from: {self.stacks[command[1] - 1]}')
        # print(f'to: {self.stacks[command[2] - 1]}')
        return self.stacks

if __name__ == '__main__':
    with open('./stacks.yaml', 'r') as file:
        data = yaml.safe_load(file)

    pprint(data['stacks'])
    container_stack_a = ContainerStack(data['stacks'])
    print('===== ANSWER A =====')
    # print('Original Stacks')
    # print('===============')
    # pprint(container_stack_a.stacks)
    for command in data['commands']:
        container_stack_a.move_container_sequential(command)
    # print('Final Stacks')
    # print('===============')
    # pprint(container_stack_a.stacks)
    answer_a = ''.join([x[-1] for x in container_stack_a.stacks])
    print(f'Answer A: {answer_a}')
    # submit(answer_a, part="a", day=5, year=2022)

    pprint(data['stacks'])
    container_stack_b = ContainerStack(data['stacks'])
    print('===== ANSWER B =====')
    # print('Original Stacks')
    # print('===============')
    # pprint(container_stack_b.stacks)
    # pprint(container_stack_b.move_container_bundle(data['commands'][0]))
    for command in data['commands']:
        container_stack_b.move_container_bundle(command)
    # print('Final Stacks')
    # print('===============')
    # pprint(container_stack_b.stacks)
    answer_b = ''.join([x[-1] for x in container_stack_b.stacks])
    print(f'Answer B: {answer_b}')
    # submit(answer_b, part="b", day=5, year=2022)
