# Week 10, Day 1 — full kit

**Goroutines and the scheduler.** Observe races. Fan-out validation kata. Keep SMS create synchronous.

**PDFs:** [`pdf/`](pdf/) — Epic Learn logo + footer *Epic Learn Institute of Higher Education - Go Programming Master Course*.

| PDF | Use |
| --- | --- |
| [week-10-day-01-slides.pdf](pdf/week-10-day-01-slides.pdf) | Projector |
| [week-10-day-01-slides.pptx](pdf/week-10-day-01-slides.pptx) | Editable PPTX |
| [student-handout.pdf](pdf/student-handout.pdf) | Students |
| [lab-sheet.pdf](pdf/lab-sheet.pdf) | Lab gate |
| [week-10-day-01-notes.pdf](pdf/week-10-day-01-notes.pdf) | Script |
| [troubleshooting.pdf](pdf/troubleshooting.pdf) | Room walk |
| [homework.pdf](pdf/homework.pdf) | Quiz |
| [pre-class.pdf](pdf/pre-class.pdf) | Send ahead |
| [instructor-checklist.pdf](pdf/instructor-checklist.pdf) | Packing |

```bash
./docs/week-10-day-01/generate.sh
```

| Who | Open |
| --- | --- |
| Presenting | [../slides/week-10-day-01.html](../slides/week-10-day-01.html) |
| Students | [student-handout.html](student-handout.html) |
| Lab | [lab-sheet.html](lab-sheet.html) |
| Homework | [homework.md](homework.md) |
| Race + fan-out kata | [starter/goroutine-lab/](starter/goroutine-lab/) |
| SMS (still sync) | [starter/backend/](starter/backend/) |

**Gate:** `-race` shows DATA RACE on the counter lab; SMS create stays sync.
