package validate

import (
	"fmt"
	"strings"
	"sync"
)

// StudentInput is a tiny request shape for the fan-out kata.
type StudentInput struct {
	FirstName string
	Email     string
	Course    string
	Phone     string
}

func ValidateStudentSync(in StudentInput) []error {
	var errs []error
	if e := checkName(in.FirstName); e != nil {
		errs = append(errs, e)
	}
	if e := checkEmail(in.Email); e != nil {
		errs = append(errs, e)
	}
	if e := checkCourse(in.Course); e != nil {
		errs = append(errs, e)
	}
	return errs
}

// ValidateStudentConcurrent runs three independent checks in parallel.
// For SMS create this is often overkill — learn the pattern, keep product sync.
func ValidateStudentConcurrent(in StudentInput) []error {
	checks := []func(StudentInput) error{
		func(s StudentInput) error { return checkName(s.FirstName) },
		func(s StudentInput) error { return checkEmail(s.Email) },
		func(s StudentInput) error { return checkCourse(s.Course) },
	}

	errCh := make(chan error, len(checks))
	var wg sync.WaitGroup
	wg.Add(len(checks))
	for _, check := range checks {
		check := check
		go func() {
			defer wg.Done()
			if err := check(in); err != nil {
				errCh <- err
			}
		}()
	}
	wg.Wait()
	close(errCh)

	var errs []error
	for err := range errCh {
		errs = append(errs, err)
	}
	return errs
}

func checkName(name string) error {
	if strings.TrimSpace(name) == "" {
		return fmt.Errorf("first_name is required")
	}
	return nil
}

func checkEmail(email string) error {
	if !strings.Contains(email, "@") {
		return fmt.Errorf("email is invalid")
	}
	return nil
}

func checkCourse(course string) error {
	if strings.TrimSpace(course) == "" {
		return fmt.Errorf("course is required")
	}
	return nil
}
