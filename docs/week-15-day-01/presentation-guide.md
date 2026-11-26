# Week 15, Day 1 — Presentation guide (all slides)

**Deck:** `docs/slides/week-15-day-01.html` (26 slides)  
**Theme:** Auth, frontend wiring, project completion — JWT, Bearer, CORS, React.

**How to present:** Fullscreen (**F**) · arrows · **N** notes · **P** presenter view.

**Suggested timing (3–3.5 h)**

| Block | Slides | Focus |
| --- | --- | --- |
| Open | 1–4 | Bridge + application flow |
| Core ideas | 5–12 | JWT, login, middleware, CORS, React, debug, milestone, lab |
| Live + lab | 13–17 | 401→200, React token, CORS, pitfalls, gate |
| Close | 18–26 | Homework, vocabulary, limits, status map, Q&A |

**One sentence for the day:** Browser → Vite → Gin → JWT → repository → Postgres.

---

## Slide 1 — Title

**Say:** Students are in Postgres. Today we decide **who** may call the API, and we wire the React app for real login.

**Do:** Confirm Postgres + migrated `sms` before demos.

---

## Slide 2 — Since last week

CRUD with `$1` stays. Unlock auth: JWT, Bearer middleware, protect student routes. Wire provided Vite app.

**Ask:** “Is GET /api/students public right now?” — if yes, we’ll lock it today.

---

## Slide 3 — Outcomes

Contract: issue/validate JWT; protect students; public register/login; CORS for `:5173`; React login with Bearer; debug 401 vs CORS vs `VITE_API_URL`.

---

## Slide 4 — SE frame / application flow

**Draw and leave up:** Browser → Vite → Gin → JWT middleware → repository → Postgres.

Never log passwords. bcrypt hashes; JWT is the client-held session credential. Homework: runbook + one bug fix.

---

## Slide 5 — JWT (HS256)

Show `GenerateToken` / `ValidateToken`. Claims: `user_id`, `username`, `exp`. Secret from `JWT_SECRET`.

---

## Slide 6 — Login public

`POST /api/register`, `POST /api/login` → `{ token, user }`. Same vague error for bad user/password.

---

## Slide 7 — Bearer middleware

`Authorization: Bearer <token>`. Invalid/missing → **401**. Sets `user_id` / `username` on context. Student routes under protected group.

**Live cue:** List without token → 401.

---

## Slide 8 — CORS

Allow Vite origin + `Authorization` header. Postman ignores CORS; browsers don’t — classic confusion.

---

## Slide 9 — Frontend

Repo `frontend/`: `VITE_API_URL`, axios interceptor attaches Bearer from `localStorage`. Students page may remain a stub.

---

## Slide 10 — Debug map

401 token · 404 path · 500 logs · CORS browser-only · wrong `VITE_API_URL`.

---

## Slide 11 — SMS milestone

Protected CRUD + React login against *their* API. Stretch: `Students.jsx`.

---

## Slide 12 — Lab overview

Postman E2E **and** React E2E. Both required for the gate.

---

## Slide 13 — Live: 401 then 200

```bash
curl /api/students                 # 401
curl -H "Authorization: Bearer $T" /api/students  # 200
```

---

## Slide 14 — Live: React login

Show `localStorage.token` and Network Request Headers Bearer.

---

## Slide 15 — Live: CORS fail (optional)

Break `AllowOrigins`, reload React, show console error; Postman still green; fix.

---

## Slide 16 — Pitfalls

Bearer typo; empty JWT secret; routes left public; `VITE_API_URL` trailing slash; logging passwords.

---

## Slide 17 — Lab gate

JWT login; 401 without Bearer; CORS OK; React path works; explain 401 vs CORS vs URL.

---

## Slide 18 — Homework

README runbook (Postgres, backend, frontend, env). One real lab bug fix in the PR.

---

## Slide 19 — Next: Week 16

Review, Go design, final demo. Bring working login → list.

---

## Slide 20 — Words

JWT · Bearer · CORS · 401.

---

## Slide 21 — Layout

`internal/utils/jwt.go`, `middleware/auth_middleware.go`, protected group in `main`, repo `frontend/`.

---

## Slide 22 — Honest limits

Not refresh/OAuth. Stub Students OK. Not Docker Compose. Never log passwords.

---

## Slide 23 — Safety

Example secrets only in git. bcrypt; gofmt; no binaries.

---

## Slide 24 — Review bar

Protected students; public auth; JWT login; React path; runbook.

---

## Slide 25 — Status codes quick map

401 / 403 / 404 / 500 / CORS browser-only.

---

## Slide 26 — Questions

Close: “Protect List first, then Postman E2E, then React login.”

---

## Appendix — Demo cheat sheet

```bash
cd docs/week-15-day-01/starter/backend
go test ./...
JWT_SECRET=dev-only-change-me go run ./cmd/server

# see starter/auth-lab/README.md for curl + frontend steps
```

## Appendix — Q&A

**Q: Why is Postman fine but React broken?**  
A: CORS and/or `VITE_API_URL` — Postman is not a browser.

**Q: Where is the token stored?**  
A: `localStorage` in this app (teaching simplicity). Mention XSS risk briefly; don’t derail into cookie auth.

---

*Teaching aid for Week 15 Day 1 presentation.*
