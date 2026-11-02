# Week 10 goroutine lab

## Counter race (intentionally broken)

```bash
go test -race ./counter/
```

Expect **DATA RACE**. Mutex fix is week 12 — observe today.

## Fan-out validation

```bash
go test ./validate/
```

Three independent field checks run concurrently; errors are collected.
