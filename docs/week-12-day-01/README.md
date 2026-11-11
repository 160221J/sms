# Week 12, Day 1 — full kit

**Mutex, WaitGroup, context, races.** Lab: race detector red → mutex → green. SMS: lock map (confirm), pass `context.Context` into repo methods, timeout demo, graceful shutdown sketch.

**PDFs:** [`pdf/`](pdf/) — Epic Learn logo + footer *Epic Learn Institute of Higher Education - Go Programming Master Course*.

| PDF | Use |
| --- | --- |
| [week-12-day-01-slides.pdf](pdf/week-12-day-01-slides.pdf) | Projector |
| [week-12-day-01-slides.pptx](pdf/week-12-day-01-slides.pptx) | Editable PPTX |
| [student-handout.pdf](pdf/student-handout.pdf) | Students |
| [lab-sheet.pdf](pdf/lab-sheet.pdf) | Lab gate |
| [week-12-day-01-notes.pdf](pdf/week-12-day-01-notes.pdf) | Script |
| [troubleshooting.pdf](pdf/troubleshooting.pdf) | Room walk |
| [homework.pdf](pdf/homework.pdf) | `-race` in README |
| [pre-class.pdf](pdf/pre-class.pdf) | Send ahead |
| [instructor-checklist.pdf](pdf/instructor-checklist.pdf) | Packing |

```bash
./docs/week-12-day-01/generate.sh
```

| Who | Open |
| --- | --- |
| Presenting | [../slides/week-12-day-01.html](../slides/week-12-day-01.html) |
| Students | [student-handout.html](student-handout.html) |
| Lab | [lab-sheet.html](lab-sheet.html) |
| Homework | [homework.md](homework.md) |
| Race lab | [starter/race-lab/](starter/race-lab/) |
| SMS + context | [starter/backend/](starter/backend/) |

**Gate:** `go test -race ./...` green on race-lab; handlers pass request context.
