"""
Ryan McGregor, 10DEC2022
AOC2022:Day11
https://adventofcode.com/2022/day/11
Note: Time to catch up :-)....
"""

from pprint import pprint
from aocd import get_data, submit
import yaml
import numpy
from datetime import datetime

class Monkeys():
    """Basic object to manage a group of monkeys"""
    def __init__(self, monkeys, destress):
        """
        Initialize Monkey group object
        Input:
          monkey.monkeys (list(monkey)): list of all the monkeys in a group.
        Outpost: None
        """
        self.monkeys = []
        for monkey in monkeys:
            self.monkeys.append(Monkey(self, monkey, destress))

class Monkey():
    """Basic object to represent a monkey"""
    def __init__(self, monkey_group, monkey, destress):
        """
        Initialize Monkey object
        Input:
          monkey.start_items (list): Initial populater of self.contents
          monkey.operation (tuple(str, int)): Operation performed to be performed
              against an object in a monkey's inventory
          monkey.test (int): Number monkey checks if item is divisible by
          monkey.true_state (int): Monkey that this monkey will
              pass the object to if test is true
          monkey.false_state (int): Monkey that this monkey will
              pass the object to if test is false
        Outpost: None
        """
        self.destress = destress
        self.inspections = 0
        self.monkey_group = monkey_group
        self.inventory = monkey['starting_items'].copy()
        self.operation = monkey['operation']
        self.test = monkey['test']
        self.true_state = monkey['true_state']
        self.false_state = monkey['false_state']

    def send(self, old_number, new_number, recipient):
        """Sends item to another monkey"""
        for _ in range(0, self.inventory.count(old_number)):
            self.monkey_group.monkeys[recipient].inventory.append(new_number)
            self.inspections += 1
            self.inventory.remove(old_number)

    def operate(self, number):
        """Operate on a single item in the monkey's inventory"""
        if self.operation['operand'] == 'old':
            operand = number
        else:
            operand = self.operation['operand']
        match self.operation['operator']:
            case "multiply":
                new_number = operand * number
            case "add":
                new_number = operand + number

        # Apply De-stress (Part A)
        if self.destress:
            new_number = int(new_number / 3)

        if new_number % self.test == 0:
            self.send(number, new_number, self.true_state)
        else:
            self.send(number, new_number, self.false_state)

    def loop(self):
        """Loop over a monkey's inventory"""
        for item in set(self.inventory):
            self.operate(item)

if __name__ == '__main__':
    with open('./data.yml', 'r', encoding="utf-8") as file:
        data = yaml.safe_load(file)

    # Answer A
    group_of_monkeys_a = Monkeys(data, destress=True)
    for _ in range(0, 20):
        for monkey in group_of_monkeys_a.monkeys:
            monkey.loop()
    answer_a = numpy.prod(sorted([monkey.inspections for monkey in group_of_monkeys_a.monkeys])[-2:])
    print(f'Answer_A: {answer_a}')
    # submit(answer_a, part="a", day=11, year=2022)

    # Answer B
    startTime = datetime.now()
    timeLast = startTime
    print(f'Start Time: {startTime}')
    group_of_monkeys_b = Monkeys(data, destress=False)
    for i in range(0, 10000):
        if i % 10 == 0:
            timeNow = datetime.now()
            print('=============================')
            print(f'Interation: {i}')
            print(f'Last 10 interations time: {timeNow - startTime}')
            print(f'Time since start: {timeNow - timeLast}')
            print(f'Current Monkeys:')
            pprint([x.inventory for x in group_of_monkeys_b.monkeys])
            timeLast = timeNow
        for monkey in group_of_monkeys_b.monkeys:
            monkey.loop()
    answer_b = numpy.prod(sorted([monkey.inspections for monkey in group_of_monkeys_b.monkeys])[-2:])
    print(f'Answer_b: {answer_b}')

    # print(f'Answer_B: {answer_b}')

    # submit(answer_b, part="b", day=7, year=2022)
