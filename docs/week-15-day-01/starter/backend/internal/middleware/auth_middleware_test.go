package middleware_test

import (
	"net/http"
	"net/http/httptest"
	"testing"

	"student-management-system/internal/middleware"
	"student-management-system/internal/utils"

	"github.com/gin-gonic/gin"
)

func TestAuthMiddlewareRequiresBearer(t *testing.T) {
	gin.SetMode(gin.TestMode)
	utils.SetJWTSecret("test-secret-week-15")

	r := gin.New()
	r.GET("/x", middleware.AuthMiddleware(), func(c *gin.Context) {
		c.Status(http.StatusOK)
	})

	w := httptest.NewRecorder()
	req := httptest.NewRequest(http.MethodGet, "/x", nil)
	r.ServeHTTP(w, req)
	if w.Code != http.StatusUnauthorized {
		t.Fatalf("code=%d", w.Code)
	}

	tok, err := utils.GenerateToken(1, "ada")
	if err != nil {
		t.Fatal(err)
	}
	w = httptest.NewRecorder()
	req = httptest.NewRequest(http.MethodGet, "/x", nil)
	req.Header.Set("Authorization", "Bearer "+tok)
	r.ServeHTTP(w, req)
	if w.Code != http.StatusOK {
		t.Fatalf("code=%d body=%s", w.Code, w.Body.String())
	}
}
