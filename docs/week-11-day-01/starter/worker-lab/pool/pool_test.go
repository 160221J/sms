package pool

import (
	"crypto/sha256"
	"encoding/hex"
	"testing"
)

func TestRunHashesMatchesSHA256(t *testing.T) {
	texts := []string{"ada", "lovelace", "go"}
	got := RunHashes(texts, 3)
	if len(got) != len(texts) {
		t.Fatalf("got %d results, want %d", len(got), len(texts))
	}
	byIndex := map[int]Result{}
	for _, r := range got {
		byIndex[r.Index] = r
	}
	for i, text := range texts {
		sum := sha256.Sum256([]byte(text))
		want := hex.EncodeToString(sum[:])
		if byIndex[i].Digest != want {
			t.Fatalf("index %d: got %s want %s", i, byIndex[i].Digest, want)
		}
	}
}

func TestRunHashesSingleWorker(t *testing.T) {
	got := RunHashes([]string{"x"}, 1)
	if len(got) != 1 {
		t.Fatalf("got %d", len(got))
	}
}
