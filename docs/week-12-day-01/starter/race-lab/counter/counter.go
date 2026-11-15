package counter

import "sync"

// UnsafeAdd increments n from many goroutines with no synchronization.
// Intentionally racy — use to show go test -race FAIL.
func UnsafeAdd(goroutines int) int {
	var n int
	var wg sync.WaitGroup
	wg.Add(goroutines)
	for i := 0; i < goroutines; i++ {
		go func() {
			defer wg.Done()
			n++
		}()
	}
	wg.Wait()
	return n
}

// SafeAdd is the week-12 fix: Mutex around the increment.
func SafeAdd(goroutines int) int {
	var (
		n  int
		mu sync.Mutex
		wg sync.WaitGroup
	)
	wg.Add(goroutines)
	for i := 0; i < goroutines; i++ {
		go func() {
			defer wg.Done()
			mu.Lock()
			n++
			mu.Unlock()
		}()
	}
	wg.Wait()
	return n
}
