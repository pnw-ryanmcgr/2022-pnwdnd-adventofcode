package main

import (
	_ "embed"
	"fmt"
	"strconv"
	"strings"
)

//go:embed input
var input string

func main() {
	runData(input)
}

type Tree struct {
	Height       int
	Score        int
	NorthVisible bool
	EastVisible  bool
	WestVisible  bool
	SouthVisible bool
}

func calcVertScore(ri, ci, direction int, f [][]*Tree) int {
	count := 0
	for i := ri + direction; i >= 0 && i < len(f); i += direction {
		count++
		if f[ri][ci].Height <= f[i][ci].Height {
			break
		}
	}
	return count
}

func calcHorizScore(ri, ci, direction int, f [][]*Tree) int {
	count := 0
	for i := ci + direction; i >= 0 && i < len(f[0]); i += direction {
		count++
		if f[ri][ci].Height <= f[ri][i].Height {
			break
		}
	}
	return count
}

func calcScore(ri, ci int, f [][]*Tree) int {
	// score := 1
	score := calcVertScore(ri, ci, -1, f)
	score *= calcHorizScore(ri, ci, -1, f)
	score *= calcHorizScore(ri, ci, 1, f)
	score *= calcVertScore(ri, ci, 1, f)
	return score
}

func runData(data string) {
	rows := strings.Split(string(data), "\n")
	rows = rows[:len(rows)-1]

	forest := [][]*Tree{}
	numVisibleTrees := 0
	topScenicScore := 0

	lastRow := len(rows) - 1
	lastCol := len(rows[0]) - 1
	tallestWest := make([]int, len(rows))
	tallestNorth := make([]int, len(rows[0]))
	for ri, r := range rows {
		row := make([]*Tree, len(r))

		for ci, t := range r {
			tree := &Tree{}
			tree.Height, _ = strconv.Atoi(string(t))
			row[ci] = tree

			if ri == 0 {
				tree.NorthVisible = true
			}

			if ci == 0 {
				tree.WestVisible = true
			}

			if ri == lastRow {
				tree.SouthVisible = true
			}

			if ci == lastCol {
				tree.EastVisible = true
			}

			if tree.Height > tallestNorth[ci] {
				tree.NorthVisible = true
				tallestNorth[ci] = tree.Height
			}

			if tree.Height > tallestWest[ri] {
				tree.WestVisible = true
				tallestWest[ri] = tree.Height
			}
		}

		forest = append(forest, row)
	}

	tallestEast := make([]int, len(rows))
	tallestSouth := make([]int, len(rows[0]))
	for ri := lastRow; ri >= 0; ri-- {
		for ci := lastCol; ci >= 0; ci-- {
			tree := forest[ri][ci]

			if tree.Height > tallestSouth[ci] {
				tree.SouthVisible = true
				tallestSouth[ci] = tree.Height
			}

			if tree.Height > tallestEast[ri] {
				tree.EastVisible = true
				tallestEast[ri] = tree.Height
			}

			if tree.EastVisible || tree.NorthVisible || tree.SouthVisible || tree.WestVisible {
				numVisibleTrees++
			}

			tree.Score = calcScore(ri, ci, forest)
			if tree.Score > topScenicScore {
				topScenicScore = tree.Score
			}
		}
	}

	fmt.Println("Part 1 Num Visible Trees:", numVisibleTrees)
	fmt.Println("Part 2 Top Scenic Score:", topScenicScore)
}
