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

const max_size = 100000
const fs_size = 70000000
const space_needed = 30000000

type File struct {
	Name     string
	Size     int
	Parent   *File
	Children []*File
}

func runData(data string) {
	rows := strings.Split(string(data), "\n")
	rows = rows[:len(rows)-1]

	root := File{}
	var currentDir *File
	allSizeUnderMaxSize := 0

	for _, v := range rows {
		parts := strings.Split(v, " ")

		switch parts[0] {
		case "$":
			if parts[1] == "cd" {
				switch parts[2] {
				case "/":
					currentDir = &root
				case "..":
					for _, c := range currentDir.Children {
						currentDir.Size += c.Size
					}
					if currentDir.Size <= max_size {
						allSizeUnderMaxSize += currentDir.Size
					}
					currentDir = currentDir.Parent
				default:
					for _, c := range currentDir.Children {
						if c.Name == parts[2] {
							currentDir = c
							break
						}
					}
				}
			}
		case "dir":
			currentDir.Children = append(currentDir.Children, &File{
				Name:     parts[1],
				Size:     0,
				Parent:   currentDir,
				Children: []*File{},
			})
		default:
			size, _ := strconv.Atoi(parts[0])
			currentDir.Children = append(currentDir.Children, &File{
				Name:     parts[1],
				Size:     size,
				Parent:   currentDir,
				Children: []*File{},
			})
		}
	}

	for currentDir != nil {
		for _, c := range currentDir.Children {
			currentDir.Size += c.Size
		}
		if currentDir.Size <= max_size {
			allSizeUnderMaxSize += currentDir.Size
		}
		currentDir = currentDir.Parent
	}

	sizeOfDirToDelete := space_needed - (fs_size - root.Size)

	fmt.Println("Part 1 All Size Under Max Size:", allSizeUnderMaxSize)
	fmt.Println("Part 2 Amount To Delete:", findDirToDelete(&root, sizeOfDirToDelete))
}

func findDirToDelete(dir *File, spaceNeeded int) int {
	amountToDelete := dir.Size

	for _, c := range dir.Children {
		if len(c.Children) == 0 || c.Size < spaceNeeded {
			continue
		}

		size := findDirToDelete(c, spaceNeeded)
		if size < amountToDelete {
			amountToDelete = size
		}
	}

	return amountToDelete
}
