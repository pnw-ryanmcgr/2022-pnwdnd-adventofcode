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

type CleaningArea struct {
	Start int64
	End   int64
}

func parseCleaningAreaPair(line string) (CleaningArea, CleaningArea) {
	areas := strings.Split(line, ",")
	area1 := strings.Split(areas[0], "-")
	area2 := strings.Split(areas[1], "-")

	ca1 := CleaningArea{}
	ca2 := CleaningArea{}

	ca1.Start, _ = strconv.ParseInt(area1[0], 10, 64)
	ca1.End, _ = strconv.ParseInt(area1[1], 10, 64)
	ca2.Start, _ = strconv.ParseInt(area2[0], 10, 64)
	ca2.End, _ = strconv.ParseInt(area2[1], 10, 64)

	return ca1, ca2
}

func runData(data string) {
	rows := strings.Split(string(data), "\n")
	rows = rows[:len(rows)-1]

	var count1 int = 0
	var count2 int = 0

	for _, v := range rows {
		ca1, ca2 := parseCleaningAreaPair(v)

		if (ca1.Start <= ca2.Start && ca1.End >= ca2.End) || (ca2.Start <= ca1.Start && ca2.End >= ca1.End) {
			count1++
			count2++
		} else if (ca1.Start >= ca2.Start && ca1.Start <= ca2.End) || (ca1.End >= ca2.Start && ca1.End <= ca2.End) {
			count2++
		}
	}

	fmt.Println("Part 1 Count:", count1)
	fmt.Println("Part 2 Count:", count2)
}
