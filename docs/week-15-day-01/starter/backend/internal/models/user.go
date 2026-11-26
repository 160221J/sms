package models

// User is the auth user (in-memory in this starter; WIP uses Postgres users).
type User struct {
	ID           int    `json:"id"`
	FirstName    string `json:"first_name"`
	LastName     string `json:"last_name"`
	Username     string `json:"username"`
	Email        string `json:"email"`
	PasswordHash string `json:"-"`
}

// RegisterRequest matches this repo’s binding style.
type RegisterRequest struct {
	FirstName string `json:"first_name" binding:"required,min=2"`
	LastName  string `json:"last_name" binding:"required,min=2"`
	Username  string `json:"username" binding:"required,min=3"`
	Email     string `json:"email" binding:"required,email"`
	Password  string `json:"password" binding:"required,min=6"`
}

// LoginRequest is the public login body.
type LoginRequest struct {
	Username string `json:"username" binding:"required"`
	Password string `json:"password" binding:"required"`
}

// LoginResponse is what the React app expects after login.
type LoginResponse struct {
	Token string `json:"token"`
	User  User   `json:"user"`
}
