# Instructor checklist — Week 5, Day 1

## Pack

- [ ] Slides: `docs/slides/week-05-day-01.html`
- [ ] Your backend health already returns 200
- [ ] Postman collection ready to project
- [ ] Printed lab sheets
- [ ] Week 4 leftover: who has no skeleton PR

## Board

```
GET /health  → 200  {"status":"ok","message":"Backend is running"}
GET /api/hello → 200 JSON

stdlib:  net/http  ListenAndServe
Gin:     gin.Default()  GET  c.JSON  Run(":8080")

curl -i http://localhost:8080/health
```

## Lab

Pair stuck with done. Typical: port in use, forgot `go get`, Postman hitting https by mistake.

## Collect

| # | Student | Health 200 | Postman shot / PR | Notes |
| --- | --- | --- | --- | --- |
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |
| 6 |  |  |  |  |
| 7 |  |  |  |  |
| 8 |  |  |  |  |
| 9 |  |  |  |  |
| 10 |  |  |  |  |
| 11 |  |  |  |  |
| 12 |  |  |  |  |
| 13 |  |  |  |  |
| 14 |  |  |  |  |
| 15 |  |  |  |  |

## After

- [ ] Message homework due date
- [ ] Spot-check 3 PRs: health JSON exact, README curl, no secrets
