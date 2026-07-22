package routes

import (
	"net/http"

	"student-management-system/internal/handlers"
	"student-management-system/internal/middleware"

	"github.com/gin-gonic/gin"
)

func SetupRoutes(router *gin.Engine) {

	authHandler := handlers.NewAuthHandler()
	studentHandler := handlers.NewStudentHandler()

	router.GET("/health", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"status":  "ok",
			"message": "Backend is running",
		})
	})

	api := router.Group("/api")
	{
		api.POST("/register", authHandler.Register)
		api.POST("/login", authHandler.Login)
	}

	protected := api.Group("/")
	protected.Use(middleware.AuthMiddleware())
	{
		protected.GET("/profile", func(c *gin.Context) {
			c.JSON(http.StatusOK, gin.H{
				"user_id":  c.GetInt("user_id"),
				"username": c.GetString("username"),
			})
		})

		protected.POST("/students", studentHandler.CreateStudent)
		protected.GET("/students", studentHandler.GetStudents)
		protected.GET("/students/:id", studentHandler.GetStudentByID)
		protected.PUT("/students/:id", studentHandler.UpdateStudent)
		protected.DELETE("/students/:id", studentHandler.DeleteStudent)
	}
}
