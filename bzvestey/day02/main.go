package day02

import (
	_ "embed"
	"strings"
)

const (
	ROCK int = iota + 1
	PAPER
	SCISSORS
	LOSE
	DRAW
	WIN
)

type Play struct {
	Opponent int
	Player   int
	Strategy int
}

func opponentDecode(play string) int {
	switch play {
	case "A":
		return ROCK
	case "B":
		return PAPER
	case "C":
		return SCISSORS
	}
	return 0
}

func playerDecode(play string) int {
	switch play {
	case "X":
		return ROCK
	case "Y":
		return PAPER
	case "Z":
		return SCISSORS
	}
	return 0
}
func strategyDecode(play string) int {
	switch play {
	case "X":
		return LOSE
	case "Y":
		return DRAW
	case "Z":
		return WIN
	}
	return 0
}

func calcScore1Play(player, opponent int) int {
	var score int = 0

	switch player {
	case ROCK:
		score += 1
		switch opponent {
		case ROCK:
			score += 3
			break
		case PAPER:
			break
		case SCISSORS:
			score += 6
			break
		}
		break
	case PAPER:
		score += 2
		switch opponent {
		case ROCK:
			score += 6
			break
		case PAPER:
			score += 3
			break
		case SCISSORS:
			break
		}
		break
	case SCISSORS:
		score += 3
		switch opponent {
		case ROCK:
			break
		case PAPER:
			score += 6
			break
		case SCISSORS:
			score += 3
			break
		}
		break
	}

	return score
}

func calcScore2Play(strategy, opponent int) int {
	var score int = 0
	switch strategy {
	case LOSE:
		switch opponent {
		case ROCK:
			score += 3
			break
		case PAPER:
			score += 1
			break
		case SCISSORS:
			score += 2
			break
		}
		break
	case DRAW:
		score += 3
		switch opponent {
		case ROCK:
			score += 1
			break
		case PAPER:
			score += 2
			break
		case SCISSORS:
			score += 3
			break
		}
		break
	case WIN:
		score += 6
		switch opponent {
		case ROCK:
			score += 2
			break
		case PAPER:
			score += 3
			break
		case SCISSORS:
			score += 1
			break
		}
	}
	return score
}

func runData(data string) []Play {
	rows := strings.Split(string(data), "\n")
	rows = rows[:len(rows)-1]

	plays := []Play{}
	for _, v := range rows {
		parts := strings.Split(v, " ")
		plays = append(plays, Play{
			Opponent: opponentDecode(parts[0]),
			Player:   playerDecode(parts[1]),
			Strategy: strategyDecode(parts[1]),
		})
	}

	return plays

	// var score1 int64 = 0
	// var score2 int64 = 0

	// for _, play := range plays {
	// 	score1 += calcScore1Play(play.Player, play.Opponent)
	// 	score2 += calcScore2Play(play.Strategy, play.Opponent)
	// }

	// fmt.Println("Part 1:", score1)
	// fmt.Println("Part 2:", score2)
}

func RunPart1(data string) int {
	plays := runData(data)
	var score int = 0
	for _, play := range plays {
		score += calcScore1Play(play.Player, play.Opponent)
	}
	return score
}

func RunPart2(data string) int {
	plays := runData(data)
	var score int = 0
	for _, play := range plays {
		score += calcScore2Play(play.Strategy, play.Opponent)
	}
	return score
}
