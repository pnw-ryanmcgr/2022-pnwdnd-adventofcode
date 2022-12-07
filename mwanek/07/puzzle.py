#!python
""" AOC 2022: Day X """
import pathlib
class File():
    def __init__(self, name, size=0, parent=None):
        self.name = name
        self.children: list[File] = []
        self.parent: File = parent if parent else self
        self._size = int(size)

    @property
    def size(self):
        if not self.children:
            return self._size
        else:
            return sum([c.size for c in self.children])

def parse(terminal_history: str) -> set[File]:
    pwd = root = File("root")
    viewed_directories = set()

    for line in terminal_history.splitlines():
        if line.startswith("$"):
            command = line.lstrip("$ ").split()
            if command[0] == "ls":
                viewed_directories.add(pwd)
            elif command[0] == "cd":
                dirname = command[1]
                if dirname == "/":
                    pwd = root
                elif dirname =="..":
                    pwd = pwd.parent
                else:
                    pwd = next(dir for dir in pwd.children if dir.name == dirname)
        else:
            if line.startswith("dir"):
                size = 0
                _, name = line.split()
            else:
                size, name = line.split()
            pwd.children.append(File(name, size, pwd))

    return viewed_directories

def part1(directories: set[File]) -> int:
    total = 0
    for directory in directories:
        if directory.size <= 100000:
            total += directory.size
    return total

def part2(directories: set[File]) -> int:
    root = next(d for d in directories if d.name == "root")

    filesystem_max_size = 70000000
    free_space_needed = 30000000
    current_free_space = filesystem_max_size - root.size
    amount_to_delete = free_space_needed - current_free_space

    candidates = []
    for directory in directories:
        if directory.size >= amount_to_delete:
            candidates.append(directory.size)

    return min(candidates)

def solve(puzzle_input: str) -> tuple:
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
