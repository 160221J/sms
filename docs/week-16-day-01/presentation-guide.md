# Week 16, Day 1 — Presentation guide (all slides)

**Deck:** `docs/slides/week-16-day-01.html` (26 slides)  
**Theme:** Review, Go design, refactor, demo — polish and ship.

**How to present:** Fullscreen (**F**) · arrows · **N** notes · **P** presenter view.

**Suggested timing (3–3.5 h)**

| Block | Slides | Focus |
| --- | --- | --- |
| Open | 1–5 | Bridge, outcomes, rubric |
| Polish + design | 6–10 | Errors, refactor, Go idioms |
| Demo setup | 11–13 | Compose stretch, format, milestone |
| Live + lab | 14–18 | Model demo, refactor win, self-review, pitfalls, gate |
| Close | 19–26 | Portfolio, vocabulary, limits, grading, Q&A |

**One sentence for the day:** Ship is a review, not a feature dump.

---

## Slide 1 — Title

**Say:** Final week. We polish, walk the layers, demo for 8–10 minutes, merge `main`.

---

## Slide 2 — Since last week

Auth + React path done. Today: rubric, errors/logs, design lens, demos.

**Do:** Spot-check one team can still login → list.

---

## Slide 3 — Outcomes

Self-review, errors/JSON pass, name Go design choices, 8–10 min demo, portfolio README + v2 list.

---

## Slide 4 — SE frame

Quality bar from COURSE.md. No homework after demo. Compose is stretch only.

---

## Slide 5 — Rubric (8 points)

Walk each line. Optionally score a volunteer PR on the projector.

---

## Slide 6 — Errors and logging pass

Prefer `slog` + `{"error":"..."}`. Wrap with `%w`. Never panic on bad input; never log passwords.

---

## Slide 7 — Refactor pass

Dead code out. One JSON error shape. Rename vague identifiers. `gofmt` + `go vet`.

---

## Slide 8 — Go design (SOLID as lens only)

Small interfaces · composition · accept interfaces, return structs · package clarity · a little copying beats a little dependency.

**Do not** grade SOLID acronyms.

---

## Slide 9 — Accept interfaces, return structs

Show `StudentStore` interface + concrete constructor. Point at week-13 fakes.

---

## Slide 10 — Package clarity

`cmd/server` + `internal/{handlers,repository,middleware,models,...}`. Muddy placement = muddy responsibility.

---

## Slide 11 — Docker Compose stretch

Sketch only. Do not block demos on Docker.

---

## Slide 12 — Demo format 8–10 min

Product → live path → code tour → tests/design → v2. Hard stop.

---

## Slide 13 — Milestone

Demo + merged `main` + retrospective (pagination, OpenAPI, refresh tokens).

---

## Slide 14 — Live: instructor model

Run the 8-minute script once so they feel the pace.

---

## Slide 15 — Live: one error-shape fix

`c.String(500, err.Error())` → JSON + slog.

---

## Slide 16 — Lab: self-review

`starter/review-lab/checklist.md`. Silent work, then pair share.

---

## Slide 17 — Pitfalls

Empty demo DB, secrets in README, feature spam, unexplained AI code, overtime.

---

## Slide 18 — Lab gate

Checklist · one refactor · rehearsed script · portfolio draft.

---

## Slide 19 — Portfolio README

What / stack / run / env names / curls / architecture / tests / v2.

---

## Slide 20 — Words

Layer · idiom · retrospective · portfolio.

---

## Slide 21 — Layout

review-lab, refactor-lab, demo-kit, docker-compose.yml.

---

## Slide 22 — Honest limits

Not K8s. Not React course. Not SOLID letter grades. Compose optional.

---

## Slide 23 — Safety

No secrets; no password logs; AI explainability.

---

## Slide 24 — Review bar

Clear request→DB story; rubric mostly green; merge-ready; spoken v2.

---

## Slide 25 — Grading

Final SMS weeks 14–16 = 25%. Weekly PRs already banked.

---

## Slide 26 — Questions

Then: self-review → refactor → rehearse → demo.

---

## Appendix — Demo cheat sheet

```bash
# Instructor machine
cd backend && go test ./... && go run ./cmd/server
# Follow starter/demo-kit/demo-script.md with a visible timer
```

## Appendix — Q&A

**Q: Must we finish Students.jsx?**  
A: No. Stub is OK if Postman path is solid.

**Q: Must Compose work?**  
A: No. Stretch only.

**Q: Can we use Copilot?**  
A: Yes — if you can explain every line you show.

---

*Teaching aid for Week 16 Day 1 presentation.*
