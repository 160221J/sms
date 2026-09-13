# Week 3 troubleshooting

Walk the room with this page. Most failures are missing braces, forgotten `append` assign, nil maps, or flaky map-order tests.

| What they see | Likely cause | What you do |
| --- | --- | --- |
| `non-boolean condition in if` | `if score` with an int | `if score != 0` or compare properly |
| syntax error near `if` | parentheses from C/JS, or missing `{` | braces required; no `( )` around cond |
| `i declared and not used` | ranged but ignored poorly | use `_` for unused index/value |
| slice length wrong after append | did not assign | `s = append(s, x)` |
| “append changed the other slice” | shared backing array | draw boxes; `copy` / `append([]T(nil), s...)` for independence |
| `assignment to entry in nil map` | wrote before `make` | `m = make(map[string]int)` |
| `go test` fails comparing maps as strings | relied on print order | check each key with comma-ok |
| `Unique` output shuffled | ranged a map for output | use `seen` map + append to slice in input order |
| `Contains` always false | compared wrong type / trimmed badly | print inputs; keep it simple equality |
| `go: cannot find main module` | no `go.mod` | `go mod init epiclearn/week03` in `slicekit` |
| `undefined: Contains` in test | different packages / unsaved file | both files `package slicekit` |
| infinite loop | `for {` without `break` | add exit condition |
| Windows PowerShell oddities | wrong terminal | stay in **Ubuntu (WSL)** |
| Binary on GitHub | `.gitignore` missing | ignore binaries; `git rm --cached` |

## `go test` ritual

```bash
cd ~/epic-go/week03/slicekit
go mod init epiclearn/week03   # once
go test
```

If they already have a `go.mod`, do not run `go mod init` again.

## Nuclear rewrite

If a student’s folder is a mess, clean `~/epic-go/week03` and retype demos. Do not paste the starter until they have tried the labs.
