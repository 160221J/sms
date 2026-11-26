# Week 14, Day 1 — Presentation guide (all slides)

**Deck:** `docs/slides/week-14-day-01.html` (26 slides)  
**Theme:** PostgreSQL, SQL, CRUD, transactions, migrations — the map leaves memory.

**How to present:** Fullscreen (**F**) · arrows · **N** notes · **P** presenter view.

**Suggested timing (3–3.5 h)**

| Block | Slides | Focus |
| --- | --- | --- |
| Open | 1–4 | Bridge from week 13 + SE frame |
| Core ideas | 5–12 | SQL, install, migrations, pgx, injection, repo, tx |
| Live + lab | 13–18 | psql, injection, API persistence, pitfalls, gate |
| Close | 19–26 | Homework, vocabulary, limits, Q&A |

**One sentence for the day:** Persist with pgx and `$1` placeholders — never concatenate user input into SQL.

---

## Slide 1 — Title

**On screen:** Week 14, Day 1 — PostgreSQL, SQL, CRUD, transactions, migrations.

**Say:** Week 13 gave you tests and fakes. Today students **survive a restart** because they live in PostgreSQL — not in a Go map.

**Do:** Don’t open JWT/frontend talk. Confirm who has Postgres (apt vs Docker) before coding.

---

## Slide 2 — Since last week

**On screen:** Green tests. Now persist for real.

**Explain:**
- Table-driven tests, httptest, fakes, CI habit stay.
- The in-memory map was a scaffold — today it becomes **fake-only** for unit tests.
- Week-12 `context.Context` on repos finally matters: every query takes the request context.

**Ask:** “Who can create a student, restart the server, and still see it?” — nobody, until today.

---

## Slide 3 — Outcomes

**On screen:** If Day 1 works, you can…

**Contract with the class:**
1. Explain relational tables vs an in-memory map.
2. Run `SELECT` / `INSERT` / `UPDATE` / `DELETE` in `psql`.
3. Connect with a **pgx** pool from Go.
4. Use only parameterized queries (`$1`, `$2`).
5. Apply a SQL **migration file** (not a GUI click).
6. Hit `GET /api/students` and see rows from Postgres.

**Gate later:** Create + List survive process restart.

---

## Slide 4 — Software engineering frame

**On screen:** The database is the source of truth.

**Say:** App restarts must not erase students. SQL is the API to that truth. Never concatenate user input into SQL.

**Course driver:** `pgx` (`internal/database`).  
**Homework preview:** prefer `users` table + persist register (or document deferral to week 15).

---

## Slide 5 — Relational DB

**On screen:** Tables, rows, keys.

**Explain simply:**
- Table ≈ typed collection; row ≈ one student/user.
- `SERIAL` (or identity) for ids; `UNIQUE` on email/username.
- Foreign keys can wait — this week: `students` (+ `users` in the migration for homework).

**Board:** one box for `students`, one for `users`.

---

## Slide 6 — SQL four verbs

**On screen:** SELECT / INSERT / UPDATE / DELETE.

**Do live in `psql` (2–3 minutes):** insert one row by hand, select it, update course, delete if you want.

**Bridge:** Go will run the same verbs through pgx with `$1` placeholders.

---

## Slide 7 — Install

**On screen:** Ubuntu packages or Docker + `.env`.

```bash
sudo apt install postgresql postgresql-contrib
sudo -u postgres createdb sms
psql -U postgres -d sms
```

**Or Docker:** Postgres on `:5432` with a known password.  
**Align** `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, `DB_NAME=sms` in `.env`.

---

## Slide 8 — Migrations

**On screen:** Schema as SQL files — not a GUI click.

```bash
psql -U postgres -d sms -f migrations/001_init.sql
```

**Open `001_init.sql` on the projector.** Versioned, reviewable, same on every laptop. Tables: `users` + `students`.

---

## Slide 9 — pgx pool

**On screen:** `pgxpool.New` → `Ping` → `Query` / `Exec` / `QueryRow`.

**Explain:**
- Pool = shared connections (don’t open a new connection per request by hand).
- Pass `c.Request.Context()` into repository methods (week 12 payoff).
- Placeholders are `$1`, `$2` (Postgres style), not `?`.

---

## Slide 10 — SQL injection (mandatory)

**On screen:** BAD concat → GOOD `$1`.

```go
// BAD
q := "SELECT * FROM students WHERE email = '" + email + "'"
// GOOD
q := "SELECT * FROM students WHERE email = $1"
row := pool.QueryRow(ctx, q, email)
```

**Say:** Concat lets the user change the *shape* of the query. Placeholders keep input as data.

**Live cue:** `sql-lab` next (slide 15). Do not skip this demo.

---

## Slide 11 — Repository

**On screen:** Replace the map with SQL.

**Explain:**
- `StudentRepository` talks to Postgres with parameterized SQL.
- Keep **`StudentStore` interface** from week 13 — fake for unit tests / CI without DB; pgx for real.
- Handlers stay dumb: bind → call store → JSON.

---

## Slide 12 — Transactions

**On screen:** Begin → work → Commit; `defer Rollback`.

**Explain:** All succeed or all roll back. Sketch: create student + audit row (audit table optional — pattern matters).

**Depth limit:** one live Begin/Commit is enough; don’t teach every isolation level.

---

## Slide 13 — SMS milestone

**On screen:** Postman hits Postgres.

**Checklist:**
1. `createdb sms` → apply `001_init.sql`
2. Wire `database.Connect` in `main`
3. `POST /api/students` inserts a row
4. `GET /api/students` lists from Postgres
5. **Restart the server** — rows still there

---

## Slide 14 — Live demo: psql

```bash
createdb sms
psql -d sms -f migrations/001_init.sql
psql -d sms -c '\dt'
```

Projector must show `students` (and `users`) tables.

---

## Slide 15 — Live demo: injection

```bash
cd docs/week-14-day-01/starter/sql-lab
go test -v ./inject/
```

**Point at** the BAD query text containing `OR '1'='1`. Then show GOOD keeps `$1` and never splices the argument into the SQL string.

