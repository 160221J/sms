package models

// Student is the in-memory SMS student shape (no DB tags yet).
type Student struct {
	ID        int    `json:"id"`
	FirstName string `json:"first_name"`
	LastName  string `json:"last_name"`
	Email     string `json:"email"`
	Phone     string `json:"phone"`
	Course    string `json:"course"`
}

// CreateStudentRequest is the POST/PUT body (id assigned by server).
type CreateStudentRequest struct {
	FirstName string `json:"first_name"`
	LastName  string `json:"last_name"`
	Email     string `json:"email"`
	Phone     string `json:"phone"`
	Course    string `json:"course"`
}
