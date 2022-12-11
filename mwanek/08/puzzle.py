#!python
""" AOC 2022: Day 8 """
import pathlib

def parse(puzzle_input: str) -> tuple[tuple[int], tuple[int], int]:
    rows = []

    for line in puzzle_input.splitlines():
        rows.append(tuple(int(i) for i in line))

    return tuple(rows), tuple(zip(*rows)), len(rows[0])

def visible_tree_indexes(treeline: tuple[int]) -> tuple[int]:
    visible_trees = []

    for i,tree_height in enumerate(treeline):
        if i == 0 or tree_height > highest_seen:
            highest_seen = tree_height
            visible_trees.append(i)
        if tree_height == 9:
            break

    return tuple(visible_trees)

def part1(forest: tuple) -> int:
    rows, columns, forest_size = forest
    visible = set()
    rev = lambda n: abs(n-forest_size+1)

    for i in range(forest_size):
        visible.update(     #from the west:
            set((x, i) for x in visible_tree_indexes(rows[i]))
        )
        visible.update(     #from the north:
            set((i, y) for y in visible_tree_indexes(columns[i]))
        )
        visible.update(     #from the east:
            set((rev(x), i) for x in visible_tree_indexes(reversed(rows[i])))
        )
        visible.update(      #from the east
            set((i, rev(y)) for y in visible_tree_indexes(reversed(columns[i])))
        )

    return(len(visible))

def part2(forest: tuple) -> int:
    rows, columns, forest_size = forest
    highest_scenic_score = 0

    for x in range(1, forest_size-1):
        for y in range(1, forest_size-1):
            views = (
                rows[y][x+1:], #right
                rows[y][x-1::-1], #left
                columns[x][y+1:], #above
                columns[x][y-1::-1] #below
            )
            my_tree = columns[x][y]
            scenic_score = 1
            for view in views:
                scenic_score *= next(
                    (i+1 for i,height in enumerate(view) if height>=my_tree),
                    len(view)
                )
            if scenic_score > highest_scenic_score:
                highest_scenic_score = scenic_score

    return highest_scenic_score

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
