package handlers

import (
	"net/http"
	"strconv"
	"time"

	"student-management-system/internal/models"
	"student-management-system/internal/repository"

	"github.com/gin-gonic/gin"
)

type StudentHandler struct {
	studentRepo *repository.StudentRepository
}

func NewStudentHandler() *StudentHandler {
	return &StudentHandler{
		studentRepo: repository.NewStudentRepository(),
	}
}

func (h *StudentHandler) CreateStudent(c *gin.Context) {

	var req models.CreateStudentRequest

	if err := c.ShouldBindJSON(&req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{
			"error": err.Error(),
		})
		return
	}

	dob, err := time.Parse("2006-01-02", req.DateOfBirth)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{
			"error": "invalid date format. Use YYYY-MM-DD",
		})
		return
	}

	student := models.Student{
		FirstName:   req.FirstName,
		LastName:    req.LastName,
		Email:       req.Email,
		Phone:       req.Phone,
		Course:      req.Course,
		DateOfBirth: dob,
	}

	if err := h.studentRepo.Create(&student); err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{
			"error": err.Error(),
		})
		return
	}

	c.JSON(http.StatusCreated, gin.H{
		"message": "Student created successfully",
	})
}

func (h *StudentHandler) GetStudents(c *gin.Context) {

	students, err := h.studentRepo.GetAll()
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{
			"error": err.Error(),
		})
		return
	}

	c.JSON(http.StatusOK, students)
}

func (h *StudentHandler) GetStudentByID(c *gin.Context) {

	id, err := strconv.Atoi(c.Param("id"))
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{
			"error": "invalid student id",
		})
		return
	}

	student, err := h.studentRepo.GetByID(id)
	if err != nil {
		c.JSON(http.StatusNotFound, gin.H{
			"error": "student not found",
		})
		return
	}

	c.JSON(http.StatusOK, student)
}

func (h *StudentHandler) UpdateStudent(c *gin.Context) {

	id, err := strconv.Atoi(c.Param("id"))
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{
			"error": "invalid student id",
		})
		return
	}

	var req models.UpdateStudentRequest

	if err := c.ShouldBindJSON(&req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{
			"error": err.Error(),
		})
		return
	}

	dob, err := time.Parse("2006-01-02", req.DateOfBirth)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{
			"error": "invalid date format",
		})
		return
	}

	student := models.Student{
		ID:          id,
		FirstName:   req.FirstName,
		LastName:    req.LastName,
		Email:       req.Email,
		Phone:       req.Phone,
		Course:      req.Course,
		DateOfBirth: dob,
	}

	if err := h.studentRepo.Update(&student); err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{
			"error": err.Error(),
		})
		return
	}

	c.JSON(http.StatusOK, gin.H{
		"message": "Student updated successfully",
	})
}

func (h *StudentHandler) DeleteStudent(c *gin.Context) {

	id, err := strconv.Atoi(c.Param("id"))
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{
			"error": "invalid student id",
		})
		return
	}

	if err := h.studentRepo.Delete(id); err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{
			"error": err.Error(),
		})
		return
	}

	c.JSON(http.StatusOK, gin.H{
		"message": "Student deleted successfully",
	})
}