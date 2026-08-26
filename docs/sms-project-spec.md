# SMS demo project spec

This is the capstone for the Epic Learn **Go Programming Master Course**. The codebase is this repository (`160221J/sms`). The full week-by-week plan is in [`COURSE.md`](../COURSE.md).

## Product

Student Management System for campus staff:

- Staff **register** and **login** (JWT).
- Authenticated staff **CRUD students** (name, email, phone, course, date of birth).
- Simple React client for login/register/dashboard. Student UI is a stretch.

## Architecture (target)

```
browser / Postman
    → Gin (:8080)
        → middleware (CORS, JWT)
        → handlers
        → repository
        → PostgreSQL (sms)
```

| Package | Role |
| --- | --- |
| `cmd/server` | Process entry, CORS, listen |
| `internal/config` | Env: DB, JWT, port |
| `internal/database` | `pgx` pool |
| `internal/routes` | `/health`, `/api/register`, `/api/login`, `/api/students` |
| `internal/handlers` | HTTP + validation |
| `internal/repository` | SQL |
| `internal/models` | DTOs and entities |
| `internal/middleware` | Bearer JWT |
| `internal/utils` | JWT sign/verify |
| `frontend/` | Vite React client (not the grading core) |

## Classroom build order

Git history built auth early. **Class order** (so week 5 has a demo without functions/SQL mastery):

1. Weeks 4–5: module layout, `GET /health`
2. Weeks 6–8: functions, student structs, in-memory CRUD, repository
3. Week 9: errors, `slog`, config
4. Weeks 10–12: races, mutex, context; optional bulk import
5. Week 13: tests + CI
6. Week 14: PostgreSQL + migrations
7. Week 15: JWT, protect routes, run `frontend/`
8. Week 16: review and demo

## Definition of done (week 16)

- [ ] Register, login, student CRUD against PostgreSQL
- [ ] JWT on student routes
- [ ] Parameterized SQL; schema in `backend/migrations/`
- [ ] `.env` gitignored; `.env.example` present
- [ ] `gofmt` + `go test ./...`
- [ ] README with run steps and example `curl`
- [ ] Oral walkthrough of one request

## Known WIP gaps (assign these)

- `frontend/src/pages/Students.jsx` is a stub
- `internal/handlers/dashboard_handler.go` is empty
- No `*_test.go` files
- Logging is still `log` / Gin default, not `slog`
- No GitHub Actions yet
