# Week 12 race lab — red → mutex → green

```bash
# needs a C compiler (Ubuntu: sudo apt-get install -y build-essential)
CGO_ENABLED=1 go test -race ./counter/   # start from Unsafe* if teaching fail-first
CGO_ENABLED=1 go test -race ./...
```

Packages:

- `counter` — unsafe increment (racy) + `SafeAdd` with Mutex
- `store` — unsafe map writes vs mutex-protected map

Homework: put `go test -race ./...` in your project README.
