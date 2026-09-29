# Week 6 troubleshooting

| What they see | Cause | Fix |
| --- | --- | --- |
| health 404 after move | route not registered / wrong method value | `r.GET("/health", h.Get)` — pass method, don’t call `h.Get()` |
| `invalid memory address` | nil handler pointer | `h := handlers.NewHealthHandler()` before register |
| package handlers not found | wrong dir / module path | `internal/handlers` + import `student-management-system/internal/handlers` |
| `go test` no tests | wrong package path | from `backend/`: `go test ./internal/handlers` |
| import cycle | routes ↔ handlers wrong | handlers must not import the package that imports handlers for registration in a cycle |
| FullName test fail | trim/space rules | empty last → first only; trim both |
| still all code in main | incomplete lab | move bodies into handler methods |

## Minimal health handler

```go
type HealthHandler struct{}

func NewHealthHandler() *HealthHandler { return &HealthHandler{} }

func (h *HealthHandler) Get(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{
		"status":  "ok",
		"message": "Backend is running",
	})
}
```
