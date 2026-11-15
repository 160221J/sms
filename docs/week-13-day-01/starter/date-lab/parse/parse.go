package parse

import (
	"fmt"
	"time"
)

// ParseDate parses a calendar date in YYYY-MM-DD form.
// The layout string must be Go's reference time: 2006-01-02.
func ParseDate(s string) (time.Time, error) {
	if s == "" {
		return time.Time{}, fmt.Errorf("empty date")
	}
	t, err := time.Parse("2006-01-02", s)
	if err != nil {
		return time.Time{}, fmt.Errorf("invalid date %q: use YYYY-MM-DD", s)
	}
	return t, nil
}
