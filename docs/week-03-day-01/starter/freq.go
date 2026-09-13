package main

import "fmt"

func main() {
	words := []string{"SE", "CS", "SE", "IT", "SE"}
	count := make(map[string]int)
	for _, w := range words {
		count[w]++
	}
	fmt.Println(count)
	n, ok := count["SE"]
	fmt.Println(n, ok)
}
