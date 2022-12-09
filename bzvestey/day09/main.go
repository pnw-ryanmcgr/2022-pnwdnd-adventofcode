package main

import (
	_ "embed"
	"fmt"
	"math"
	"strconv"
	"strings"
)

//go:embed input
var input string

func main() {
	runData(input)
}

type Point struct {
	X int
	Y int
}

func (l Point) Add(r Point) Point {
	return Point{X: l.X + r.X, Y: l.Y + r.Y}
}

func visit(p Point, m map[int]map[int]bool) map[int]map[int]bool {
	_, ok := m[p.Y]
	if !ok {
		m[p.Y] = map[int]bool{}
	}
	m[p.Y][p.X] = true
	return m
}

func checkMove(h, t Point) (Point, bool) {
	dx := h.X - t.X
	dy := h.Y - t.Y
	xMove := dx > 1 || dx < -1
	yMove := dy > 1 || dy < -1

	if dx > 2 || dx < -2 || dy > 2 || dy < -2 {
		fmt.Println("MASSIVE MOVE!!!", dx, dy)
	}

	if xMove && yMove {
		t.X += int(math.Round(float64(dx) / 2))
		t.Y += int(math.Round(float64(dy) / 2))
	} else if xMove {
		t.X += int(math.Round(float64(dx) / 2))
		if dy != 0 {
			t.Y += dy
		}
	} else if yMove {
		t.Y += int(math.Round(float64(dy) / 2))
		if dx != 0 {
			t.X += dx
		}
	}

	return t, xMove || yMove
}

func runData(data string) {
	rows := strings.Split(string(data), "\n")
	rows = rows[:len(rows)-1]

	head := Point{}
	tail1 := Point{}
	tail2 := make([]Point, 9)

	visitedH := map[int]map[int]bool{0: {0: true}}
	visited1 := map[int]map[int]bool{0: {0: true}}
	visited2 := map[int]map[int]bool{0: {0: true}}

	for _, v := range rows {
		parts := strings.Split(v, " ")
		movement, _ := strconv.Atoi(parts[1])

		var dir Point
		switch parts[0] {
		case "R":
			dir.X = 1
		case "L":
			dir.X = -1
		case "U":
			dir.Y = -1
		case "D":
			dir.Y = 1
		default:
			fmt.Println("Unknown move:", v)
		}

		for movement > 0 {
			// Setting things up
			movement--
			head = head.Add(dir)
			visitedH = visit(head, visitedH)

			// Movement 1
			nt, moved := checkMove(head, tail1)
			tail1 = nt
			if moved {
				visited1 = visit(tail1, visited1)
			}

			// Movement 2
			prev := head
			for i, t := range tail2 {
				nt, moved := checkMove(prev, t)
				tail2[i] = nt
				prev = nt
				if moved && i == 8 {
					visited2 = visit(nt, visited2)
				}
			}
		}
	}

	numVisited1 := 0
	for _, r := range visited1 {
		numVisited1 += len(r)
	}

	numVisited2 := 0
	for _, r := range visited2 {
		numVisited2 += len(r)
	}

	fmt.Println("Part 1 number tail visited:", numVisited1)
	fmt.Println("Part 2 number tail visited:", numVisited2)
}
