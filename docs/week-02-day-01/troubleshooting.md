# Week 2 troubleshooting

Walk the room with this page. Most failures are declaration syntax, missing `go.mod`, or forgetting `*` on flags.

| What they see | Likely cause | What you do |
| --- | --- | --- |
| `syntax error: non-declaration statement outside function body` | `:=` at package level | `var name = "Ada"` at the top of the file |
| `no new variables on left side of :=` | name already exists | use `=` |
| `undefined: name` | they used `=` before `var` / `:=` | declare first |
| `invalid operation: mismatched types int and float64` | implicit conversion habit from JS/Python/Java | `float64(n)` or `int(f)` |
| `cannot use x (variable of type int64) as int` | `int` ≠ `int64` | convert explicitly |
| prints `0xc000010230` | they printed the flag pointer | `*first` not `first` |
| `undefined: flag` | missing import | `import "flag"` |
| `flag provided but not defined` | they used `-name` but declared `-first` | match the flag names |
| `go: cannot find main module; see 'go help modules'` | `go test` with no `go.mod` | `go mod init epiclearn/week02` in that folder |
| `package names is not in std` | they ran `go run names.go` from the wrong place | `cd` into the `names` folder; `go test` |
| `undefined: FullName` in the test | different packages, or file not saved | both files `package names` in the same folder |
| `len("café")` is 5 | they think `len` counts letters | bytes vs runes; `utf8.RuneCountInString` |
| `a++` error inside `Println` | `++` is a statement | `a++` on its own line |
| `time: parsing time … cannot parse` | they used `YYYY-MM-DD` as the layout | layout is `2006-01-02` |
| `go version` still not 1.25 | leftover from week 1 | use the week 1 install sheet; do not start types on apt Go |
| Windows: flags work in PowerShell, fail in Ubuntu | they are in the wrong terminal | stay in **Ubuntu (WSL)** |
| Binary `zeros` / `greet` on GitHub | `.gitignore` missing | ignore the binaries; `git rm --cached` |

## `go test` ritual (not a modules lecture)

```bash
cd ~/epic-go/week02/names
go mod init epiclearn/week02   # once
go test
```

If they already have a `go.mod`, do not run `go mod init` again.

## Nuclear rewrite of the demo files

If a student’s folder is a mess, they start a clean `~/epic-go/week02` and copy only what they typed today. Do not paste the starter until they have tried.
