
"""
Ryan McGregor, 11Dec2022
AOC2022:Day10
https://adventofcode.com/2022/day/10
Note: And another one goes....
"""

from pprint import pprint
from aocd import get_data, submit
import numpy as np

class CRTScreen():
    """Basic object representing a CRT Screen"""
    def __init__(self, command_list):
        """
        Initialize CRTScreen Object
        Input: command_list (list) - list of addx or noop commands
        Output: None
        """
        self.screen = np.full((6,40), '.', dtype=str)
        self.command_list = command_list
        self.render()

    def _check_pixel(self, active_cycle, active_sum):
        """Interal function to check if a pixel should be lit"""
        active_pixel = (int((active_cycle / 40)), int((active_cycle % 40)))
        if abs(active_sum - active_cycle % 40) <= 1:
            self.screen[active_pixel] = "#"

    def render(self):
        """Render entire screen"""
        current_cycle, rolling_sum = 0, 1
        # First two pixels preceed any command
        self._check_pixel(current_cycle, rolling_sum)
        current_cycle += 1
        self._check_pixel(current_cycle, rolling_sum)
        for command in self.command_list:
            # Calculate rolling sum
            print(f'Operation: {command}')
            if 'addx' in command:
                rolling_sum += int(command.replace('addx ', ''))
                for _ in [0,1]:
                    current_cycle += 1
                    self._check_pixel(current_cycle, rolling_sum)
            else:
                current_cycle += 1
                self._check_pixel(current_cycle, rolling_sum)
        print(f'Total Cycles: {current_cycle}')

    def show(self):
        """Show current CRT Screen"""
        np.set_printoptions(linewidth=200)
        print(str(np.array2string(self.screen)).translate({ord(i): None for i in "'[] "}))

    def retrieve_value_at_cycle(self, cycle):
        """
        Retrieves active value for X at a given iteration.
        Input:
            command_list (list): sequence of commands
            number_retrieved (int): the cycle which is to be retrieved
        Output:
            (int): Value of X on cycle provided
        """
        current_idx, current_cycle, rolling_sum = 0, 1, 1
        while True:
            print('======================')
            print(f'Current Cycle: {current_cycle}')
            print(f'Current Index: {current_idx}')
            print(f'Rolling Sum (Start): {rolling_sum}')
            print(f'Current Op: {self.command_list[current_idx]}')
            if current_cycle >= cycle - 1:
                return rolling_sum
            if 'addx' in self.command_list[current_idx]:
                rolling_sum += int(self.command_list[current_idx].replace('addx ', ''))
                current_cycle += 2
            else:
                current_cycle += 1
            # print(f'Rolling Sum (Finish): {rolling_sum}')
            current_idx += 1


if __name__ == '__main__':
    # data = [x for x in TEST_DATA.split('\n') if x != '']
    data = [x for x in get_data(day=10, year=2022).split('\n') if x != '']
    crt_screen = CRTScreen(data)

    # Part A
    answer_a = []
    for cycle_number in [20, 60, 100, 140, 180, 220]:
        answer_a.append(crt_screen.retrieve_value_at_cycle(cycle_number) * cycle_number)
    answer_a = sum(answer_a)
    print(f'Answer_A: {answer_a}')
    # submit(str(answer_a), part="a", day=10, year=2022)

    # Part B
    print('Answer_B:')
    crt_screen.show()
    ## Answer manually retrieved from image
    # submit('RKPJBPLA', part="b", day=10, year=2022)
