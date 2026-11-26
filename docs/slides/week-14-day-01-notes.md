# Week 14, Day 1 — presenter notes

Slides: [`week-14-day-01.html`](week-14-day-01.html) → **F** · arrows · **N** · **P**.

**PostgreSQL + pgx.** Lab: createdb → migrate → API hits DB. **SQL injection demo is mandatory.**

## Timing (3–3.5 hours)

| Clock | Block | Slides |
| --- | --- | --- |
| 0:00–0:20 | Bridge + outcomes | 1–4 |
| 0:20–1:20 | SQL, install, migrations, pgx | 5–9 |
| 1:20–2:20 | Injection, repo, transactions | 10–12 |
| 2:20–end | Live demos + lab | 13–end |

Never skip BAD concat → `$1` fix.

## Live demo

1. `createdb` + `001_init.sql` + `\dt`  
2. sql-lab injection  
3. Create/List via API; restart proves persistence  

## Lab gate

- [ ] Migration applied  
- [ ] Injection understood  
- [ ] Create + List from Postgres  

## Homework

Prefer users table + persist register; else document defer to week 15.

## What not to teach

JWT/frontend (15), ORMs, pool tuning.
