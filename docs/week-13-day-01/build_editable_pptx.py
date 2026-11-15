#!/usr/bin/env python3
"""Build an editable PowerPoint of the Week 13 Day 1 deck (native text, not screenshots)."""

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
OUT = ROOT / "pdf" / "week-13-day-01-slides.pptx"
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
        "WEEK 13  ·  DAY 1",
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
    dest.parent.mkdir(parents=True, exist_ok=True)
    prs = Presentation()
    prs.slide_width = Inches(W)
    prs.slide_height = Inches(H)
    page = 0
    def P():
        nonlocal page
        page += 1
        return page

    s = new_slide(prs, P(), dark=True)
    add_textbox(s, MX, 2.15, 12, 0.4, "GO PROGRAMMING MASTER COURSE", size=14, bold=True, color=CREAM_TEXT)
    add_textbox(s, MX, 2.55, 12, 1.0, "Week 13, Day 1", size=48, bold=True, color=WHITE)
    add_textbox(s, MX, 3.7, 11, 1.1, "Testing and code quality — table-driven tests, httptest, fakes, vet, coverage, CI.", size=20, color=RGBColor(0xE7, 0xDD, 0xD0))
    add_textbox(s, MX, 5.3, 11, 0.9, "Umesh Indrajith · BSc Eng (Hons), University of Moratuwa\nSenior Software Engineer / Lecturer", size=16, color=RGBColor(0xD7, 0xCB, 0xB8))
    add_notes(s, "Deep testing week.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Since last week", "Green -race. Now prove behavior with tests.", 24)
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Mutex + context signatures in place.",
        "Known gap: almost no *_test.go next to SMS packages.",
        "Today: table-driven, httptest, interface + fake, vet, cover, CI.",
    ], 18)
    add_notes(s, "Confirm -race briefly.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Today", "If Day 1 of week 13 works, you can")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Write table-driven tests with t.Run.",
        "Hit Gin with httptest (health + one student handler).",
        "Swap the repo for an in-memory fake via an interface.",
        "Run go vet and go test -cover; ship GitHub Actions CI.",
    ], 17)
    add_notes(s, "Homework: ≥5 tests + CI.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Software engineering", "Tests are how the next you trusts this code", 22)
    add_textbox(s, MX, 2.1, 12, 1.0, "Interfaces exist so you can fake dependencies. CI exists so red never merges quietly.", size=17, color=MUTED)
    add_bullets(s, MX, 3.3, 12, 3.2, [
        "SMS: FullName, validation/date parse, GET /health.",
        "Homework: CI workflow + at least 5 tests.",
    ], 18)
    add_notes(s, "Why interfaces — say it.")

    s = new_slide(prs, P())
    add_kicker_title(s, "testing", "testing · t.Run · table-driven")
    add_code(s, MX, 2.05, 12, 3.6, """cases := []struct{ name, in, want string }{...}
for _, tc := range cases {
    t.Run(tc.name, func(t *testing.T) {
        if got := f(tc.in); got != tc.want {
            t.Fatalf("got %q want %q", got, tc.want)
        }
    })
}""", 13)
    add_notes(s, "Name every case.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Lab seed", "Parse YYYY-MM-DD — layout is 2006-01-02", 24)
    add_code(s, MX, 2.05, 12, 1.8, """t, err := time.Parse("2006-01-02", s)
// NOT "YYYY-MM-DD" as the layout string""", 15)
    add_bullets(s, MX, 4.1, 12, 2.6, [
        "Matches CreateStudent date-of-birth parsing.",
        "Table: valid, invalid month, empty, wrong shape.",
    ], 18)
    add_notes(s, "Classic footgun.")

    s = new_slide(prs, P())
    add_kicker_title(s, "FullName", "Pure function — easiest win")
    add_code(s, MX, 2.05, 12, 1.4, """func FullNameOf(first, last string) string { /* trim + join */ }""", 15)
    add_bullets(s, MX, 3.7, 12, 3.0, [
        "Revisit week 2/6 rules: trim; empty last → first only.",
        "Table-driven tests live next to the package.",
    ], 18)
    add_notes(s, "Warm-up.")

    s = new_slide(prs, P())
    add_kicker_title(s, "httptest", "Call Gin without starting a real port")
    add_code(s, MX, 2.05, 12, 3.0, """r := gin.New()
r.GET("/health", health.Get)
w := httptest.NewRecorder()
req := httptest.NewRequest(http.MethodGet, "/health", nil)
r.ServeHTTP(w, req)""", 14)
    add_notes(s, "No Listen.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Interfaces + fakes", "This is why interfaces exist", 26)
    add_code(s, MX, 2.05, 12, 2.8, """type StudentStore interface {
    Create(ctx context.Context, in CreateStudentRequest) Student
    GetByID(ctx context.Context, id int) (Student, error)
}
// production: *StudentRepository  ·  tests: *FakeStudentStore""", 13)
    add_notes(s, "Draw Handler → interface.")

    s = new_slide(prs, P())
    add_kicker_title(s, "go vet · cover", "Quality commands next to test")
    add_code(s, MX, 2.05, 12, 2.4, """go vet ./...
go test ./... -cover
gofmt -l .""", 16)
    add_notes(s, "Show cover once.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Delve", "Breakpoint in a handler (once)")
    add_code(s, MX, 2.05, 12, 2.2, """dlv test ./internal/handlers
# break handlers.(*StudentHandler).Create""", 15)
    add_notes(s, "Optional.")

    s = new_slide(prs, P())
    add_kicker_title(s, "CI", "GitHub Actions — gofmt · vet · test")
    add_code(s, MX, 2.05, 12, 2.4, """# .github/workflows/ci.yml
# setup-go → gofmt -l → go vet → go test ./...""", 15)
    add_notes(s, "Starter ships workflow.")

    s = new_slide(prs, P())
    add_kicker_title(s, "SMS milestone", "Fill the test gap")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "FullName tests",
        "Date / validation table tests",
        "GET /health via httptest",
        "One student handler with a fake store",
        "CI workflow committed",
    ], 18)
    add_notes(s, "Five tests minimum.")

    s = new_slide(prs, P())
    add_textbox(s, MX, CONTENT_TOP, 3, 0.35, "LIVE DEMO", size=12, bold=True, color=LIVE)
    add_kicker_title(s, "Table-driven", "Parse date cases go red → green", top=CONTENT_TOP+0.28)
    add_code(s, MX, 2.2, 12, 1.8, """cd starter/date-lab
go test -v ./parse/""", 16)
    add_notes(s, "date-lab.")

    s = new_slide(prs, P())
    add_textbox(s, MX, CONTENT_TOP, 3, 0.35, "LIVE DEMO", size=12, bold=True, color=LIVE)
    add_kicker_title(s, "httptest", "Health returns 200 + JSON", top=CONTENT_TOP+0.28)
    add_code(s, MX, 2.2, 12, 1.6, """go test ./internal/handlers/ -v -run Health""", 15)
    add_notes(s, "Show Code and Body.")

    s = new_slide(prs, P())
    add_textbox(s, MX, CONTENT_TOP, 3, 0.35, "LIVE DEMO", size=12, bold=True, color=LIVE)
    add_kicker_title(s, "Fake + Create", "Handler test with FakeStudentStore", top=CONTENT_TOP+0.28)
    add_code(s, MX, 2.2, 12, 1.6, """go test ./internal/handlers/ -v -run Create""", 15)
    add_notes(s, "Point at interface.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Pitfalls", "Common week-13 bugs")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Layout YYYY-MM-DD instead of 2006-01-02.",
        "httptest 404 — route not registered.",
        "No interface → can’t fake.",
        "CI without gofmt -l.",
        "One giant test — use t.Run.",
    ], 18)
    add_notes(s, "Quiz.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Lab · rest of class", "Done when all of this is true")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Date-lab table tests green",
        "FullName + health httptest green",
        "At least one handler test with a fake store",
        "go vet ./... clean; CI workflow file present",
    ], 17)
    add_notes(s, "Gate.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Homework", "CI + at least 5 tests")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "GitHub Actions: gofmt, vet, go test ./....",
        "≥5 tests; PR notes on what you covered.",
    ], 18)
    add_notes(s, "Quality notes required.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Next session", "Week 14 — PostgreSQL", 26)
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Replace in-memory store with Postgres + migrations.",
        "Parameterized queries; SQL injection demo.",
        "Bring green tests — they’ll catch schema mistakes.",
    ], 18)
    add_notes(s, "Teaser.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Words to keep", "Say these correctly next week")
    add_card(s, MX, 2.1, 5.9, 1.8, "Table-driven", "Cases + t.Run; one assertion shape.")
    add_card(s, 7.0, 2.1, 5.7, 1.8, "httptest", "In-process HTTP without Listen.")
    add_card(s, MX, 4.1, 5.9, 1.8, "Fake", "Test double behind an interface.")
    add_card(s, 7.0, 4.1, 5.7, 1.8, "CI", "gofmt · vet · test on every PR.")
    add_notes(s, "Oral quiz.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Layout reminder", "Where lab code lives")
    add_code(s, MX, 2.05, 12, 3.2, """docs/week-13-day-01/starter/
  date-lab/
  backend/
    internal/models/  internal/repository/
    internal/handlers/*_test.go
    .github/workflows/ci.yml""", 13)
    add_notes(s, "Date-lab first.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Honest limits", "What this week is not")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Not Postgres (week 14).",
        "Not 100% coverage theater.",
        "Not mock frameworks — hand-written fakes only.",
        "Not mastering Delve — one breakpoint is enough.",
    ], 18)
    add_notes(s, "Honest.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Safety", "Still true")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "No secrets in fixtures — use example.com.",
        "gofmt; no binaries / cover.out in git unless ignored.",
        "CI on PRs, not only on your laptop.",
    ], 18)
    add_notes(s, "Quick.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Review bar", "Instructor merges when")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "≥5 meaningful tests green",
        "CI workflow present and green (or clear local evidence)",
        "Interface + fake used for at least one handler test",
        "gofmt / vet clean",
    ], 17)
    add_notes(s, "Collect PRs.")

    s = new_slide(prs, P(), dark=True)
    add_textbox(s, MX, 3.0, 12, 1.2, "Questions", size=64, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    add_notes(s, "Then date-lab → httptest → CI.")

    if page != TOTAL:
        raise SystemExit(f"expected {TOTAL} slides, built {page}")
    prs.save(str(dest))
    print("Wrote", dest)
    return dest

if __name__ == "__main__":
    build()
