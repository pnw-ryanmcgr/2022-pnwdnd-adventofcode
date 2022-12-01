package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	fileName := "./input"
	if len(os.Args) > 1 {
		fileName = os.Args[1]
	}
	data, err := os.ReadFile(fileName)
	if err != nil {
		panic(err)
	}

	runData(string(data))
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
