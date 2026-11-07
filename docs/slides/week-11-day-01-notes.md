# Week 11, Day 1 — presenter notes

Slides: [`week-11-day-01.html`](week-11-day-01.html) → **F** · arrows · **N** · **P**.

**Channels, pipelines, worker pool.** Lab = pool kata. Import API is stretch. Mutex fix still week 12.

## Timing (3–3.5 hours)

| Clock | Block | Slides |
| --- | --- | --- |
| 0:00–0:15 | Week 10 check | 1–2 |
| 0:15–0:30 | Outcomes + SE | 3–4 |
| 0:30–1:30 | Channels, close, select, pipeline | 5–9 |
| 1:30–2:30 | Worker pool + WaitGroup + live | 10–15 |
| 2:30–end | Lab kata / import stretch | 16–end |

Never skip the fixed-N pool. Cut import live if needed.

## Live demo

1. Buffered channel + range  
2. Worker pool hashing strings (`worker-lab`)  
3. Optional: sketch `POST /api/students/import`

## Lab gate

- [ ] Unbuffered vs buffered explained  
- [ ] Pool with fixed N + job channel  
- [ ] WaitGroup join before closing results  
- [ ] No go-per-job  

## Homework

Import endpoint **or** documented kata in `internal/workers/`.

## What not to teach

Mutex race fix, Postgres bulk copy, unbounded fan-out.
