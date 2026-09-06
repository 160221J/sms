package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {
	word := "සිංහල"
	fmt.Printf("bytes=%d runes=%d %q\n",
		len(word), utf8.RuneCountInString(word), word)
	for i, r := range word {
		fmt.Printf("%d %c %U\n", i, r, r)
	}
}
