# Week 12, Day 1 — Presentation guide (all slides)

**Deck:** `docs/slides/week-12-day-01.html` (26 slides)  
**Theme:** Mutex, WaitGroup, context, races — protect shared memory and cancel work safely.

**How to present:** Fullscreen (**F**) · arrows · **N** notes · **P** presenter view.

**Suggested timing (3–3.5 h)**

| Block | Slides | Focus |
| --- | --- | --- |
| Open | 1–4 | Bridge from week 11 + outcomes |
| Core ideas | 5–12 | Race, Mutex, WaitGroup, context, SMS, shutdown |
| Live + lab | 13–18 | `-race` FAIL→PASS, timeout, lab gate |
| Close | 19–26 | Homework, vocabulary, limits, Q&A |

**One sentence for the day:** Channels move work; mutexes protect data; context cancels work; `-race` proves you got it right.

---

## Slide 1 — Title

**On screen:** Week 12, Day 1 — Mutex, WaitGroup, context, and races.

**Say:** Last week you built a **worker pool** — fixed N workers pulling jobs. Today we fix the other half of concurrency: **shared memory** (mutex) and **cancellation** (context), and we make `go test -race` go green for real.

**Do:** Don’t dive into code yet. Set the mood: “If two goroutines touch the same variable with no rule, Go does not save you.”

---

## Slide 2 — Since last week

**On screen:** You have a pool. Now protect shared state.

**Explain each bullet:**
- **Worker pool + WaitGroup** — keep that mental model; WaitGroup joins workers, it does *not* lock data.
- **Week 10 previewed `-race`** — many students saw the tool; today we complete **red → mutex → green**.
- **Create stays sync** — normal CRUD is still one goroutine per request. Import may use a pool, but the **map must stay locked**.

**Ask:** “If Import has 4 workers calling Create, what protects the map?” → Mutex (already in the repo; today we name it and prove it).

---

## Slide 3 — Outcomes (“If Day 1 works, you can…”)

**On screen:** Checklist of skills.

**Walk the list as a contract with the class:**
1. Use **`sync.Mutex`** (and at least *name* **RWMutex**).
2. Use **WaitGroup as a join**, not a lock.
3. Pass **`c.Request.Context()`** into repository methods.
4. Demo a **timeout** with `context.WithTimeout`.
5. Sketch **graceful shutdown** with `signal.Notify`.
6. Get **`go test -race` green** on the lab.

**Gate for later:** write “race red → mutex → green” on the board and leave it up.

---

## Slide 4 — Software engineering frame

**On screen:** Shared memory needs a rule.  
*Channels coordinate work. Mutexes protect data. Context cancels work.*

**Teach the triangle:**
| Tool | Job |
| --- | --- |
| Channel | Hand work between goroutines |
| Mutex | Only one goroutine touches this memory at a time |
| Context | “Stop / deadline / canceled” flowing down the stack |

**SMS milestone (preview):** lock the in-memory map; add `context.Context` to repo method signatures (body can ignore it until Postgres in week 14).  
**Homework preview:** README must show `go test -race ./...`.

---

## Slide 5 — Data race

**On screen:** Two goroutines, `n++`, no sync.

**Explain simply:**
- A **data race** = two goroutines access the same variable at the same time, and at least one writes, with **no** synchronization.
- It may “work” on your laptop and fail in production — that is **undefined behavior**.
- **`go test -race`** instruments the binary and reports races. Needs **cgo + gcc** (`build-essential` on Ubuntu).

**Live cue:** Promise to show a real DATA RACE report on the projector (slides 13–14).

**Analogy:** Two people editing the same spreadsheet cell with no locking — last write wins, or the file corrupts.

---

## Slide 6 — Mutex

**On screen:** `Lock` / `Unlock` around `n++`.

