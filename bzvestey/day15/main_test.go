package day15

import (
	_ "embed"
	"fmt"
	"testing"
)

//go:embed test1
var test1 string

//go:embed input
var input string

const T1P1_EXPECTED = 26
const T1P2_EXPECTED = 56000011
const INPUT_P1_EXPECTED = 4873353
const INPUT_P2_EXPECTED = 11600823139120

func TestPart1(t *testing.T) {
	t1p1 := RunPart1(test1, 10)
	fmt.Println("Test data 1 Question part 1 received", t1p1)
	if t1p1 != T1P1_EXPECTED {
		t.Fatalf("Test data 1 Question Part 1 received %d when it should have been %d", t1p1, T1P1_EXPECTED)
	}
	inputP1 := RunPart1(input, 2000000)
	fmt.Println("Input data Question part 1 received", inputP1)
	if inputP1 != INPUT_P1_EXPECTED {
		t.Fatalf("Input data Question Part 1 received %d when it should have been %d", inputP1, INPUT_P1_EXPECTED)
	}
}

func TestPart2(t *testing.T) {
	t1p2 := RunPart2(test1, 20)
	fmt.Println("Test data 1 Question part 2 received", t1p2)
	if t1p2 != T1P2_EXPECTED {
		t.Fatalf("Test data 1 Question Part 2 received %d when it should have been %d", t1p2, T1P2_EXPECTED)
	}
	inputP2 := RunPart2(input, 4000000)
	fmt.Println("Input data Question part 2 received", inputP2)
	if inputP2 != INPUT_P2_EXPECTED {
		t.Fatalf("Input data Question Part 2 received %d when it should have been %d", inputP2, INPUT_P2_EXPECTED)
	}
}
