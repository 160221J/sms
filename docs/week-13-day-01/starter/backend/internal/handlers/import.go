package handlers

import (
	"encoding/json"
	"log/slog"
	"net/http"
	"sync"

	"student-management-system/internal/models"

	"github.com/gin-gonic/gin"
)

// ImportResult is the week-11 stretch response shape.
type ImportResult struct {
	Created int      `json:"created"`
	Failed  int      `json:"failed"`
	Errors  []string `json:"errors,omitempty"`
}

// Import accepts a JSON array and processes rows with a small worker pool (stretch).
// Per-row validation happens in workers (not Gin binding tags), so bad rows become failed counts.
func (h *StudentHandler) Import(c *gin.Context) {
	var rows []models.CreateStudentRequest
	if err := json.NewDecoder(c.Request.Body).Decode(&rows); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "invalid request; expect a JSON array"})
		return
	}

	ctx := c.Request.Context()
	const workers = 4
	jobs := make(chan models.CreateStudentRequest)
	type outcome struct {
		err error
	}
	outcomes := make(chan outcome)

	var wg sync.WaitGroup
	wg.Add(workers)
	for i := 0; i < workers; i++ {
		go func() {
			defer wg.Done()
			for req := range jobs {
				if req.FirstName == "" || req.Email == "" || req.Course == "" {
					outcomes <- outcome{err: errImportValidation}
					continue
				}
				_ = h.repo.Create(ctx, req)
				outcomes <- outcome{}
			}
		}()
	}

	go func() {
		wg.Wait()
		close(outcomes)
	}()

	go func() {
		for _, row := range rows {
			jobs <- row
		}
		close(jobs)
	}()

	res := ImportResult{}
	for o := range outcomes {
		if o.err != nil {
			res.Failed++
			res.Errors = append(res.Errors, o.err.Error())
			continue
		}
		res.Created++
	}

	slog.Info("students imported", "created", res.Created, "failed", res.Failed)
	c.JSON(http.StatusOK, res)
}

var errImportValidation = &importError{"first_name, email, and course are required"}

type importError struct{ msg string }

func (e *importError) Error() string { return e.msg }
