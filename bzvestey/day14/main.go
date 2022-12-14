package day14

import (
	"fmt"
	"strconv"
	"strings"
)

type GameMap struct {
	Grid   map[int]map[int]rune
	SandX  int
	SandY  int
	Left   int
	Right  int
	Bottom int
}

func addPointToMap(gm *GameMap, x, y int, shape rune) {
	_, ok := gm.Grid[y]
	if ok {
		gm.Grid[y][x] = shape
	} else if !ok {
		gm.Grid[y] = map[int]rune{x: shape}
	}

	if x < gm.Left {
		gm.Left = x
	} else if x > gm.Right {
		gm.Right = x
	}
}

func parseData(data string) *GameMap {
	rows := strings.Split(string(data), "\n")
	rows = rows[:len(rows)-1]

	gm := &GameMap{
		Grid:   map[int]map[int]rune{},
		Left:   -1,
		Right:  -1,
		Bottom: -1,
		SandX:  500,
		SandY:  0,
	}

	for _, v := range rows {
		points := strings.Split(v, " -> ")
		lastX := -1
		lastY := -1
		for i, p := range points {
			parts := strings.Split(p, ",")
			x, _ := strconv.Atoi(parts[0])
			y, _ := strconv.Atoi(parts[1])
			addPointToMap(gm, x, y, '#')

			if gm.Left == -1 || x < gm.Left {
				gm.Left = x
			}
			if gm.Right == -1 || x > gm.Right {
				gm.Right = x
			}
			if gm.Bottom == -1 || y > gm.Bottom {
				gm.Bottom = y
			}

			if i != 0 {
				startX, endX := lastX, x
				if x < lastX {
					startX = x
					endX = lastX
				}
				startY, endY := lastY, y
				if y < lastY {
					startY = y
					endY = lastY
				}

				for startX < endX || startY < endY {
					addPointToMap(gm, startX, startY, '#')
					if startX < endX {
						startX++
					}
					if startY < endY {
						startY++
					}
				}
				addPointToMap(gm, startX, startY, '#')
			}
			lastX = x
			lastY = y
		}
	}

	return gm
}

func PrintMap(gm *GameMap) {
	for y := 0; y <= gm.Bottom; y++ {
		row, rok := gm.Grid[y]
		for x := gm.Left; x <= gm.Right; x++ {
			if x == gm.SandX && y == gm.SandY {
				fmt.Print("+")
				continue
			}
			if !rok {
				fmt.Print(".")
				continue
			}
			cell, cok := row[x]
			if !cok {
				fmt.Print(".")
				continue
			}

			fmt.Print(string(cell))
		}
		fmt.Println("")
	}
}

func checkStop(gm *GameMap, x, y int, hasFloor bool) bool {
	if hasFloor && y >= gm.Bottom {
		return false
	}
	row, rok := gm.Grid[y]
	if !rok {
		return true
	}
	_, cok := row[x]
	return !cok
}

func dropSand(gm *GameMap, hasFloor bool) bool {
	x, y := gm.SandX, gm.SandY

	for didMove, i := true, 0; didMove; i++ {
		if !hasFloor && (x < gm.Left || x > gm.Right || y > gm.Bottom) {
			return false
		}

		if checkStop(gm, x, y+1, hasFloor) {
			y++
		} else if checkStop(gm, x-1, y+1, hasFloor) {
			y++
			x--
		} else if checkStop(gm, x+1, y+1, hasFloor) {
			y++
			x++
		} else if i == 0 {
			return false
		} else {
			if i == 0 {

				return false
			}
			addPointToMap(gm, x, y, 'o')
			didMove = false
		}
	}

	return true
}

func RunPart1(data string) int {
	gm := parseData(data)
	count := 0
	for dropSand(gm, false) {
		count++
	}
	return count
}

func RunPart2(data string) int {
	gm := parseData(data)
	count := 1
	gm.Bottom += 2
	for dropSand(gm, true) {
		count++
	}
	return count
}
