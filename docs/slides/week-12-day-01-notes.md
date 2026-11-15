# Week 12, Day 1 — presenter notes

Slides: [`week-12-day-01.html`](week-12-day-01.html) → **F** · arrows · **N** · **P**.

**Mutex, WaitGroup, context, races.** Lab = `-race` red → mutex → green. Context signatures + timeout demo + graceful shutdown sketch.

## Timing (3–3.5 hours)

| Clock | Block | Slides |
| --- | --- | --- |
| 0:00–0:15 | Week 11 check | 1–2 |
| 0:15–0:30 | Outcomes + SE | 3–4 |
| 0:30–1:30 | Race, Mutex, RWMutex, WaitGroup | 5–8 |
| 1:30–2:30 | Context, Gin, SMS, shutdown | 9–12 |
| 2:30–end | Lab red→green + demos | 13–end |

Never skip the race FAIL on the projector.

## Live demo

1. `go test -race ./counter/` FAIL → add Mutex → PASS  
2. Timeout demo endpoint  
3. Optional Ctrl+C graceful shutdown  

## Lab gate

- [ ] `-race` green on race-lab  
- [ ] Mutex vs WaitGroup explained  
- [ ] Repo takes `context.Context`; handlers pass `c.Request.Context()`  

## Homework

README documents `go test -race ./...`. PR explains what was red / what fixed it.

## What not to teach

Postgres cancel, deep testing/CI (week 13), “replace every mutex with a channel.”
