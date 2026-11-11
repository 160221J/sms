package store

import (
	"sync"
	"testing"
)

func TestSafeStoreConcurrent(t *testing.T) {
	s := NewSafeStore()
	var wg sync.WaitGroup
	const n = 50
	wg.Add(n)
	for i := 0; i < n; i++ {
		go func(v int) {
			defer wg.Done()
			s.Set("n", v)
		}(i)
	}
	wg.Wait()
	if _, ok := s.Get("n"); !ok {
		t.Fatal("missing key")
	}
}

func TestUnsafeSetDocumentsRace(t *testing.T) {
	t.Skip("enable to demo map DATA RACE on projector")
	_ = UnsafeSet(50)
}
