package apperrors

import "errors"

// ErrNotFound is returned when a requested entity does not exist.
var ErrNotFound = errors.New("not found")

// ErrConflict is returned when creating a duplicate (e.g. username).
var ErrConflict = errors.New("conflict")
