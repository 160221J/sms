# Troubleshooting — Week 15

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| 401 on `/api/students` | Missing/invalid Bearer | Login again; header `Authorization: Bearer <token>` |
| React blocked, Postman OK | CORS | Allow `http://localhost:5173` + `Authorization` header |
| Network error in React | Wrong `VITE_API_URL` | `http://localhost:8080` (no trailing slash issues) |
| `unexpected signing method` | Token not HS256 / wrong secret | Same `JWT_SECRET` across restarts |
| Login 401 always | Bad password or user missing | Register first; check bcrypt compare |
| 500 on protected route | Panic in middleware claims cast | Ensure `user_id` claim present |

Room walk: “Postman works, browser doesn’t — what do you check first?” → CORS / `VITE_API_URL`.
