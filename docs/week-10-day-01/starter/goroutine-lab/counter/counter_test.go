package counter

import "testing"

func TestUnsafeAddRace(t *testing.T) {
	// Run with: go test -race ./counter/
	// Expect a DATA RACE warning. The returned count is often < 1000.
	got := UnsafeAdd(1000)
	t.Logf("got %d (may be less than 1000 under race)", got)
}
