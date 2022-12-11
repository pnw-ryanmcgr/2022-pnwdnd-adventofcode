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

type Monkey struct {
	Items       []int64
	OpType      string
	OpValue     int64
	TestValue   int64
	TrueMonkey  int
	FalseMonkey int
	ItemsTossed int64
}

func runData(data string) {
	rows := strings.Split(string(data), "\n")
	rows = rows[:len(rows)-1]

	monkeys1 := []Monkey{}
	monkeys2 := []Monkey{}

	for i := 0; i < len(rows); i += 7 {
		monkey := Monkey{}

		items := strings.Split(strings.TrimSpace(strings.Split(rows[i+1], ": ")[1]), ", ")
		for _, i := range items {
			item, _ := strconv.ParseInt(i, 10, 64)
			monkey.Items = append(monkey.Items, item)
		}

		opParts := strings.Split(rows[i+2], " ")
		if opParts[len(opParts)-1] == "old" {
			monkey.OpType = "^"
		} else {
			monkey.OpType = opParts[len(opParts)-2]
			opValue, _ := strconv.ParseInt(opParts[len(opParts)-1], 10, 64)
			monkey.OpValue = opValue
		}

		testParts := strings.Split(rows[i+3], " ")
		testValue, _ := strconv.ParseInt(testParts[len(testParts)-1], 10, 64)
		monkey.TestValue = testValue

		trueParts := strings.Split(rows[i+4], " ")
		trueMonkey, _ := strconv.Atoi(trueParts[len(trueParts)-1])
		monkey.TrueMonkey = trueMonkey

		falseParts := strings.Split(rows[i+5], " ")
		falseMonkey, _ := strconv.Atoi(falseParts[len(falseParts)-1])
		monkey.FalseMonkey = falseMonkey

		monkeys1 = append(monkeys1, monkey)
		monkeys2 = append(monkeys2, monkey)
	}

	fmt.Println("Part 1 Monkey Business: ", test(monkeys1, 3, 20))
	fmt.Println("Part 2 Monkey Business: ", test(monkeys2, 1, 10000))
}

func test(monkeys []Monkey, div int64, rounds int) int64 {
	// Because the number gets too big in 10000 rounds when not dividing, we need
	// to use the lowest common multiple of the test values to keep the stored
	// worry level down.
	var lcm int64 = 1
	for _, m := range monkeys {
		lcm *= m.TestValue
	}
	for r := 0; r < rounds; r++ {
		for mi, m := range monkeys {
			items := m.Items
			monkeys[mi].Items = []int64{}
			monkeys[mi].ItemsTossed += int64(len(items))
			for _, i := range items {
				worry := i

				switch m.OpType {
				case "^":
					worry *= worry
				case "*":
					worry *= m.OpValue
				case "+":
					worry += m.OpValue
				}

				if div > 1 {
					worry /= div
				}
				worry %= lcm

				if worry%m.TestValue == 0 {
					monkeys[m.TrueMonkey].Items = append(monkeys[m.TrueMonkey].Items, worry)
				} else {
					monkeys[m.FalseMonkey].Items = append(monkeys[m.FalseMonkey].Items, worry)
				}
			}
		}
	}

	var l11, l12 int64 = 0, 0
	for _, m := range monkeys {
		if m.ItemsTossed > l11 {
			l12 = l11
			l11 = m.ItemsTossed
		} else if m.ItemsTossed > l12 {
			l12 = m.ItemsTossed
		}
	}

	return l11 * l12
}
