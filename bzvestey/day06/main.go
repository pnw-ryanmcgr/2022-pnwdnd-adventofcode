package main

import (
	_ "embed"
	"fmt"
	"strings"
)

//go:embed input
var input string

func main() {
	runData(input)
}

func checkForMarker(section string) bool {
	lastIndex := len(section) - 1
	for p, r := range section {
		if strings.Count(section, string(r)) > 1 {
			break
		}
		if p == lastIndex {
			return true
		}
	}
	return false
}

func runData(data string) {
	var firstEndOfStartOfPacket int = 0
	var firstEndOfStartOfMessage int = 0

	for i := 3; i < len(data); i++ {
		if firstEndOfStartOfPacket == 0 {
			if checkForMarker(data[i-3 : i+1]) {
				firstEndOfStartOfPacket = i + 1
			}
		}

		if i >= 13 && firstEndOfStartOfMessage == 0 {
			if checkForMarker(data[i-13 : i+1]) {
				firstEndOfStartOfMessage = i + 1
			}
		}
	}

	fmt.Println("Part 1 First Start-of-Packet marker:", firstEndOfStartOfPacket)
	fmt.Println("Part 2 First Start-of-Message marker:", firstEndOfStartOfMessage)
}
