package counter

import "sync"

// UnsafeAdd increments n from many goroutines with no synchronization.
// This is intentionally racy for the week-10 lab.
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
