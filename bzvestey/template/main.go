package day10

import (
	"strconv"
	"strings"
)

func runData(data string) int {
	rows := strings.Split(string(data), "\n")
	rows = rows[:len(rows)-1]

	var last int = 0

	for _, v := range rows {
		cur, err := strconv.Atoi(v)
		if err != nil {
			panic(err)
		}

		if last != 0 {
			// do Something
		}

		last = cur
	}

	return last
}

func RunPart1(data string) int {
	return runData(data)
}

func RunPart2(data string) int {
	return runData(data)
}
