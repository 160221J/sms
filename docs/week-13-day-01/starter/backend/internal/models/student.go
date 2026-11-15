package models

import (
	"fmt"
	"strings"
	"time"
)

// Student is the in-memory SMS student shape (no DB tags yet).
type Student struct {
	ID          int       `json:"id"`
	FirstName   string    `json:"first_name"`
	LastName    string    `json:"last_name"`
	Email       string    `json:"email"`
	Phone       string    `json:"phone"`
	Course      string    `json:"course"`
	DateOfBirth time.Time `json:"date_of_birth,omitempty"`
	FullName    string    `json:"full_name,omitempty"`
}

// FullNameOf joins trimmed first and last names (week 2/6 rules).
func FullNameOf(first, last string) string {
	first = strings.TrimSpace(first)
	last = strings.TrimSpace(last)
	switch {
	case first == "" && last == "":
		return ""
	case last == "":
		return first
	case first == "":
		return last
	default:
		return first + " " + last
	}
}

// CreateStudentRequest is the POST/PUT body (id assigned by server).
type CreateStudentRequest struct {
	FirstName   string `json:"first_name" binding:"required"`
	LastName    string `json:"last_name"`
	Email       string `json:"email" binding:"required,email"`
	Phone       string `json:"phone"`
	Course      string `json:"course" binding:"required"`
	DateOfBirth string `json:"date_of_birth"` // optional YYYY-MM-DD
}

// ParseDate parses YYYY-MM-DD using Go's reference layout 2006-01-02.
func ParseDate(s string) (time.Time, error) {
	if s == "" {
		return time.Time{}, fmt.Errorf("empty date")
	}
	t, err := time.Parse("2006-01-02", s)
	if err != nil {
		return time.Time{}, fmt.Errorf("invalid date format. Use YYYY-MM-DD")
	}
	return t, nil
}
