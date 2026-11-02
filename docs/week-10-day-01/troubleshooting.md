# Troubleshooting — Week 10

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| `-race` not available | Old Go / wrong toolchain | Use Go 1.22+; `go version` |
| No DATA RACE | Compiler optimized trivial case / too few iters | Use the provided counter lab as-is |
| Fan-out hangs | Forgot to signal done / closed wrong | Follow starter `ValidateStudentConcurrent` |
| Prints out of order | Expected | Goroutine scheduling is nondeterministic |
| Create “async” flakes | Naked `go` in handler | Remove it; keep sync (course rule) |
| Loop variable bug | `go func(){ use i }` without arg | `go func(i int){ ... }(i)` |

Room walk: ask “may Create use go today?” — answer must be no.
