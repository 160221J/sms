package validate

import "testing"

func TestValidateStudentSyncOK(t *testing.T) {
	errs := ValidateStudentSync(StudentInput{
		FirstName: "Ada",
		Email:     "ada@example.com",
		Course:    "SE",
	})
	if len(errs) != 0 {
		t.Fatalf("expected no errors, got %v", errs)
	}
}

func TestValidateStudentConcurrentCollects(t *testing.T) {
	errs := ValidateStudentConcurrent(StudentInput{
		FirstName: "",
		Email:     "nope",
		Course:    "",
	})
	if len(errs) < 2 {
		t.Fatalf("expected multiple errors, got %v", errs)
	}
}

func TestValidateStudentConcurrentOK(t *testing.T) {
	errs := ValidateStudentConcurrent(StudentInput{
		FirstName: "Ada",
		Email:     "ada@example.com",
		Course:    "SE",
	})
	if len(errs) != 0 {
		t.Fatalf("expected no errors, got %v", errs)
	}
}
