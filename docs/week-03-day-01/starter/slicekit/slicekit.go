package slicekit

// Contains reports whether want appears in list.
func Contains(list []string, want string) bool {
	for _, v := range list {
		if v == want {
			return true
		}
	}
	return false
}

// Unique returns values in first-seen order.
func Unique(list []string) []string {
	seen := make(map[string]bool)
	out := make([]string, 0, len(list))
	for _, v := range list {
		if seen[v] {
			continue
		}
		seen[v] = true
		out = append(out, v)
	}
	return out
}

// Freq counts occurrences of each word.
func Freq(words []string) map[string]int {
	count := make(map[string]int)
	for _, w := range words {
		count[w]++
	}
	return count
}
