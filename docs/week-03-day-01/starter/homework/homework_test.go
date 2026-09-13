package homework

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
	}
	for _, tt := range tests {
		if got := Contains(tt.list, tt.want); got != tt.ok {
			t.Fatalf("Contains(%v, %q)=%v want %v", tt.list, tt.want, got, tt.ok)
		}
	}
}

func TestUnique(t *testing.T) {
	got := Unique([]string{"SE", "CS", "SE", "IT", "CS"})
	want := []string{"SE", "CS", "IT"}
	if len(got) != len(want) {
		t.Fatalf("got %v want %v", got, want)
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
		t.Fatalf("a: %d ok=%v", n, ok)
	}
	if n, ok := got["b"]; !ok || n != 1 {
		t.Fatalf("b: %d ok=%v", n, ok)
	}
	if len(Freq(nil)) != 0 {
		t.Fatalf("Freq(nil) should be empty map")
	}
}

func TestFilter(t *testing.T) {
	got := Filter([]string{"SE", "CS", "SE"}, "SE")
	if len(got) != 2 || got[0] != "SE" || got[1] != "SE" {
		t.Fatalf("got %v", got)
	}
	if len(Filter([]string{"SE", "CS"}, "IT")) != 0 {
		t.Fatalf("expected empty")
	}
}

func TestMax(t *testing.T) {
	n, ok := Max([]int{3, 9, 4})
	if !ok || n != 9 {
		t.Fatalf("got %d ok=%v", n, ok)
	}
	if _, ok := Max(nil); ok {
		t.Fatalf("nil should be not ok")
	}
	if _, ok := Max([]int{}); ok {
		t.Fatalf("empty should be not ok")
	}
}

func TestReverse(t *testing.T) {
	in := []int{1, 2, 3}
	got := Reverse(in)
	want := []int{3, 2, 1}
	if len(got) != 3 || got[0] != 3 || got[1] != 2 || got[2] != 1 {
		t.Fatalf("got %v want %v", got, want)
	}
	if in[0] != 1 || in[2] != 3 {
		t.Fatalf("Reverse mutated input: %v", in)
	}
	_ = want
}

func TestIntersection(t *testing.T) {
	got := Intersection([]string{"SE", "CS", "IT"}, []string{"IT", "SE", "SE"})
	want := []string{"SE", "IT"}
	if len(got) != len(want) {
		t.Fatalf("got %v want %v", got, want)
	}
	for i := range want {
		if got[i] != want[i] {
			t.Fatalf("got %v want %v", got, want)
		}
	}
	if len(Intersection([]string{"SE"}, []string{"CS"})) != 0 {
		t.Fatalf("expected empty")
	}
}

func TestGrade(t *testing.T) {
	tests := map[int]string{80: "A", 70: "B", 55: "C", 10: "F", -1: "?", 101: "?"}
	for score, want := range tests {
		if got := Grade(score); got != want {
			t.Fatalf("Grade(%d)=%q want %q", score, got, want)
		}
	}
}
