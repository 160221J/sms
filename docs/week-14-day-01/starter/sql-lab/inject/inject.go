package inject

import "strings"

// BadLookupEmail builds SQL by concatenating user input (NEVER do this in the app).
func BadLookupEmail(email string) string {
	return "SELECT id, email FROM students WHERE email = '" + email + "'"
}

// GoodLookupEmail is the shape you use with pgx: placeholder + separate arg.
func GoodLookupEmail() (query string, placeholder string) {
	return "SELECT id, email FROM students WHERE email = $1", "$1"
}

// LooksInjected is a tiny detector for the classroom demo (not a security scanner).
func LooksInjected(sql string) bool {
	u := strings.ToUpper(sql)
	return strings.Contains(u, " OR ") || strings.Contains(u, "--") || strings.Contains(u, ";")
}
