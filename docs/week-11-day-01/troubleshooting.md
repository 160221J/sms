# Troubleshooting — Week 11

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| `range` hangs | Channel never closed | Sender closes after last send |
| Panic: send on closed channel | Closed too early / wrong owner | Only producer closes |
| Panic: close of closed channel | Multiple closers | One closer only |
| Results missing | Closed `results` before workers finished | `wg.Wait()` then close |
| “Pool” still races map | Concurrent map writes | Week 12 mutex; or single writer goroutine |
| Import 400 always | Bind expects object not array | `[]CreateStudentRequest` |

Room walk: “How many goroutines per 10k jobs?” — answer must be ~N workers, not 10k.
