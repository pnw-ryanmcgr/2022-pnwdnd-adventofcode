package day12

import (
	_ "embed"
	"sort"
	"strings"
)

type Node struct {
	Height int
	Left   *Node
	Right  *Node
	Top    *Node
	Bottom *Node

	Visited  bool
	Prev     *Node
	PrevCost int
}

func parseMap(data string) (*Node, *Node, []*Node) {
	rows := strings.Split(string(data), "\n")
	rows = rows[:len(rows)-1]

	nodes := []*Node{}
	var start *Node = nil
	var end *Node = nil

	for ri, row := range rows {
		for ci, c := range row {
			n := &Node{PrevCost: -1}

			switch c {
			case 'S':
				n.Height = 0
				start = n
				n.PrevCost = 0
			case 'E':
				n.Height = 25
				end = n
			default:
				n.Height = int(c - 'a')
			}

			if ri > 0 {
				top := nodes[((ri-1)*len(row))+ci]
				n.Top = top
				top.Bottom = n
			}
			if ci > 0 {
				left := nodes[(ri*len(row))+(ci-1)]
				n.Left = left
				left.Right = n
			}

			nodes = append(nodes, n)
		}
	}

	return start, end, nodes
}

func findShortestRoute(start, end *Node) *Node {
	nodes := []*Node{start}

	for len(nodes) > 0 {
		cur := nodes[0]
		nodes = nodes[1:]

		if cur == end {
			return end
		}

		if cur.Visited {
			continue
		}

		cur.Visited = true

		toCheck := []*Node{cur.Top, cur.Bottom, cur.Left, cur.Right}

		for _, n := range toCheck {
			if n == nil {
				continue
			}

			if n.Height-cur.Height > 1 {
				continue
			}

			h := cur.PrevCost + (25 - n.Height)

			if n.PrevCost == -1 {
				n.PrevCost = h
				n.Prev = cur
				nodes = append(nodes, n)
			} else if h < n.PrevCost {
				n.PrevCost = h
				n.Prev = cur
			}
		}

		sort.Slice(nodes, func(left, right int) bool {
			return nodes[left].PrevCost < nodes[right].PrevCost
		})
	}

	return nil
}

func getLength(end *Node) int {
	length := -1
	cur := end
	for cur != nil {
		length++
		cur = cur.Prev
	}
	return length
}

func RunPart1(data string) int {
	start, end, _ := parseMap(data)
	return getLength(findShortestRoute(start, end))
}

func RunPart2(data string) int {
	_, end, nodes := parseMap(data)

	allLowest := []*Node{}
	for _, n := range nodes {
		if n.Height == 0 {
			allLowest = append(allLowest, n)
		}
	}

	shortest := 2147483647
	for _, start := range allLowest {
		for _, n := range nodes {
			if n == start {
				n.PrevCost = 0
			} else {
				n.PrevCost = -1
			}
			n.Prev = nil
			n.Visited = false
		}

		target := findShortestRoute(start, end)
		length := getLength(target)

		if length > -1 && length < shortest {
			shortest = length
		}
	}

	return shortest
}
