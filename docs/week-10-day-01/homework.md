# Homework — Week 10, Day 1

Due: _______________ · **GitHub PR** (quiz answers in the description or a `quiz.md`)

## Already done in lab

- Saw `-race` DATA RACE on the counter  
- Fan-out validation kata ran  
- SMS create still synchronous  

## Required quiz (short answers)

1. Concurrency vs parallelism — one sentence each.  
2. What does `go f()` do? Does it wait for `f` to finish?  
3. Why must HTTP handlers not use a naked `go` for Create?  
4. Name G, M, and P in the Go scheduler poster.  
5. What command detects data races in tests?

## Optional

If your in-memory student store can race under concurrent tests, paste `go test -race` output. **Do not require a mutex fix** unless you already know it — week 12.

## Marking

| Check | Pass |
| --- | --- |
| Quiz answers clear |  |
| No naked `go` sneaked into Create |  |
| Optional race evidence (if claimed) |  |
