package handlers

import "strings"

// FullName joins trimmed first and last names with one space.
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
