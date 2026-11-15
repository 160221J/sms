# Week 13, Day 1 — Presentation guide (all slides)

**Deck:** `docs/slides/week-13-day-01.html` (26 slides)  
**Theme:** Testing and code quality — table-driven tests, httptest, fakes, vet, coverage, CI.

**How to present:** Fullscreen (**F**) · arrows · **N** notes · **P** presenter view.

**Suggested timing (3–3.5 h)**

| Block | Slides | Focus |
| --- | --- | --- |
| Open | 1–4 | Bridge from week 12 + why tests/CI |
| Core ideas | 5–13 | Tables, dates, FullName, httptest, fakes, vet, Delve, CI |
| Live + lab | 14–18 | date-lab, health, Create+fake, pitfalls, gate |
| Close | 19–26 | Homework, vocabulary, limits, Q&A |

**One sentence for the day:** Interfaces exist so you can fake; CI exists so red never merges quietly.

---

## Slide 1 — Title

**On screen:** Week 13, Day 1 — Testing and code quality.

**Say:** They’ve seen `go test` since week 2. Today they **own** it: table-driven tests, httptest, fakes, vet, cover, and GitHub Actions.

**Do:** Don’t open Postgres talk. This week is proof and quality gates.

---

## Slide 2 — Since last week

**On screen:** Green `-race`. Now prove behavior with tests.

**Explain:**
- Mutex + context signatures are in place.
- Known gap: almost no `*_test.go` beside SMS packages — students fill it.
- Today’s stack: table-driven → httptest → interface+fake → vet/cover → CI.

**Ask:** “Who still runs `-race` before a PR?” — keep the habit; add tests beside it.

---

## Slide 3 — Outcomes

**Contract:**
1. Table-driven tests with `t.Run`.
2. Gin via `httptest` (health + one student handler).
3. Swap repo for an in-memory **fake** via an **interface**.
4. `go vet` + `go test -cover`.
5. One Delve breakpoint (skim).
6. Ship CI: gofmt, vet, test.

**Homework preview:** ≥5 tests + green workflow.

---

## Slide 4 — Software engineering frame

**On screen:** Tests are how the next you trusts this code.

**Say out loud:** “Interfaces exist so you can fake dependencies. CI exists so red never merges quietly.”

**SMS milestone:** `FullName`, date/validation, `GET /health`, fake-backed handler, CI file.

---

## Slide 5 — testing · t.Run · table-driven

**On screen:** cases slice + `t.Run`.

**Teach the shape:**
- Name every case.
- One assertion style: `got` vs `want`.
- Fail with `t.Fatalf` including inputs.

**Anti-pattern:** one giant test with 12 `if`s and no subtests.

---

## Slide 6 — Lab seed: Parse YYYY-MM-DD

**On screen:** layout is `2006-01-02`, **not** the letters `YYYY-MM-DD`.

**Hammer the footgun:** Go’s reference time is the layout. Using `"YYYY-MM-DD"` as layout fails.

**Table ideas:** valid, empty, wrong shape, invalid month, the mistaken layout string itself.

**Bridge:** Same parse used for CreateStudent date-of-birth in the real SMS path / starter.

---

## Slide 7 — FullName

**On screen:** pure function / `FullNameOf` — easiest win.

**Rules (week 2/6):** trim; empty last → first only; both empty → `""`.

**Do:** table-driven tests next to `models` before touching HTTP.

---

## Slide 8 — httptest

**On screen:** `gin.New` → register route → `httptest` recorder → `ServeHTTP`.

**Explain:** No real port / `Listen`. In-process HTTP is enough.

**Order:** health first (simple JSON), then one student handler.

**Common fail:** forgot to register the route → 404.

---

## Slide 9 — Interfaces + fakes (core SE slide)

**On screen:** `StudentStore` interface; real repo vs `FakeStudentStore`.

**Board drawing:**
```text
Handler ──► StudentStore ◄── Fake (tests)
                ▲
                └── StudentRepository (production)
```

**Say:** This is why interfaces exist in this course — not ceremony.

**Handler constructor takes the interface**, not only `*StudentRepository`.

---

## Slide 10 — go vet · cover

**Commands:**
```bash
go vet ./...
go test ./... -cover
gofmt -l .    # must be empty in CI
```

**Say:** Coverage is a **signal**, not a religion. Aim to cover the new tests you write.

Show cover once on the projector.

---

