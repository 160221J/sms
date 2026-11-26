package repository

import (
	"context"
	"errors"
	"fmt"
	"time"

	"student-management-system/internal/apperrors"
	"student-management-system/internal/models"

	"github.com/jackc/pgx/v5"
	"github.com/jackc/pgx/v5/pgxpool"
)

// StudentRepository is the Postgres-backed store (week 14).
type StudentRepository struct {
	pool *pgxpool.Pool
}

func NewStudentRepository(pool *pgxpool.Pool) *StudentRepository {
	return &StudentRepository{pool: pool}
}

var _ StudentStore = (*StudentRepository)(nil)

func (r *StudentRepository) Create(ctx context.Context, in models.CreateStudentRequest) (models.Student, error) {
	var dob *time.Time
	if in.DateOfBirth != "" {
		if t, err := models.ParseDate(in.DateOfBirth); err == nil {
			dob = &t
		}
	}

	const q = `
INSERT INTO students (first_name, last_name, email, phone, course, date_of_birth)
VALUES ($1, $2, $3, $4, $5, $6)
RETURNING id, first_name, last_name, email, phone, course, date_of_birth, created_at, updated_at`

	row := r.pool.QueryRow(ctx, q, in.FirstName, in.LastName, in.Email, in.Phone, in.Course, dob)
	s, err := scanStudent(row)
	if err != nil {
		return models.Student{}, err
	}
	return s, nil
}

func (r *StudentRepository) GetAll(ctx context.Context) ([]models.Student, error) {
	const q = `
SELECT id, first_name, last_name, email, phone, course, date_of_birth, created_at, updated_at
FROM students
ORDER BY id`

	rows, err := r.pool.Query(ctx, q)
	if err != nil {
		return nil, err
	}
	defer rows.Close()

	out := []models.Student{}
	for rows.Next() {
		s, err := scanStudent(rows)
		if err != nil {
			return nil, err
		}
		out = append(out, s)
	}
	return out, rows.Err()
}

func (r *StudentRepository) GetByID(ctx context.Context, id int) (models.Student, error) {
	const q = `
SELECT id, first_name, last_name, email, phone, course, date_of_birth, created_at, updated_at
FROM students WHERE id = $1`

	s, err := scanStudent(r.pool.QueryRow(ctx, q, id))
	if errors.Is(err, pgx.ErrNoRows) {
		return models.Student{}, fmt.Errorf("student %d: %w", id, apperrors.ErrNotFound)
	}
	return s, err
}

func (r *StudentRepository) Update(ctx context.Context, id int, in models.CreateStudentRequest) (models.Student, error) {
	var dob *time.Time
	if in.DateOfBirth != "" {
		if t, err := models.ParseDate(in.DateOfBirth); err == nil {
			dob = &t
		}
	}
	const q = `
UPDATE students
SET first_name=$1, last_name=$2, email=$3, phone=$4, course=$5, date_of_birth=$6, updated_at=NOW()
WHERE id=$7
RETURNING id, first_name, last_name, email, phone, course, date_of_birth, created_at, updated_at`

	s, err := scanStudent(r.pool.QueryRow(ctx, q, in.FirstName, in.LastName, in.Email, in.Phone, in.Course, dob, id))
	if errors.Is(err, pgx.ErrNoRows) {
		return models.Student{}, fmt.Errorf("student %d: %w", id, apperrors.ErrNotFound)
	}
	return s, err
}

func (r *StudentRepository) Delete(ctx context.Context, id int) error {
	tag, err := r.pool.Exec(ctx, `DELETE FROM students WHERE id = $1`, id)
	if err != nil {
		return err
	}
	if tag.RowsAffected() == 0 {
		return fmt.Errorf("student %d: %w", id, apperrors.ErrNotFound)
	}
	return nil
}

// CreateInTx sketches Begin/Commit (audit table optional — pattern only).
func (r *StudentRepository) CreateInTx(ctx context.Context, in models.CreateStudentRequest) (models.Student, error) {
	tx, err := r.pool.Begin(ctx)
	if err != nil {
		return models.Student{}, err
	}
	defer tx.Rollback(ctx)

	var dob *time.Time
	if in.DateOfBirth != "" {
		if t, err := models.ParseDate(in.DateOfBirth); err == nil {
			dob = &t
		}
	}
	s, err := scanStudent(tx.QueryRow(ctx, `
INSERT INTO students (first_name, last_name, email, phone, course, date_of_birth)
VALUES ($1,$2,$3,$4,$5,$6)
RETURNING id, first_name, last_name, email, phone, course, date_of_birth, created_at, updated_at`,
		in.FirstName, in.LastName, in.Email, in.Phone, in.Course, dob))
	if err != nil {
		return models.Student{}, err
	}
	if err := tx.Commit(ctx); err != nil {
		return models.Student{}, err
	}
	return s, nil
}

type scannable interface {
	Scan(dest ...any) error
}

func scanStudent(row scannable) (models.Student, error) {
	var s models.Student
	var rawDOB *time.Time
	err := row.Scan(&s.ID, &s.FirstName, &s.LastName, &s.Email, &s.Phone, &s.Course, &rawDOB, &s.CreatedAt, &s.UpdatedAt)
	if err != nil {
		return models.Student{}, err
	}
	if rawDOB != nil {
		s.DateOfBirth = *rawDOB
	}
	s.FullName = models.FullNameOf(s.FirstName, s.LastName)
	return s, nil
}
