# Demo script (8–10 minutes)

Print or keep this open. Hard stop at 10:00.

| Min | You say / do |
| --- | --- |
| 0:00–1:00 | “SMS is a campus staff API: register/login, then CRUD students. Stack: Go, Gin, Postgres, JWT, React client.” |
| 1:00–4:30 | Live: health → register → login → Bearer list/create (Postman **or** React). |
| 4:30–7:00 | Code tour: `routes` / `main` → `AuthMiddleware` → handler → `StudentRepository` SQL `$1`. |
| 7:00–8:30 | Tests: `go test ./...` or CI green. One design choice (e.g. small store interface). |
| 8:30–10:00 | v2: “I’d add pagination / OpenAPI / refresh tokens.” Stop. |

## Backup

If React fails: Postman collection only. If DB empty: register live, don’t apologize for long.
