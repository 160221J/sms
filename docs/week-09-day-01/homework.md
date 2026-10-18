# Homework — Week 9, Day 1

Due: _______________ · **GitHub PR**

## Already done in lab (must stay green)

- `ErrNotFound` from repo; missing student → 404 JSON  
- Unexpected errors → 500 (not panic)  
- Bind failures → 400  

## Required homework

1. Replace `fmt.Println` debugging with **`log/slog`** (`Info` / `Error` + attrs like `student_id`, `err`).  
2. Add **`.env.example`** with `PORT` and `JWT_SECRET` placeholders. Keep `.env` gitignored.  
3. Wire **`internal/config`** so the server port comes from env (default `8080`).  
4. PR shows a sample JSON log line for a 5xx or create path.

## Stretch

- `POST /api/register` (bcrypt, in-memory users)  
- Login returns a JWT string (do not protect student routes yet)  

## Marking

| Check | Pass |
| --- | --- |
| 404 mapping still works |  |
| slog used (no print spam) |  |
| `.env.example` present |  |
| `.env` not in git |  |
| Evidence in PR |  |
