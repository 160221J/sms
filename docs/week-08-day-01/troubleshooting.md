# Troubleshooting — Week 8

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| `panic: runtime error: invalid memory address` | Nil handler or nil repo | `New…()` before `r.GET`; check field assignment |
| `undefined: repository` | Missing import / package | `internal/repository`; module path matches `go.mod` |
| Create works but list empty after extract | Two maps (handler + repo) | Delete map fields from handler; only use `h.repo` |
| Import cycle | Repo imports handlers | Never; repository must not know HTTP |
| `go: download go1.25` fails | Toolchain mismatch | Use `go 1.22` in starter `go.mod` or set `GOTOOLCHAIN=local` |
| Tests fail randomly | Map iteration order | Sort by id in tests if asserting order |

Room walk: ask “where does the map live now?” — answer must be repository.
