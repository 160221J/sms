package repository

import (
	"context"
	"fmt"
	"sync"

	"student-management-system/internal/apperrors"
	"student-management-system/internal/models"
)

// FakeStudentStore is an in-memory test double (still used for unit tests without Postgres).
type FakeStudentStore struct {
	mu       sync.Mutex
	students map[int]models.Student
	nextID   int
	Creates  int
}

func NewFakeStudentStore() *FakeStudentStore {
	return &FakeStudentStore{
		students: map[int]models.Student{},
		nextID:   1,
	}
}

var _ StudentStore = (*FakeStudentStore)(nil)

func (f *FakeStudentStore) Create(ctx context.Context, in models.CreateStudentRequest) (models.Student, error) {
	_ = ctx
	f.mu.Lock()
	defer f.mu.Unlock()
	f.Creates++
	s := models.Student{
		ID:        f.nextID,
		FirstName: in.FirstName,
		LastName:  in.LastName,
		Email:     in.Email,
		Phone:     in.Phone,
		Course:    in.Course,
		FullName:  models.FullNameOf(in.FirstName, in.LastName),
	}
	f.students[s.ID] = s
	f.nextID++
	return s, nil
}

func (f *FakeStudentStore) GetAll(ctx context.Context) ([]models.Student, error) {
	_ = ctx
	f.mu.Lock()
	defer f.mu.Unlock()
	out := make([]models.Student, 0, len(f.students))
	for _, s := range f.students {
		out = append(out, s)
	}
	return out, nil
}

func (f *FakeStudentStore) GetByID(ctx context.Context, id int) (models.Student, error) {
	_ = ctx
	f.mu.Lock()
	defer f.mu.Unlock()
	s, ok := f.students[id]
	if !ok {
		return models.Student{}, fmt.Errorf("student %d: %w", id, apperrors.ErrNotFound)
	}
	return s, nil
}

func (f *FakeStudentStore) Update(ctx context.Context, id int, in models.CreateStudentRequest) (models.Student, error) {
	_ = ctx
	f.mu.Lock()
	defer f.mu.Unlock()
	if _, ok := f.students[id]; !ok {
		return models.Student{}, fmt.Errorf("student %d: %w", id, apperrors.ErrNotFound)
	}
	s := models.Student{
		ID:        id,
		FirstName: in.FirstName,
		LastName:  in.LastName,
		Email:     in.Email,
		Phone:     in.Phone,
		Course:    in.Course,
		FullName:  models.FullNameOf(in.FirstName, in.LastName),
	}
	f.students[id] = s
	return s, nil
}

func (f *FakeStudentStore) Delete(ctx context.Context, id int) error {
	_ = ctx
	f.mu.Lock()
	defer f.mu.Unlock()
	if _, ok := f.students[id]; !ok {
		return fmt.Errorf("student %d: %w", id, apperrors.ErrNotFound)
	}
	delete(f.students, id)
	return nil
}
