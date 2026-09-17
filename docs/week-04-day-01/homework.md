# Homework — Week 4, Day 1

Due: **before the next session** (date _______________).

Submit a **GitHub pull request** (not a zip, not WhatsApp photos).

## Deliverable

SMS backend skeleton:

```
backend/
  go.mod
  .gitignore
  .env.example
  README.md
  cmd/server/main.go
  internal/config/.gitkeep
  internal/handlers/.gitkeep
  internal/repository/.gitkeep
  internal/models/.gitkeep
  internal/routes/.gitkeep
  internal/middleware/.gitkeep
  internal/database/.gitkeep
  internal/utils/.gitkeep
```

## Requirements

1. `go.mod` module path: `student-management-system` (or your fork’s consistent module path — tell me in the PR if different).
2. `go run ./cmd/server` prints exactly: `sms starting`
3. README includes:
   - three sentences on what SMS is
   - Go version
   - how to run the server command above
4. `.gitignore` includes `.env` and common binaries
5. `.env.example` has placeholder keys only (`PORT`, `DATABASE_URL`, `JWT_SECRET`) — empty values OK
6. `gofmt` clean
7. **No** Gin, **no** HTTP handlers, **no** real secrets

## PR checklist

| Check | Pass |
| --- | --- |
| Branch + PR URL sent |  |
| Tree matches layout |  |
| `sms starting` works |  |
| README usable by a classmate |  |
| `.env` not in the PR |  |
| No third-party deps required |  |

## Optional (bonus)

One short PR paragraph: why `internal/` exists in Go, in your own words.

Instructor merges only if `gofmt` is clean and `.env` is not committed.
