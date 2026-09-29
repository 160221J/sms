package handlers

import "testing"

func TestFullName(t *testing.T) {
	tests := []struct {
		first, last, want string
	}{
		{"Ada", "Lovelace", "Ada Lovelace"},
		{"  Ada  ", "  Lovelace  ", "Ada Lovelace"},
		{"Ada", "   ", "Ada"},
		{"", "Lovelace", "Lovelace"},
	}
	for _, tt := range tests {
		got := FullName(tt.first, tt.last)
		if got != tt.want {
			t.Fatalf("FullName(%q,%q)=%q want %q", tt.first, tt.last, got, tt.want)
		}
	}
}