## Slide 11 — Delve (skim)

**Goal:** one breakpoint in a handler; see locals once.

```bash
dlv test ./internal/handlers
# break …Create · continue · next · print req
```

**Cut** if the lab needs time. Not a Delve mastery day.

---

## Slide 12 — CI (GitHub Actions)

**On screen:** gofmt → vet → `go test ./...`.

**Explain:** Starter ships `.github/workflows/ci.yml` under the backend module (move to repo root when they adopt it).

Badge optional. `-race` optional on CI if cgo is painful — local `-race` still required from week 12 habit.

---

## Slide 13 — SMS milestone checklist

- [ ] FullName tests  
- [ ] Date / validation table tests  
- [ ] Health httptest  
- [ ] One student handler + fake store  
- [ ] CI workflow committed  

Five tests minimum for homework.

---

## Slide 14 — Live demo: table-driven date-lab

```bash
cd docs/week-13-day-01/starter/date-lab
go test ./...
go test -v ./parse/
```

Optional teaching vibe: break one case first, then fix.

---

## Slide 15 — Live demo: health httptest

```bash
cd docs/week-13-day-01/starter/backend
go test ./internal/handlers/ -v -run Health
```

Point at `Code == 200` and JSON `status: ok`.

---

## Slide 16 — Live demo: Fake + Create

```bash
go test ./internal/handlers/ -v -run Create
```

**Point at:** fake’s `Creates` counter and `full_name` in the response — proof the handler used the fake, not magic.

---

## Slide 17 — Pitfalls

| Bug | Fix |
| --- | --- |
| Layout `"YYYY-MM-DD"` | Use `"2006-01-02"` |
| httptest 404 | Register route on test engine |
| Concrete-only handler | Depend on `StudentStore` |
| CI without gofmt | `gofmt -l .` step |
| Giant test | `t.Run` per case |

---

## Slide 18 — Lab gate

- [ ] Date-lab green  
- [ ] FullName + health green  
- [ ] Handler test with fake  
- [ ] `go vet` clean  
- [ ] CI workflow file present  

---

## Slide 19 — Homework

1. ≥5 tests across packages.  
2. GitHub Actions: gofmt, vet, test.  
3. PR quality notes (what you covered; optional cover %).

---

## Slide 20 — Next session

Week 14 — PostgreSQL, migrations, parameterized queries, injection demo. Green tests will catch schema mistakes.

---

## Slide 21 — Words to keep

**Cold-call:**
1. Table-driven? → cases + `t.Run`.  
2. httptest? → in-process HTTP without Listen.  
3. Fake? → test double behind an interface.  
4. CI? → gofmt · vet · test on every PR.

---

## Slide 22 — Layout reminder

```
docs/week-13-day-01/starter/
  date-lab/                      # start here
  backend/
    internal/models/             # FullName + ParseDate
    internal/repository/         # interface + fake
    internal/handlers/*_test.go
    .github/workflows/ci.yml
```

---

## Slide 23 — Honest limits

Not Postgres. Not 100% coverage theater. Not mock frameworks — hand-written fakes only. Not mastering Delve.

---

## Slide 24 — Safety

`example.com` fixtures. `gofmt`; ignore `cover.out`. CI on PRs, not only laptops.

---

## Slide 25 — Review bar

Merge when: ≥5 meaningful tests; CI present (+ green or clear evidence); interface+fake used; gofmt/vet clean.

**Reject:** “tests” that only print; concrete-only handlers with no seam.

---

## Slide 26 — Questions

**Close with:** “First lab action: `go test` in `date-lab`, then health httptest in backend.”

---

## Appendix — Demo cheat sheet

```bash
cd docs/week-13-day-01/starter/date-lab && go test -v ./parse/

cd ../backend
go test ./...
go test ./internal/handlers/ -v -run 'Health|Create'
go vet ./...
gofmt -l .
go test ./... -cover
```

## Appendix — Anticipated questions

**Q: Why not testify/gomock?**  
A: Hand-written fakes teach the interface seam. Frameworks later if needed.

**Q: Why ignore `ctx` in the fake?**  
A: Same spiral as week 12 — signature now; DB cancel week 14.

**Q: CI under `starter/backend/.github` won’t run on the monorepo.**  
A: Correct — when adopting, move workflow to repo root or set `working-directory`. The file is the teaching artifact.

---

*Teaching aid for Week 13 Day 1 presentation.*
