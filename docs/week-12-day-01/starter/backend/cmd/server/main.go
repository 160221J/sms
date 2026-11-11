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

	// Week 12: timeout demo — wrap request context with 1s deadline.
	r.GET("/api/demo/slow", func(c *gin.Context) {
		ctx, cancel := context.WithTimeout(c.Request.Context(), time.Second)
		defer cancel()
		c.Request = c.Request.WithContext(ctx)
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

	// Week 12: graceful shutdown sketch.
	ctx, stop := signal.NotifyContext(context.Background(), os.Interrupt, syscall.SIGTERM)
	defer stop()
	<-ctx.Done()
	slog.Info("shutting down")

	shutdownCtx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()
	if err := srv.Shutdown(shutdownCtx); err != nil {
		slog.Error("shutdown", "err", err)
		os.Exit(1)
	}
	slog.Info("bye")
}
