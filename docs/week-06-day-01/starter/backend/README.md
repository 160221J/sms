# Student Management System — Week 6 starter

Week 5 API refactored into `internal/handlers`. Thin `main` wires routes.

## Run

```bash
cd backend
go mod tidy
go run ./cmd/server
```

```bash
curl -i http://localhost:8080/health
go test ./internal/handlers -v
```
