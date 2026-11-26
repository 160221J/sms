package handlers_test

import (
	"bytes"
	"encoding/json"
	"net/http"
	"net/http/httptest"
	"testing"

	"student-management-system/internal/handlers"
	"student-management-system/internal/repository"

	"github.com/gin-gonic/gin"
)

func TestCreateStudentWithFake(t *testing.T) {
	gin.SetMode(gin.TestMode)
	fake := repository.NewFakeStudentStore()
	h := handlers.NewStudentHandler(fake)

	r := gin.New()
	r.POST("/api/students", h.Create)

	body := []byte(`{"first_name":"Ada","last_name":"Lovelace","email":"ada@example.com","course":"SE"}`)
	w := httptest.NewRecorder()
	req := httptest.NewRequest(http.MethodPost, "/api/students", bytes.NewReader(body))
	req.Header.Set("Content-Type", "application/json")
	r.ServeHTTP(w, req)

	if w.Code != http.StatusCreated {
		t.Fatalf("code=%d body=%s", w.Code, w.Body.String())
	}
	if fake.Creates != 1 {
		t.Fatalf("Creates=%d", fake.Creates)
	}
	var got map[string]any
	if err := json.Unmarshal(w.Body.Bytes(), &got); err != nil {
		t.Fatal(err)
	}
	if got["full_name"] != "Ada Lovelace" {
		t.Fatalf("full_name=%v", got["full_name"])
	}
}

func TestCreateStudentBadDate(t *testing.T) {
	gin.SetMode(gin.TestMode)
	h := handlers.NewStudentHandler(repository.NewFakeStudentStore())
	r := gin.New()
	r.POST("/api/students", h.Create)

	body := []byte(`{"first_name":"Ada","email":"ada@example.com","course":"SE","date_of_birth":"10-12-1995"}`)
	w := httptest.NewRecorder()
	req := httptest.NewRequest(http.MethodPost, "/api/students", bytes.NewReader(body))
	req.Header.Set("Content-Type", "application/json")
	r.ServeHTTP(w, req)

	if w.Code != http.StatusBadRequest {
		t.Fatalf("code=%d body=%s", w.Code, w.Body.String())
	}
}

func TestListStudentsWithFake(t *testing.T) {
	gin.SetMode(gin.TestMode)
	fake := repository.NewFakeStudentStore()
	h := handlers.NewStudentHandler(fake)
	r := gin.New()
	r.GET("/api/students", h.List)

	w := httptest.NewRecorder()
	req := httptest.NewRequest(http.MethodGet, "/api/students", nil)
	r.ServeHTTP(w, req)
	if w.Code != http.StatusOK {
		t.Fatalf("code=%d", w.Code)
	}
}
