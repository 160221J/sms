# Student Management System — Week 5 starter

Minimal Gin API: health + hello. No database. No JWT.

## Run

```bash
cd backend
go mod tidy
go run ./cmd/server
```

```bash
curl -i http://localhost:8080/health
curl -s http://localhost:8080/api/hello
```

Expected health body:

```json
{"status":"ok","message":"Backend is running"}
```