**Explain:**
- **`mu.Lock()`** — “I own this data now.” Others wait.
- **`mu.Unlock()`** — “I’m done.” Prefer **`defer mu.Unlock()`** immediately after Lock so you don’t forget on early return.
- Hold locks **short**. Don’t call slow I/O (HTTP, disk) while holding the lock.
- One mutex “owns” one piece of data (e.g. the students map). Document that ownership.

**Live cue:** Later you’ll change `UnsafeAdd` → `SafeAdd` by wrapping `n++` in a mutex.

**Common student confusion:** “I used WaitGroup, so I’m safe.” → No. WaitGroup only waits for finish; it does not serialize access.

---

## Slide 7 — RWMutex

**On screen:** `RLock` for readers, `Lock` for writers.

**Explain lightly (don’t force a rewrite):**
- **RWMutex** allows **many concurrent readers**, or **one writer**, not both kinds at once.
- Useful when reads dominate and critical sections are tiny (e.g. many GetByID, rare Create).
- **SMS starter uses plain `Mutex`** — that’s enough this week. Goal: students can *say* what RWMutex is for.

**Ask:** “If we only ever Create, does RWMutex help?” → Not really; writers still exclusive.

---

## Slide 8 — WaitGroup (join, not lock)

**On screen:** `Add` / `Done` / `Wait`.

**Explain:**
- **WaitGroup** answers: “Have all N workers finished?”
- Week 11 used it before `close(results)`.
- It does **not** protect `n++`. Race still happens if you only WaitGroup.

**Quiz (say aloud):**
1. Mutex vs WaitGroup? → lock data vs join goroutines.  
2. Can you need both? → Yes (pool workers + shared counter, or lock map + wait for workers).

---

## Slide 9 — context

**On screen:** `WithTimeout`, `select` on `ctx.Done()`.

**Explain:**
- **Context** carries deadlines and cancellation down the call stack.
- **`WithTimeout(parent, 2s)`** — work must finish or stop in 2 seconds.
- Always **`defer cancel()`** when *you* create a derived context (releases timers).
- Convention: **`ctx` is the first parameter** of functions that can be canceled.
- **`ctx.Err()`** after Done: usually `context.DeadlineExceeded` or `context.Canceled`.

**Analogy:** A meeting timer. When it rings, everyone stops — you don’t keep talking forever.

**Keep depth limited:** one timeout demo later is enough; don’t teach every Context type today.

---

## Slide 10 — Gin: `c.Request.Context()`

**On screen:** Handler passes request context into `repo.GetByID(ctx, id)`.

**Explain:**
- Every HTTP request has a context. Gin exposes it as **`c.Request.Context()`**.
- If the **client disconnects** or the **server shuts down**, that context is canceled.
- Handlers should pass it down so lower layers can stop early (especially once you have DB calls in week 14).
- **This week:** repository may still **`_ = ctx`** (ignore). Changing the **signature now** is the spiral curriculum move — wire use later.

**Say:** “Don’t invent a new Background context in the handler for request work — use the request’s own context.”

---

## Slide 11 — SMS milestone

**On screen:** `Create(ctx context.Context, …)` + mutex + `_ = ctx`.

**Explain the week-12 SMS diff:**
1. **Map stays locked** with `mu.Lock()` / `Unlock` (confirm it’s intentional, not accidental).
2. **Every repo method takes `ctx`** first.
3. **Handlers pass `c.Request.Context()`.**
4. **Timeout demo endpoint** shows slow work respecting a deadline (`GET /api/demo/slow`).

**Honest note:** Ignoring ctx until Postgres is OK *if* the signature and handler wiring are correct. Students should not pretend the in-memory map “cancels” mid-write.

---

## Slide 12 — Graceful shutdown sketch

**On screen:** `signal.NotifyContext` → `ListenAndServe` in a goroutine → `Shutdown`.

**Explain the story:**
1. Server runs in a **goroutine**.
2. Main waits for **Ctrl+C / SIGTERM**.
3. **`Shutdown`** stops accepting new connections and waits (with a timeout) for in-flight requests to finish.
4. Prefer this over killing the process mid-request.

