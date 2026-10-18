package handlers

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

type HelloHandler struct{}

func NewHelloHandler() *HelloHandler {
	return &HelloHandler{}
}

func (h *HelloHandler) Get(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{"message": "hello from SMS"})
}
