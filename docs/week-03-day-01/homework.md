# Homework — Week 3, Day 1

Due: **before the next session** (instructor: fill date _______________).

Submit in a GitHub repo (same as weeks 1–2, or a new `epic-go-week03` repo). Folder layout:

```
week03/
  control.go
  slices.go
  freq.go
  slicekit/
    go.mod
    slicekit.go
    slicekit_test.go
  exercises.md          # short answers for 1–8
```

No zip files, no WhatsApp screenshots-only.

## Exercises 1–8 (write the answer in `exercises.md`)

Run the code. Then write **one or two sentences** plus the output. Your words.

1. **`if` short statement.** Write an `if` that declares `n := len(s)` and prints `"empty"` when `n == 0`. Is `n` visible after the `if`?
2. **Tagless `switch`.** Grade bands for scores 80 / 65 / 40 using a tagless `switch`. Paste the code.
3. **`for` shapes.** Show a C-style loop and a while-style loop that both print `3 2 1`.
4. **`append` assign.** Start with `var xs []int`, append `1`, then `2`. What is wrong with calling `append` and ignoring the return?
5. **Backing array.** Reproduce the gotcha: `a := []int{10,20,30,40}`; `b := a[:2]`; `b = append(b, 99)`. What is `a` after? Why?
6. **Independent copy.** Make a copy of a slice that does **not** share a backing array. Prove it by mutating the copy.
7. **Comma-ok.** On a map, distinguish “key missing” from “key present with value `0`”. Paste the check.
8. **Map range order.** Range the same map twice. Did the print order match? What does that mean for tests?

## Exercise 9 — harden the lab package

In `slicekit`, keep green tests for:

```go
func Contains(list []string, want string) bool
func Unique(list []string) []string
func Freq(words []string) map[string]int
```

Add these cases (table-driven is fine; copy the week-2 test style if you prefer):

| Function | Input | Want |
| --- | --- | --- |
| `Contains` | `nil`, `"SE"` | `false` |
| `Unique` | `["SE","CS","SE","IT","CS"]` | `["SE","CS","IT"]` (order preserved) |
| `Unique` | `nil` or empty | empty slice |
| `Freq` | `["a","b","a"]` | `a:2`, `b:1` |
| `Freq` | empty | empty map (len 0) |

```bash
cd slicekit
go test
```

Must be green. Assert map contents with comma-ok — do **not** compare `fmt.Sprint` of a map.

## Exercise 10 (optional reading)

Skim [Effective Go](https://go.dev/doc/effective_go) sections on slices and maps. Write five lines in `exercises.md`: one thing you already knew, one thing that surprised you.

## How it is checked

| Requirement | Pass |
| --- | --- |
| Repo URL sent | Yes |
| Demo files run | Shown in class or committed |
| `go test` in `slicekit/` is green | Including harden cases |
| `exercises.md` is your words | Oral question next class |
| `gofmt` clean, no binaries | `.gitignore` working |
