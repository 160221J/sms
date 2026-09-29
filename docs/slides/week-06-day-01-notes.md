# Week 6, Day 1 — presenter notes

Slides: [`week-06-day-01.html`](week-06-day-01.html) → **F** · arrows · **N** notes · **P** print.

**Functions and methods inside SMS.** Refactor week 5 into `handlers`. No new product feature required.

## Timing (3–3.5 hours)

| Clock | Block | Slides |
| --- | --- | --- |
| 0:00–0:15 | Health check from week 5 | 1–2 |
| 0:15–0:30 | Outcomes + why refactor | 3–4 |
| 0:30–1:10 | Function parts, value, multi-return, defer | 5–8 |
| 1:10–1:40 | Methods, New…, pointer preview, generics light | 9–12 |
| 1:40–2:20 | **Live** extract handlers + FullName test | 13–16 |
| 2:20–end | Lab + PR | 17–end |

Never skip green health after the move. Cut generics live typing first if late.

## Live demo

1. Confirm `curl -i :8080/health` is 200.
2. Create `internal/handlers/health.go` + `hello.go` with `New…` and pointer methods.
3. Thin `main` wires `r.GET`.
4. Add `FullName` + test; `go test ./internal/handlers`.

## Lab gate

- [ ] Health + hello still 200
- [ ] Logic in `internal/handlers`
- [ ] `go test ./internal/handlers` green for `FullName`
- [ ] PR describes the refactor

## Homework

Same gate as PR. Stretch: `internal/routes` register function.

## Typical failures

| Symptom | Fix |
| --- | --- |
| import cycle | handlers must not import main/routes that import handlers wrongly |
| `undefined: handlers` | module path + folder under `internal/handlers` |
| health JSON changed | copy exact keys |
| tests not found | `go test ./internal/handlers` from `backend/` |

## What not to teach

Student CRUD, JWT, Postgres, deep pointer theory, interfaces. Tease week 7 only.
