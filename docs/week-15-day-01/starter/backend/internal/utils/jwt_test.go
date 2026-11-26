package utils

import "testing"

func TestGenerateAndValidateToken(t *testing.T) {
	SetJWTSecret("test-secret-week-15")
	tok, err := GenerateToken(7, "ada")
	if err != nil {
		t.Fatal(err)
	}
	parsed, err := ValidateToken(tok)
	if err != nil {
		t.Fatal(err)
	}
	if !parsed.Valid {
		t.Fatal("expected valid token")
	}
}

func TestValidateTokenRejectsGarbage(t *testing.T) {
	SetJWTSecret("test-secret-week-15")
	if _, err := ValidateToken("not-a-jwt"); err == nil {
		t.Fatal("expected error")
	}
}
