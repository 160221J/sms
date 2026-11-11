package repository

import (
	"context"
	"fmt"
	"sync"

	"student-management-system/internal/apperrors"
	"student-management-system/internal/models"
)

// StudentRepository stores students in memory (Postgres arrives later).
// Week 12: Mutex protects the map; methods take context.Context (ignored until week 14).
type StudentRepository struct {
	mu       sync.Mutex
	students map[int]models.Student
	nextID   int
}

func NewStudentRepository() *StudentRepository {
	return &StudentRepository{
		students: map[int]models.Student{},
		nextID:   1,
	}
}

func (r *StudentRepository) Create(ctx context.Context, in models.CreateStudentRequest) models.Student {
	_ = ctx
	r.mu.Lock()
	defer r.mu.Unlock()
	s := models.Student{
		ID:        r.nextID,
		FirstName: in.FirstName,
		LastName:  in.LastName,
		Email:     in.Email,
		Phone:     in.Phone,
		Course:    in.Course,
	}
	r.students[s.ID] = s
	r.nextID++
	return s
}

func (r *StudentRepository) GetAll(ctx context.Context) []models.Student {
	_ = ctx
	r.mu.Lock()
	defer r.mu.Unlock()
	out := make([]models.Student, 0, len(r.students))
	for _, s := range r.students {
		out = append(out, s)
	}
	return out
}

func (r *StudentRepository) GetByID(ctx context.Context, id int) (models.Student, error) {
	_ = ctx
	r.mu.Lock()
	defer r.mu.Unlock()
	s, ok := r.students[id]
	if !ok {
		return models.Student{}, fmt.Errorf("student %d: %w", id, apperrors.ErrNotFound)
	}
	return s, nil
}

func (r *StudentRepository) Update(ctx context.Context, id int, in models.CreateStudentRequest) (models.Student, error) {
	_ = ctx
	r.mu.Lock()
	defer r.mu.Unlock()
	if _, ok := r.students[id]; !ok {
		return models.Student{}, fmt.Errorf("student %d: %w", id, apperrors.ErrNotFound)
	}
	s := models.Student{
		ID:        id,
		FirstName: in.FirstName,
		LastName:  in.LastName,
		Email:     in.Email,
		Phone:     in.Phone,
		Course:    in.Course,
	}
	r.students[id] = s
	return s, nil
}

func (r *StudentRepository) Delete(ctx context.Context, id int) error {
	_ = ctx
	r.mu.Lock()
	defer r.mu.Unlock()
	if _, ok := r.students[id]; !ok {
		return fmt.Errorf("student %d: %w", id, apperrors.ErrNotFound)
	}
	delete(r.students, id)
	return nil
}
