package repository

import (
	"context"

	"student-management-system/internal/models"
)

// StudentStore is the seam from week 13: handlers depend on this interface.
// Production: *StudentRepository (pgx). Tests: *FakeStudentStore.
type StudentStore interface {
	Create(ctx context.Context, in models.CreateStudentRequest) (models.Student, error)
	GetAll(ctx context.Context) ([]models.Student, error)
	GetByID(ctx context.Context, id int) (models.Student, error)
	Update(ctx context.Context, id int, in models.CreateStudentRequest) (models.Student, error)
	Delete(ctx context.Context, id int) error
}
