# Pre-class — Week 12, Day 1

Bring week 11: worker pool + WaitGroup join.

Today: **mutex**, **context**, **`go test -race`** for real (red → green), and a graceful-shutdown sketch.

**Install before class (Ubuntu):**

```bash
sudo apt-get install -y build-essential
# then: CGO_ENABLED=1 go test -race ./...
```

Without a C compiler, `-race` cannot run.
