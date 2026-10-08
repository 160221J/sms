package handlers

import (
	"net/http"
	"strconv"

	"student-management-system/internal/models"
	"student-management-system/internal/repository"

	"github.com/gin-gonic/gin"
)

// StudentHandler talks HTTP only — storage lives in the repository.
type StudentHandler struct {
	repo *repository.StudentRepository
}

func NewStudentHandler(repo *repository.StudentRepository) *StudentHandler {
	return &StudentHandler{repo: repo}
}

func (h *StudentHandler) Create(c *gin.Context) {
	var req models.CreateStudentRequest
	if err := c.ShouldBindJSON(&req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "invalid json"})
		return
	}
	if req.FirstName == "" || req.Email == "" || req.Course == "" {
		c.JSON(http.StatusBadRequest, gin.H{"error": "first_name, email, and course are required"})
		return
	}
	s := h.repo.Create(req)
	c.JSON(http.StatusCreated, s)
}

func (h *StudentHandler) List(c *gin.Context) {
	c.JSON(http.StatusOK, h.repo.GetAll())
}

func (h *StudentHandler) GetByID(c *gin.Context) {
	id, err := strconv.Atoi(c.Param("id"))
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "invalid id"})
		return
	}
	s, ok := h.repo.GetByID(id)
	if !ok {
		c.JSON(http.StatusNotFound, gin.H{"error": "student not found"})
		return
	}
	c.JSON(http.StatusOK, s)
}

func (h *StudentHandler) Update(c *gin.Context) {
	id, err := strconv.Atoi(c.Param("id"))
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "invalid id"})
		return
	}
	var req models.CreateStudentRequest
	if err := c.ShouldBindJSON(&req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "invalid json"})
		return
	}
	s, ok := h.repo.Update(id, req)
	if !ok {
		c.JSON(http.StatusNotFound, gin.H{"error": "student not found"})
		return
	}
	c.JSON(http.StatusOK, s)
}

func (h *StudentHandler) Delete(c *gin.Context) {
	id, err := strconv.Atoi(c.Param("id"))
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "invalid id"})
		return
	}
	if !h.repo.Delete(id) {
		c.JSON(http.StatusNotFound, gin.H{"error": "student not found"})
		return
	}
	c.Status(http.StatusNoContent)
}
