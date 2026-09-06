package main

import (
	"flag"
	"fmt"
	"strings"
)

func FullName(first, last string) string {
	first = strings.TrimSpace(first)
	last = strings.TrimSpace(last)
	if first == "" {
		return last
	}
	if last == "" {
		return first
	}
	return first + " " + last
}

func main() {
	first := flag.String("first", "", "first name")
	last := flag.String("last", "", "last name")
	flag.Parse()
	fmt.Println(FullName(*first, *last))
}
