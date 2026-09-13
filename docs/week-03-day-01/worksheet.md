# Lab worksheet — control flow, slices, maps

Name: _______________________ · GitHub: _______________________

Fill this **before** you leave. Then tick the [lab sheet](lab-sheet.html).

## A. Control flow

| Question | Your answer |
| --- | --- |
| Does `if score {` compile when `score` is `int`? |  |
| Are braces required on a one-line `if`? |  |
| What is a tagless `switch`? |  |
| Go’s only loop keyword is… |  |

## B. Slice gotcha

Run (or predict, then run):

```go
a := []int{10, 20, 30, 40}
b := a[:2]
b = append(b, 99)
fmt.Println(a, b, cap(b))
```

| Prompt | Write it |
| --- | --- |
| `cap(b)` before append |  |
| `a` after append |  |
| One sentence: why did `a` change (or not)? |  |

## C. Maps / comma-ok

| Code | What prints / happens? |
| --- | --- |
| `var m map[string]int; m["x"] = 1` |  |
| `m := make(map[string]int); fmt.Println(m["x"])` |  |
| `v, ok := m["x"]` when missing |  |

## D. Paper test table for `Contains`

Fill **before** you code.

| list | want | result |
| --- | --- | --- |
| `["SE","CS"]` | `"SE"` |  |
| `["SE","CS"]` | `"IT"` |  |
| `[]` | `"SE"` |  |
| `["SE","SE"]` | `"SE"` |  |

## E. Labs (tick when done)

- [ ] `Contains` tests green
- [ ] `Unique` preserves first-seen order; tests green
- [ ] `Freq` tests green (comma-ok assertions)
- [ ] I can explain the backing-array gotcha in one sentence
