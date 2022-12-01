package main

import (
	_ "embed"
	"fmt"
	"sort"
	"strconv"
	"strings"
)

//go:embed input
var input string

func main() {
	runData(input)
}

type Elf struct {
	Index    int
	Calories int
}

func runData(data string) {
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

	sort.Slice(elves, func(left, right int) bool {
		return elves[left].Calories > elves[right].Calories
	})

	fmt.Println("Top Elf:", elves[0].Index, " | Calories", elves[0].Calories)
	fmt.Println("Top 3 elves calories:", elves[0].Calories+elves[1].Calories+elves[2].Calories)
}