package handlers

import (
	"context"
	"net/http"
	"strconv"
	"time"

	"github.com/gin-gonic/gin"
)

// DemoHandler shows context timeouts (week 12).
type DemoHandler struct{}

func NewDemoHandler() *DemoHandler { return &DemoHandler{} }

// Slow sleeps for ?ms= (default 2500) but cancels if the request context times out.
// Server wraps the request with a 1s timeout in main for the live demo.
func (h *DemoHandler) Slow(c *gin.Context) {
	ms := 2500
	if raw := c.Query("ms"); raw != "" {
		if v, err := strconv.Atoi(raw); err == nil && v > 0 && v < 30_000 {
			ms = v
		}
	}

	ctx := c.Request.Context()
	timer := time.NewTimer(time.Duration(ms) * time.Millisecond)
	defer timer.Stop()

	select {
	case <-ctx.Done():
		c.JSON(http.StatusGatewayTimeout, gin.H{
			"error":  "canceled or deadline exceeded",
			"detail": ctx.Err().Error(),
		})
	case <-timer.C:
		c.JSON(http.StatusOK, gin.H{"slept_ms": ms, "ok": true})
	}
}

// WithTimeout is a tiny helper shown in slides / notes (not required by routes).
func WithTimeout(parent context.Context, d time.Duration) (context.Context, context.CancelFunc) {
	return context.WithTimeout(parent, d)
}
