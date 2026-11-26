# Week 14 sql-lab — injection BAD vs GOOD

Shows how string concatenation builds a dangerous SQL string, and how `$1` placeholders keep input separate.

```bash
go test -v ./inject/
```

No live database required — the lesson is in the query *text*.
