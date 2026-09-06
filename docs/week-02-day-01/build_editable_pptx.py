#!/usr/bin/env python3
"""Build an editable PowerPoint of the Week 2 Day 1 deck (native text, not screenshots)."""

from __future__ import annotations

import sys
from pathlib import Path

try:
    from pptx import Presentation
    from pptx.dml.color import RGBColor
    from pptx.enum.shapes import MSO_SHAPE
    from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
    from pptx.util import Inches, Pt
except ImportError:
    req = Path(__file__).resolve().parent / "requirements.txt"
    sys.stderr.write(
        "Missing python-pptx. From the repo root run:\n"
        f"  python3 -m pip install --user -r {req}\n"
    )
    raise

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[1]
LOGO = REPO / "docs" / "branding" / "epic-learn-logo.png"
OUT = ROOT / "pdf" / "week-02-day-01-slides.pptx"
FOOTER = "Epic Learn Institute of Higher Education - Go Programming Master Course"

INK = RGBColor(0x14, 0x20, 0x2B)
MUTED = RGBColor(0x4D, 0x5D, 0x6B)
TEAL = RGBColor(0x0B, 0x6E, 0x68)
TEAL_DARK = RGBColor(0x08, 0x4F, 0x4B)
NAVY = RGBColor(0x0A, 0x2A, 0x5C)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
CREAM = RGBColor(0xF4, 0xEF, 0xE6)
CARD = RGBColor(0xFF, 0xFD, 0xF9)
LINE = RGBColor(0xD8, 0xCF, 0xC2)
CODE_BG = RGBColor(0x10, 0x21, 0x2C)
CODE_FG = RGBColor(0xE8, 0xF2, 0xEF)
GOLD = RGBColor(0xD9, 0xB8, 0x26)
TITLE_BG = RGBColor(0x14, 0x2A, 0x32)
CREAM_TEXT = RGBColor(0xEA, 0xD9, 0xA3)
LIVE = RGBColor(0xC2, 0x4E, 0x1D)

W, H = 13.333, 7.5
MX = 0.65
HEADER_H = 0.78
FOOTER_H = 0.42
CONTENT_TOP = 0.95
TOTAL = 26


def _font(run, name="Calibri", size=18, bold=False, color=INK):
    run.font.name = name
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color


def _fill(shape, color):
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()


def add_textbox(slide, l, t, w, h, text, size=18, bold=False, color=INK, font="Calibri", align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP):
    box = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    tf = box.text_frame
    tf.word_wrap = True
    tf.auto_size = None
    try:
        tf._txBody.bodyPr.set("anchor", {MSO_ANCHOR.TOP: "t", MSO_ANCHOR.MIDDLE: "ctr", MSO_ANCHOR.BOTTOM: "b"}[anchor])
    except Exception:
        pass
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    _font(run, font, size, bold, color)
    return box


def add_bullets(slide, l, t, w, h, items, size=20, color=INK):
    box = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    tf = box.text_frame
    tf.word_wrap = True
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        p.space_after = Pt(10)
        p.level = 0
        run = p.add_run()
        run.text = "•  " + item
        _font(run, "Calibri", size, False, color)
    return box


def add_code(slide, l, t, w, h, text, size=15):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(l), Inches(t), Inches(w), Inches(h)
    )
    shape.adjustments[0] = 0.08
    shape.fill.solid()
    shape.fill.fore_color.rgb = CODE_BG
    shape.line.fill.background()
    tf = shape.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.18)
    tf.margin_right = Inches(0.12)
    tf.margin_top = Inches(0.12)
    tf.margin_bottom = Inches(0.1)
    lines = text.strip("\n").split("\n")
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(2)
        run = p.add_run()
        run.text = line if line else " "
        _font(run, "Consolas", size, False, CODE_FG)
    return shape


def add_card(slide, l, t, w, h, title, body, title_size=16, body_size=13):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(l), Inches(t), Inches(w), Inches(h)
    )
    shape.adjustments[0] = 0.08
    shape.fill.solid()
    shape.fill.fore_color.rgb = CARD
    shape.line.color.rgb = LINE
    tf = shape.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.16)
    tf.margin_right = Inches(0.12)
    tf.margin_top = Inches(0.12)
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = title
    _font(run, "Calibri", title_size, True, TEAL_DARK)
    p2 = tf.add_paragraph()
    p2.space_before = Pt(6)
    run2 = p2.add_run()
    run2.text = body
    _font(run2, "Calibri", body_size, False, INK)
    return shape


