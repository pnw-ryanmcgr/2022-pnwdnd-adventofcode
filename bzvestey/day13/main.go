package day13

import (
	"sort"
	"strconv"
	"strings"
)

type Data struct {
	IsList bool
	Value  int
	Array  []Data
}

type DataPair struct {
	Left  *Data
	Right *Data
}

func isCorrectOrder(left, right *Data) int {
	if !left.IsList && !right.IsList {
		if left.Value < right.Value {
			return 1
		} else if left.Value > right.Value {
			return -1
		} else {
			return 0
		}
	}

	if left.IsList && right.IsList {
		for i := 0; i < len(left.Array); i++ {
			if i == len(right.Array) {
				return -1
			}

			answer := isCorrectOrder(&left.Array[i], &right.Array[i])
			if answer != 0 {
				return answer
			}
		}

		if len(left.Array) < len(right.Array) {
			return 1
		}
		return 0
	}

	if !left.IsList && right.IsList {
		return isCorrectOrder(&Data{IsList: true, Array: []Data{*left}}, right)
	}
	if left.IsList && !right.IsList {
		return isCorrectOrder(left, &Data{IsList: true, Array: []Data{*right}})
	}

	return 0
}

func parseData(line string, offset int) (*Data, int) {
	data := &Data{Value: -1, Array: []Data{}, IsList: true}

	for i := offset + 1; i < len(line); i++ {
		switch line[i] {
		case '[':
			d, ni := parseData(line, i)
			i = ni
			data.Array = append(data.Array, *d)
		case ']':
			return data, i
		case ',':
			continue
		default:
			ci := strings.IndexAny(line[i:], ",]")
			v, _ := strconv.Atoi(line[i : i+ci])
			data.Array = append(data.Array, Data{Value: v})
			i += ci - 1
		}
	}

	return data, len(line)
}

func parseDataPairs(data string) []DataPair {
	rows := strings.Split(string(data), "\n")
	rows = rows[:len(rows)-1]

	dataPairs := []DataPair{}

	for i := 0; i < len(rows); i += 3 {
		left, _ := parseData(rows[i], 0)
		right, _ := parseData(rows[i+1], 0)
		dataPairs = append(dataPairs, DataPair{Left: left, Right: right})
	}

	return dataPairs
}

func RunPart1(data string) int {
	pairs := parseDataPairs(data)
	count := 0
	for i, p := range pairs {
		if isCorrectOrder(p.Left, p.Right) >= 0 {
			count += i + 1
		}
	}
	return count
}

func RunPart2(data string) int {
	pairs := parseDataPairs(data)
	two := &Data{IsList: true, Array: []Data{{Value: 2}}}
	six := &Data{IsList: true, Array: []Data{{Value: 6}}}
	list := []*Data{two, six}
	for _, p := range pairs {
		list = append(list, p.Left, p.Right)
	}

	twoIndex, sixIndex := 0, 0
	sort.Slice(list, func(left, right int) bool {
		return isCorrectOrder(list[left], list[right]) > 0
	})
	for i, d := range list {
		if d == two {
			twoIndex = i + 1
		}
		if d == six {
			sixIndex = i + 1
		}
	}

	return twoIndex * sixIndex
}
