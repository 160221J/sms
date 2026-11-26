# Student Management System — Week 14 starter

Week 13 testing base + **PostgreSQL via pgx**.

- `migrations/001_init.sql` — `users` + `students`
- `internal/database` — pgx pool
- `StudentRepository` — parameterized CRUD (`$1`…)
- Fake store still for unit tests (no DB required)
- Users remain in-memory until homework (prefer migrate register to `users`)

## Setup

```bash
# create DB
createdb sms   # or Docker Postgres with POSTGRES_DB=sms

psql -d sms -f migrations/001_init.sql

cp .env.example .env
# edit DB_* as needed

go mod tidy
go run ./cmd/server
```

## Test (no Postgres required for unit tests)

```bash
go test ./...
go vet ./...
```

Injection kata (separate module):

```bash
cd ../sql-lab && go test -v ./inject/
```

## Prove persistence

```bash
curl -s -X POST localhost:8080/api/students \
  -H 'Content-Type: application/json' \
  -d '{"first_name":"Ada","last_name":"Lovelace","email":"ada@example.com","course":"SE"}'

curl -s localhost:8080/api/students
# Ctrl+C server, start again, GET again — rows remain
```
