# Troubleshooting — Week 16

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| Demo DB empty | Fresh DB / wrong `DB_NAME` | Re-run migration; register a user live |
| JWT 401 mid-demo | Stale token / wrong secret | Login again; check `JWT_SECRET` |
| React CORS mid-demo | Origin mismatch | Prefer Postman backup path |
| CI red, local green | Different Go / missing workflow | Fix before demo if possible; show local `go test` |
| Overtime | Too many features | Cut to health → login → one CRUD → one file |
| Can’t explain a function | AI paste | Drop that slide; show code they own |

Room walk: “What’s your backup if the React app dies?” → Postman collection.
