# Troubleshooting — Week 14

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| connection refused | Postgres not running / wrong port | Start service; check `DB_PORT` |
| password authentication failed | `.env` mismatch | Align user/password with `psql` |
| relation "students" does not exist | Migration not applied | `psql -d sms -f migrations/001_init.sql` |
| database "sms" does not exist | No `createdb` | `createdb sms` (or Docker `POSTGRES_DB`) |
| scan error on date_of_birth | NULL into `time.Time` | Use `pgtype` / pointer / `COALESCE` |
| tests fail without DB | Hitting pgx in unit tests | Keep Fake for unit tests; integration optional |

Room walk: “Show me the `$1` in Create” — must not be string concat.