def add_brand(slide, page, dark=False):
    header = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(W), Inches(HEADER_H))
    _fill(header, WHITE)
    slide.shapes.add_picture(str(LOGO), Inches(0.35), Inches(0.12), height=Inches(0.55))
    add_textbox(
        slide, 10.2, 0.22, 2.8, 0.4,
        "WEEK 2  ·  DAY 1",
        size=12, bold=True, color=CREAM_TEXT if dark else TEAL_DARK, align=PP_ALIGN.RIGHT,
    )
    gold = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0.35), Inches(HEADER_H), Inches(W - 0.7), Inches(0.02)
    )
    _fill(gold, GOLD)

    footer_bg = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0), Inches(H - FOOTER_H), Inches(W), Inches(FOOTER_H)
    )
    _fill(footer_bg, WHITE)
    line = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0.35), Inches(H - FOOTER_H), Inches(W - 0.7), Inches(0.015)
    )
    _fill(line, NAVY)
    add_textbox(
        slide, 0.5, H - FOOTER_H + 0.06, 10.5, 0.3,
        FOOTER, size=11, color=NAVY, align=PP_ALIGN.LEFT,
    )
    add_textbox(
        slide, 11.3, H - FOOTER_H + 0.06, 1.6, 0.3,
        f"{page} / {TOTAL}", size=11, color=MUTED, align=PP_ALIGN.RIGHT,
    )


def add_notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text


def add_kicker_title(slide, kicker, title, title_size=32, top=None):
    top = CONTENT_TOP if top is None else top
    add_textbox(slide, MX, top, 12, 0.32, kicker.upper(), size=13, bold=True, color=TEAL)
    add_textbox(slide, MX, top + 0.28, 12, 0.7, title, size=title_size, bold=True, color=INK)


def new_slide(prs, page, dark=False):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    if dark:
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(W), Inches(H))
        _fill(bg, TITLE_BG)
    else:
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(W), Inches(H))
        _fill(bg, CREAM)
    add_brand(slide, page, dark=dark)
    return slide


