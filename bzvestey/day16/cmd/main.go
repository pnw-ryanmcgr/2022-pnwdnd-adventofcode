package main

import (
	_ "embed"
	"fmt"

	"github.com/bzvestey/advent_of_code/2022/day16"
)

//go:embed input
var input string

func main() {
	fmt.Println(day16.RunPart2(input))
}
