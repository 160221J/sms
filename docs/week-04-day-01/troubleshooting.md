# Week 4 troubleshooting

| What they see | Likely cause | What you do |
| --- | --- | --- |
| `package X is not in std` | no `go.mod` / wrong import | `go mod init student-management-system` in `backend/` |
| `directory prefix . does not contain main module` | ran go tools outside module | `cd` into `backend/` |
| `go run: cannot run *_test.go` files | wrong files | run `./cmd/server` |
| prints nothing / wrong file | ran an old `main.go` | show `go run ./cmd/server` |
| empty folders missing on GitHub | Git ignores empty dirs | add `.gitkeep` in each `internal/*` |
| `go: go.mod file not found` | nested wrong folder | one `go.mod` at `backend/` |
| trying to `go get github.com/gin-gonic/gin` | jumped ahead | stop — week 5 |
| `.env` in the PR | never created ignore | add `.gitignore`; `git rm --cached .env` |
| binaries committed | built in-tree | ignore `*.exe`, `server`, `bin/` |
| Windows path / PowerShell | wrong shell | stay in **Ubuntu (WSL)** |

## Scaffold reset

```bash
rm -rf ~/epic-go/sms
mkdir -p ~/epic-go/sms/backend
cd ~/epic-go/sms/backend
go mod init student-management-system
# recreate folders + main.go from the handout
```

Do not paste the whole finished course repo. They must type the skeleton.
