#!python
""" AOC 2022: Day X """
import pathlib
from typing import List

class File():
    def __init__(self, name, size=0):
        self.name = name
        self.children: List[File] = []
        self.parent: File = self
        self._size = size

    @property
    def size(self):
        if not self.children:
            return self._size
        else:
            return sum([c.size for c in self.children])

    @property
    def path(self):
        if self.parent is not self:
            return "/".join([self.parent.path, self.name])
        else:
            return self.name

def parse(puzzle_input: str):
    """ Parse input """
    root = File("root")
    pwd = root
    dirs = {}

    for line in puzzle_input.splitlines():
        if pwd.path not in dirs:
            dirs[pwd.path] = pwd
        if line.startswith("$ ls"):
            continue
        elif line.startswith("$ cd"):
            dirname = line[5:]
            if dirname == "/":
                pwd = root
            elif dirname =="..":
                pwd = pwd.parent
            else:
                pwd = next(dir for dir in pwd.children if dir.name == dirname)
        elif line.startswith("dir"):
            dirname = line[4:]
            new_dir = File(dirname)
            new_dir.parent = pwd
            pwd.children.append(new_dir)
        else:
            size, filename = line.split(' ')
            new_file = File(filename, int(size))
            pwd.children.append(new_file)

    return root, dirs

def part1(data):
    """ Solve part 1 """
    root, dirs = data
    total = 0
    for _,d in dirs.items():
        if d.size <= 100000:
            total += d.size
    return total

def part2(data):
    """ Solve part 2 """
    root, dirs = data
    max = 70000000
    need = 30000000
    unused = max - root.size
    to_delete = need - unused

    candidates = []
    for _,d in dirs.items():
        if d.size >= to_delete:
            candidates.append(d.size)

    return min(candidates)


def solve(puzzle_input: str) -> tuple:
    """ Parse, solve, return solutions """
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_file = pathlib.Path(__file__).parent.joinpath("input.txt")
    puzzle_text = puzzle_file.read_text(encoding='utf-8').strip()
    answer1, answer2 = solve(puzzle_text)
    print(f"Part 1: {answer1}")
    print(f"Part 2: {answer2}")
