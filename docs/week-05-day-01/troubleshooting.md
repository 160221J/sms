# Week 5 troubleshooting

| What they see | Cause | Fix |
| --- | --- | --- |
| `connection refused` | server not running | `go run ./cmd/server` in `backend/` |
| `bind: address already in use` | old process on 8080 | `lsof -i :8080` / kill; or temporary other port |
| `cannot find package gin` | no get / wrong dir | `cd backend && go get github.com/gin-gonic/gin && go mod tidy` |
| 404 on `/health` | path typo / old binary | check `r.GET("/health"...)`; restart server |
| Postman red | `https://` or wrong host | use `http://localhost:8080/health` |
| empty JSON / HTML error | panic / wrong handler | read terminal stack; `gofmt`; fix and rerun |
| WSL: Postman on Windows fails | rare networking | try `localhost` vs `127.0.0.1`; ensure listen `:8080` |
| `go.mod` conflict | module path drift | keep `student-management-system` |

## Reset health handler

```go
r.GET("/health", func(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{
		"status":  "ok",
		"message": "Backend is running",
	})
})
```

Do not paste the full finished course repo (auth, DB, CORS). Week 5 is health + hello only.