**Teaching depth:** This is a **sketch**. Enough to read in `cmd/server/main.go`. Don’t derail into production orchestration.

**If short on time:** walk the starter code; skip live Ctrl+C.

---

## Slide 13 — Lab overview

**On screen:** `race-lab` commands — FAIL then PASS.

**Explain the lab loop:**
```bash
cd starter/race-lab
CGO_ENABLED=1 go test -race ./counter/   # show FAIL with unsafe path
# add / use Mutex (SafeAdd)
CGO_ENABLED=1 go test -race ./...        # PASS
```

**Environment warning:** Without gcc, students get `cgo: C compiler "gcc" not found`. Fix: `sudo apt-get install -y build-essential`.

**Point to folders:** `race-lab/` first; SMS backend second.

---

## Slide 14 — Live demo: `-race`

**On screen:** Show FAIL, then fix.

**Do this live (do not skip):**
1. Run unsafe path so the projector shows **DATA RACE** (e.g. enable the skipped unsafe test, or temporarily call `UnsafeAdd` in a test).
2. Switch to **`SafeAdd`** (mutex around `n++`).
3. Re-run — **ok**.

**Say while pointing at the race report:** “This is the same bug class as concurrent map writes — `-race` found it before production did.”

---

## Slide 15 — Live demo: context timeout

**On screen:** `GET /api/demo/slow?ms=3000` with 1s server timeout.

**Do:**
```bash
curl -s 'localhost:8080/api/demo/slow?ms=200'    # ok
curl -s 'localhost:8080/api/demo/slow?ms=3000'   # canceled / deadline exceeded
```

**Explain:** Route wraps the request with `context.WithTimeout(..., 1*time.Second)`. Handler `select`s on `ctx.Done()` vs a timer. Over 1s sleep → timeout response, not a hung server.

---

## Slide 16 — Live demo: shutdown (optional)

**On screen:** Ctrl+C → shutting down → clean exit.

**Do if time:**
```bash
go run ./cmd/server
# Ctrl+C
# expect logs: shutting down → bye
```

**Cut this** if the race lab still needs airtime. Students can read `main.go` for homework.

---

## Slide 17 — Pitfalls

**On screen:** Common week-12 bugs.

**Quiz the room (rapid fire):**

| Bug | Why it hurts | Fix |
| --- | --- | --- |
| WaitGroup without mutex | Still races | Lock the data |
| Forgot Unlock | Deadlock | `defer mu.Unlock()` |
| No `defer cancel()` | Timer/leak / unclear lifetime | Always cancel derived ctx |
| Ignore `ctx.Done()` | Work runs forever after client left | `select` / check Err |
| `-race` won’t run | No gcc / CGO off | build-essential + `CGO_ENABLED=1` |

---

## Slide 18 — Lab gate (rest of class)

**On screen:** Done when all true.

**Put on the board as exit criteria:**
- [ ] `go test -race ./...` green on race-lab  
- [ ] Can explain Mutex vs WaitGroup vs channel  
- [ ] Repo methods take `context.Context`; handlers pass request context  
- [ ] Timeout demo works (or sketched)  
- [ ] Optional: graceful shutdown in `main`  

**Circulate:** Reject “I added WaitGroup so the race is fixed.”

---

## Slide 19 — Homework

**On screen:** PR with `-race` in the README.

**Assign clearly:**
1. README documents `go test -race ./...`.
2. Shared maps locked; context on repo signatures; handlers pass request context.
3. PR text: what was red, what made it green.

**Optional:** screenshot of a green `-race` run.

---

## Slide 20 — Next session (Week 13 teaser)

**On screen:** Testing and code quality.

**Say:** Next week is the deep testing week — table-driven tests, `httptest`, fakes, CI. Bring the habit of green `-race` with you. Don’t preview CI YAML today.

---

## Slide 21 — Words to keep

