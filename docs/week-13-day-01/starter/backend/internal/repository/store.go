package repository

import (
	"context"

	"student-management-system/internal/models"
)

// StudentStore is the week-13 seam: handlers depend on this interface so tests can inject a fake.
type StudentStore interface {
	Create(ctx context.Context, in models.CreateStudentRequest) models.Student
	GetAll(ctx context.Context) []models.Student
	GetByID(ctx context.Context, id int) (models.Student, error)
	Update(ctx context.Context, id int, in models.CreateStudentRequest) (models.Student, error)
	Delete(ctx context.Context, id int) error
}

// Ensure the in-memory repo satisfies the interface at compile time.
var _ StudentStore = (*StudentRepository)(nil)