---

## Slide 16 — Live demo: API + DB

```bash
cd docs/week-14-day-01/starter/backend
cp -n .env.example .env   # edit DB_* if needed
go run ./cmd/server

curl -s -X POST localhost:8080/api/students \
  -H 'Content-Type: application/json' \
  -d '{"first_name":"Ada","last_name":"Lovelace","email":"ada@example.com","course":"SE"}'
curl -s localhost:8080/api/students
# Ctrl+C, start again, GET again — rows remain
```

**Contrast:** week 8 memory wipe on restart.

---

## Slide 17 — Pitfalls

**Quiz aloud:**

| Bug | Fix |
| --- | --- |
| connection refused | Start Postgres; check `DB_PORT` |
| relation "students" does not exist | Run migration |
| password authentication failed | Fix `.env` |
| Concat SQL “just for a demo leftover” | Delete it from Create |
| NULL `date_of_birth` scan error | Pointer / `pgtype` / careful Scan |

---

## Slide 18 — Lab gate

**On board:**
- [ ] Postgres up; `sms` DB exists  
- [ ] Migration applied; `\dt` shows students  
- [ ] Injection BAD vs GOOD understood  
- [ ] Create + List via API hit Postgres  
- [ ] Optional: transaction sketch / users persist  

---

## Slide 19 — Homework

**Prefer A:** Persist `/api/register` into `users` (table already in migration). Parameterized inserts; never log passwords.

**B (only if JWT is the week-15 focus):** Keep users in memory one more week — PR must say why; students already on Postgres.

PR includes migrate steps + “parameterized only.”

---

## Slide 20 — Next session

Week 15 — JWT, Bearer middleware, CORS, React app. Bring a working Postgres List/Create.

---

## Slide 21 — Words to keep

**Cold-call:**
1. Migration? → versioned SQL that defines schema.  
2. Parameterized? → `$1` placeholders; never concat input.  
3. pgx pool? → shared connections to Postgres.  
4. Transaction? → commit all or roll back all.

---

## Slide 22 — Layout reminder

```
docs/week-14-day-01/starter/
  sql-lab/                    # injection BAD vs GOOD
  backend/
    migrations/001_init.sql
    internal/database/        # pgx pool
    internal/repository/      # SQL StudentRepository + fake
    .env.example
```

**Migration first**, then sql-lab, then API.

---

## Slide 23 — Honest limits

Not JWT/frontend (15). Not ORMs. Not every isolation level. Not production pool tuning.

---

## Slide 24 — Safety

No real passwords in git. Parameterized queries only after the injection demo. `gofmt`; no binaries in git.

---

## Slide 25 — Review bar

Merge when: migration documented; students CRUD uses pgx + `$n`; List survives restart; no concat SQL in app paths.

**Reject:** string-built queries in Create/List/Get.

---

## Slide 26 — Questions

**Close with:** “First actions: `createdb`, apply `001_init.sql`, run sql-lab, then Create/List and restart.”

---

## Appendix — Demo cheat sheet

```bash
createdb sms
psql -d sms -f docs/week-14-day-01/starter/backend/migrations/001_init.sql

cd docs/week-14-day-01/starter/sql-lab && go test -v ./inject/

cd ../backend
cp -n .env.example .env
go test ./...          # unit tests use Fake (no DB)
go run ./cmd/server
```

## Appendix — Anticipated questions

**Q: Why keep the fake if we have Postgres?**  
A: Unit tests and CI without a live database. The lab *proof* still needs Postgres for persistence.

**Q: Why not GORM?**  
A: Course teaches SQL + pgx first so injection and migrations stay visible.

**Q: Users still in memory?**  
A: Starter leaves register in-memory on purpose — homework prefers moving it to `users`.

---

*Teaching aid for Week 14 Day 1 presentation.*
