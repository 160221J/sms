package pool

import (
	"crypto/sha256"
	"encoding/hex"
	"sync"
)

// Job is one string to hash.
type Job struct {
	Index int
	Text  string
}

// Result is the digest (or empty Text on unlikely failure path).
type Result struct {
	Index  int
	Text   string
	Digest string
}

// RunHashes processes texts with nWorkers. nWorkers is clamped to at least 1.
func RunHashes(texts []string, nWorkers int) []Result {
	if nWorkers < 1 {
		nWorkers = 1
	}
	jobs := make(chan Job)
	results := make(chan Result)

	var wg sync.WaitGroup
	wg.Add(nWorkers)
	for w := 0; w < nWorkers; w++ {
		go func() {
			defer wg.Done()
			for job := range jobs {
				sum := sha256.Sum256([]byte(job.Text))
				results <- Result{
					Index:  job.Index,
					Text:   job.Text,
					Digest: hex.EncodeToString(sum[:]),
				}
			}
		}()
	}

	go func() {
		wg.Wait()
		close(results)
	}()

	go func() {
		for i, text := range texts {
			jobs <- Job{Index: i, Text: text}
		}
		close(jobs)
	}()

	out := make([]Result, 0, len(texts))
	for r := range results {
		out = append(out, r)
	}
	return out
}
