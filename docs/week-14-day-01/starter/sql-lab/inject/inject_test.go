package inject

import (
	"strings"
	"testing"
)

func TestBadLookupEmail_InjectionChangesQuery(t *testing.T) {
	malicious := "x' OR '1'='1"
	q := BadLookupEmail(malicious)
	if !LooksInjected(q) {
		t.Fatalf("expected injection markers in %q", q)
	}
	if !strings.Contains(q, malicious) {
		t.Fatalf("input was not concatenated into query: %q", q)
	}
	t.Logf("BAD query text:\n%s", q)
}

func TestGoodLookupEmail_KeepsPlaceholder(t *testing.T) {
	q, ph := GoodLookupEmail()
	if !strings.Contains(q, ph) {
		t.Fatalf("missing placeholder in %q", q)
	}
	if LooksInjected(q) {
		t.Fatalf("template itself should be clean: %q", q)
	}
	// Argument is passed separately to pgx — never spliced into q.
	arg := "x' OR '1'='1"
	if strings.Contains(q, arg) {
		t.Fatal("argument must not appear inside the SQL template")
	}
}
