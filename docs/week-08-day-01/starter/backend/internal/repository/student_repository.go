package repository

import (
	"sync"

	"student-management-system/internal/models"
)

// StudentRepository stores students in memory (Postgres arrives later).
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

func (r *StudentRepository) Create(in models.CreateStudentRequest) models.Student {
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

func (r *StudentRepository) GetAll() []models.Student {
	r.mu.Lock()
	defer r.mu.Unlock()
	out := make([]models.Student, 0, len(r.students))
	for _, s := range r.students {
		out = append(out, s)
	}
	return out
}

func (r *StudentRepository) GetByID(id int) (models.Student, bool) {
	r.mu.Lock()
	defer r.mu.Unlock()
	s, ok := r.students[id]
	return s, ok
}

func (r *StudentRepository) Update(id int, in models.CreateStudentRequest) (models.Student, bool) {
	r.mu.Lock()
	defer r.mu.Unlock()
	if _, ok := r.students[id]; !ok {
		return models.Student{}, false
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
	return s, true
}

func (r *StudentRepository) Delete(id int) bool {
	r.mu.Lock()
	defer r.mu.Unlock()
	if _, ok := r.students[id]; !ok {
		return false
	}
	delete(r.students, id)
	return true
}
