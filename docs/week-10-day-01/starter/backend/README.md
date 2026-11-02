# Student Management System — Week 10 starter

Same as week 9 (errors, slog, config, optional register) with an explicit rule:

**Do not add `go` inside Create/List/Get.** Keep the request path synchronous.

Concurrency practice lives in `../goroutine-lab/` (race counter + fan-out validate).

```bash
cd backend
go mod tidy
go run ./cmd/server
```
