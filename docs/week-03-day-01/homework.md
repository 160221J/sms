# Homework — Week 3 coding (due before next class)

Instructor: fill due date _______________

Submit a GitHub repo (same as weeks 1–2, or `epic-go-week03`). **No zip files.**

```
week03/
  go.mod
  main.go                 # optional demos / prints
  homework/
    homework.go           # your functions
    homework_test.go      # green tests
  notes.md                # short answers (Q1–Q3 only)
```

```bash
cd week03
go mod init epiclearn/week03   # once
cd homework && go test -v
```

Use only Week 3 tools: `if` / `switch` / `for` / `range`, slices, maps, functions, `go test`.  
No structs methods, no pointers theory, no HTTP, no SMS repo.

---

## Part A — short notes (`notes.md`)

Answer in **2–4 sentences each** (your words):

1. Why must you write `s = append(s, x)` instead of only `append(s, x)`?
2. After `b := a[:2]; b = append(b, 99)`, why can `a` change? How do you make an independent copy?
3. How do you tell “key missing” from “key present with value `0`” on a map?

---

## Part B — coding (all in `homework/`)

Implement these functions. Keep them small. Add table-driven tests.

### 1. `Contains(list []string, want string) bool`

Return true if `want` appears at least once.

| list | want | result |
| --- | --- | --- |
| `["SE","CS"]` | `"SE"` | true |
| `["SE","CS"]` | `"IT"` | false |
| `nil` | `"SE"` | false |

### 2. `Unique(list []string) []string`

First occurrence wins; **keep order**.

| input | want |
| --- | --- |
| `["SE","CS","SE","IT","CS"]` | `["SE","CS","IT"]` |
| `nil` / empty | empty slice (len 0) |

### 3. `Freq(words []string) map[string]int`

Count how often each word appears.

| input | want |
| --- | --- |
| `["a","b","a"]` | `a:2`, `b:1` |
| empty / nil | empty map (`len == 0`) |

Assert with **comma-ok**. Do not compare `fmt.Sprint(map)`.

### 4. `Filter(list []string, keep string) []string`

Return a new slice with only values equal to `keep` (SMS preview: filter by course).

| list | keep | want |
| --- | --- | --- |
| `["SE","CS","SE"]` | `"SE"` | `["SE","SE"]` |
| `["SE","CS"]` | `"IT"` | empty |

### 5. `Max(nums []int) (int, bool)`

Return the largest value. Second result is `false` if the slice is empty/nil (no panic).

| nums | want | ok |
| --- | --- | --- |
| `[]int{3, 9, 4}` | `9` | true |
| `nil` / empty | `0` | false |

### 6. `Reverse(nums []int) []int`

Return a **new** reversed slice. Do not mutate the caller’s slice (backing-array lesson).

| input | want |
| --- | --- |
| `[]int{1, 2, 3}` | `[]int{3, 2, 1}` |
| after call, original still | `[]int{1, 2, 3}` |

### 7. `Intersection(a, b []string) []string`

Values that appear in **both** slices. Order = first-seen order from `a`. No duplicates in the result.

| a | b | want |
| --- | --- | --- |
| `["SE","CS","IT"]` | `["IT","SE","SE"]` | `["SE","IT"]` |
| `["SE"]` | `["CS"]` | empty |

Hint: build a `map[string]bool` from `b`, then range `a`.

### 8. `Grade(score int) string` (light algorithm + `switch`)

| score | grade |
| --- | --- |
| 75–100 | `"A"` |
| 65–74 | `"B"` |
| 50–64 | `"C"` |
| 0–49 | `"F"` |
| anything else | `"?"` |

Use a **tagless** `switch`.

---

## Skeleton (optional start)

```go
package homework

func Contains(list []string, want string) bool { /* ... */ }

func Unique(list []string) []string { /* ... */ }

func Freq(words []string) map[string]int { /* ... */ }

func Filter(list []string, keep string) []string { /* ... */ }

func Max(nums []int) (int, bool) { /* ... */ }

func Reverse(nums []int) []int { /* ... */ }

func Intersection(a, b []string) []string { /* ... */ }

func Grade(score int) string { /* ... */ }
```

---

## Stretch (optional, not required to pass)

Pick **one**:

- `SumEven(nums []int) int` — sum only even numbers  
- `IsPalindrome(s string) bool` — ignore spaces; compare runes, not bytes  
- `TopWord(words []string) (string, int)` — word with highest frequency (if tie, any is fine)

Add tests if you do a stretch.

---

## How it is marked

| Requirement | Pass |
| --- | --- |
| Repo URL sent | Yes |
| `notes.md` answers Q1–Q3 | Your words |
| `go test` in `homework/` is green for functions 1–8 | Required |
| `gofmt` clean, no binaries committed | Yes |
| Stretch | Bonus only |

**Time box:** aim for **2–4 hours**. If stuck >20 minutes on one function, move on and ask next class — bring your failing test output.
