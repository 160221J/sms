# Week 5, Day 1 — presenter notes

Slides: [`week-05-day-01.html`](week-05-day-01.html) → **F** fullscreen → arrows. **N** notes. **P** print.

**HTTP, JSON, Gin, first SMS API.** Stdlib first. No DB. No JWT. No CORS implementation.

## Timing (3–3.5 hours)

| Clock | Block | Slides |
| --- | --- | --- |
| 0:00–0:15 | Week 4 skeleton check | 1–2 |
| 0:15–0:30 | Outcomes + why REST now | 3–4 |
| 0:30–0:50 | HTTP + JSON concepts | 5–6 |
| 0:50–1:20 | **Live** `net/http` hello | 7 |
| 1:20–2:10 | Gin, health, hello, minimal struct (**live**) | 8–13 |
| 2:10–2:30 | Status, validation light, curl | 14–16 |
| 2:30–end | Postman lab + PR | 17–end |

Never skip stdlib HTTP. Never skip a 200 in Postman.

## Live demo script

### 1. Stdlib (throwaway ok)

```go
http.HandleFunc("/hello", func(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "hello from stdlib")
})
http.ListenAndServe(":8080", nil)
```

### 2. Gin health in `cmd/server`

```bash
cd backend
go get github.com/gin-gonic/gin
go mod tidy
```

```go
r := gin.Default()
r.GET("/health", func(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{
		"status":  "ok",
		"message": "Backend is running",
	})
})
r.Run(":8080")
```

```bash
curl -i http://localhost:8080/health
```

## Lab gate

- [ ] Gin in `go.mod`
- [ ] `GET /health` exact JSON
- [ ] `GET /api/hello` JSON
- [ ] curl 200 + Postman 200
- [ ] Pushed / PR started

## Homework

PR + Postman screenshot. Stretch: hard-coded `GET /api/students` array.

## Typical failures

| Symptom | Fix |
| --- | --- |
| `connection refused` | server not running / wrong port |
| port already in use | kill old process |
| package gin not found | `go get` + tidy from `backend/` |
| empty body | wrong path or method |
| JSON keys differ | match `status` / `message` exactly |

## What not to teach today

JWT, Postgres, CORS code, full CRUD, deep structs, middleware. Tease week 6 only.
