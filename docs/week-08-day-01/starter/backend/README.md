# Student Management System — Week 8 starter

In-memory students behind a **repository**. Handlers talk HTTP only.

## Run

```bash
cd backend
go mod tidy
go run ./cmd/server
```

```bash
curl -s -X POST http://localhost:8080/api/students \
  -H 'Content-Type: application/json' \
  -d '{"first_name":"Ada","last_name":"Lovelace","email":"ada@example.com","phone":"077","course":"SE"}'

curl -s http://localhost:8080/api/students
curl -s http://localhost:8080/api/students/1
```

Layout: `internal/repository` owns the map; `internal/handlers` holds `*StudentRepository`.

No Postgres. No JWT. Restart clears the map.
