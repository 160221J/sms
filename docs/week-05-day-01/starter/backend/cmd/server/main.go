package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()

	r.GET("/health", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"status":  "ok",
			"message": "Backend is running",
		})
	})

	r.GET("/api/hello", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"message": "hello from SMS",
		})
	})

	// Stretch (optional): hard-coded students — no DB
	// r.GET("/api/students", ...)

	if err := r.Run(":8080"); err != nil {
		panic(err)
	}
}
