# Instructor checklist — Week 4, Day 1

## Pack / prepare

- [ ] Slides local: `docs/slides/week-04-day-01.html`
- [ ] HDMI / remote / markers
- [ ] Printed lab sheet (one per student)
- [ ] Your own `~/epic-go/sms/backend` already prints `sms starting`
- [ ] Week 3 leftover list: who still had red homework tests
- [ ] URL sheet below

## On the board (leave up)

```
module  = go.mod name / import prefix
package = one folder, one package clause
internal/  = app code (compiler boundary)
cmd/server = main only

go run ./cmd/server   →  sms starting

.gitignore must include .env
```

## During lab

Walk the room. Typical: wrong directory for `go run`, missing `.gitkeep`, no `go.mod`, trying to add Gin early.

Pace valve: skip deep `go get` if scaffold runs long. Never skip `.env` gitignore.

## Collect before they leave

| # | Student | GitHub PR URL | `sms starting` | README | `.env` absent |
| --- | --- | --- | --- | --- | --- |
| 1 |  |  |  |  |  |
| 2 |  |  |  |  |  |
| 3 |  |  |  |  |  |
| 4 |  |  |  |  |  |
| 5 |  |  |  |  |  |
| 6 |  |  |  |  |  |
| 7 |  |  |  |  |  |
| 8 |  |  |  |  |  |
| 9 |  |  |  |  |  |
| 10 |  |  |  |  |  |
| 11 |  |  |  |  |  |
| 12 |  |  |  |  |  |
| 13 |  |  |  |  |  |
| 14 |  |  |  |  |  |
| 15 |  |  |  |  |  |

## After class

- [ ] Message due date for unfinished PRs
- [ ] Spot-check 3 PRs: `gofmt`, tree, no secrets
- [ ] Note who has no GitHub collaborator invite for week 5
