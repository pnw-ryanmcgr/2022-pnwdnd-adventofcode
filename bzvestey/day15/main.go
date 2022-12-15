package day15

import (
	"math"
	"regexp"
	"strconv"
	"strings"
)

type BeaconRow = map[int]rune

type BeaconMap = map[int]BeaconRow

func addPointToMap(bm BeaconMap, x, y int, shape rune, addIfUsed bool) BeaconMap {
	_, ok := bm[y]
	if !ok {
		bm[y] = BeaconRow{}
	}

	_, ok = bm[y][x]
	if !ok || addIfUsed {
		bm[y][x] = shape
	}

	return bm
}

func parseData1(data string, line int) BeaconMap {
	rows := strings.Split(string(data), "\n")
	rows = rows[:len(rows)-1]

	bm := BeaconMap{}

	lineParse := regexp.MustCompile(`-?\d+`)

	for _, v := range rows {
		nums := lineParse.FindAllString(v, -1)
		cx, _ := strconv.Atoi(nums[0])
		cy, _ := strconv.Atoi(nums[1])
		ox, _ := strconv.Atoi(nums[2])
		oy, _ := strconv.Atoi(nums[3])

		bm = addPointToMap(bm, cx, cy, 'S', true)
		bm = addPointToMap(bm, ox, oy, 'B', true)

		distance := int(math.Abs(float64(cx-ox)) + math.Abs(float64(cy-oy)))

		minY := cy - distance
		maxY := cy + distance

		if minY > line || maxY < line {
			continue
		}

		dx := (distance - int(math.Abs(float64(cy-line))))
		maxX := cx + dx
		for x := cx - dx; x <= maxX; x++ {
			bm = addPointToMap(bm, x, line, '#', false)
		}
	}

	return bm
}

type Area struct {
	X     int
	Y     int
	Range int
}

func checkAreas(x, y int, areas []Area) bool {
	for _, a := range areas {
		distance := int(math.Abs(float64(x-a.X)) + math.Abs(float64(y-a.Y)))
		if distance <= a.Range {
			return false
		}
	}
	return true
}

func parseData2(data string, size int) int {
	rows := strings.Split(string(data), "\n")
	rows = rows[:len(rows)-1]

	lineParse := regexp.MustCompile(`-?\d+`)
	areas := []Area{}

	for _, v := range rows {
		nums := lineParse.FindAllString(v, -1)
		cx, _ := strconv.Atoi(nums[0])
		cy, _ := strconv.Atoi(nums[1])
		ox, _ := strconv.Atoi(nums[2])
		oy, _ := strconv.Atoi(nums[3])

		distance := int(math.Abs(float64(cx-ox)) + math.Abs(float64(cy-oy)))

		areas = append(areas, Area{X: cx, Y: cy, Range: distance})
	}

	for _, a := range areas {
		maxY := min(size, a.Y+a.Range+1)
		for y := max(0, a.Y-a.Range-1); y <= maxY; y++ {
			dx := (a.Range - int(math.Abs(float64(a.Y-y))))
			minX := a.X - dx - 1
			maxX := a.X + dx + 1

			if minX >= 0 && checkAreas(minX, y, areas) {
				return 4000000*minX + y
			} else if maxX <= size && checkAreas(maxX, y, areas) {
				return 4000000*maxX + y
			}
		}
	}

	return 0
}

func min(l, r int) int {
	return int(math.Min(float64(l), float64(r)))
}

func max(l, r int) int {
	return int(math.Max(float64(l), float64(r)))
}

func RunPart1(data string, line int) int {
	bm := parseData1(data, line)
	count := 0
	for _, r := range bm[line] {
		if r != 'B' {
			count++
		}
	}
	return count
}

func RunPart2(data string, size int) int {
	return parseData2(data, size)
}
