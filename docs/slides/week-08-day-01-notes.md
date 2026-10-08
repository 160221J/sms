# Week 8, Day 1 — presenter notes

Slides: [`week-08-day-01.html`](week-08-day-01.html) → **F** · arrows · **N** · **P**.

**Pointers, memory pictures, repository layer.** Nil crash → fix → move map into `StudentRepository`. No JWT / Postgres.

## Timing (3–3.5 hours)

| Clock | Block | Slides |
| --- | --- | --- |
| 0:00–0:15 | Week 7 create/list check | 1–2 |
| 0:15–0:30 | Outcomes + SE framing | 3–4 |
| 0:30–1:20 | Pointers, nil, receivers, value/ref, stack/heap/GC | 5–12 |
| 1:20–2:20 | Nil crash live + extract repo | 13–18 |
| 2:20–end | Lab extract | 19–end |

Cut escape-analysis `-m` and make/new if create/list extract eats time. Never skip the nil panic.

## Live demo

1. Register routes with a nil `*StudentHandler` → panic on first request  
2. Fix with `NewStudentHandler(repo)`  
3. Move map into `internal/repository/student_repository.go`  
4. Handler holds `*StudentRepository`; curl create/list still green  

## Lab gate

- [ ] Nil crash seen and fixed  
- [ ] Repo owns the map  
- [ ] Handler has no map fields  
- [ ] Postman create + list + get  
- [ ] Health still green  

## Homework

PR with handler → repository. Memory diagram in the PR (notebook photo OK).

## What not to teach

Postgres/`pgx`, JWT, deep escape analysis, repository interfaces (concrete type is fine).
