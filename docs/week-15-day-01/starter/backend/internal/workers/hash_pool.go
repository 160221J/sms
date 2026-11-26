package workers

import (
	"crypto/sha256"
	"encoding/hex"
	"sync"
)

// HashAll is the same pool shape as the worker-lab kata (homework option B).
func HashAll(texts []string, nWorkers int) []string {
	if nWorkers < 1 {
		nWorkers = 1
	}
	jobs := make(chan string)
	results := make(chan string)

	var wg sync.WaitGroup
	wg.Add(nWorkers)
	for i := 0; i < nWorkers; i++ {
		go func() {
			defer wg.Done()
			for text := range jobs {
				sum := sha256.Sum256([]byte(text))
				results <- hex.EncodeToString(sum[:])
			}
		}()
	}

	go func() {
		wg.Wait()
		close(results)
	}()

	go func() {
		for _, text := range texts {
			jobs <- text
		}
		close(jobs)
	}()

	out := make([]string, 0, len(texts))
	for digest := range results {
		out = append(out, digest)
	}
	return out
}
