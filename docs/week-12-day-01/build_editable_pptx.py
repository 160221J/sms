#!/usr/bin/env python3
"""Build an editable PowerPoint of the Week 12 Day 1 deck (native text, not screenshots)."""

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
OUT = ROOT / "pdf" / "week-12-day-01-slides.pptx"
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
        "WEEK 12  ·  DAY 1",
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
    add_textbox(s, MX, 2.55, 12, 1.0, "Week 12, Day 1", size=48, bold=True, color=WHITE)
    add_textbox(s, MX, 3.7, 11, 1.1, "Mutex, WaitGroup, context, and races — make shared memory and cancellation safe.", size=22, color=RGBColor(0xE7, 0xDD, 0xD0))
    add_textbox(s, MX, 5.3, 11, 0.9, "Umesh Indrajith · BSc Eng (Hons), University of Moratuwa\nSenior Software Engineer / Lecturer", size=16, color=RGBColor(0xD7, 0xCB, 0xB8))
    add_notes(s, "Week 11 pool. Today: lock, context, -race green, shutdown sketch.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Since last week", "You have a pool. Now protect shared state.", 26)
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Worker pool + WaitGroup join — keep that.",
        "Week 10 previewed go test -race; today we finish red → green.",
        "Create still sync. Import still uses a pool. Map must stay locked.",
    ], 18)
    add_notes(s, "Confirm pool mental model.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Today", "If Day 1 of week 12 works, you can")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Protect shared data with sync.Mutex (and name RWMutex).",
        "Use WaitGroup as a join (not a lock).",
        "Pass c.Request.Context() into repository signatures.",
        "Demo a timeout with context.WithTimeout.",
        "Sketch graceful shutdown; get go test -race green.",
    ], 17)
    add_notes(s, "Gate: race red → mutex → green.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Software engineering", "Shared memory needs a rule", 26)
    add_textbox(s, MX, 2.1, 12, 1.0, "Channels coordinate work. Mutexes protect data. Context cancels work.", size=18, color=MUTED)
    add_bullets(s, MX, 3.3, 12, 3.2, [
        "SMS: lock the map; add context.Context to repo methods.",
        "Homework: README test command includes -race.",
    ], 18)
    add_notes(s, "Three tools: channel / mutex / context.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Data race", "Two goroutines · one variable · no sync")
    add_code(s, MX, 2.05, 12, 2.0, """var n int
go func() { n++ }()
go func() { n++ }()""", 16)
    add_bullets(s, MX, 4.3, 12, 2.4, [
        "May “work” until it doesn’t — undefined behavior.",
        "go test -race makes it visible (needs cgo + gcc).",
    ], 18)
    add_notes(s, "Show unsafe counter.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Mutex", "One writer (or reader) at a time")
    add_code(s, MX, 2.05, 12, 2.2, """var mu sync.Mutex
mu.Lock()
n++
mu.Unlock()
// prefer: defer mu.Unlock() right after Lock""", 15)
    add_bullets(s, MX, 4.5, 12, 2.2, [
        "Hold locks short. Don’t call slow I/O under lock.",
        "Same mutex for the same data — document ownership.",
    ], 18)
    add_notes(s, "Live fix UnsafeAdd → SafeAdd.")

    s = new_slide(prs, P())
    add_kicker_title(s, "RWMutex", "Many readers · one writer")
    add_code(s, MX, 2.05, 12, 2.0, """var mu sync.RWMutex
mu.RLock(); defer mu.RUnlock()  // readers
mu.Lock();  defer mu.Unlock()   // writers""", 15)
    add_bullets(s, MX, 4.3, 12, 2.4, [
        "Use when reads dominate and critical sections are tiny.",
        "SMS starter: Mutex is enough; name RWMutex so the word sticks.",
    ], 18)
    add_notes(s, "Optional depth.")

    s = new_slide(prs, P())
    add_kicker_title(s, "WaitGroup", "Join, not lock")
    add_code(s, MX, 2.05, 12, 2.2, """var wg sync.WaitGroup
wg.Add(N)
go func() { defer wg.Done(); work() }()
wg.Wait() // all Done""", 15)
    add_bullets(s, MX, 4.5, 12, 2.2, [
        "Does not protect n++ — still need a mutex (or channels).",
        "Week 11: WaitGroup before closing results.",
    ], 18)
    add_notes(s, "Quiz: WaitGroup vs Mutex.")

    s = new_slide(prs, P())
    add_kicker_title(s, "context", "Cancel · deadline · timeout")
    add_code(s, MX, 2.05, 12, 2.8, """ctx, cancel := context.WithTimeout(parent, 2*time.Second)
defer cancel()
select {
case <-ctx.Done():
    return ctx.Err()
case result := <-work:
    return result, nil
}""", 14)
    add_notes(s, "One timeout demo.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Gin", "c.Request.Context() on every handler", 26)
    add_code(s, MX, 2.05, 12, 2.4, """func (h *StudentHandler) GetByID(c *gin.Context) {
    ctx := c.Request.Context()
    s, err := h.repo.GetByID(ctx, id)
}""", 15)
    add_bullets(s, MX, 4.7, 12, 2.0, [
        "Client disconnect / shutdown cancels that context.",
        "Repo may ignore ctx until Postgres — signature changes now.",
    ], 17)
    add_notes(s, "Spiral: signature first.")

    s = new_slide(prs, P())
    add_kicker_title(s, "SMS milestone", "Lock the map · pass context")
    add_code(s, MX, 2.05, 12, 2.6, """func (r *StudentRepository) Create(ctx context.Context, in ...) Student {
    _ = ctx // ignored until DB
    r.mu.Lock()
    defer r.mu.Unlock()
    ...
}""", 14)
    add_notes(s, "ctx signatures are the week-12 diff.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Graceful shutdown", "Sketch — don’t leave listeners hanging", 24)
    add_code(s, MX, 2.05, 12, 3.0, """ctx, stop := signal.NotifyContext(context.Background(), os.Interrupt, syscall.SIGTERM)
defer stop()
srv := &http.Server{Addr: addr, Handler: r}
go srv.ListenAndServe()
<-ctx.Done()
srv.Shutdown(context.WithTimeout(...))""", 13)
    add_notes(s, "Walk starter main.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Lab", "Race detector: red → mutex → green")
    add_code(s, MX, 2.05, 12, 2.4, """cd starter/race-lab
go test -race ./counter/     # FAIL: data race
# fix with Mutex
go test -race ./...          # PASS""", 15)
    add_bullets(s, MX, 4.7, 12, 2.0, [
        "Needs CGO_ENABLED=1 and a C compiler (build-essential).",
    ], 18)
    add_notes(s, "Core lab.")

    s = new_slide(prs, P())
    add_textbox(s, MX, CONTENT_TOP, 3, 0.35, "LIVE DEMO", size=12, bold=True, color=LIVE)
    add_kicker_title(s, "-race", "Show the FAIL, then the fix", top=CONTENT_TOP+0.28)
    add_code(s, MX, 2.2, 12, 2.4, """go test -race -run TestUnsafeAddDocumentsRace ./counter/
# DATA RACE
go test -race ./counter/   # SafeAdd ok""", 14)
    add_notes(s, "Projector must show race once.")

    s = new_slide(prs, P())
    add_textbox(s, MX, CONTENT_TOP, 3, 0.35, "LIVE DEMO", size=12, bold=True, color=LIVE)
    add_kicker_title(s, "Context timeout", "Demo endpoint respects deadline", top=CONTENT_TOP+0.28)
    add_code(s, MX, 2.2, 12, 2.0, """GET /api/demo/slow?ms=3000
# with 1s server timeout → canceled""", 16)
    add_notes(s, "curl under and over timeout.")

    s = new_slide(prs, P())
    add_textbox(s, MX, CONTENT_TOP, 3, 0.35, "LIVE DEMO", size=12, bold=True, color=LIVE)
    add_kicker_title(s, "Shutdown", "Ctrl+C drains, then exits", top=CONTENT_TOP+0.28)
    add_code(s, MX, 2.2, 12, 1.8, """go run ./cmd/server
# Ctrl+C → shutting down → bye""", 16)
    add_notes(s, "Optional.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Pitfalls", "Common week-12 bugs")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "WaitGroup without mutex → still races.",
        "Forget Unlock → deadlock.",
        "Create context without defer cancel().",
        "Ignore ctx.Done() in long loops.",
        "-race fails: no gcc / CGO disabled.",
    ], 18)
    add_notes(s, "Quiz aloud.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Lab · rest of class", "Done when all of this is true")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "go test -race ./... green on race-lab",
        "Can explain Mutex vs WaitGroup vs channel",
        "Repo methods take context.Context; handlers pass request context",
        "Timeout demo works (or sketched)",
        "Optional: graceful shutdown in main",
    ], 17)
    add_notes(s, "Gate on board.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Homework", "PR with -race in the README")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Test command documents go test -race ./....",
        "Mutex on shared maps; context on repo signatures.",
        "PR notes: what was red, what made it green.",
    ], 18)
    add_notes(s, "Screenshot optional.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Next session", "Week 13 — testing and code quality", 24)
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Table-driven tests, httptest, fakes.",
        "CI: gofmt, vet, test.",
        "Bring a green -race habit.",
    ], 20)
    add_notes(s, "Teaser.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Words to keep", "Say these correctly next week")
    add_card(s, MX, 2.1, 5.9, 1.8, "Mutex", "Exclusive access to shared memory.")
    add_card(s, 7.0, 2.1, 5.7, 1.8, "WaitGroup", "Join N goroutines; not a lock.")
    add_card(s, MX, 4.1, 5.9, 1.8, "context", "Cancel / deadline flowing down the stack.")
    add_card(s, 7.0, 4.1, 5.7, 1.8, "-race", "Detector for concurrent unsynchronized access.")
    add_notes(s, "Oral quiz.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Layout reminder", "Where lab code lives")
    add_code(s, MX, 2.05, 12, 3.2, """docs/week-12-day-01/starter/
  race-lab/                 # red → mutex → green
  backend/
    internal/repository/    # Mutex + context.Context params
    cmd/server/main.go      # graceful shutdown sketch
    internal/handlers/      # c.Request.Context() + timeout demo""", 13)
    add_notes(s, "Race lab first.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Honest limits", "What this week is not")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Not Postgres / real query cancel (week 14).",
        "Not deep testing / CI (week 13).",
        "Not “channels instead of every mutex.”",
        "Not production-hardening every edge case.",
    ], 18)
    add_notes(s, "Keep spiral honest.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Safety", "Still true")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Cap demo timeouts; don’t sleep forever in handlers.",
        "No secrets in fixtures.",
        "gofmt; no binaries in git.",
    ], 20)
    add_notes(s, "Quick.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Review bar", "Instructor merges when")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "go test -race ./... documented and green (or lab evidence)",
        "Shared maps locked",
        "Repo signatures take context; handlers pass request context",
        "Create/list/import still behave",
    ], 18)
    add_notes(s, "Collect PRs.")

    s = new_slide(prs, P(), dark=True)
    add_textbox(s, MX, 3.0, 12, 1.2, "Questions", size=64, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    add_notes(s, "Then race lab: red → green.")

    if page != TOTAL:
        raise SystemExit(f"expected {TOTAL} slides, built {page}")
    prs.save(str(dest))
    print("Wrote", dest)
    return dest

if __name__ == "__main__":
    build()
