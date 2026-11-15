# Student Management System — Week 13 starter

Week 12 base plus testing & CI:

- **`FullNameOf` / optional `date_of_birth`** on models + table tests
- **`StudentStore` interface** + **`FakeStudentStore`**
- Handlers depend on the interface; **httptest** tests for health + Create
- **GitHub Actions:** `.github/workflows/ci.yml` (`gofmt`, `vet`, `test`)

Primary lab kata: `../date-lab/` (table-driven `YYYY-MM-DD`).

## Test (homework)

```bash
go test ./...
go test ./... -cover
go vet ./...
gofmt -l .
```

At least **5 tests** in your PR. CI workflow must be present.

## Run

```bash
go mod tidy
go run ./cmd/server
curl -s localhost:8080/health
```

Note: if you copy this starter into a real repo root, move `.github/workflows/ci.yml` to the repository root (or set `working-directory` to this module).
