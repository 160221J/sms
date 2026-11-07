# Week 11 worker pool kata

Hash a list of strings with a fixed pool of N workers.

```bash
go test ./...
go run . -n 4
```

Pattern: `jobs` channel → N workers → `results` channel. Close `jobs` after enqueue; `WaitGroup` then close `results`.
