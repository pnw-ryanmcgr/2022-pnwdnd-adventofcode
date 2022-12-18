package day16

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"
)

type Valve struct {
	Name            string
	IsOpen          bool
	OpenedRemaining int
	Pressure        int
	Connected       []string
}

type ValveMap struct {
	Valves        map[string]*Valve
	NodesToAccess []string
}

var ValveExp = regexp.MustCompile(`[A-Z]{2}`)
var PressureExp = regexp.MustCompile(`\d{1,4}`)

func parseData(data string) *ValveMap {
	rows := strings.Split(string(data), "\n")
	rows = rows[:len(rows)-1]

	vm := ValveMap{Valves: map[string]*Valve{}, NodesToAccess: []string{"AA"}}

	for _, v := range rows {
		valves := ValveExp.FindAllString(v, -1)
		pressureStr := PressureExp.FindString(v)
		pressure, _ := strconv.Atoi(pressureStr)

		valve := &Valve{Name: valves[0], Connected: valves[1:], Pressure: pressure}
		vm.Valves[valves[0]] = valve
		if pressure > 0 {
			vm.NodesToAccess = append(vm.NodesToAccess, valve.Name)
		}
	}

	return &vm
}

func PrintMap(vm *ValveMap) {
	for k, v := range vm.Valves {
		fmt.Println(k, "(", v.Pressure, ")", v.IsOpen, v.OpenedRemaining, v.Connected)
	}

	for i, v := range vm.NodesToAccess {
		fmt.Println(i, v)
	}
}

type Edge struct {
	ToValve string
	Cost    int
}

type Node struct {
	Valve *Valve
	Edges []Edge
	EM    map[string]Edge
}

type PathNode struct {
	Valve    *Valve
	PrevCost int
	Time     int
}

func findQuickestPathBetweenValves(from, to string, vm *ValveMap) Edge {
	nodes := []*PathNode{{Valve: vm.Valves[from], PrevCost: 0}}
	visited := map[string]*PathNode{}

	for len(nodes) > 0 {
		cur := nodes[0]
		nodes = nodes[1:]

		if cur.Valve.Name == to {
			return Edge{ToValve: to, Cost: cur.PrevCost}
		}

		visited[cur.Valve.Name] = cur

		cost := cur.PrevCost + 1
		for _, v := range cur.Valve.Connected {
			pn, ok := visited[v]

			if ok && pn.PrevCost < cost {
				pn.PrevCost = cost
			} else {
				pn := &PathNode{Valve: vm.Valves[v], PrevCost: cost}
				nodes = append(nodes, pn)
				visited[v] = pn
			}
		}
	}

	return Edge{ToValve: to, Cost: 999999}
}

func findHighestPressure1(node *Node, time int, web map[string]*Node, visited []string) (int, []string) {
	if time <= 1 {
		return 0, visited
	}
	highest := 0
	visited = append(visited, node.Valve.Name)
	hv := visited

	for _, e := range node.Edges {
		if contains(visited, e.ToValve) {
			continue
		}

		value, vv := findHighestPressure1(web[e.ToValve], time-e.Cost-1, web, visited)
		if value > highest {
			highest = value
			hv = vv
		}
	}

	return highest + (time * node.Valve.Pressure), hv
}

func contains(l []string, v string) bool {
	for _, t := range l {
		if t == v {
			return true
		}
	}
	return false
}

type Player struct {
	Target *Node
	Steps  int
}

func RemoveIndex(s []string, index int) []string {
	ret := make([]string, 0, len(s)-1)
	ret = append(ret, s[:index]...)
	return append(ret, s[index+1:]...)
}

const COST_MOD = 1
const RUN_2_TIME = 26

type VisitedTime struct {
	Name   string
	Time   int
	Player int
}

func stepThroughTime(p1, p2 Player, flow, flowed, time int, toVisit []string, visited []VisitedTime, web map[string]*Node) int {

	for time < RUN_2_TIME {
		time += 1
		flowed += flow

		if p1.Steps >= 0 {
			p1.Steps--
			if p1.Steps == 0 {
				flow += p1.Target.Valve.Pressure
				visited = append(visited, VisitedTime{Name: p1.Target.Valve.Name, Time: time, Player: 1})
			}
		}

		if p2.Steps >= 0 {
			p2.Steps--
			if p2.Steps == 0 {
				flow += p2.Target.Valve.Pressure
				visited = append(visited, VisitedTime{Name: p2.Target.Valve.Name, Time: time, Player: 2})
			}
		}

		if p1.Steps == 0 || p2.Steps == 0 {
			if len(toVisit) > 0 {
				hf := 0
				if p1.Steps == 0 && p2.Steps == 0 {
					if len(toVisit) == 1 {
						tv := toVisit[0]
						hf = stepThroughTime(
							Player{Target: web[tv], Steps: web[p1.Target.Valve.Name].EM[tv].Cost + COST_MOD}, p2,
							flow, flowed, time, []string{}, visited, web,
						)
						f := stepThroughTime(
							p1, Player{Target: web[tv], Steps: web[p2.Target.Valve.Name].EM[tv].Cost + COST_MOD},
							flow, flowed, time, []string{}, visited, web,
						)
						if f > hf {
							hf = f
						}
					} else {
						for i1, tv1 := range toVisit {
							subToVisit := RemoveIndex(toVisit, i1)
							for i2, tv2 := range subToVisit {
								subToVisit2 := RemoveIndex(subToVisit, i2)
								f := stepThroughTime(
									Player{Target: web[tv1], Steps: web[p1.Target.Valve.Name].EM[tv1].Cost + COST_MOD},
									Player{Target: web[tv2], Steps: web[p2.Target.Valve.Name].EM[tv2].Cost + COST_MOD},
									flow, flowed, time, subToVisit2, visited, web,
								)
								if f > hf {
									hf = f
								}
							}
						}
					}
				} else if p1.Steps == 0 {
					for i, tv := range toVisit {
						f := stepThroughTime(
							Player{Target: web[tv], Steps: web[p1.Target.Valve.Name].EM[tv].Cost + COST_MOD}, p2,
							flow, flowed, time, RemoveIndex(toVisit, i), visited, web,
						)
						if f > hf {
							hf = f
						}
					}
				} else if p2.Steps == 0 {
					for i, tv := range toVisit {
						f := stepThroughTime(
							p1, Player{Target: web[tv], Steps: web[p2.Target.Valve.Name].EM[tv].Cost + COST_MOD},
							flow, flowed, time, RemoveIndex(toVisit, i), visited, web,
						)
						if f > hf {
							hf = f
						}
					}
				}

				return hf
			}
		}
	}

	return flowed
}

func buildWeb(vm *ValveMap) map[string]*Node {
	web := map[string]*Node{}

	for _, v := range vm.NodesToAccess {
		node := &Node{Valve: vm.Valves[v], EM: map[string]Edge{}}
		for _, c := range vm.NodesToAccess {
			if c == v {
				continue
			}
			edge := findQuickestPathBetweenValves(v, c, vm)
			node.Edges = append(node.Edges, edge)
			node.EM[c] = edge
		}
		web[v] = node
	}

	return web
}

func RunPart1(data string) int {
	vm := parseData(data)
	web := buildWeb(vm)
	cost, _ := findHighestPressure1(web["AA"], 30, web, []string{})
	return cost
}

func RunPart2(data string) int {
	vm := parseData(data)
	web := buildWeb(vm)

	return stepThroughTime(
		Player{Target: web["AA"], Steps: 1}, Player{Target: web["AA"], Steps: 1}, 0, 0, -1,
		vm.NodesToAccess[1:], []VisitedTime{}, web,
	)
}
