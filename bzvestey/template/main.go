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

func runData(data string) {
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

	fmt.Println("Last:", last)
}
