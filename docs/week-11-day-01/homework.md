# Homework — Week 11, Day 1

Due: _______________ · **GitHub PR**

## Already done in lab

- Worker pool kata with fixed N  
- Understood who closes `jobs` / `results`  

## Pick one

### Option A — Import API
`POST /api/students/import`  
- Body: JSON array of students  
- Pool of N workers validates + inserts (in-memory)  
- Response: `{ "created": n, "failed": m }` (errors optional)  

### Option B — Documented kata
- Pool under `backend/internal/workers/` (or keep `worker-lab`)  
- README: N, job type, who closes which channel  
- Note: delete before production if unused  

## Marking

| Check | Pass |
| --- | --- |
| Fixed N workers |  |
| Job channel (not go-per-item) |  |
| Close ownership correct |  |
| PR explanation |  |
