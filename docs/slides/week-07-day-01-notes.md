# Week 7, Day 1 — presenter notes

Slides: [`week-07-day-01.html`](week-07-day-01.html) → **F** · arrows · **N** · **P**.

**Structs, JSON tags, in-memory students.** Create + list in lab. Update/delete homework. No JWT / Postgres.

## Timing (3–3.5 hours)

| Clock | Block | Slides |
| --- | --- | --- |
| 0:00–0:15 | Week 6 handlers check | 1–2 |
| 0:15–0:30 | Outcomes + SE framing | 3–4 |
| 0:30–1:15 | Structs, tags, methods, embed light, interfaces, Reader | 5–10 |
| 1:15–2:15 | Store + POST/GET live + Postman | 11–16 |
| 2:15–end | Lab create/list | 17–end |

Cut embedding live and generics-of-interfaces talk. Never skip 400 on bad JSON.

## Live demo

1. `models.Student` with tags  
2. Map store + `StudentHandler.Create` / `List` / `GetByID`  
3. Postman POST → GET list → GET :id → bad JSON 400 → missing id 404  

## Lab gate

- [ ] POST creates (201)  
- [ ] GET list shows it  
- [ ] GET :id / 404  
- [ ] Bad JSON → 400  
- [ ] Health still green  

## Homework

PUT + DELETE. Invalid JSON → 400.

## What not to teach

Postgres, JWT, repository extract (week 8), mutex deep dive.
