# Student Management System — Week 12 starter

Week 11 base plus:

- **Mutex** on in-memory maps (confirmed)
- **`context.Context`** on repository methods; handlers pass `c.Request.Context()`
- **Timeout demo:** `GET /api/demo/slow?ms=3000` (1s server deadline → canceled)
- **Graceful shutdown** sketch in `cmd/server/main.go`

Primary lab: `../race-lab/` (red → mutex → green).

## Test (homework)

```bash
# race lab
cd ../race-lab
CGO_ENABLED=1 go test -race ./...

# SMS module (no -race package tests yet — week 13 adds them; still document the habit)
cd ../backend
go test -race ./...
```

Ubuntu needs `build-essential` for `-race` (cgo + gcc).

## Run

```bash
go mod tidy
go run ./cmd/server
# Ctrl+C → clean shutdown log

curl -s 'localhost:8080/api/demo/slow?ms=200'     # ok
curl -s 'localhost:8080/api/demo/slow?ms=3000'    # deadline exceeded
```
