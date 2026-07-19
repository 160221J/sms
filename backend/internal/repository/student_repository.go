package repository

import (
	"context"

	"student-management-system/internal/database"
	"student-management-system/internal/models"
)

type StudentRepository struct{}

func NewStudentRepository() *StudentRepository {
	return &StudentRepository{}
}

func (r *StudentRepository) Create(student *models.Student) error {

	query := `
	INSERT INTO students
	(first_name,last_name,email,phone,course,date_of_birth)
	VALUES ($1,$2,$3,$4,$5,$6)
	`

	_, err := database.DB.Exec(
		context.Background(),
		query,
		student.FirstName,
		student.LastName,
		student.Email,
		student.Phone,
		student.Course,
		student.DateOfBirth,
	)

	return err
}

func (r *StudentRepository) GetAll() ([]models.Student, error) {

	query := `
	SELECT
		id,
		first_name,
		last_name,
		email,
		phone,
		course,
		date_of_birth,
		created_at,
		updated_at
	FROM students
	ORDER BY id DESC
	`

	rows, err := database.DB.Query(context.Background(), query)
	if err != nil {
		return nil, err
	}
	defer rows.Close()

	var students []models.Student

	for rows.Next() {

		var s models.Student

		err := rows.Scan(
			&s.ID,
			&s.FirstName,
			&s.LastName,
			&s.Email,
			&s.Phone,
			&s.Course,
			&s.DateOfBirth,
			&s.CreatedAt,
			&s.UpdatedAt,
		)

		if err != nil {
			return nil, err
		}

		students = append(students, s)
	}

	return students, nil
}

func (r *StudentRepository) GetByID(id int) (*models.Student, error) {

	query := `
	SELECT
		id,
		first_name,
		last_name,
		email,
		phone,
		course,
		date_of_birth,
		created_at,
		updated_at
	FROM students
	WHERE id=$1
	`

	var s models.Student

	err := database.DB.QueryRow(
		context.Background(),
		query,
		id,
	).Scan(
		&s.ID,
		&s.FirstName,
		&s.LastName,
		&s.Email,
		&s.Phone,
		&s.Course,
		&s.DateOfBirth,
		&s.CreatedAt,
		&s.UpdatedAt,
	)

	if err != nil {
		return nil, err
	}

	return &s, nil
}

func (r *StudentRepository) Update(student *models.Student) error {

	query := `
	UPDATE students
	SET
		first_name=$1,
		last_name=$2,
		email=$3,
		phone=$4,
		course=$5,
		date_of_birth=$6,
		updated_at=NOW()
	WHERE id=$7
	`

	_, err := database.DB.Exec(
		context.Background(),
		query,
		student.FirstName,
		student.LastName,
		student.Email,
		student.Phone,
		student.Course,
		student.DateOfBirth,
		student.ID,
	)

	return err
}

func (r *StudentRepository) Delete(id int) error {

	query := `DELETE FROM students WHERE id=$1`

	_, err := database.DB.Exec(
		context.Background(),
		query,
		id,
	)

	return err
}