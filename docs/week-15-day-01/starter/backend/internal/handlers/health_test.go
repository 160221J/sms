package handlers_test

import (
	"encoding/json"
	"net/http"
	"net/http/httptest"
	"testing"

	"student-management-system/internal/handlers"

	"github.com/gin-gonic/gin"
)

func TestHealthGet(t *testing.T) {
	gin.SetMode(gin.TestMode)
	r := gin.New()
	h := handlers.NewHealthHandler()
	r.GET("/health", h.Get)

	w := httptest.NewRecorder()
	req := httptest.NewRequest(http.MethodGet, "/health", nil)
	r.ServeHTTP(w, req)

	if w.Code != http.StatusOK {
		t.Fatalf("code=%d", w.Code)
	}
	var body map[string]any
	if err := json.Unmarshal(w.Body.Bytes(), &body); err != nil {
		t.Fatal(err)
	}
	if body["status"] != "ok" {
		t.Fatalf("body=%v", body)
	}
}
