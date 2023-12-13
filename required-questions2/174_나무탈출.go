package main

import (
	"bufio"
	"fmt"
	"os"
)

func main174() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var n int
	fmt.Fscanln(reader, &n)

	graph := make([][]int, n+1)
	var a, b int = 0, 0
	for i := 0; i < n-1; i++ {
		a, b = 0, 0
		fmt.Fscanln(reader, &a, &b)
		graph[a] = append(graph[a], b)
		graph[b] = append(graph[b], a)
	}
	visited := make([]bool, n+1)
	visited[1] = true
	que := [][2]int{{1, 0}}
	var total int
	for len(que) != 0 {
		num, count := que[0][0], que[0][1]
		que = que[1:]
		if len(graph[num]) == 1 && num != 1 {
			total += count
		} else {
			for _, next := range graph[num] {
				if !visited[next] {
					que = append(que, [2]int{next, count + 1})
					visited[next] = true
				}
			}
		}
	}
	if total%2 == 1 {
		fmt.Fprintln(writer, "Yes")
	} else {
		fmt.Fprintln(writer, "No")
	}
}
