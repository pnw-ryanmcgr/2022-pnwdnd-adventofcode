package day17

import (
	"fmt"
	"strings"
)

const MAP_WIDTH = 7
const START_LEFT = 2
const START_BOTTOM = 3
const CLEANUP_STEP = 1000000

var PIECES = [][][]rune{
	{
		{'#', '#', '#', '#'},
	},
	{
		{'.', '#', '.'},
		{'#', '#', '#'},
		{'.', '#', '.'},
	},
	{
		{'.', '.', '#'},
		{'.', '.', '#'},
		{'#', '#', '#'},
	},
	{
		{'#'},
		{'#'},
		{'#'},
		{'#'},
	},
	{
		{'#', '#'},
		{'#', '#'},
	},
}

type Movement = []int
type BoardRow = []rune
type Board = map[int]BoardRow

func parseData(data string) Movement {
	rows := strings.Split(string(data), "\n")
	rows = rows[:len(rows)-1]

	m := Movement{}

	for _, v := range rows[0] {
		switch v {
		case '<':
			m = append(m, -1)
		case '>':
			m = append(m, 1)
		}
	}

	return m
}

func checkMove(piece, x, y int, b Board) bool {
	p := PIECES[piece]
	maxY := y + len(p) - 1
	maxX := x + len(p[0]) - 1
	if y < 0 || x < 0 || maxX >= MAP_WIDTH {
		return false
	}

	for py := 0; py < len(p); py++ {
		if _, ok := b[maxY-py]; !ok {
			continue
		}
		for px := 0; px < len(p[0]); px++ {
			if p[py][px] != '#' {
				continue
			}
			if b[maxY-py][x+px] != rune(0) {
				return false
			}
		}
	}

	// TODO: Check Board
	return true
}

func PrintBoard(b Board) {
	// for y := 3100; y >= 0; y-- {
	// 	if _, ok := b[y]; !ok {
	// 		continue
	// 	}
	// 	for x := 0; x < MAP_WIDTH; x++ {
	// 		p, ok := b[y][x]
	// 		if !ok {
	// 			fmt.Print(".")
	// 		} else {
	// 			fmt.Print(string(p))
	// 		}
	// 	}
	// 	fmt.Println("")
	// }
}

func cleanBoard(b Board, highest int) Board {
	newBot := highest - 10000

	nb := Board{}
	for y := newBot; y <= highest; y++ {
		row, ok := b[y]
		if ok {
			nb[y] = row
		}
	}

	return nb
}

func checkMapHeight(m Movement, numRocksToStop int) int {
	numPiecesLanded := 0

	curPiece := 0
	curLeftX := START_LEFT
	curBotY := START_BOTTOM
	curMovement := 0
	numMovement := len(m)
	numPieces := len(PIECES)
	maxY := 0

	b := Board{}

	for numPiecesLanded < numRocksToStop {
		nextLeftX := curLeftX + m[curMovement]
		nextBotY := curBotY - 1

		curMovement++
		if curMovement >= numMovement {
			curMovement -= numMovement
		}

		if checkMove(curPiece, nextLeftX, curBotY, b) {
			curLeftX = nextLeftX
		}

		if checkMove(curPiece, curLeftX, nextBotY, b) {
			curBotY = nextBotY
			continue
		}

		numPiecesLanded++

		nextMaxY := curBotY + len(PIECES[curPiece]) - 1
		if nextMaxY > maxY {
			maxY = nextMaxY
		}

		for py := 0; py < len(PIECES[curPiece]); py++ {
			y := nextMaxY - py
			_, ok := b[y]
			if !ok {
				b[y] = make(BoardRow, MAP_WIDTH)
			}
			for px := 0; px < len(PIECES[curPiece][0]); px++ {
				if PIECES[curPiece][py][px] == '#' {
					switch curPiece {
					case 0:
						b[y][px+curLeftX] = '-'
					case 1:
						b[y][px+curLeftX] = '+'
					case 2:
						b[y][px+curLeftX] = 'L'
					case 3:
						b[y][px+curLeftX] = 'I'
					case 4:
						b[y][px+curLeftX] = 'O'
					default:
						fmt.Println("INVALID PIECE!!!!")
					}
				}
			}
		}

		curLeftX = START_LEFT
		curBotY = maxY + START_BOTTOM + 1

		curPiece++
		if curPiece >= numPieces {
			curPiece -= numPieces
		}

		if numPiecesLanded > 0 && numPiecesLanded%CLEANUP_STEP == 0 {
			oldLength := len(b)
			b = cleanBoard(b, maxY)
			if numPiecesLanded%100000000 == 0 {
				fmt.Printf(
					"%d (%2f) pieces have landed. Row cleanup %d -> %d\n",
					numPiecesLanded,
					float64(numPiecesLanded)/float64(numRocksToStop)*100,
					oldLength,
					len(b),
				)
			}
		}
	}

	return maxY + 1
}

func RunPart1(data string) int {
	m := parseData(data)
	return checkMapHeight(m, 2022)
}

func RunPart2(data string) int {
	m := parseData(data)
	return checkMapHeight(m, 1000000000000)
}
