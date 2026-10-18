# Troubleshooting — Week 9

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| Missing id still 200 / empty | Repo returns zero value without error | Return `ErrNotFound` |
| Always 500 on missing | Not using `errors.Is` | Map sentinel before generic 500 |
| `errors.Is` false after wrap | Used `%v` / `%s` instead of `%w` | `fmt.Errorf("...: %w", err)` |
| Panic in handler | `panic(err)` or nil deref | Return JSON; construct handlers |
| slog not JSON | Text handler / Println left | `slog.NewJSONHandler(os.Stdout, nil)` |
| Secrets in git | Committed `.env` | Delete from history discussion; gitignore; rotate secret |
| `godotenv` missing | Module not tidy | `go get github.com/joho/godotenv` |

Room walk: ask “404 or 500?” for missing student — answer must be 404.
