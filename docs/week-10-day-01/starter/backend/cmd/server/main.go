package main

import (
	"log/slog"
	"os"

	"student-management-system/internal/config"
	"student-management-system/internal/handlers"
	"student-management-system/internal/repository"

	"github.com/gin-gonic/gin"
)

func main() {
	slog.SetDefault(slog.New(slog.NewJSONHandler(os.Stdout, &slog.HandlerOptions{Level: slog.LevelInfo})))

	cfg := config.Load()
	r := gin.Default()

	studentRepo := repository.NewStudentRepository()
	userRepo := repository.NewUserRepository()

	health := handlers.NewHealthHandler()
	hello := handlers.NewHelloHandler()
	students := handlers.NewStudentHandler(studentRepo)
	auth := handlers.NewAuthHandler(userRepo)

	r.GET("/health", health.Get)
	r.GET("/api/hello", hello.Get)

	r.POST("/api/students", students.Create)
	r.GET("/api/students", students.List)
	r.GET("/api/students/:id", students.GetByID)
	r.PUT("/api/students/:id", students.Update)
	r.DELETE("/api/students/:id", students.Delete)

	r.POST("/api/register", auth.Register)
	r.POST("/api/login", auth.Login)

	addr := ":" + cfg.Port
	slog.Info("starting server", "addr", addr)
	if err := r.Run(addr); err != nil {
		slog.Error("server stopped", "err", err)
		os.Exit(1)
	}
}
