package handlers

import (
	"net/http"
	"strconv"
	"sync"

	"student-management-system/internal/models"

	"github.com/gin-gonic/gin"
)

type StudentHandler struct {
	mu       sync.Mutex
	students map[int]models.Student
	nextID   int
}

func NewStudentHandler() *StudentHandler {
	return &StudentHandler{
		students: map[int]models.Student{},
		nextID:   1,
	}
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

	h.mu.Lock()
	defer h.mu.Unlock()
	s := models.Student{
		ID:        h.nextID,
		FirstName: req.FirstName,
		LastName:  req.LastName,
		Email:     req.Email,
		Phone:     req.Phone,
		Course:    req.Course,
	}
	h.students[s.ID] = s
	h.nextID++
	c.JSON(http.StatusCreated, s)
}

func (h *StudentHandler) List(c *gin.Context) {
	h.mu.Lock()
	defer h.mu.Unlock()
	out := make([]models.Student, 0, len(h.students))
	for _, s := range h.students {
		out = append(out, s)
	}
	c.JSON(http.StatusOK, out)
}

func (h *StudentHandler) GetByID(c *gin.Context) {
	id, err := strconv.Atoi(c.Param("id"))
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "invalid id"})
		return
	}
	h.mu.Lock()
	defer h.mu.Unlock()
	s, ok := h.students[id]
	if !ok {
		c.JSON(http.StatusNotFound, gin.H{"error": "student not found"})
		return
	}
	c.JSON(http.StatusOK, s)
}

// Update is homework (PUT /api/students/:id).
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
	h.mu.Lock()
	defer h.mu.Unlock()
	if _, ok := h.students[id]; !ok {
		c.JSON(http.StatusNotFound, gin.H{"error": "student not found"})
		return
	}
	s := models.Student{
		ID:        id,
		FirstName: req.FirstName,
		LastName:  req.LastName,
		Email:     req.Email,
		Phone:     req.Phone,
		Course:    req.Course,
	}
	h.students[id] = s
	c.JSON(http.StatusOK, s)
}

// Delete is homework (DELETE /api/students/:id).
func (h *StudentHandler) Delete(c *gin.Context) {
	id, err := strconv.Atoi(c.Param("id"))
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "invalid id"})
		return
	}
	h.mu.Lock()
	defer h.mu.Unlock()
	if _, ok := h.students[id]; !ok {
		c.JSON(http.StatusNotFound, gin.H{"error": "student not found"})
		return
	}
	delete(h.students, id)
	c.Status(http.StatusNoContent)
}
