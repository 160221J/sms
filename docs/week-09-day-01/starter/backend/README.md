# Student Management System — Week 9 starter

In-memory students behind a repository. Handlers map `ErrNotFound` → 404, log 5xx with **slog**, load **config** from env. Optional in-memory **register**.

## Run

```bash
cd backend
cp .env.example .env   # optional
go mod tidy
go run ./cmd/server
```

```bash
curl -s http://localhost:8080/api/students/999
# {"error":"student not found"}

curl -s -X POST http://localhost:8080/api/students \
  -H 'Content-Type: application/json' \
  -d '{"first_name":"Ada","last_name":"Lovelace","email":"ada@example.com","course":"SE"}'

curl -s -X POST http://localhost:8080/api/register \
  -H 'Content-Type: application/json' \
  -d '{"first_name":"Ada","last_name":"Lovelace","username":"ada","email":"ada@example.com","password":"secret1"}'
```

No Postgres. Student routes are not JWT-protected yet.
