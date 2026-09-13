package main

import "fmt"

func main() {
	a := []int{10, 20, 30, 40}
	b := a[:2]
	fmt.Println("before", a, b, "cap(b)=", cap(b))
	b = append(b, 99)
	fmt.Println("after ", a, b)
}
