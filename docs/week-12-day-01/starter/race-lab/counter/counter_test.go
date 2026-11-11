package counter

import "testing"

func TestSafeAdd(t *testing.T) {
	const n = 100
	got := SafeAdd(n)
	if got != n {
		t.Fatalf("SafeAdd(%d) = %d, want %d", n, got, n)
	}
}

// TestUnsafeAddDocumentsRace is skipped by default so `go test -race ./...` stays green.
// To demo the FAIL on the projector:
//
//	go test -race -run TestUnsafeAddDocumentsRace ./counter/
func TestUnsafeAddDocumentsRace(t *testing.T) {
	t.Skip("enable to demo DATA RACE on projector; then use SafeAdd")
	_ = UnsafeAdd(100)
}
