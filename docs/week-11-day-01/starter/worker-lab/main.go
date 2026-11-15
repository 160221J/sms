package main

import (
	"flag"
	"fmt"
	"os"

	"worker-lab/pool"
)

func main() {
	n := flag.Int("n", 4, "number of workers")
	flag.Parse()

	texts := []string{
		"ada", "charles", "grace", "linus", "rob", "ken", "dijkstra", "hopper",
	}
	if flag.NArg() > 0 {
		texts = flag.Args()
	}

	results := pool.RunHashes(texts, *n)
	for _, r := range results {
		fmt.Printf("%d\t%s\t%s\n", r.Index, r.Text, r.Digest[:12]+"…")
	}
	fmt.Fprintf(os.Stderr, "workers=%d jobs=%d\n", *n, len(texts))
}
