# Lab worksheet — zero values and conversions

Name: _______________________ · GitHub: _______________________

Fill this **before** you leave. Then tick the [lab sheet](lab-sheet.html).

## A. Zero values

Write the zero value. Do not guess from another language.

| Declaration | Type | Zero value (write it) |
| --- | --- | --- |
| `var n int` |  |  |
| `var f float64` |  |  |
| `var s string` |  |  |
| `var ok bool` |  |  |
| `var p *int` |  |  |

What printed when you ran `zeros.go`?

```
(paste)
```

## B. Which lines compile?

Mark **OK** or **FAIL**. If FAIL, write the fix.

| Code | OK / FAIL | Fix (if FAIL) |
| --- | --- | --- |
| `var a int = 3; var b float64 = 1.5; fmt.Println(a + b)` |  |  |
| `year := 2026; fmt.Println(float64(year) + 0.5)` |  |  |
| `fmt.Println(int(3.9))` |  |  |
| `var x int = 5; var y int64 = x` |  |  |
| `name := "Ada"; name := "Grace"` |  |  |
| `count := 1; count = 2` |  |  |

## C. Operators (quick)

| Expression | Result | Why |
| --- | --- | --- |
| `10 / 3` |  |  |
| `10 % 3` |  |  |
| `true && false` |  |  |
| `"Ada" == "ada"` |  |  |

## D. Bytes vs runes

| String | `len(...)` | `utf8.RuneCountInString(...)` |
| --- | --- | --- |
| `"cafe"` |  |  |
| `"café"` |  |  |
| `"සිංහල"` |  |  |

One sentence: why is `len("café")` not 4?

## E. CLI + test (tick when done)

- [ ] `go run greet.go -first Ada -last Lovelace` prints a full name
- [ ] `cd names && go test` is green
- [ ] I can explain what `go mod init` did in one sentence (even if the full story is week 4)
