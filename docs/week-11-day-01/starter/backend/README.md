# Student Management System — Week 11 starter

Week 9/10 base (errors, slog, sync Create) plus:

- **Stretch:** `POST /api/students/import` — worker pool over a JSON array → `{created, failed}`
- **Homework option B:** `internal/workers` hash pool kata

Primary lab kata lives in `../worker-lab/`.

```bash
cd backend
go mod tidy
go run ./cmd/server

curl -s -X POST localhost:8080/api/students/import \
  -H 'Content-Type: application/json' \
  -d '[{"first_name":"Ada","email":"ada@example.com","course":"SE"},{"first_name":"","email":"x","course":""}]'
```
