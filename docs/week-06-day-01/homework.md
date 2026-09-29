# Homework — Week 6, Day 1

Due: _______________ · **GitHub PR** (refactor).

## Required

1. `internal/handlers` package with at least:
   - health handler (`New…` + pointer method)
   - hello handler
   - `FullName(first, last string) string` with tests (trim; no extra spaces)
2. `cmd/server/main.go` mostly wires routes — not a paste of all JSON logic
3. `GET /health` and `GET /api/hello` still 200 on `:8080`
4. `go test ./internal/handlers` green
5. PR description: what moved and why (5–10 lines)
6. `gofmt` clean; no secrets

## Stretch

- `internal/routes` with `Register(r *gin.Engine)` called from `main`
- Table-driven tests for `FullName` (Ada/Lovelace, trim, empty last)

## Not required

JWT, Postgres, student CRUD, new endpoints.

## Marking

| Check | Pass |
| --- | --- |
| PR URL |  |
| Handlers package real |  |
| Health unchanged |  |
| FullName tests green |  |
| Thin main |  |
| Stretch routes package | bonus |
