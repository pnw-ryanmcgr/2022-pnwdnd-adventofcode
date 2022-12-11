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

func updateSignalStrengthSum(cycle, x int) int {
	if (cycle-20)%40 == 0 {
		return x * cycle
	}
	return 0
}

func updateScreen(cycle, x int, screen []rune) []rune {
	min, max := x-1, x+1
	pos := (cycle) % 40

	if pos >= min && pos <= max {
		screen[cycle] = '#'
	}
	return screen
}

func runData(data string) {
	rows := strings.Split(string(data), "\n")
	rows = rows[:len(rows)-1]

	var signalStrengthSum1 int = 0
	var x1 int = 1

	screen2 := make([]rune, 240)
	for i := 0; i < 240; i++ {
		screen2[i] = '.'
	}

	cycle := 0
	for _, v := range rows {
		screen2 = updateScreen(cycle, x1, screen2)
		cycle++
		signalStrengthSum1 += updateSignalStrengthSum(cycle, x1)

		if v != "noop" {
			screen2 = updateScreen(cycle, x1, screen2)
			cycle++
			signalStrengthSum1 += updateSignalStrengthSum(cycle, x1)

			parts := strings.Split(v, " ")
			value, _ := strconv.Atoi(parts[1])
			x1 += value
		}

	}

	fmt.Println("Part 1 Signal Strength Sum:", signalStrengthSum1)
	fmt.Println("Part 2 Word:")
	for i := 0; i < 6; i++ {
		fmt.Println(string(screen2[i*40 : 40+(i*40)]))
	}
}
