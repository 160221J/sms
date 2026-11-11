# Troubleshooting — Week 12

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| `-race` needs cgo | CGO_ENABLED=0 | `CGO_ENABLED=1 go test -race ./...` |
| `cgo: C compiler "gcc" not found` | No gcc | `sudo apt-get install -y build-essential` |
| Still races with WaitGroup | WaitGroup is not a lock | Add `sync.Mutex` around shared data |
| Deadlock | Forgot Unlock / locked twice | `defer mu.Unlock()` right after Lock |
| Timeout demo never cancels | Ignoring `ctx.Done()` | `select` on `ctx.Done()` in the wait |
| Shutdown hangs | In-flight request blocked | Shorten demo sleeps; use Shutdown timeout |

Room walk: “Does WaitGroup stop a data race?” — answer must be **no**.
