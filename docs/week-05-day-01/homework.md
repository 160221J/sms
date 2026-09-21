# Homework — Week 5, Day 1

Due: _______________ · Submit a **GitHub PR** (not zip-only).

## Required

1. Gin dependency in `backend/go.mod`
2. Server listens on **`:8080`**
3. `GET /health` returns **exactly**:

```json
{
  "status": "ok",
  "message": "Backend is running"
}
```

4. `GET /api/hello` returns JSON with a `message` field
5. README section: how to run + example

```bash
cd backend
go run ./cmd/server
curl -i http://localhost:8080/health
```

6. Proof: Postman (or Insomnia) **200** screenshot in the PR description or `docs/postman-health.png`
7. `gofmt` clean; no `.env` secrets; no binaries

## Stretch (bonus)

`GET /api/students` returns a **hard-coded** JSON array of 2–3 fake students (no database, no JWT). Example shape:

```json
[
  {"id": 1, "first_name": "Ada", "last_name": "Lovelace", "course": "SE"},
  {"id": 2, "first_name": "Grace", "last_name": "Hopper", "course": "CS"}
]
```

## Marking

| Check | Pass |
| --- | --- |
| PR URL |  |
| Health JSON exact |  |
| Hello works |  |
| Postman/curl proof |  |
| README runnable by a classmate |  |
| Stretch students array | bonus |

**Do not** add JWT, Postgres, or CORS unless you already had them — not required this week.
