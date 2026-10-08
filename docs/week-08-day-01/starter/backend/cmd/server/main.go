package main

import (
	"student-management-system/internal/handlers"
	"student-management-system/internal/repository"

	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()

	repo := repository.NewStudentRepository()
	health := handlers.NewHealthHandler()
	hello := handlers.NewHelloHandler()
	students := handlers.NewStudentHandler(repo)

	r.GET("/health", health.Get)
	r.GET("/api/hello", hello.Get)

	r.POST("/api/students", students.Create)
	r.GET("/api/students", students.List)
	r.GET("/api/students/:id", students.GetByID)
	r.PUT("/api/students/:id", students.Update)
	r.DELETE("/api/students/:id", students.Delete)

	if err := r.Run(":8080"); err != nil {
		panic(err)
	}
}
