package main

import (
	"context"
	"errors"
	"log/slog"
	"net/http"
	"os"
	"os/signal"
	"syscall"
	"time"

	"student-management-system/internal/config"
	"student-management-system/internal/database"
	"student-management-system/internal/handlers"
	"student-management-system/internal/repository"

	"github.com/gin-gonic/gin"
)

func main() {
	slog.SetDefault(slog.New(slog.NewJSONHandler(os.Stdout, &slog.HandlerOptions{Level: slog.LevelInfo})))

	cfg := config.Load()
	ctx := context.Background()

	pool, err := database.Connect(ctx, cfg)
	if err != nil {
		slog.Error("database", "err", err)
		os.Exit(1)
	}
	defer pool.Close()

	r := gin.Default()

	studentRepo := repository.NewStudentRepository(pool)
	userRepo := repository.NewUserRepository() // homework: prefer Postgres users

	health := handlers.NewHealthHandler()
	hello := handlers.NewHelloHandler()
	students := handlers.NewStudentHandler(studentRepo)
	auth := handlers.NewAuthHandler(userRepo)
	demo := handlers.NewDemoHandler()

	r.GET("/health", health.Get)
	r.GET("/api/hello", hello.Get)

	r.POST("/api/students", students.Create)
	r.GET("/api/students", students.List)
	r.GET("/api/students/:id", students.GetByID)
	r.PUT("/api/students/:id", students.Update)
	r.DELETE("/api/students/:id", students.Delete)
	r.POST("/api/students/import", students.Import)

	r.POST("/api/register", auth.Register)
	r.POST("/api/login", auth.Login)

	r.GET("/api/demo/slow", func(c *gin.Context) {
		reqCtx, cancel := context.WithTimeout(c.Request.Context(), time.Second)
		defer cancel()
		c.Request = c.Request.WithContext(reqCtx)
		demo.Slow(c)
	})

	addr := ":" + cfg.Port
	srv := &http.Server{Addr: addr, Handler: r}

	go func() {
		slog.Info("starting server", "addr", addr)
		if err := srv.ListenAndServe(); err != nil && !errors.Is(err, http.ErrServerClosed) {
			slog.Error("server stopped", "err", err)
			os.Exit(1)
		}
	}()

	sigCtx, stop := signal.NotifyContext(context.Background(), os.Interrupt, syscall.SIGTERM)
	defer stop()
	<-sigCtx.Done()
	slog.Info("shutting down")

	shutdownCtx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()
	if err := srv.Shutdown(shutdownCtx); err != nil {
		slog.Error("shutdown", "err", err)
		os.Exit(1)
	}
	slog.Info("bye")
}
