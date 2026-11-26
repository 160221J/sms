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
	"student-management-system/internal/middleware"
	"student-management-system/internal/repository"
	"student-management-system/internal/utils"

	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
)

func main() {
	slog.SetDefault(slog.New(slog.NewJSONHandler(os.Stdout, &slog.HandlerOptions{Level: slog.LevelInfo})))

	cfg := config.Load()
	if cfg.JWTSecret == "" {
		slog.Error("JWT_SECRET is required")
		os.Exit(1)
	}
	utils.SetJWTSecret(cfg.JWTSecret)

	ctx := context.Background()
	pool, err := database.Connect(ctx, cfg)
	if err != nil {
		slog.Error("database", "err", err)
		os.Exit(1)
	}
	defer pool.Close()

	r := gin.Default()
	r.Use(cors.New(cors.Config{
		AllowOrigins: []string{
			"http://localhost:5173",
			"http://localhost:5174",
		},
		AllowMethods:     []string{"GET", "POST", "PUT", "DELETE", "OPTIONS"},
		AllowHeaders:     []string{"Origin", "Content-Type", "Authorization"},
		ExposeHeaders:    []string{"Content-Length"},
		AllowCredentials: true,
	}))

	studentRepo := repository.NewStudentRepository(pool)
	userRepo := repository.NewUserRepository()

	health := handlers.NewHealthHandler()
	hello := handlers.NewHelloHandler()
	students := handlers.NewStudentHandler(studentRepo)
	auth := handlers.NewAuthHandler(userRepo)
	demo := handlers.NewDemoHandler()

	r.GET("/health", health.Get)
	r.GET("/api/hello", hello.Get)

	// Public auth
	r.POST("/api/register", auth.Register)
	r.POST("/api/login", auth.Login)

	// Protected student API (week 15)
	api := r.Group("/api")
	api.Use(middleware.AuthMiddleware())
	{
		api.POST("/students", students.Create)
		api.GET("/students", students.List)
		api.GET("/students/:id", students.GetByID)
		api.PUT("/students/:id", students.Update)
		api.DELETE("/students/:id", students.Delete)
		api.POST("/students/import", students.Import)
		api.GET("/profile", func(c *gin.Context) {
			c.JSON(http.StatusOK, gin.H{
				"user_id":  c.GetInt("user_id"),
				"username": c.GetString("username"),
			})
		})
	}

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
