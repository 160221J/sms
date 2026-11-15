# Week 11, Day 1 — Presentation guide (all slides)

**Deck:** `docs/slides/week-11-day-01.html` (26 slides)  
**Theme:** Channels, pipelines, and the **worker pool** — the concurrency pattern to keep.

**How to present:** Fullscreen (**F**) · arrows · **N** notes · **P** presenter view.

**Suggested timing (3–3.5 h)**

| Block | Slides | Focus |
| --- | --- | --- |
| Open | 1–4 | Bridge from week 10 + “one pattern” |
| Core ideas | 5–13 | Channels, select, pipeline, pool, WaitGroup, SMS/kata |
| Live + lab | 14–18 | Channel demo, pool demo, pitfalls, lab gate |
| Close | 19–26 | Homework, vocabulary, limits, Q&A |

**One sentence for the day:** Bound concurrency with a fixed-N worker pool — never `go` once per row.

---

## Slide 1 — Title

**On screen:** Week 11, Day 1 — Channels, pipelines, and the worker pool.

**Say:** Week 10 you could start goroutines and you saw races. Today goroutines **talk** through channels, and you learn the one pattern to remember: the **worker pool**. Import API is stretch.

**Do:** Write “worker pool” on the board early; leave it up all day.

---

## Slide 2 — Since last week

**On screen:** You can start Gs. Now make them talk safely.

**Explain:**
- `-race` literacy exists; **Create stays sync**.
- Cold-call: “What is a channel?” → typed pipe between goroutines.
- Today: send/receive, close, range, `select`, pipeline, **worker pool**.
- Mutex deep-dive is **week 12** — today WaitGroup is only **glue** for the pool.

**Ask:** “Did anyone put naked `go` inside Create?” — if yes, undo before continuing.

---

## Slide 3 — Outcomes

**On screen:** If Day 1 works, you can…

**Contract with the class:**
1. Choose unbuffered vs buffered and say why.
2. Close a channel and `range` until drained.
3. Use `select` once (timeout is enough).
4. Sketch a pipeline (stage → stage).
5. Implement a **worker pool** of N workers over a job channel.

**Gate later:** fixed N + job channel + no go-per-job.

---

## Slide 4 — Software engineering: worker pool

**On screen:** Bound concurrency. N workers pull jobs. Results on another channel.

**Explain simply:**
- Bad: `go` once per student in a 10k import → unbounded goroutines.
- Good: start **N** workers once; they **pull** from `jobs`; send outcomes on `results`.
- SMS stretch: `POST /api/students/import` → `{created, failed}`.
- If the room struggles: **hash-list kata only**; sketch import on the board.

**Leave on board:** `jobs → N workers → results`.

---

## Slide 5 — Channels

**On screen:** `make(chan T)` vs `make(chan T, n)`; send / receive.

**Explain:**
- **Unbuffered:** send waits for a receive (handshake / sync point).
- **Buffered:** send waits only when the buffer is full.
- Syntax: `ch <- x` send · `v := <-ch` receive.

**Live cue:** tiny send/receive in 60 seconds (slide 14 expands this).

---

## Slide 6 — Directional channels

**On screen:** `chan<-` send-only · `<-chan` receive-only.

**Explain lightly:** function signatures document intent; compiler blocks reverse use. Optional depth — show once, don’t dwell.

---

## Slide 7 — Close + range

**On screen:** Sender closes; receivers drain with `range`.

**Rules to hammer:**
1. **Only the sender** should close.
2. **Never send** on a closed channel → panic.
3. `for v := range ch` runs until closed **and** empty.
4. `v, ok := <-ch` → `ok == false` when closed and drained.

**Common bug:** multiple workers all call `close` → panic.

---

## Slide 8 — select

**On screen:** Wait on several channel ops; timeout with `time.After`.

**Explain:**
- One ready case runs; if several ready, Go picks at random.
- `default` makes it non-blocking — use sparingly (easy to busy-loop mentally).
- One live timeout example is enough for today.

---

## Slide 9 — Pipeline

**On screen:** `gen` → `square` → `range`.

**Explain:** `gen` and `square` are **example stages you write**, not builtins. Each stage = goroutine(s) + channel(s). Data flows stage → stage.

**Bridge:** A worker pool is a special pipeline — many workers, one shared job queue.

**Board:** boxes for gen / square / print with arrows.

---

## Slide 10 — Worker pool (core)

**On screen:** `jobs`, `results`, loop `N` workers.

**Explain the forever pattern:**
1. Make `jobs` and `results` channels.
2. Start **N** workers that `range` jobs and send results.
3. Enqueue work; **`close(jobs)`** when done sending.
4. Collect from `results` (after WaitGroup — next slide).

**Say:** Fixed N — no `go` per student/row.

