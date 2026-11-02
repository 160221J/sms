# Week 10, Day 1 — presenter notes

Slides: [`week-10-day-01.html`](week-10-day-01.html) → **F** · arrows · **N** · **P**.

**Goroutines and the scheduler.** See a data race. Fan-out validation kata. No channels. No mutex fix yet.

## Timing (3–3.5 hours)

| Clock | Block | Slides |
| --- | --- | --- |
| 0:00–0:15 | Week 9 check | 1–2 |
| 0:15–0:30 | Outcomes + SE | 3–4 |
| 0:30–1:30 | Concurrency, go, GMP, leaks, handlers | 5–9 |
| 1:30–2:15 | Race preview + -race live | 10–11, 14–15 |
| 2:15–end | Fan-out lab + quiz start | 12–13, 16–end |

Never skip `-race` red. Do not teach mutex fix today.

## Live demo

1. Tiny `go say` / 10k prints  
2. Shared counter → `go test -race` DATA RACE  
3. Fan-out three validations in starter  

## Lab gate

- [ ] 10k (or similar) goroutine demo run  
- [ ] `-race` red on counter lab  
- [ ] Fan-out validate understood  
- [ ] SMS create still sync + health green  

## Homework

Short quiz. Optional: race evidence on unsafe global map (fix week 12).

## What not to teach

Channels, worker pools, mutex deep-dive, GOMAXPROCS tuning.
