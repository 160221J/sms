package main

import "fmt"

func main() {
	var seats int
	var label string
	var open bool
	fmt.Printf("zeroes: %d %q %t\n", seats, label, open)

	celsius := 33
	fmt.Println(float64(celsius)*9/5 + 32)
}
