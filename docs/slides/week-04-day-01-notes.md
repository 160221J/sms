# Week 4, Day 1 — presenter notes

Slides: open [`week-04-day-01.html`](week-04-day-01.html) → **F** fullscreen → arrows. **N** notes. **P** print/PDF.

This session is **modules, packages, layout, SMS kickoff**. No HTTP. No Gin. No database. The product clock starts.

## Timing (3–3.5 hours)

| Clock | Block | Slides |
| --- | --- | --- |
| 0:00–0:15 | Week 3 homework check | 1–2 |
| 0:15–0:30 | Outcomes + product clock | 3–4 |
| 0:30–1:00 | Packages, imports, export, `internal/` | 5–8 |
| 1:00–1:25 | Modules, `go.mod`, tidy (light) | 9–11 |
| 1:25–2:10 | Layout, `cmd/server`, package jobs (**live** scaffold) | 12–15 |
| 2:10–2:35 | Clean code, README, PR, `.env` | 16–19 |
| 2:35–end | Lab: skeleton + PR URL | 20–end |

Prefer a finished skeleton over a perfect lecture on `go get`. Never skip `.gitignore` for `.env`.

## Live demo script

```bash
mkdir -p ~/epic-go/sms/backend
cd ~/epic-go/sms/backend
go mod init student-management-system
mkdir -p cmd/server internal/{config,handlers,repository,models,routes,middleware,database,utils}
```

`cmd/server/main.go`:

```go
package main

import "fmt"

func main() {
	fmt.Println("sms starting")
}
```

```bash
gofmt -w cmd/server/main.go
go run ./cmd/server
```

Track empty dirs with `.gitkeep` files so Git keeps them.

## Lab gate

- [ ] `go.mod` module `student-management-system`
- [ ] Folder tree matches the course layout
- [ ] `go run ./cmd/server` → `sms starting`
- [ ] README: three product sentences + how to run
- [ ] `.env` gitignored; no binaries
- [ ] PR URL collected

## Homework

Same gate, as a GitHub PR. No Gin yet.

## Typical failures

| Symptom | Fix |
| --- | --- |
| `package … is not in std` | missing / wrong `go.mod` |
| `go run main.go` from repo root | `go run ./cmd/server` from `backend/` |
| empty folders missing on GitHub | add `.gitkeep` |
| `.env` in the PR | remove; fix `.gitignore` |
| module path typos in future imports | keep `student-management-system` consistent |

## What not to teach today

`net/http`, Gin, JSON handlers, PostgreSQL, JWT, structs beyond naming folders, interfaces. Tease week 5 only.
