# Student Management System — Week 15 starter

Week 14 Postgres base + **JWT auth**, **Bearer middleware**, **CORS** for Vite.

- `internal/utils/jwt.go` — HS256 issue/validate
- `internal/middleware/auth_middleware.go` — `Authorization: Bearer …`
- Student routes under protected `/api` group; `/api/register` + `/api/login` public
- CORS allows `http://localhost:5173`
- Login returns `{ token, user }` for the React app

Users in this starter remain **in-memory** (fast lab). Prefer Postgres `users` if you finished week-14 homework A.

## Setup

```bash
# Postgres + migration (from week 14)
createdb sms 2>/dev/null || true
psql -d sms -f migrations/001_init.sql

cp .env.example .env
# set JWT_SECRET=dev-only-change-me
# set DB_* 

go mod tidy
go run ./cmd/server
```

## Auth smoke

```bash
curl -s -X POST localhost:8080/api/register -H 'Content-Type: application/json' \
  -d '{"first_name":"Ada","last_name":"Lovelace","username":"ada","email":"ada@example.com","password":"secret123"}'

TOKEN=$(curl -s -X POST localhost:8080/api/login -H 'Content-Type: application/json' \
  -d '{"username":"ada","password":"secret123"}' | python3 -c 'import sys,json; print(json.load(sys.stdin)["token"])')

curl -si localhost:8080/api/students | head -1          # 401
curl -s -H "Authorization: Bearer $TOKEN" localhost:8080/api/students
```

## Frontend (repo root)

```bash
cd ../../../frontend   # or repo frontend/
echo 'VITE_API_URL=http://localhost:8080' > .env
npm install && npm run dev
```

## Test

```bash
go test ./...
```
