package main

import "fmt"

func main() {
	grade := "B"
	switch grade {
	case "A", "B":
		fmt.Println("good")
	default:
		fmt.Println("work")
	}
	for i, r := range "Go" {
		fmt.Printf("%d %c\n", i, r)
	}
}
