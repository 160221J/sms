# Week 9, Day 1 — full kit

**Errors, wrapping, validation, slog, JWT preview.** Consistent `{"error":"..."}`. No DB. Auth register is stretch.

**PDFs:** [`pdf/`](pdf/) — Epic Learn logo + footer *Epic Learn Institute of Higher Education - Go Programming Master Course*.

| PDF | Use |
| --- | --- |
| [week-09-day-01-slides.pdf](pdf/week-09-day-01-slides.pdf) | Projector |
| [week-09-day-01-slides.pptx](pdf/week-09-day-01-slides.pptx) | Editable PPTX |
| [student-handout.pdf](pdf/student-handout.pdf) | Students |
| [lab-sheet.pdf](pdf/lab-sheet.pdf) | Lab gate |
| [week-09-day-01-notes.pdf](pdf/week-09-day-01-notes.pdf) | Script |
| [troubleshooting.pdf](pdf/troubleshooting.pdf) | Room walk |
| [homework.pdf](pdf/homework.pdf) | slog + env |
| [pre-class.pdf](pdf/pre-class.pdf) | Send ahead |
| [instructor-checklist.pdf](pdf/instructor-checklist.pdf) | Packing |

```bash
./docs/week-09-day-01/generate.sh
```

| Who | Open |
| --- | --- |
| Presenting | [../slides/week-09-day-01.html](../slides/week-09-day-01.html) |
| Students | [student-handout.html](student-handout.html) |
| Lab | [lab-sheet.html](lab-sheet.html) |
| Homework | [homework.md](homework.md) |
| Starter | [starter/backend/](starter/backend/) |

**Gate:** missing student → 404 via `ErrNotFound`; 5xx logged with slog.
