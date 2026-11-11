package store

import "sync"

// UnsafeSet writes the same key from many goroutines — racy map.
func UnsafeSet(goroutines int) map[string]int {
	m := map[string]int{}
	var wg sync.WaitGroup
	wg.Add(goroutines)
	for i := 0; i < goroutines; i++ {
		go func(v int) {
			defer wg.Done()
			m["n"] = v
		}(i)
	}
	wg.Wait()
	return m
}

// SafeStore protects the map with a Mutex (SMS-shaped).
type SafeStore struct {
	mu   sync.Mutex
	data map[string]int
}

func NewSafeStore() *SafeStore {
	return &SafeStore{data: map[string]int{}}
}

func (s *SafeStore) Set(key string, v int) {
	s.mu.Lock()
	defer s.mu.Unlock()
	s.data[key] = v
}

func (s *SafeStore) Get(key string) (int, bool) {
	s.mu.Lock()
	defer s.mu.Unlock()
	v, ok := s.data[key]
	return v, ok
}
