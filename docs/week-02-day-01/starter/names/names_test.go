package names

import "testing"

func TestFullName(t *testing.T) {
	got := FullName("Ada", "Lovelace")
	if got != "Ada Lovelace" {
		t.Fatalf("got %q, want %q", got, "Ada Lovelace")
	}

	got = FullName("  Ada  ", "  Lovelace  ")
	if got != "Ada Lovelace" {
		t.Fatalf("trim: got %q, want %q", got, "Ada Lovelace")
	}

	got = FullName("Ada", "   ")
	if got != "Ada" {
		t.Fatalf("empty last: got %q, want %q", got, "Ada")
	}
}
