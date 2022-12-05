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

type Move struct {
	Count int
	From  int
	To    int
}

func runData(data string) {
	rows := strings.Split(string(data), "\n")
	rows = rows[:len(rows)-1]

	// [P]     [C]         [M]
	// [D]     [P] [B]     [V] [S]
	// [Q] [V] [R] [V]     [G] [B]
	// [R] [W] [G] [J]     [T] [M]     [V]
	// [V] [Q] [Q] [F] [C] [N] [V]     [W]
	// [B] [Z] [Z] [H] [L] [P] [L] [J] [N]
	// [H] [D] [L] [D] [W] [R] [R] [P] [C]
	// [F] [L] [H] [R] [Z] [J] [J] [D] [D]
	// 1   2   3   4   5   6   7   8   9

	stacks1 := map[int]string{
		1: "FHBVRQDP",
		2: "LDZQWV",
		3: "HLZQGRPC",
		4: "RDHFJVB",
		5: "ZWLC",
		6: "JRPNTGVM",
		7: "JRLVMBS",
		8: "DPJ",
		9: "DCNWV",
	}

	stacks2 := map[int]string{
		1: "FHBVRQDP",
		2: "LDZQWV",
		3: "HLZQGRPC",
		4: "RDHFJVB",
		5: "ZWLC",
		6: "JRPNTGVM",
		7: "JRLVMBS",
		8: "DPJ",
		9: "DCNWV",
	}

	moves := []Move{}

	pastMap := false

	for _, v := range rows {
		if !pastMap {
			if v == "" {
				fmt.Println("Past Map")
				pastMap = true
			}
			continue
		}

		parts := strings.Split(v, " ")
		move := Move{}

		move.Count, _ = strconv.Atoi(parts[1])
		move.From, _ = strconv.Atoi(parts[3])
		move.To, _ = strconv.Atoi(parts[5])

		moves = append(moves, move)
	}

	for _, m := range moves {
		loc1 := len(stacks1[m.From]) - m.Count
		stacks1[m.To] += reverse(stacks1[m.From][loc1:])
		stacks1[m.From] = stacks1[m.From][:loc1]

		loc2 := len(stacks2[m.From]) - m.Count
		stacks2[m.To] += stacks2[m.From][loc2:]
		stacks2[m.From] = stacks2[m.From][:loc2]
	}

	fmt.Println(stacks1)

	topOfstacks1 := []rune{}
	topOfstacks2 := []rune{}
	for i := 1; i < 10; i++ {
		s1 := stacks1[i]
		topOfstacks1 = append(topOfstacks1, []rune(s1)[len(s1)-1])
		s2 := stacks2[i]
		topOfstacks2 = append(topOfstacks2, []rune(s2)[len(s2)-1])
	}

	fmt.Println("Part one top of stacks1: ", string(topOfstacks1))
	fmt.Println("Part one top of stacks2: ", string(topOfstacks2))
}

func reverse(s string) string {
	working := []rune(s)
	for i, j := 0, len(working)-1; i < j; i, j = i+1, j-1 {
		working[i], working[j] = working[j], working[i]
	}
	return string(working)
}
