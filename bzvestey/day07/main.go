package day07

import (
	_ "embed"
	"strconv"
	"strings"
)

//go:embed input
var input string

const max_size = 100000
const fs_size = 70000000
const space_needed = 30000000

type File struct {
	Name     string
	Size     int
	Parent   *File
	Children []*File
}

func calcDirSizeAndGetParent(dir *File) *File {
	for _, c := range dir.Children {
		dir.Size += c.Size
	}
	return dir.Parent
}

func createDirectoryStructure(data string) *File {
	rows := strings.Split(string(data), "\n")
	rows = rows[:len(rows)-1]

	root := File{}
	var currentDir *File

	for _, v := range rows {
		parts := strings.Split(v, " ")

		switch parts[0] {
		case "$":
			if parts[1] == "cd" {
				switch parts[2] {
				case "/":
					currentDir = &root
				case "..":
					currentDir = calcDirSizeAndGetParent(currentDir)
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
		currentDir = calcDirSizeAndGetParent(currentDir)
	}

	return &root
}

func calcAllUnderMaxSize(dir *File, maxSize int) int {
	total := 0
	if dir.Size <= maxSize {
		total += dir.Size
	}

	for _, c := range dir.Children {
		if len(c.Children) > 0 {
			total += calcAllUnderMaxSize(c, maxSize)
		}
	}

	return total
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

func RunPart1(data string) int {
	root := createDirectoryStructure(data)
	return calcAllUnderMaxSize(root, max_size)
}

func RunPart2(data string) int {
	root := createDirectoryStructure(data)
	sizeOfDirToDelete := space_needed - (fs_size - root.Size)
	return findDirToDelete(root, sizeOfDirToDelete)
}
