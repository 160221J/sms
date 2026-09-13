# Week 3, Day 1 — presenter notes

Slides: open [`week-03-day-01.html`](week-03-day-01.html) in Chrome/Firefox → **F** fullscreen → arrows. **N** shows the speaker note for the current slide. **P** prints to PDF.

This session is **control flow + collections + survival functions**. No SMS code. Two labs. Dense — protect the backing-array demo and comma-ok.

## Timing (3–3.5 hours)

| Clock | Block | Slides |
| --- | --- | --- |
| 0:00–0:15 | Homework check (`FullName` + exercises) | 1–2 |
| 0:15–0:25 | Outcomes + SE framing | 3–4 |
| 0:25–0:55 | `if`, short statement, `switch` | 5–8 |
| 0:55–1:20 | `for`, `range`, break/continue (**live** `control.go`) | 9–12 |
| 1:20–2:00 | Arrays/slices, `append`, backing gotcha (**live**) | 13–17 |
| 2:00–2:25 | Maps, comma-ok, freq (**live**) | 18–21 |
| 2:25–2:40 | Functions survival kit + test tables | 22–24 |
| 2:40–end | Lab 1 then Lab 2 | 25–end |

There is **no agenda slide** and **no homework slide**. Homework stays on the student handout. If late, cut variadic/closures live typing — never cut the slice gotcha or comma-ok.

## Live demo script

### 1. Control (`~/epic-go/week03/control.go`)

```go
package main

import "fmt"

func main() {
	grade := "B"
	switch grade {
	case "A", "B":
		fmt.Println("good")
	default:
		fmt.Println("work")
	}
	for i, r := range "Go" {
		fmt.Printf("%d %c\n", i, r)
	}
}
```

```bash
gofmt -w control.go
go run control.go
```

### 2. Slice gotcha (`~/epic-go/week03/slices.go`)

```go
package main

import "fmt"

func main() {
	a := []int{10, 20, 30, 40}
	b := a[:2]
	fmt.Println("before", a, b, "cap(b)=", cap(b))
	b = append(b, 99)
	fmt.Println("after ", a, b)
}
```

Draw the backing array. Then show a full-capacity case where `append` allocates and `a` is unchanged.

### 3. Frequency (`~/epic-go/week03/freq.go`)

```go
words := []string{"SE", "CS", "SE", "IT", "SE"}
count := make(map[string]int)
for _, w := range words {
	count[w]++
}
```

Point out: missing key reads as `0`, so `++` works. Then comma-ok for `"SE"`.

### 4. Lab package (`~/epic-go/week03/slicekit/`)

```bash
mkdir -p ~/epic-go/week03/slicekit
cd ~/epic-go/week03/slicekit
go mod init epiclearn/week03
```

Students implement `Contains`, `Unique`, `Freq` with tests. Fail a test first when you demo `Contains`.

## Lab gate (they do not leave without)

- [ ] Worksheet filled (control, slice gotcha, comma-ok)
- [ ] Paper test table for `Contains`
- [ ] `go test` green for `Contains`, `Unique`, `Freq`
- [ ] Can explain the shared backing array in one sentence
- [ ] GitHub URL collected

## Homework

Slice/map exercises on the handout; harden `Unique` / `Freq`; optional Effective Go reading (slices + maps sections).

## Typical failures

| Symptom | Fix |
| --- | --- |
| `if score {` | need a bool: `if score != 0` |
| missing braces on `if` | braces required in Go |
| `append(s, x)` without assign | `s = append(s, x)` |
| subslice overwrite surprise | draw backing array; copy if independent |
| `m[k] = v` on nil map | `m = make(map[K]V)` first |
| test fails on `fmt.Sprint(map)` | assert keys with comma-ok, not print order |
| `Unique` loses order | append to result only on first see |
| unused loop variable | use `_` |
| `go test`: no `go.mod` | `go mod init epiclearn/week03` |

## What not to teach today

Methods, pointers as theory, modules as theory, REST, Gin, the SMS repo, `defer`, generics, channels. Tease week 4 only.
