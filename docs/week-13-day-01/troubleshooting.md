# Troubleshooting — Week 13

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| `parsing time ... YYYY-MM-DD` | Used `YYYY-MM-DD` as layout | Layout must be `2006-01-02` |
| httptest always 404 | Route not registered on test engine | `r.GET("/health", ...)` before ServeHTTP |
| Can’t inject fake | Handler takes concrete `*StudentRepository` | Depend on `StudentStore` interface |
| CI gofmt fails | Unformatted files | `gofmt -w .` |
| Cover 0% on handlers | Tests in wrong package / build tags | `*_test.go` next to code; same module |
| Delve not found | Not installed | `go install github.com/go-delve/delve/cmd/dlv@latest` |

Room walk: “Why an interface on the repository?” — answer must mention **fakes / tests**.
