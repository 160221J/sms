package repository

import (
	"context"

	"student-management-system/internal/database"
	"student-management-system/internal/models"
)

type UserRepository struct{}

func NewUserRepository() *UserRepository {
	return &UserRepository{}
}

func (r *UserRepository) CreateUser(user *models.User) error {

	query := `
	INSERT INTO users
	(first_name,last_name,username,email,password_hash)
	VALUES ($1,$2,$3,$4,$5)
	`

	_, err := database.DB.Exec(
		context.Background(),
		query,
		user.FirstName,
		user.LastName,
		user.Username,
		user.Email,
		user.PasswordHash,
	)

	return err
}

func (r *UserRepository) GetUserByUsername(username string) (*models.User, error) {

	query := `
	SELECT
		id,
		first_name,
		last_name,
		username,
		email,
		password_hash,
		created_at
	FROM users
	WHERE username=$1
	`

	var user models.User

	err := database.DB.QueryRow(
		context.Background(),
		query,
		username,
	).Scan(
		&user.ID,
		&user.FirstName,
		&user.LastName,
		&user.Username,
		&user.Email,
		&user.PasswordHash,
		&user.CreatedAt,
	)

	if err != nil {
		return nil, err
	}

	return &user, nil
}