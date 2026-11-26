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

**Say:** Week 13 gave you tests and fakes. Today students **survive a restart** because they live in PostgreSQL.

**Do:** Confirm who has Postgres (apt vs Docker) before coding.

---

## Slide 2 — Since last week

Green tests stay. In-memory map becomes fake-only. `context.Context` on repos finally drives DB cancel/timeouts.

---

## Slide 3 — Outcomes

Contract: explain tables; run CRUD SQL in `psql`; connect with **pgx**; parameterized queries only; apply a migration file; `GET /api/students` reads Postgres.

---

## Slide 4 — SE frame

DB is source of truth. SQL is the API. Never concat input into SQL. Driver: **pgx**. Homework prefers users table.

---

## Slide 5 — Relational DB

Tables/rows/keys. `SERIAL` ids. `UNIQUE` email/username. Migration includes `users` + `students`.

---

## Slide 6 — SQL four verbs

Live briefly in `psql`: SELECT / INSERT / UPDATE / DELETE. Emphasize `WHERE` with placeholders later.

---

## Slide 7 — Install

Ubuntu packages or Docker. Align `.env` (`DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, `DB_NAME=sms`).

---

## Slide 8 — Migrations

`psql -d sms -f migrations/001_init.sql`. Schema as reviewed SQL files — not GUI clicks. Open file on projector.

---

## Slide 9 — pgx pool

`pgxpool.New` → `Ping` → `Query`/`Exec`/`QueryRow` with `$1`. Pass request context into repo methods.

---

## Slide 10 — SQL injection (mandatory)

BAD: `"... '" + email + "'"`. GOOD: `WHERE email = $1` + separate arg. Live `sql-lab` shows the malicious string rewriting the query.

---

## Slide 11 — Repository

Replace map with SQL. Keep `StudentStore` interface — fake for unit tests, pgx for real.

---

## Slide 12 — Transactions

`Begin` → work → `Commit`; `defer Rollback`. Sketch create + audit (audit table optional). Pattern > depth today.

---

## Slide 13 — SMS milestone

createdb → migrate → Connect in main → POST inserts → GET lists → **restart still has rows**.

---

## Slide 14 — Live: psql

```bash
createdb sms
psql -d sms -f migrations/001_init.sql
psql -d sms -c '\dt'
```

---

## Slide 15 — Live: injection

```bash
cd starter/sql-lab && go test -v ./inject/
```

Point at BAD query containing `OR '1'='1`.

---

## Slide 16 — Live: API + DB

POST create, GET list, restart server, GET again. Contrast week-8 memory wipe.

---

## Slide 17 — Pitfalls

Wrong `.env`; forgot migration; concat leftover; `Background` everywhere; NULL date scan into `time.Time`.

---

## Slide 18 — Lab gate

Postgres up; migration applied; injection understood; Create+List hit DB; optional tx/users.

---

## Slide 19 — Homework

Prefer persist register into `users`. Or document deferring users to week 15. PR: migrate steps + parameterized only.

---

## Slide 20 — Next: Week 15 auth + frontend

JWT, Bearer, CORS, React. Need Postgres List/Create working.

---

## Slide 21 — Words

Migration · Parameterized · pgx pool · Transaction.

---

## Slide 22 — Layout

`sql-lab/` · `backend/migrations/` · `internal/database/` · `internal/repository/` · `.env.example`

---

## Slide 23 — Limits

Not JWT/frontend. Not ORMs. Not isolation-level deep dive. Not pool tuning.

---

## Slide 24 — Safety

No secrets in git. Parameterized after demo. gofmt; no binaries.

---

## Slide 25 — Review bar

Migration documented; CRUD uses `$n`; List survives restart; no concat SQL.

---

## Slide 26 — Questions

Close: “First actions: createdb, apply `001_init.sql`, run sql-lab, then Create/List.”

---

## Appendix — Demo cheat sheet

```bash
createdb sms
psql -d sms -f docs/week-14-day-01/starter/backend/migrations/001_init.sql

cd docs/week-14-day-01/starter/sql-lab && go test -v ./inject/

cd ../backend
cp -n .env.example .env
go test ./...
go run ./cmd/server
```

## Appendix — Q&A

**Q: Why keep the fake?**  
A: Unit tests and CI without a live database. Integration still needs Postgres for the lab proof.

**Q: Why not GORM?**  
A: Course teaches SQL + pgx first so injection and migrations stay visible.

---

*Teaching aid for Week 14 Day 1 presentation.*
