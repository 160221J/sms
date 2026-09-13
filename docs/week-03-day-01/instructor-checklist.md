# Instructor checklist — Week 3, Day 1

## Pack / prepare the night before

- [ ] Slides open locally (`docs/slides/week-03-day-01.html`) — do not depend on GitHub in the room
- [ ] HDMI / dongle, presenter remote, markers, board
- [ ] Printed worksheet + lab sheet (one each per student)
- [ ] Your own `~/epic-go/week03` already working: `control.go`, `slices.go`, `freq.go`, `slicekit` with green `go test`
- [ ] Week 2 leftover list: who still had red `FullName` tests
- [ ] Student URL sheet below (or a Google Form)

## On the board (leave up all day)

```
if cond { }          braces required; cond is bool
for { }              only loop keyword
range                i, v := range xs

slice header:        ptr  len  cap
append:              s = append(s, x)     always assign
gotcha:              subslice may share backing array

map:                 m = make(map[K]V)
comma-ok:            v, ok := m[k]
```

## During lab

Two labs. Lab 1 (`Contains` + `Unique`) before Lab 2 (`Freq`). Force paper test tables before coding.

Pace valve: skip variadic/closures live typing if slices ate time. Never skip the backing-array demo or comma-ok.

Typical: forgot `s = append(...)`, nil map write, asserting map print order, `Unique` that sorts or drops first occurrence.

## Collect before they leave

| # | Student name | GitHub URL (`week03` visible) | Worksheet | Paper table | `go test` OK |
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

- [ ] Message the batch: homework due date + link to `homework.md`
- [ ] Spot-check 3 repos: `gofmt` clean, `go test` green, no binaries committed
- [ ] Note who cannot explain the slice gotcha — first 5 minutes of week 4
