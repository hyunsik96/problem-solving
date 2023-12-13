package main

import (
	"bufio"
	"fmt"
	"os"
)

func main173() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var s string
	var open, ans int
	for i := 1; ; i++ {
		fmt.Fscanln(reader, &s)
		// - : 45
		if s[0] == 45 {
			break
		}
		open = 0
		ans = 0
		for _, num := range s {
			// { : 123
			if num == 123 {
				open++
			} else {
				if open < 1 {
					ans++
					open++
				} else {
					open--
				}
			}
		}
		ans += open / 2
		fmt.Fprintf(writer, "%d. %d\n", i, ans)
	}
}
