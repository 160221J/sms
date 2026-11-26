# Week 15, Day 1 — presenter notes

Slides: [`week-15-day-01.html`](week-15-day-01.html) → **F** · arrows · **N** · **P**.

**JWT, Bearer middleware, CORS, React.** Lab: register → login → GET students in Postman **and** React.

## Timing (3–3.5 hours)

| Clock | Block | Slides |
| --- | --- | --- |
| 0:00–0:20 | Bridge + flow | 1–4 |
| 0:20–1:30 | JWT, login, middleware, CORS | 5–8 |
| 1:30–2:20 | Frontend + debug map | 9–12 |
| 2:20–end | Live demos + E2E lab | 13–end |

Never skip 401-without-token → 200-with-Bearer.

## Live demo

1. Protect List; curl 401 then 200  
2. React login; show localStorage + Authorization header  
3. Optional: break CORS briefly  

## Lab gate

- [ ] JWT login works  
- [ ] Student routes protected  
- [ ] React login path works  
- [ ] Can explain 401 vs CORS vs VITE_API_URL  

## Homework

README runbook + one real bug fix from lab.

## What not to teach

Refresh tokens, OAuth, full Students UI polish, Docker Compose.
