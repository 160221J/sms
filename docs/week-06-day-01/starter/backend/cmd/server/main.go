package main

import (
	"student-management-system/internal/handlers"

	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()

	health := handlers.NewHealthHandler()
	hello := handlers.NewHelloHandler()

	r.GET("/health", health.Get)
	r.GET("/api/hello", hello.Get)

	if err := r.Run(":8080"); err != nil {
		panic(err)
	}
}
