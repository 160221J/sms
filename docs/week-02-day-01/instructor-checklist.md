# Instructor checklist — Week 2, Day 1

## Pack / prepare the night before

- [ ] Slides open locally (`docs/slides/week-02-day-01.html`) — do not depend on GitHub in the room
- [ ] HDMI / dongle, presenter remote, markers, board
- [ ] Printed worksheet + lab sheet (one each per student)
- [ ] Your own `~/epic-go/week02` already working: `zeros.go`, `greet.go`, `names` with green `go test`
- [ ] Week 1 leftover list: who still had no GitHub / wrong `go version`
- [ ] Student URL sheet below (or a Google Form)

## On the board (leave up all day)

```
Declare:   var name type = value
           name := value          (inside func only)
           name = value           (already exists)

Zero:      int 0   string ""   bool false   pointer nil

Convert:   float64(year)     not   year + 0.5

len        = bytes
runes      = utf8.RuneCountInString
```

## During lab

Walk the room. Pair done students with stuck students. Typical: `:=` at package level, missing `*` on flags, `go test` without `go.mod`, arguing about `len("café")`.

Pace valve: skip bitwise live typing if conversions ran long. Never skip zero values or the red→green test.

## Collect before they leave

| # | Student name | GitHub URL (`week02` visible) | Worksheet | `go test` OK |
| --- | --- | --- | --- | --- |
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |
| 6 |  |  |  |  |
| 7 |  |  |  |  |
| 8 |  |  |  |  |
| 9 |  |  |  |  |
| 10 |  |  |  |  |
| 11 |  |  |  |  |
| 12 |  |  |  |  |
| 13 |  |  |  |  |
| 14 |  |  |  |  |
| 15 |  |  |  |  |

## After class

- [ ] Message the batch: homework due date + link to `homework.md` (10 exercises + `TrimSpace` tests)
- [ ] Spot-check 3 repos: `gofmt` clean, `go test` green, no binaries committed
- [ ] Note who still cannot run `go test` for the first 10 minutes of week 3
