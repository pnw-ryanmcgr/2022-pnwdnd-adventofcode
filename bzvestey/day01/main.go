package day01

import (
	"sort"
	"strconv"
	"strings"
)

type Elf struct {
	Index    int
	Calories int
}

func runData(data string) []Elf {
	rows := strings.Split(string(data), "\n")
	rows = rows[:len(rows)-1]

	var currentElf int = 0
	var currentCount int = 0
	var elves = []Elf{}

	for _, v := range rows {
		if len(v) == 0 {
			elves = append(elves, Elf{Index: currentElf, Calories: currentCount})

			currentElf++
			currentCount = 0
		} else {
			cur, err := strconv.Atoi(v)
			if err != nil {
				panic(err)
			}

			currentCount += cur
		}
	}

	elves = append(elves, Elf{Index: currentElf, Calories: currentCount})

	sort.Slice(elves, func(left, right int) bool {
		return elves[left].Calories > elves[right].Calories
	})

	return elves
}

func RunPart1(data string) int {
	elves := runData(data)
	return elves[0].Calories
}

func RunPart2(data string) int {
	elves := runData(data)
	return elves[0].Calories + elves[1].Calories + elves[2].Calories
}
