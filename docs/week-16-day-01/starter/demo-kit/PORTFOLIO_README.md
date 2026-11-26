# Student Management System (SMS)

Campus staff API: register/login with JWT, then create / list / update / delete students. React + Vite client talks to the Go API.

## Stack

- Go · Gin · PostgreSQL (`pgx`) · JWT (HS256) · bcrypt  
- Frontend (provided): React + Vite  

## Run

```bash
# Postgres
createdb sms
psql -d sms -f backend/migrations/001_init.sql

# Backend
cd backend
cp .env.example .env   # set DB_* and JWT_SECRET locally — never commit real secrets
go run ./cmd/server

# Frontend
cd frontend
echo 'VITE_API_URL=http://localhost:8080' > .env
npm install && npm run dev
```

## Env vars (names only)

`PORT`, `JWT_SECRET`, `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`, `VITE_API_URL`

## Example curls

```bash
curl -s localhost:8080/health

curl -s -X POST localhost:8080/api/register -H 'Content-Type: application/json' \
  -d '{"first_name":"Ada","last_name":"Lovelace","username":"ada","email":"ada@example.com","password":"secret123"}'

TOKEN=$(curl -s -X POST localhost:8080/api/login -H 'Content-Type: application/json' \
  -d '{"username":"ada","password":"secret123"}' | jq -r .token)

curl -s -H "Authorization: Bearer $TOKEN" localhost:8080/api/students
```

## Architecture

Browser → Vite → Gin → JWT middleware → handler → repository → Postgres → JSON.

## Tests / CI

```bash
cd backend && go test ./...
```

CI: GitHub Actions workflow on push/PR.

## What I’d do in v2

1. Pagination + filtering on `GET /api/students`  
2. OpenAPI / generated client docs  
3. Refresh tokens (shorter access JWT lifetime)  
