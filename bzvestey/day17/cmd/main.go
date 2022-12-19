package main

import (
	_ "embed"
	"fmt"

	"github.com/bzvestey/advent_of_code/2022/day17"
)

//go:embed test1
var test1 string

//go:embed input
var input string

const T1P2_EXPECTED int = 1514285714288
const INPUT_P2_EXPECTED = 11756

func main() {
	t1p2 := day17.RunPart2(test1)
	fmt.Println("Test data 1 Question part 2 received", t1p2)
	if t1p2 != T1P2_EXPECTED {
		fmt.Printf("Test data 1 Question Part 2 received %d when it should have been %d\n", t1p2, T1P2_EXPECTED)
	}
	inputP2 := day17.RunPart2(input)
	fmt.Println("Input data Question part 2 received", inputP2)
	if inputP2 != INPUT_P2_EXPECTED {
		fmt.Printf("Input data Question Part 2 received %d when it should have been %d\n", inputP2, INPUT_P2_EXPECTED)
	}
}