def build(dest: Path | None = None) -> Path:
    dest = dest or OUT
    prs = Presentation()
    prs.slide_width = Inches(W)
    prs.slide_height = Inches(H)
    page = 0

    def P():
        nonlocal page
        page += 1
        return page

    # 1 title
    s = new_slide(prs, P(), dark=True)
    add_textbox(s, MX, 2.15, 12, 0.4, "GO PROGRAMMING MASTER COURSE", size=14, bold=True, color=CREAM_TEXT)
    add_textbox(s, MX, 2.55, 12, 1.0, "Week 2, Day 1", size=48, bold=True, color=WHITE)
    add_textbox(
        s, MX, 3.7, 11, 1.1,
        "Variables, types, zero values, operators, and strings — the data you will later put on a student record.",
        size=22, color=RGBColor(0xE7, 0xDD, 0xD0),
    )
    add_textbox(
        s, MX, 5.3, 11, 0.9,
        "Umesh Indrajith · BSc Eng (Hons), University of Moratuwa\nSenior Software Engineer / Lecturer",
        size=16, color=RGBColor(0xD7, 0xCB, 0xB8),
    )
    add_notes(s, "Welcome back. First 10 minutes: leftover installs and homework. Still no SMS code. Still no slices.")

    # 2 recap
    s = new_slide(prs, P())
    add_kicker_title(s, "Since last week", "We start only if the toolchain works")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "go version is 1.25.x. If not, we fix that before anyone types new code.",
        "Homework was why-go.md + version proof in the same GitHub repo as hello.go.",
        "I will ask two people: programming vs software engineering, and why Go for SMS.",
        "Unformatted Go is still returned. gofmt did not expire.",
    ], 20)
    add_notes(s, "Spot-check three repos if time. Cold-call two students on why-go.")

    # 3 outcomes
    s = new_slide(prs, P())
    add_kicker_title(s, "Today", "If Day 1 of week 2 works, you can")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Declare values with var, :=, and const.",
        "Name the zero value of int, string, bool, and a pointer.",
        "Convert types explicitly. Go will not do it for you.",
        "Use fmt and strings; tell bytes from runes.",
        "Run go test on FullName — first test of the course.",
    ], 20)
    add_notes(s, "Lab is a worksheet + a tiny CLI. Modules are one command today, theory in week 4.")

    # 4 types are SE
    s = new_slide(prs, P())
    add_kicker_title(s, "Software engineering", "Types are a design decision", 28)
    add_textbox(
        s, MX, 2.1, 12, 1.3,
        "A type answers: what kind of value is this, and what is allowed? That is how a team agrees before the first line of a handler.",
        size=18, color=MUTED,
    )
    add_bullets(s, MX, 3.5, 12, 3.0, [
        "SMS later: student age is an int, email is a string, enrolled is a bool.",
        "Wrong type compiles only if you force it. That is a gift. Use it.",
        "Names: camelCase inside a package, MixedCaps to export. Comments explain why.",
    ], 18)
    add_notes(s, "Ask: what type is a phone number? String — we do not do arithmetic on it.")

    # 5 var
    s = new_slide(prs, P())
    add_kicker_title(s, "Declaration", "var — say the name, then the type")
    add_code(s, MX, 2.05, 12, 2.35, """var campus string = "Epic Learn"
var seats int
var open bool = true

var (
    first string
    last  string
)""", 16)
    add_bullets(s, MX, 4.55, 12, 2.1, [
        "Works at package level and inside functions.",
        "If you omit the value, you still have a value: the zero value.",
        "var seats int is not “empty”. It is 0.",
    ], 18)
    add_notes(s, "Type this with them. Point at seats.")

    # 6 :=
    s = new_slide(prs, P())
    add_kicker_title(s, "Declaration", ":= — short, only inside a function")
    add_bullets(s, MX, 2.1, 6.6, 4.5, [
        "Declare and assign. Go infers the type from the right-hand side.",
        "Illegal at package level. Illegal if the name already exists on the left alone (reuse needs =).",
        "Inside func, this is the usual form.",
    ], 18)
    add_code(s, 7.5, 2.2, 5.15, 2.8, """func main() {
    name := "Ada"
    year := 1815
    ok := true
    fmt.Println(name, year, ok)
}""", 15)
    add_notes(s, "Common error: := at package level. At least one name on the left must be new.")

    # 7 which one
    s = new_slide(prs, P())
    add_kicker_title(s, "Which one?", "var vs :=")
    cards = [
        ("Use var", "Package level. Or you want the zero value and will assign later. Or you want the type written down because the value is not obvious."),
        ("Use :=", "Inside a function, first time you need the name, the value is right there. This is most of the course."),
        ("Use =", "The name already exists. You are changing it, not inventing it."),
        ("Do not mix for style points", "Pick one per line. gofmt will not save a confusing declaration."),
    ]
    cw2, ch2 = 5.85, 1.95
    for i, (t, b) in enumerate(cards):
        col, row = i % 2, i // 2
        add_card(s, MX + col * (cw2 + 0.2), 2.15 + row * (ch2 + 0.18), cw2, ch2, t, b, 18, 15)
    add_notes(s, "Write the three operators on the board: var  :=  =.")

    # 8 const
    s = new_slide(prs, P())
    add_kicker_title(s, "Constants", "const, and a light look at iota")
    add_code(s, MX, 2.05, 12, 2.55, """const institute = "Epic Learn"
const maxSeats = 30

const (
    statusActive = iota  // 0
    statusIdle           // 1
    statusArchived       // 2
)""", 16)
    add_bullets(s, MX, 4.75, 12, 1.9, [
        "A const is known at compile time. You cannot assign a variable into it.",
        "iota counts up in a const block. Remember the idea; do not build an enum library today.",
    ], 18)
    add_notes(s, "iota is light. Do not teach bit shifts with iota today.")

    # 9 types
    s = new_slide(prs, P())
    add_kicker_title(s, "The types you will actually use", "Start with four, then two aliases")
    feats = [
        ("int", "Whole numbers. Default integer. Size follows the machine (64-bit in this lab)."),
        ("float64", "Decimals. Prefer this over float32 unless a library forces you."),
        ("bool", "true or false. Nothing else."),
        ("string", "Text in double quotes. Immutable. UTF-8 under the hood."),
        ("byte", "Alias for uint8. One byte of data."),
        ("rune", "Alias for int32. One Unicode code point. Written 'අ'."),
    ]
    cw3, ch3 = 3.85, 2.15
    for i, (t, b) in enumerate(feats):
        col, row = i % 3, i // 3
        add_card(s, MX + col * (cw3 + 0.18), 2.05 + row * (ch3 + 0.16), cw3, ch3, t, b, 16, 13)
    add_notes(s, "Skip int8/uint64 tables unless someone asks. Phone is string.")

    # 10 zero values
    s = new_slide(prs, P())
    add_kicker_title(s, "The idea that saves you later", "Zero values — Go never leaves junk", 28)
    add_code(s, MX, 2.05, 12, 2.35, """var n int          // 0
var s string       // ""
var ok bool        // false
var p *int         // nil
var names []string // nil  (week 3 — just notice it)""", 16)
    add_textbox(
        s, MX, 4.6, 12, 1.8,
        "C and some older languages give you garbage. Go gives you a known value. That is why if s == \"\" is a real check, not a crash.",
        size=20, color=MUTED,
    )
    add_notes(s, "This is the week-2 idea they must take home. Pointers and slices are a preview only.")

    # 11 conversion
    s = new_slide(prs, P())
    add_kicker_title(s, "Conversions", "No implicit numeric conversion")
    add_bullets(s, MX, 2.1, 6.4, 4.5, [
        "int and int64 are different types. So are int and float64.",
        "You write the conversion. The compiler will not guess.",
        "Truncation is your problem: int(3.9) is 3.",
    ], 18)
    add_code(s, 7.3, 2.15, 5.35, 3.4, """var year int = 2026
var precise float64 = float64(year)

var score float64 = 3.9
var whole int = int(score) // 3

// year + 0.5           // no
// int64(year) + year   // no""", 14)
    add_notes(s, "Type the failing lines, read the compiler error aloud.")

    # 12 live zeros
    s = new_slide(prs, P())
    add_textbox(s, MX, CONTENT_TOP, 2.2, 0.32, "LIVE DEMO", size=12, bold=True, color=LIVE)
    add_kicker_title(s, "Zero values and conversions", "Type this with me", top=1.22)
    add_code(s, MX, 2.25, 12, 4.25, """package main
import "fmt"
func main() {
    var seats int
    var label string
    var open bool
    fmt.Printf("zeroes: %d %q %t\\n", seats, label, open)
    celsius := 33
    fmt.Println(float64(celsius) * 9 / 5 + 32)
}""", 16)
    add_notes(s, "File: ~/epic-go/week02/zeros.go. Show the failing celsius + 0.5 line.")

    # 13 arithmetic
    s = new_slide(prs, P())
    add_kicker_title(s, "Operators", "Arithmetic and assignment")
    add_code(s, MX, 2.05, 12, 2.15, """a, b := 10, 3
sum := a + b     // 13
mod := a % b     // 1
a += 2           // 12
a++              // 13  (statement, not an expression)""", 16)
    add_bullets(s, MX, 4.4, 12, 2.2, [
        "+ on strings concatenates: \"Ada\" + \" \" + \"Lovelace\".",
        "There is no a++ + b cleverness. ++ is a statement of its own.",
        "Integer division: 10 / 3 is 3. Use a float64 if you want 3.33.",
    ], 18)
    add_notes(s, "Show 10/3 vs float64(10)/3. a++ cannot be used inside fmt.Println.")

    # 14 comparison
    s = new_slide(prs, P())
    add_kicker_title(s, "Operators", "Comparison and logic")
    add_code(s, MX, 2.05, 12, 2.35, """name := "Ada"
fmt.Println(name == "Ada")   // true
fmt.Println(name != "ada")   // true — case matters
enrolled, paid := true, false
fmt.Println(enrolled && paid) // false
fmt.Println(enrolled || paid) // true
fmt.Println(!paid)            // true""", 15)
    add_bullets(s, MX, 4.6, 12, 2.0, [
        "Strings compare lexicographically, byte by byte. Locale sorting is not today.",
        "We will put these inside if next week. Today, print the bool.",
    ], 18)
    add_notes(s, "Do not start if/for. There is no conversion from int to bool.")

    # 15 bitwise
    s = new_slide(prs, P())
    add_kicker_title(s, "Operators · light", "Bitwise — know they exist")
    add_code(s, MX, 2.05, 12, 2.15, """fmt.Println(1<<3)   // 8   shift
fmt.Println(6 & 3)   // 2   and
fmt.Println(6 | 3)   // 7   or
fmt.Println(6 ^ 3)   // 5   xor""", 16)
    add_bullets(s, MX, 4.4, 12, 2.2, [
        "You will not need these for SMS fields.",
        "They show up in flags, permissions, and some interview questions.",
        "If the lab is slow, skip the live typing here. The handout has the table.",
    ], 18)
    add_notes(s, "Pace valve. If conversion + zeros ate time, show the slide and move to fmt.")

    # 16 fmt
    s = new_slide(prs, P())
    add_kicker_title(s, "fmt", "Print so another human can read it")
    add_code(s, MX, 2.05, 12, 1.9, """fmt.Println("plain", 42)
fmt.Printf("name=%s age=%d ok=%t type=%T\\n", "Ada", 36, true, 36)
s := fmt.Sprintf("Hello, %s", "Epic Learn")
fmt.Println(s)""", 15)
    add_bullets(s, MX, 4.15, 12, 2.5, [
        "%s string · %d int · %f float · %t bool · %v default · %T type · %q quoted string.",
        "Println adds spaces and a newline. Printf does not guess — you write the verbs.",
    ], 18)
    add_notes(s, "Have them print %T of an inferred := value.")

    # 17 strings
    s = new_slide(prs, P())
    add_kicker_title(s, "strings", "The package you will import every week")
    add_code(s, MX, 2.05, 12, 2.55, """import "strings"

s := "  Ada Lovelace  "
fmt.Println(strings.TrimSpace(s))
fmt.Println(strings.ToUpper("sms"))
fmt.Println(strings.Contains(s, "Ada"))
fmt.Println(strings.Split("a,b,c", ","))
fmt.Println(strings.Join([]string{"Ada", "Lovelace"}, " "))""", 14)
    add_bullets(s, MX, 4.8, 12, 1.8, [
        "Split/Join use a slice. Copy the line; slices as a topic are week 3.",
        "FullName homework: trim, then join with one space.",
    ], 18)
    add_notes(s, "Do not explain slices. TrimSpace is the teaching point for FullName.")

    # 18 bytes vs runes
    s = new_slide(prs, P())
    add_kicker_title(s, "Bytes and runes", "len counts bytes, not letters")
    add_code(s, MX, 2.05, 12, 2.55, """import "unicode/utf8"

fmt.Println(len("cafe"))                         // 4
fmt.Println(len("café"))                         // 5
fmt.Println(utf8.RuneCountInString("café"))      // 4
fmt.Println(len("සිංහල"))                        // 15
fmt.Println(utf8.RuneCountInString("සිංහල"))     // 5""", 14)
    add_bullets(s, MX, 4.8, 12, 1.8, [
        "A Go string is a read-only slice of bytes, usually UTF-8.",
        "A rune is a Unicode code point. é is one rune and two bytes. සි is ස plus a vowel sign.",
    ], 18)
    add_notes(s, "Students may count six letters; Unicode has five code points. Measure, do not guess.")

    # 19 live utf8
    s = new_slide(prs, P())
    add_textbox(s, MX, CONTENT_TOP, 2.2, 0.32, "LIVE DEMO", size=12, bold=True, color=LIVE)
    add_kicker_title(s, "UTF-8", "Print what len actually measured", top=1.22)
    add_code(s, MX, 2.25, 12, 4.25, """package main
import (
    "fmt"
    "unicode/utf8"
)
func main() {
    word := "සිංහල"
    fmt.Printf("bytes=%d runes=%d %q\\n",
        len(word), utf8.RuneCountInString(word), word)
    for i, r := range word {
        fmt.Printf("%d %c %U\\n", i, r, r)
    }
}""", 14)
    add_notes(s, "range over a string yields runes and byte index. Do not teach indexing word[0] as a letter.")

    # 20 time
    s = new_slide(prs, P())
    add_kicker_title(s, "time", "Dates exist. We need them for SMS later.", 28)
    add_code(s, MX, 2.05, 12, 2.15, """import "time"

now := time.Now()
fmt.Println(now.Format("2006-01-02"))
fmt.Println(now.Weekday())

dob, err := time.Parse("2006-01-02", "2001-05-17")
fmt.Println(dob, err)""", 15)
    add_bullets(s, MX, 4.4, 12, 2.2, [
        "The layout is the reference date Mon Jan 2 15:04:05 MST 2006 — not YYYY-MM-DD.",
        "Write 2006-01-02 when you want year-month-day. Memorise that pattern.",
        "err is a preview. If parse fails it is not nil. We will not master errors today.",
    ], 16)
    add_notes(s, "One format, one parse. Tell the 1 2 3 4 5 6 7 story in one sentence.")

    # 21 naming
    s = new_slide(prs, P())
    add_kicker_title(s, "Clean code this week", "Names and comments")
    names = [
        ("camelCase", "firstName, seatCount. Not first_name in Go identifiers."),
        ("MixedCaps to export", "FullName is visible later from other packages. fullName is not exported."),
        ("Comments say why", "Do not write // increment i. Write why this number is 30, or why we trim spaces."),
        ("gofmt still wins", "Alignment, tabs, spacing — not your taste. The review looks at names and behaviour."),
    ]
    for i, (t, b) in enumerate(names):
        col, row = i % 2, i // 2
        add_card(s, MX + col * (cw2 + 0.2), 2.15 + row * (ch2 + 0.18), cw2, ch2, t, b, 18, 15)
    add_notes(s, "FullName is capitalised so week 1’s export rule reappears.")

    # 22 CLI
    s = new_slide(prs, P())
    add_textbox(s, MX, CONTENT_TOP, 2.2, 0.32, "LIVE DEMO", size=12, bold=True, color=LIVE)
    add_kicker_title(s, "A tiny CLI", "Flags today, HTTP in week 5", top=1.22)
    add_code(s, MX, 2.2, 12, 2.55, """package main
import ("flag"; "fmt")
func main() {
    first := flag.String("first", "", "first name")
    last  := flag.String("last", "", "last name")
    flag.Parse()
    fmt.Println(*first, *last)
}""", 15)
    add_textbox(
        s, MX, 4.9, 12, 1.6,
        "go run greet.go -first Ada -last Lovelace — then put FullName in the middle. Pointers: flag.String returns *string. Write the * to read it. Theory is week 8.",
        size=18, color=MUTED,
    )
    add_notes(s, "File: ~/epic-go/week02/greet.go. Do not explain pointers.")

    # 23 go test
    s = new_slide(prs, P())
    add_textbox(s, MX, CONTENT_TOP, 2.2, 0.32, "LIVE DEMO", size=12, bold=True, color=LIVE)
    add_kicker_title(s, "First test of the course", "go test on a pure function", 28, top=1.22)
    add_code(s, MX, 2.2, 12, 2.7, """// names.go          package names
func FullName(first, last string) string {
    return first + " " + last
}

// names_test.go     package names
func TestFullName(t *testing.T) {
    got := FullName("Ada", "Lovelace")
    if got != "Ada Lovelace" { t.Fatalf("got %q", got) }
}""", 14)
    add_bullets(s, MX, 5.05, 12, 1.5, [
        "One new command so the test can run: go mod init epiclearn/week02. Meaning: week 4.",
        "Then: go test. Green is the gate. Improve FullName with TrimSpace for homework.",
    ], 16)
    add_notes(s, "Fail the test first (return first only), then fix. Red → green.")

    # 24 lab
    s = new_slide(prs, P())
    add_kicker_title(s, "Lab · rest of class", "Done when all of this is true")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Worksheet: every zero-value and conversion cell filled",
        "zeros.go prints zeros and a correct Celsius → Fahrenheit",
        "greet.go -first … -last … prints a single full name",
        "go test in the names folder is green for FullName(\"Ada\",\"Lovelace\")",
        "Commit and push to GitHub. Show me the URL before you leave",
    ], 20)
    add_notes(s, "Homework is on the student handout — not a slide.")

    # 25 next
    s = new_slide(prs, P())
    add_kicker_title(s, "Next session", "Week 3 — control flow, slices, maps")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "if, switch, for, range.",
        "Arrays vs slices; append and the backing-array gotcha.",
        "Maps and the comma-ok check.",
        "Bring a green go test and the ten exercises.",
    ], 22)
    add_notes(s, "Do not start slices today even if the lab finishes early.")

    # 26 questions
    s = new_slide(prs, P(), dark=True)
    add_textbox(s, 0.5, 2.9, 12.3, 1.6, "Questions", size=72, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    add_notes(s, "Take questions. Then start the worksheet. End by collecting GitHub URLs.")

    if page != TOTAL:
        raise SystemExit(f"expected {TOTAL} slides, built {page}")

    dest.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(dest))
    print(f"PPTX {dest} ({dest.stat().st_size // 1024} KB, {page} editable slides)")
    return dest


if __name__ == "__main__":
    build()
