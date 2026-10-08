# Homework — Week 7, Day 1

Due: _______________ · **GitHub PR**

## Already done in lab (must stay green)

- `models.Student` with JSON tags  
- `POST /api/students` → 201  
- `GET /api/students` → 200 array  
- `GET /api/students/:id` → 200 / 404  
- Bad JSON → 400  

## Required homework

1. **`PUT /api/students/:id`** — update fields; missing id → 404; bad JSON → 400  
2. **`DELETE /api/students/:id`** — remove; missing → 404 (200 or 204 is fine — document it)  
3. Postman (or curl) proof in the PR  
4. `gofmt` clean; no secrets; no Postgres/JWT  

## Stretch

- Reject empty `first_name` / `email` even when JSON parses  
- Return `full_name` using week-6 `FullName`  
- Sort list by `id` ascending  

## Marking

| Check | Pass |
| --- | --- |
| Lab routes still work |  |
| PUT works |  |
| DELETE works |  |
| 400 on invalid JSON |  |
| Evidence in PR |  |
