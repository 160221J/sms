package models

import "testing"

func TestFullNameOf(t *testing.T) {
	cases := []struct {
		name  string
		first string
		last  string
		want  string
	}{
		{name: "ada", first: "Ada", last: "Lovelace", want: "Ada Lovelace"},
		{name: "trim", first: "  Ada  ", last: "  Lovelace  ", want: "Ada Lovelace"},
		{name: "empty last", first: "Ada", last: "   ", want: "Ada"},
		{name: "empty first", first: "  ", last: "Lovelace", want: "Lovelace"},
		{name: "both empty", first: " ", last: "", want: ""},
	}
	for _, tc := range cases {
		t.Run(tc.name, func(t *testing.T) {
			if got := FullNameOf(tc.first, tc.last); got != tc.want {
				t.Fatalf("FullNameOf(%q,%q)=%q want %q", tc.first, tc.last, got, tc.want)
			}
		})
	}
}

func TestParseDate(t *testing.T) {
	cases := []struct {
		name   string
		in     string
		wantOK bool
	}{
		{name: "valid", in: "1995-12-10", wantOK: true},
		{name: "empty", in: "", wantOK: false},
		{name: "bad", in: "10/12/1995", wantOK: false},
	}
	for _, tc := range cases {
		t.Run(tc.name, func(t *testing.T) {
			_, err := ParseDate(tc.in)
			if tc.wantOK && err != nil {
				t.Fatalf("err=%v", err)
			}
			if !tc.wantOK && err == nil {
				t.Fatal("expected error")
			}
		})
	}
}