---

## Slide 11 — WaitGroup preview

**On screen:** `Add` / `Done` / `Wait` then `close(results)`.

**Explain:** WaitGroup answers “are workers done?” so you don’t close `results` too early (hang/panic risk).

**Important:** WaitGroup is **not** a lock. Mutex/race fix is week 12. Today it’s the **join**.

---

## Slide 12 — SMS stretch: import

**On screen:** JSON array in → pool → `{created, failed}`.

**Explain:** Still in-memory; still no Postgres. Per-row validation in workers; bad rows bump `failed`.

**If struggling:** sketch the API only; don’t force wiring during lab hour.

---

## Slide 13 — Kata options

**On screen:** Hash list / resizer sketch.

**Explain:** Same pool shape as import — swap the job type. Starter ships **hash-list** under `worker-lab/`.

---

## Slide 14 — Live demo: channel basics

**Do (≈2 min):**
```go
ch := make(chan string, 2)
ch <- "a"; ch <- "b"; close(ch)
for s := range ch { fmt.Println(s) }
```

Then move to the pool.

---

## Slide 15 — Live demo: worker pool

**Do:**
```bash
cd docs/week-11-day-01/starter/worker-lab
go test ./pool/
go run . -n 4
```

**Note:** Run from `worker-lab/`, not inside `pool/` (`pool` is not `package main`).

Walk or type the starter — don’t invent a new API live.

---

## Slide 16 — Live demo: import stretch (optional)

**Do if time:**
```bash
# backend running
curl -s -X POST localhost:8080/api/students/import \
  -H 'Content-Type: application/json' \
  -d '[{"first_name":"Ada","email":"ada@example.com","course":"SE"}]'
```

**Cut** if the kata still needs the hour.

---

## Slide 17 — Pitfalls

**Quiz aloud:**

| Bug | Result |
| --- | --- |
| Send on closed channel | panic |
| Forget to close | `range` hangs forever |
| Close from many goroutines | panic |
| `go` per job | not a pool |

---

## Slide 18 — Lab gate

**On board:**
- [ ] Unbuffered vs buffered explained  
- [ ] Worker pool kata runs  
- [ ] WaitGroup before closing results  
- [ ] No naked `go` per job  
- [ ] Optional: import sketched  

---

## Slide 19 — Homework

**A:** Import endpoint with pool → `{created, failed}`.  
**B:** Documented kata under `internal/workers/` (delete before production if unused).

PR must explain **N** and **who closes which channel**.

---

## Slide 20 — Next session

Week 12: mutex, WaitGroup deep, context, races. Bring the pool mental model.

---

## Slide 21 — Words to keep

**Cold-call:**
1. Channel? → typed pipe; send/receive sync.  
2. select? → wait on multiple channel cases.  
3. Pipeline? → stages connected by channels.  
4. Worker pool? → fixed N workers pulling from a job queue.

---

## Slide 22 — Layout reminder

```
docs/week-11-day-01/starter/
  worker-lab/              # primary lab (hash-list pool)
  backend/
    internal/workers/      # homework B
    internal/handlers/     # Import stretch
```

**Kata first**, SMS second.

---

## Slide 23 — Honest limits

Not mutex/race fix (12). Not Postgres bulk insert. Not unbounded fan-out labeled “pool.” Not every handler needs channels.

---

## Slide 24 — Safety

Cap N and job list size. `example.com` fixtures. `gofmt`; no binaries in git.

---

## Slide 25 — Review bar

Merge when: fixed N + job channel; correct close ownership; PR explains results; Create/list still sync and green.

**Reject:** go-per-row “pools.”

---

## Slide 26 — Questions

**Close with:** “First lab action: `go test ./pool/` then `go run . -n 4` from `worker-lab/`.”

---

## Appendix — Demo cheat sheet

```bash
# Channel / pool kata
cd docs/week-11-day-01/starter/worker-lab
go test ./pool/
go run . -n 4

# Import stretch
cd ../backend && go run ./cmd/server
curl -s -X POST localhost:8080/api/students/import \
  -H 'Content-Type: application/json' \
  -d '[{"first_name":"Ada","email":"ada@example.com","course":"SE"},{"first_name":"","email":"x","course":""}]'
```

## Appendix — Anticipated questions

**Q: Is worker-lab part of SMS?**  
A: Separate demo module. Same *pattern* as import; different job type (strings vs students).

**Q: Why not go per job?**  
A: Unbounded concurrency; harder to reason about load, errors, and shutdown.

**Q: Who closes `jobs` vs `results`?**  
A: Producer closes `jobs` after enqueue. Closer of `results` waits until workers finish (WaitGroup).

---

*Teaching aid for Week 11 Day 1 presentation.*