**On screen:** Four cards — Mutex, WaitGroup, context, `-race`.

**Oral quiz (cold-call):**
1. What does a Mutex do? → Exclusive access to shared memory.  
2. Is WaitGroup a lock? → No; it joins N goroutines.  
3. What does context carry? → Cancel / deadline down the stack.  
4. What is `-race`? → Detector for concurrent unsynchronized access.

---

## Slide 22 — Layout reminder

**On screen:** Where files live.

```
docs/week-12-day-01/starter/
  race-lab/                 # red → mutex → green  ← start here
  backend/
    internal/repository/    # Mutex + context.Context params
    cmd/server/main.go      # graceful shutdown sketch
    internal/handlers/      # c.Request.Context() + timeout demo
```

**Say:** Lab first (`race-lab`). SMS wiring second. Don’t get lost only in Gin before `-race` is green.

---

## Slide 23 — Honest limits

**On screen:** What this week is not.

**Keep the spiral honest:**
- Not Postgres / real query cancel → **week 14**.
- Not deep testing / CI → **week 13**.
- Not “replace every mutex with a channel.”
- Not production-hardening every edge case.

**Why say this:** Stops advanced students from derailing into Redis locks and Kubernetes probes.

---

## Slide 24 — Safety

**On screen:** Cap timeouts; no secrets; gofmt; no binaries in git.

**Quick pass:** Demo sleeps must be bounded. Example emails only. Format before PR. Don’t commit `server` binaries.

---

## Slide 25 — Review bar (instructor merges when…)

**On screen:** Merge checklist.

Use when grading PRs:
- `-race` documented and green (or clear lab evidence)
- Shared maps locked
- Repo signatures take context; handlers pass request context
- Create / list / import still behave

**Reject:** WaitGroup-only “fixes,” Background context in every handler, unlocked maps.

---

## Slide 26 — Questions

**On screen:** Questions.

**Close with:** “First lab action when you sit down: make `-race` fail once on purpose, then make it pass with a Mutex.”

Then dismiss to **race-lab**.

---

## Appendix — Live demo cheat sheet

### A. Race lab
```bash
cd docs/week-12-day-01/starter/race-lab
CGO_ENABLED=1 go test -race ./...
# Demo FAIL (optional): remove t.Skip in TestUnsafeAddDocumentsRace, then:
CGO_ENABLED=1 go test -race -run TestUnsafeAddDocumentsRace ./counter/
```

### B. Timeout demo
```bash
cd docs/week-12-day-01/starter/backend
go run ./cmd/server
curl -s 'localhost:8080/api/demo/slow?ms=200'
curl -s 'localhost:8080/api/demo/slow?ms=3000'
```

### C. Shutdown
Ctrl+C in the server terminal → logs `shutting down` then `bye`.

### D. One analogy to reuse all day
**Kitchen:**  
- **Channel** = pass tickets to cooks (work).  
- **Mutex** = only one person in the spice cabinet (shared data).  
- **Context** = “service ends in 2 minutes — stop cooking.”  
- **`-race`** = inspector who catches two cooks grabbing the same jar.

---

## Appendix — Anticipated student questions

**Q: We already had a mutex in week 8/9 — why week 12?**  
A: Earlier it was quiet infrastructure. Today we **teach** it, prove it with `-race`, and add **context** + shutdown.

**Q: Why ignore `ctx` in the repository?**  
A: In-memory map can’t meaningfully cancel mid-assignment. Signature prepares for DB; handlers learn the habit now.

**Q: Channels instead of mutex for the map?**  
A: Possible (single owner goroutine), but mutex is the right first tool for a shared map. Don’t rewrite SMS into an actor model today.

**Q: `-race` is slow — use it always?**  
A: Yes in CI/local test command for this course. It’s a correctness tool, not a production runtime flag for every deploy binary.

---

*Local teaching aid — not required in git. Generated for Week 12 Day 1 presentation.*
