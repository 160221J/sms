# Homework — Week 2, Day 1

Due: **before the next session** (instructor: fill date _______________).

Submit in a GitHub repo (same as `hello.go`, or a new `epic-go-week02` repo). Folder layout:

```
week02/
  zeros.go
  greet.go
  names/
    go.mod
    names.go
    names_test.go
  exercises.md          # short answers for 1–9
```

No zip files, no WhatsApp screenshots-only.

## Exercises 1–9 (write the answer in `exercises.md`)

Run the code. Then write **one or two sentences** plus the output. Your words.

1. **Zero values.** Declare `var n int`, `var s string`, `var ok bool` and print them with `Printf` and `%d %q %t`. What printed, and why is that better than “uninitialized”?
2. **`var` vs `:=`.** Show one `var` at package level and one `:=` inside `main`. What happens if you move the `:=` to package level?
3. **Conversion.** `year := 2026` then add `0.5`. Make it compile. What is `int(3.9)`?
4. **`const`.** Declare `const institute = "Epic Learn"`. Try to assign a new value. Paste the compiler error.
5. **`iota` (light).** A `const` block with `active`, `idle`, `archived` using `iota`. Print the three numbers.
6. **Operators.** Print `10 / 3` and `float64(10) / 3`. Explain the difference. Show `enrolled && paid` when one is `false`.
7. **`fmt` verbs.** Print one value with `%v`, `%T`, and `%q`. When would you pick each?
8. **`strings`.** `TrimSpace`, `ToUpper`, and `Contains` on `"  sms  "`. What does each return?
9. **Bytes vs runes.** Print `len` and `utf8.RuneCountInString` for `"café"` and `"සිංහල"`. Measure — do not guess how many “letters” Sinhala has. Why are the two numbers different?

## Exercise 10 — `FullName` + `go test`

```go
func FullName(first, last string) string
```

- Trim spaces on both parts.
- Join with **one** space.
- Empty last name → return only the trimmed first name (no trailing space).
- Empty first name → return only the trimmed last name.

Minimum tests in `names_test.go`:

| Input | Want |
| --- | --- |
| `"Ada"`, `"Lovelace"` | `"Ada Lovelace"` |
| `"  Ada  "`, `"  Lovelace  "` | `"Ada Lovelace"` |
| `"Ada"`, `"   "` | `"Ada"` |

```bash
cd names
go test
```

Must be green. You may add more table rows. We are **not** mastering `testing` this week — you are seeing the command and a failing vs passing test.

## How it is checked

| Requirement | Pass |
| --- | --- |
| Repo URL sent | Yes |
| `zeros.go` and `greet.go` run | Shown in class or committed |
| `go test` in `names/` is green | Including the trim cases |
| `exercises.md` is your words | Oral question next class |
| `gofmt` clean, no binaries | `.gitignore` working |
