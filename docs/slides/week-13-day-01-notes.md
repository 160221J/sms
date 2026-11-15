# Week 13, Day 1 — presenter notes

Slides: [`week-13-day-01.html`](week-13-day-01.html) → **F** · arrows · **N** · **P**.

**Testing and code quality.** Lab = table-driven `YYYY-MM-DD` parse. SMS = FullName + health httptest + fake store + CI.

## Timing (3–3.5 hours)

| Clock | Block | Slides |
| --- | --- | --- |
| 0:00–0:20 | Bridge + outcomes | 1–4 |
| 0:20–1:20 | Table-driven, date, FullName | 5–7 |
| 1:20–2:20 | httptest, fakes, vet/cover | 8–10 |
| 2:20–end | Delve skim, CI, lab | 11–end |

Never skip “interfaces exist so you can fake.”

## Live demo

1. date-lab table tests  
2. Health httptest  
3. Create with FakeStudentStore  
4. Show `ci.yml`  

## Lab gate

- [ ] Date parse table green  
- [ ] FullName + health tests  
- [ ] One handler + fake  
- [ ] `go vet` clean; CI file present  

## Homework

≥5 tests + GitHub Actions (gofmt, vet, test). PR quality notes.

## What not to teach

Postgres, mock frameworks, 100% coverage theater.
