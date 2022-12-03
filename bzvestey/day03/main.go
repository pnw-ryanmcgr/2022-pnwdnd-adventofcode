package main

import (
	_ "embed"
	"fmt"
	"strings"
)

//go:embed input
var input string

func main() {
	runData(input)
}

func runeValue(r rune) int {
	if r >= 'a' && r <= 'z' {
		return int(r) - 96
	}
	return int(r) - 38
}

func runData(data string) {
	rows := strings.Split(string(data), "\n")
	rows = rows[:len(rows)-1]

	var sum1 int = 0

	for _, v := range rows {
		compartment1 := v[:len(v)/2]
		compartment2 := v[len(v)/2:]

		for _, r := range compartment1 {
			if strings.ContainsRune(compartment2, r) {
				sum1 += runeValue(r)
				break
			}
		}
	}

	var sum2 int = 0

	for i := 0; i < len(rows); i += 3 {
		for _, r := range rows[i] {
			if strings.ContainsRune(rows[i+1], r) && strings.ContainsRune(rows[i+2], r) {
				sum2 += runeValue(r)
				break
			}
		}
	}

	fmt.Println("Part 1 Sum:", sum1)
	fmt.Println("Part 2 Sum:", sum2)
}
