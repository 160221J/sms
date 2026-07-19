package main

import (
	"log"

	"student-management-system/internal/config"
	"student-management-system/internal/database"
	"student-management-system/internal/routes"
	"student-management-system/internal/utils"

	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
)

func main() {

	// Load configuration
	cfg := config.LoadConfig()

	// Initialize JWT secret
	utils.SetJWTSecret(cfg.JWTSecret)

	// Connect to PostgreSQL
	database.Connect(cfg)

	// Create Gin router
	router := gin.Default()

	// Configure CORS
	router.Use(cors.New(cors.Config{
		AllowOrigins:     []string{"http://localhost:5173"},
		AllowMethods:     []string{"GET", "POST", "PUT", "DELETE", "OPTIONS"},
		AllowHeaders:     []string{"Origin", "Content-Type", "Authorization"},
		AllowCredentials: true,
	}))

	// Register all routes
	routes.SetupRoutes(router)

	log.Printf("🚀 Server running on port %s\n", cfg.Port)

	// Start server
	if err := router.Run(":" + cfg.Port); err != nil {
		log.Fatal("Failed to start server:", err)
	}
}