# Student Management System — Week 7 starter

In-memory students: create, list, get by id. Update/delete included as homework reference — try them yourself first.

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

No Postgres. No JWT. Restart clears the map.
