package parse

import "testing"

func TestParseDate(t *testing.T) {
	cases := []struct {
		name    string
		in      string
		wantOK  bool
		wantDay int // day of month when OK
	}{
		{name: "valid", in: "1995-12-10", wantOK: true, wantDay: 10},
		{name: "new year", in: "2000-01-01", wantOK: true, wantDay: 1},
		{name: "empty", in: "", wantOK: false},
		{name: "wrong shape", in: "10-12-1995", wantOK: false},
		{name: "letters layout mistake", in: "YYYY-MM-DD", wantOK: false},
		{name: "invalid month", in: "1995-13-10", wantOK: false},
	}

	for _, tc := range cases {
		t.Run(tc.name, func(t *testing.T) {
			got, err := ParseDate(tc.in)
			if tc.wantOK {
				if err != nil {
					t.Fatalf("ParseDate(%q) err=%v", tc.in, err)
				}
				if got.Day() != tc.wantDay {
					t.Fatalf("day=%d want %d", got.Day(), tc.wantDay)
				}
				return
			}
			if err == nil {
				t.Fatalf("ParseDate(%q) expected error, got %v", tc.in, got)
			}
		})
	}
}
