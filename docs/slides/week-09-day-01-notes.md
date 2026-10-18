# Week 9, Day 1 — presenter notes

Slides: [`week-09-day-01.html`](week-09-day-01.html) → **F** · arrows · **N** · **P**.

**Errors, wrapping, validation, slog, JWT preview.** Lab: `ErrNotFound` → 404. Homework: slog + `.env.example`. Auth register is stretch.

## Timing (3–3.5 hours)

| Clock | Block | Slides |
| --- | --- | --- |
| 0:00–0:15 | Week 8 repo check | 1–2 |
| 0:15–0:30 | Outcomes + SE framing | 3–4 |
| 0:30–1:30 | error, sentinel, wrap, HTTP map, validation, slog, config | 5–11 |
| 1:30–2:00 | Auth/JWT light + milestone | 12–14 |
| 2:00–2:40 | Live ErrNotFound + slog | 15–16 |
| 2:40–end | Lab | 17–end |

Cut register live and JWT deep-dive if mapping eats time. Never skip 404 vs 500.

## Live demo

1. Repo returns `ErrNotFound`; handler `errors.Is` → 404  
2. Unexpected path → 500 + `slog.Error` JSON line  
3. Optional: `POST /api/register` with bcrypt (no student-route lock)

## Lab gate

- [ ] `ErrNotFound` + repo returns it  
- [ ] Missing id → 404 JSON  
- [ ] Unexpected → 500 + slog  
- [ ] Bad JSON / bind → 400  
- [ ] Health green  

## Homework

Replace `fmt.Println` with `slog`. Add `.env.example` + `internal/config`.

## What not to teach

Postgres, full JWT middleware on students, panic-as-control-flow.
