# Week 3, Day 1 — full kit

Everything needed to teach and sit Week 3. **No SMS code today.** Control flow, slices, maps, and just enough functions — with two labs and `go test`.

**Print these (PDFs):** [`pdf/`](pdf/) — every page has the Epic Learn logo header and the footer *Epic Learn Institute of Higher Education - Go Programming Master Course*.

| PDF | Use |
| --- | --- |
| [week-03-day-01-slides.pdf](pdf/week-03-day-01-slides.pdf) | Projector / student copy of the deck |
| [week-03-day-01-slides.pptx](pdf/week-03-day-01-slides.pptx) | Editable PowerPoint (text boxes + logo). Rebuild: `python3 docs/week-03-day-01/build_editable_pptx.py` |
| [student-handout.pdf](pdf/student-handout.pdf) | Give every student |
| [lab-sheet.pdf](pdf/lab-sheet.pdf) | Gate before they leave |
| [worksheet.pdf](pdf/worksheet.pdf) | Control + slice gotcha + comma-ok (fill in class) |
| [week-03-day-01-notes.pdf](pdf/week-03-day-01-notes.pdf) | Your script |
| [troubleshooting.pdf](pdf/troubleshooting.pdf) | Walk the room |
| [homework.pdf](pdf/homework.pdf) | After class — slice/map exercises |
| [pre-class.pdf](pdf/pre-class.pdf) | Send 2–3 days before |
| [instructor-checklist.pdf](pdf/instructor-checklist.pdf) | Packing + URL sheet |

Regenerate on Ubuntu (PEP 668 — do **not** `pip install --user` into system Python):

```bash
sudo apt install python3-venv python3-full
# Google Chrome or Chromium must be on PATH (for PDFs)
./docs/week-03-day-01/generate.sh
```

PowerPoint only (no Chrome): `./docs/week-03-day-01/generate.sh --pptx-only`

| Who | Open / print |
| --- | --- |
| Instructor presenting | [../slides/week-03-day-01.html](../slides/week-03-day-01.html) (F fullscreen, N notes, P PDF) |
| Instructor script | [../slides/week-03-day-01-notes.md](../slides/week-03-day-01-notes.md) |
| Instructor packing + URL sheet | [instructor-checklist.md](instructor-checklist.md) |
| Night before | [pre-class.md](pre-class.md) |
| Students (print) | [student-handout.html](student-handout.html) |
| Students lab gate | [lab-sheet.html](lab-sheet.html) |
| Students fill-in | [worksheet.md](worksheet.md) |
| When something breaks | [troubleshooting.md](troubleshooting.md) |
| Homework | [homework.md](homework.md) |
| Reference only (after they type it) | [starter/](starter/) |

**Gate:** nobody leaves without a filled worksheet, a paper test table for `Contains`, and green `go test` on `Contains`, `Unique`, and `Freq`.
