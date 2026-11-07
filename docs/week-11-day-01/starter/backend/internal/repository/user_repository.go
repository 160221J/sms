package repository

import (
	"fmt"
	"sync"

	"student-management-system/internal/apperrors"
	"student-management-system/internal/models"
)

// UserRepository stores users in memory (stretch / auth preview).
type UserRepository struct {
	mu      sync.Mutex
	users   map[string]models.User // key: username
	nextID  int
}

func NewUserRepository() *UserRepository {
	return &UserRepository{
		users:  map[string]models.User{},
		nextID: 1,
	}
}

func (r *UserRepository) Create(u models.User) (models.User, error) {
	r.mu.Lock()
	defer r.mu.Unlock()
	if _, exists := r.users[u.Username]; exists {
		return models.User{}, fmt.Errorf("username %s: %w", u.Username, apperrors.ErrConflict)
	}
	u.ID = r.nextID
	r.nextID++
	r.users[u.Username] = u
	return u, nil
}

func (r *UserRepository) GetByUsername(username string) (models.User, error) {
	r.mu.Lock()
	defer r.mu.Unlock()
	u, ok := r.users[username]
	if !ok {
		return models.User{}, fmt.Errorf("user %s: %w", username, apperrors.ErrNotFound)
	}
	return u, nil
}
