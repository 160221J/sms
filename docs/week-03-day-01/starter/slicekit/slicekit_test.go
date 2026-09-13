package slicekit

import "testing"

func TestContains(t *testing.T) {
	tests := []struct {
		list []string
		want string
		ok   bool
	}{
		{[]string{"SE", "CS"}, "SE", true},
		{[]string{"SE", "CS"}, "IT", false},
		{nil, "SE", false},
		{[]string{"SE", "SE"}, "SE", true},
	}
	for _, tt := range tests {
		got := Contains(tt.list, tt.want)
		if got != tt.ok {
			t.Fatalf("Contains(%v, %q) = %v, want %v", tt.list, tt.want, got, tt.ok)
		}
	}
}

func TestUnique(t *testing.T) {
	got := Unique([]string{"SE", "CS", "SE", "IT", "CS"})
	want := []string{"SE", "CS", "IT"}
	if len(got) != len(want) {
		t.Fatalf("len=%d want %d (%v)", len(got), len(want), got)
	}
	for i := range want {
		if got[i] != want[i] {
			t.Fatalf("got %v want %v", got, want)
		}
	}
	if len(Unique(nil)) != 0 {
		t.Fatalf("Unique(nil) should be empty")
	}
}

func TestFreq(t *testing.T) {
	got := Freq([]string{"a", "b", "a"})
	if n, ok := got["a"]; !ok || n != 2 {
		t.Fatalf("a: got %d ok=%v", n, ok)
	}
	if n, ok := got["b"]; !ok || n != 1 {
		t.Fatalf("b: got %d ok=%v", n, ok)
	}
	if len(Freq(nil)) != 0 {
		t.Fatalf("Freq(nil) should be empty map")
	}
}
