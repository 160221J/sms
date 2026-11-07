#!/usr/bin/env python3
"""Build an editable PowerPoint of the Week 11 Day 1 deck (native text, not screenshots)."""

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
OUT = ROOT / "pdf" / "week-11-day-01-slides.pptx"
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
        "WEEK 11  ·  DAY 1",
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
    add_textbox(s, MX, 2.55, 12, 1.0, "Week 11, Day 1", size=48, bold=True, color=WHITE)
    add_textbox(s, MX, 3.7, 11, 1.1, "Channels, pipelines, and the worker pool — the concurrency pattern to keep.", size=22, color=RGBColor(0xE7, 0xDD, 0xD0))
    add_textbox(s, MX, 5.3, 11, 0.9, "Umesh Indrajith · BSc Eng (Hons), University of Moratuwa\nSenior Software Engineer / Lecturer", size=16, color=RGBColor(0xD7, 0xCB, 0xB8))
    add_notes(s, "Week 10: races seen. Today: channels + worker pool. Import stretch.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Since last week", "You can start Gs. Now make them talk safely.", 26)
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "go test -race literacy; Create still sync.",
        "Cold-call: what is a channel?",
        "Today: send/receive, close, range, select, pipeline, worker pool.",
        "Mutex deep-dive still week 12 — pool uses WaitGroup as glue.",
    ], 18)
    add_notes(s, "Confirm no naked go in Create.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Today", "If Day 1 of week 11 works, you can")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Choose unbuffered vs buffered channels and say why.",
        "Close a channel and range until drained.",
        "Use select for multi-way wait (one live example).",
        "Sketch a pipeline (stage → stage).",
        "Implement a worker pool of N workers over a job channel.",
    ], 18)
    add_notes(s, "Import stretch if pool is solid.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Software engineering", "One pattern to remember: worker pool", 26)
    add_textbox(s, MX, 2.1, 12, 1.0, "Bound concurrency. N workers pull jobs. Results come back on another channel. No unbounded go per item.", size=18, color=MUTED)
    add_bullets(s, MX, 3.3, 12, 3.2, [
        "SMS stretch: POST /api/students/import → {created, failed}.",
        "If struggling: hash-list kata only; sketch import on the board.",
    ], 18)
    add_notes(s, "Leave worker pool on the board.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Channels", "Typed pipes between goroutines")
    add_code(s, MX, 2.05, 12, 2.4, """ch := make(chan int)      // unbuffered
ch := make(chan int, 8)   // buffered
ch <- 1
v := <-ch""", 16)
    add_bullets(s, MX, 4.7, 12, 2.0, [
        "Unbuffered: send waits for receive (handshake).",
        "Buffered: send waits only when full.",
    ], 18)
    add_notes(s, "Live tiny send/receive.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Directional", "Make intent obvious at the boundary")
    add_code(s, MX, 2.05, 12, 1.8, """func produce(out chan<- int) { out <- 42 }
func consume(in <-chan int) { fmt.Println(<-in) }""", 16)
    add_bullets(s, MX, 4.1, 12, 2.6, [
        "chan<- send-only · <-chan receive-only.",
        "Compiler stops accidental reverse use.",
    ], 18)
    add_notes(s, "Optional depth.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Close + range", "Sender closes · receivers drain")
    add_code(s, MX, 2.05, 12, 2.4, """close(ch)
for v := range ch { /* until closed and empty */ }
v, ok := <-ch // ok==false when closed and drained""", 15)
    add_bullets(s, MX, 4.7, 12, 2.0, [
        "Only the sender should close.",
        "Never send on a closed channel — panic.",
    ], 18)
    add_notes(s, "Common bug: close from multiple workers.")

    s = new_slide(prs, P())
    add_kicker_title(s, "select", "Wait on several channel ops")
    add_code(s, MX, 2.05, 12, 2.8, """select {
case v := <-a:
    fmt.Println("a", v)
case b <- 1:
    fmt.Println("sent b")
case <-time.After(time.Second):
    fmt.Println("timeout")
}""", 14)
    add_notes(s, "One timeout example.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Pipeline", "Stage → stage → stage")
    add_code(s, MX, 2.05, 12, 1.8, """nums := gen(1,2,3)
sq := square(nums)
for v := range sq { fmt.Println(v) }""", 16)
    add_bullets(s, MX, 4.1, 12, 2.6, [
        "Each stage: goroutine(s) + channel(s).",
        "Worker pool is a special pipeline: many workers, one job queue.",
    ], 18)
    add_notes(s, "Sketch boxes.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Worker pool", "The pattern to keep forever")
    add_code(s, MX, 2.05, 12, 2.4, """jobs := make(chan Job)
results := make(chan Result)
for w := 0; w < N; w++ { go worker(jobs, results) }
// send jobs, close(jobs), collect results""", 15)
    add_bullets(s, MX, 4.7, 12, 2.0, [
        "Fixed N — no go per student/row.",
        "WaitGroup: wait until workers exit after jobs closed.",
    ], 18)
    add_notes(s, "Core slide.")

    s = new_slide(prs, P())
    add_kicker_title(s, "WaitGroup · preview", "Glue for when are workers done?", 26)
    add_code(s, MX, 2.05, 12, 2.6, """var wg sync.WaitGroup
wg.Add(N)
for i := 0; i < N; i++ {
    go func() { defer wg.Done(); worker(...) }()
}
wg.Wait()
close(results)""", 14)
    add_notes(s, "Deep mutex week 12.")

    s = new_slide(prs, P())
    add_kicker_title(s, "SMS stretch", "POST /api/students/import")
    add_code(s, MX, 2.05, 12, 2.4, """// body: [ {first_name, email, course, ...}, ... ]
// pool of N workers validate + insert
// response: { "created": 3, "failed": 1 }""", 15)
    add_bullets(s, MX, 4.7, 12, 2.0, [
        "Still in-memory. Struggling room: kata only.",
    ], 18)
    add_notes(s, "Homework: import OR kata.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Kata options", "If import is too much today")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Hash list: workers compute SHA-256; collect digests.",
        "Resizer sketch: mock image jobs; count OK/fail.",
        "Same pool shape as import — swap the job type.",
    ], 20)
    add_notes(s, "Starter ships hash-list pool.")

    s = new_slide(prs, P())
    add_textbox(s, MX, CONTENT_TOP, 3, 0.35, "LIVE DEMO", size=12, bold=True, color=LIVE)
    add_kicker_title(s, "Channel basics", "Send, receive, close, range", top=CONTENT_TOP+0.28)
    add_code(s, MX, 2.2, 12, 2.8, """ch := make(chan string, 2)
ch <- "a"; ch <- "b"; close(ch)
for s := range ch { fmt.Println(s) }""", 16)
    add_notes(s, "Two minutes.")

    s = new_slide(prs, P())
    add_textbox(s, MX, CONTENT_TOP, 3, 0.35, "LIVE DEMO", size=12, bold=True, color=LIVE)
    add_kicker_title(s, "Worker pool", "N workers · job channel · results", top=CONTENT_TOP+0.28)
    add_code(s, MX, 2.2, 12, 2.0, """cd starter/worker-lab
go test ./pool/
go run . -n 4""", 16)
    add_notes(s, "Walk starter pool.")

    s = new_slide(prs, P())
    add_textbox(s, MX, CONTENT_TOP, 3, 0.35, "LIVE DEMO · STRETCH", size=12, bold=True, color=LIVE)
    add_kicker_title(s, "Import", "Wire pool behind Gin", top=CONTENT_TOP+0.28)
    add_code(s, MX, 2.2, 12, 2.0, """r.POST("/api/students/import", students.Import)
// bind []CreateStudentRequest → {created, failed}""", 15)
    add_notes(s, "Skip if kata needs the hour.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Pitfalls", "Channel bugs that panic or hang")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Send on closed channel → panic.",
        "Forget to close → range hangs forever.",
        "Close from multiple goroutines → panic.",
        "Unbounded go per job → you are not using a pool.",
    ], 20)
    add_notes(s, "Quiz aloud.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Lab · rest of class", "Done when all of this is true")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Can explain unbuffered vs buffered",
        "Worker pool kata runs (hash list or equivalent)",
        "WaitGroup used to join workers before closing results",
        "No naked go per job in the solution",
        "Optional: import endpoint sketched or started",
    ], 18)
    add_notes(s, "Gate on board.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Homework", "Import or documented kata")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "A: POST /api/students/import with pool → {created, failed}.",
        "B: Documented worker pool under internal/workers/.",
        "PR explains N workers and who closes which channel.",
    ], 18)
    add_notes(s, "Either path is fine.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Next session", "Week 12 — mutex, WaitGroup, context, races", 24)
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Fix the week-10 race for real.",
        "Request-scoped context on handlers.",
        "Bring a working pool mental model.",
    ], 20)
    add_notes(s, "Teaser.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Words to keep", "Say these correctly next week")
    add_card(s, MX, 2.1, 5.9, 1.8, "Channel", "Typed pipe; send/receive synchronization.")
    add_card(s, 7.0, 2.1, 5.7, 1.8, "select", "Wait on multiple channel cases.")
    add_card(s, MX, 4.1, 5.9, 1.8, "Pipeline", "Stages connected by channels.")
    add_card(s, 7.0, 4.1, 5.7, 1.8, "Worker pool", "Fixed N workers pulling from a job queue.")
    add_notes(s, "Oral quiz.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Layout reminder", "Where lab code lives")
    add_code(s, MX, 2.05, 12, 3.2, """docs/week-11-day-01/starter/
  worker-lab/                 # hash-list worker pool kata
  backend/
    internal/workers/         # homework option B
    internal/handlers/        # Import stretch""", 14)
    add_notes(s, "Kata first.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Honest limits", "What this week is not")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Not mutex / race fix (week 12).",
        "Not Postgres bulk insert.",
        "Not unbounded fan-out disguised as a pool.",
        "Not every handler needs channels.",
    ], 18)
    add_notes(s, "Keep spiral honest.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Safety", "Still true")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Cap N and job list size in demos.",
        "No secrets in import fixtures — use example.com.",
        "gofmt; no binaries in git.",
    ], 20)
    add_notes(s, "Quick.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Review bar", "Instructor merges when")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Pool uses fixed N + job channel (not go-per-item)",
        "Channels closed by the right owner",
        "PR explains created/failed or kata results",
        "Create/list still sync and green",
    ], 18)
    add_notes(s, "Collect PRs.")

    s = new_slide(prs, P(), dark=True)
    add_textbox(s, MX, 3.0, 12, 1.2, "Questions", size=64, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    add_notes(s, "Then channel basics → worker pool lab.")

    if page != TOTAL:
        raise SystemExit(f"expected {TOTAL} slides, built {page}")
    prs.save(str(dest))
    print("Wrote", dest)
    return dest

if __name__ == "__main__":
    build()
