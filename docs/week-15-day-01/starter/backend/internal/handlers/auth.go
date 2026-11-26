package handlers

import (
	"errors"
	"log/slog"
	"net/http"

	"student-management-system/internal/apperrors"
	"student-management-system/internal/models"
	"student-management-system/internal/repository"
	"student-management-system/internal/utils"

	"github.com/gin-gonic/gin"
	"golang.org/x/crypto/bcrypt"
)

// AuthHandler handles public register/login (week 15 returns a real JWT).
type AuthHandler struct {
	users *repository.UserRepository
}

func NewAuthHandler(users *repository.UserRepository) *AuthHandler {
	return &AuthHandler{users: users}
}

func (h *AuthHandler) Register(c *gin.Context) {
	var req models.RegisterRequest
	if err := c.ShouldBindJSON(&req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "invalid request"})
		return
	}

	hash, err := bcrypt.GenerateFromPassword([]byte(req.Password), bcrypt.DefaultCost)
	if err != nil {
		slog.Error("hash password", "err", err)
		c.JSON(http.StatusInternalServerError, gin.H{"error": "internal error"})
		return
	}

	u := models.User{
		FirstName:    req.FirstName,
		LastName:     req.LastName,
		Username:     req.Username,
		Email:        req.Email,
		PasswordHash: string(hash),
	}
	created, err := h.users.Create(c.Request.Context(), u)
	if err != nil {
		if errors.Is(err, apperrors.ErrConflict) {
			c.JSON(http.StatusConflict, gin.H{"error": "username already exists"})
			return
		}
		slog.Error("register user", "err", err)
		c.JSON(http.StatusInternalServerError, gin.H{"error": "internal error"})
		return
	}

	slog.Info("user registered", "user_id", created.ID, "username", created.Username)
	c.JSON(http.StatusCreated, gin.H{"message": "user registered successfully", "id": created.ID})
}

func (h *AuthHandler) Login(c *gin.Context) {
	var req models.LoginRequest
	if err := c.ShouldBindJSON(&req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "invalid request"})
		return
	}

	u, err := h.users.GetByUsername(c.Request.Context(), req.Username)
	if err != nil {
		c.JSON(http.StatusUnauthorized, gin.H{"error": "invalid credentials"})
		return
	}
	if err := bcrypt.CompareHashAndPassword([]byte(u.PasswordHash), []byte(req.Password)); err != nil {
		c.JSON(http.StatusUnauthorized, gin.H{"error": "invalid credentials"})
		return
	}

	token, err := utils.GenerateToken(u.ID, u.Username)
	if err != nil {
		slog.Error("generate token", "err", err)
		c.JSON(http.StatusInternalServerError, gin.H{"error": "internal error"})
		return
	}

	c.JSON(http.StatusOK, models.LoginResponse{
		Token: token,
		User: models.User{
			ID:        u.ID,
			FirstName: u.FirstName,
			LastName:  u.LastName,
			Username:  u.Username,
			Email:     u.Email,
		},
	})
}
