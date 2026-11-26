#!/usr/bin/env python3
"""Build an editable PowerPoint of the Week 16 Day 1 deck (native text, not screenshots)."""

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
OUT = ROOT / "pdf" / "week-16-day-01-slides.pptx"
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
        "WEEK 16  ·  DAY 1",
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
    add_textbox(s, MX, 2.55, 12, 1.0, "Week 16, Day 1", size=48, bold=True, color=WHITE)
    add_textbox(s, MX, 3.7, 11, 1.2, "Review, Go design, refactor, demo — polish, walk through, ship.", size=20, color=RGBColor(0xE7, 0xDD, 0xD0))
    add_textbox(s, MX, 5.3, 11, 0.9, "Umesh Indrajith · BSc Eng (Hons), University of Moratuwa\nSenior Software Engineer / Lecturer", size=16, color=RGBColor(0xD7, 0xCB, 0xB8))
    add_notes(s, "Final week. Rubric → refactor → design → demos.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Since last week", "Auth works. Today we ship the portfolio version.", 22)
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "JWT, Bearer, CORS, React login — done in week 15.",
        "Today: code review, errors/logs pass, Go design, optional Compose.",
        "Capstone: demo + merge main + retrospective.",
    ], 18)

    s = new_slide(prs, P())
    add_kicker_title(s, "Today", "If Day 1 of week 16 works, you can")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Apply the course review rubric to your own PR.",
        "Do an errors + logging + consistent JSON-error pass.",
        "Name Go design choices (small interfaces, packages).",
        "Give an 8–10 minute demo; leave a portfolio README.",
    ], 17)

    s = new_slide(prs, P())
    add_kicker_title(s, "Software engineering", "Ship is a review, not a feature dump", 24)
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Quality bar: layers, errors/logs, tests, Postgres, README, no secrets.",
        "Homework after demo: none — portfolio README only.",
        "Stretch: Docker Compose api + postgres.",
    ], 18)

    s = new_slide(prs, P())
    add_kicker_title(s, "Rubric", "Code review (weeks 8–16)")
    add_bullets(s, MX, 2.0, 12, 5.0, [
        "Builds and gofmt is clean",
        "Errors returned and logged; no panics on bad input",
        "No secrets in git · HTTP status codes match",
        "SQL uses parameters · Go naming · tests · PR what/why",
    ], 16)

    s = new_slide(prs, P())
    add_kicker_title(s, "Pass 1", "Errors and logging")
    add_code(s, MX, 2.05, 12, 2.8, """if err != nil {
  slog.Error("list students", "err", err)
  c.JSON(500, gin.H{"error": "internal error"})
  return
}""", 14)

    s = new_slide(prs, P())
    add_kicker_title(s, "Pass 2", "Refactor: naming, dead code, JSON shape", 22)
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Delete unused handlers / commented dumps.",
        'One JSON error shape: {"error":"..."} everywhere.',
        "Rename vague data / tmp / Handle.",
        "gofmt + go vet before you demo.",
    ], 17)

    s = new_slide(prs, P())
    add_kicker_title(s, "Go design", "Idioms first — SOLID only as a lens", 24)
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Small interfaces — accept what you need.",
        "Composition via embedding.",
        "Accept interfaces, return structs.",
        "Package clarity · a little copying beats a little dependency.",
    ], 17)

    s = new_slide(prs, P())
    add_kicker_title(s, "Example", "Accept interfaces, return structs")
    add_code(s, MX, 2.05, 12, 2.6, """type StudentStore interface {
  List(ctx context.Context) ([]models.Student, error)
}
func NewStudentHandler(store StudentStore) *StudentHandler""", 13)

    s = new_slide(prs, P())
    add_kicker_title(s, "Example", "Package clarity beats clever folders")
    add_code(s, MX, 2.05, 12, 2.8, """cmd/server
internal/handlers · repository · middleware
internal/models · config · database · utils""", 14)

    s = new_slide(prs, P())
    add_kicker_title(s, "Stretch", "Docker Compose: api + postgres")
    add_code(s, MX, 2.05, 12, 2.4, """services:
  db:  { image: postgres:16, ... }
  api: { build: ./backend, ports: ["8080:8080"] }""", 14)
    add_bullets(s, MX, 4.7, 12, 1.8, ["Optional. Demo can use local Postgres + go run."], 17)

    s = new_slide(prs, P())
    add_kicker_title(s, "Demo format", "8–10 minutes per student / team")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "1 min — what SMS is; your stack",
        "3–4 min — live register → login → CRUD",
        "2–3 min — code: route → middleware → handler → repo",
        "1–2 min — tests / CI / one design choice · 1 min v2",
    ], 16)

    s = new_slide(prs, P())
    add_kicker_title(s, "Milestone", "Demo + merged main + retrospective", 24)
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Working path: auth → protected students → Postgres.",
        "Merge (or ready-to-merge) PR into main.",
        "v2 ideas: pagination, OpenAPI, refresh tokens.",
    ], 18)

    s = new_slide(prs, P())
    add_textbox(s, MX, CONTENT_TOP, 3, 0.35, "LIVE DEMO", size=12, bold=True, color=LIVE)
    add_kicker_title(s, "Instructor model", "Show a 8-minute walkthrough once", top=CONTENT_TOP+0.28)
    add_code(s, MX, 2.2, 12, 2.0, """# health → register → login → Bearer list
# open middleware → repository
# go test ./...""", 14)

    s = new_slide(prs, P())
    add_textbox(s, MX, CONTENT_TOP, 3, 0.35, "LIVE DEMO", size=12, bold=True, color=LIVE)
    add_kicker_title(s, "Refactor win", "One inconsistent error → one shape", top=CONTENT_TOP+0.28)
    add_code(s, MX, 2.2, 12, 2.0, """Before: c.String(500, err.Error())
After:  c.JSON(500, gin.H{"error": "internal error"})
        + slog.Error(...)""", 13)

    s = new_slide(prs, P())
    add_textbox(s, MX, CONTENT_TOP, 3, 0.35, "LIVE LAB", size=12, bold=True, color=LIVE)
    add_kicker_title(s, "Self-review", "Score yourself on the 8-point rubric", top=CONTENT_TOP+0.28)
    add_code(s, MX, 2.2, 12, 1.6, """docs/week-16-day-01/starter/review-lab/checklist.md""", 14)

    s = new_slide(prs, P())
    add_kicker_title(s, "Pitfalls", "What sinks a final demo")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Demo depends on data that only exists on one laptop.",
        "Secrets in the README for convenience.",
        "Ten new features, zero layer walkthrough.",
        "Cannot explain a Copilot-written function.",
        "Overtime → cut the feature, keep the story.",
    ], 16)

    s = new_slide(prs, P())
    add_kicker_title(s, "Lab · rest of class", "Done when all of this is true")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Self-review checklist completed",
        "At least one refactor landed",
        "Demo script rehearsed once (timer on)",
        "Portfolio README draft exists",
    ], 17)

    s = new_slide(prs, P())
    add_kicker_title(s, "Portfolio", "README that a hiring manager can run", 24)
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "What it is · stack · how to run",
        "Env var names only · example curls",
        "Architecture one-liner · tests / CI",
        "What you’d do in v2 (3 bullets max)",
    ], 17)

    s = new_slide(prs, P())
    add_kicker_title(s, "Words to keep", "Say these correctly in the demo")
    add_card(s, MX, 2.1, 5.9, 1.8, "Layer", "Handler vs repository responsibility.")
    add_card(s, 7.0, 2.1, 5.7, 1.8, "Idiom", "Small interfaces; concrete returns.")
    add_card(s, MX, 4.1, 5.9, 1.8, "Retrospective", "Honest v2 — not apology.")
    add_card(s, 7.0, 4.1, 5.7, 1.8, "Portfolio", "Runnable README beats a novel.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Layout reminder", "Where week-16 materials live")
    add_code(s, MX, 2.05, 12, 2.8, """docs/week-16-day-01/starter/
  review-lab/checklist.md
  refactor-lab/ · demo-kit/
  docker-compose.yml""", 14)

    s = new_slide(prs, P())
    add_kicker_title(s, "Honest limits", "What this week is not")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Not Kubernetes, not microservices split.",
        "Not a second React course.",
        "Not grading SOLID letter-by-letter.",
        "Not requiring Compose to pass.",
    ], 17)

    s = new_slide(prs, P())
    add_kicker_title(s, "Safety", "Still true on demo day")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "No real JWT secrets or DB passwords in git.",
        "Never log passwords.",
        "Explain every line you show — AI policy.",
    ], 18)

    s = new_slide(prs, P())
    add_kicker_title(s, "Review bar", "Instructor signs off when")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Demo tells a clear request → DB story",
        "Rubric items mostly green",
        "main merged (or merge-ready) with README",
        "v2 retrospective spoken aloud",
    ], 17)

    s = new_slide(prs, P())
    add_kicker_title(s, "Grading reminder", "Final SMS (weeks 14–16) = 25%", 24)
    add_code(s, MX, 2.05, 12, 2.2, """Postgres + auth + README + oral walkthrough
Weekly PRs already banked the rest.
Professionalism: pairing + AI honesty.""", 14)

    s = new_slide(prs, P(), dark=True)
    add_textbox(s, MX, 2.8, 12, 1.2, "Questions", size=64, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    add_textbox(s, MX, 4.2, 12, 0.8, "Then: self-review → refactor → rehearse → demo.", size=20, color=RGBColor(0xE7, 0xDD, 0xD0), align=PP_ALIGN.CENTER)
    add_notes(s, "Start the timer culture immediately.")

    if page != TOTAL:
        raise SystemExit(f"expected {TOTAL} slides, built {page}")
    prs.save(str(dest))
    print("Wrote", dest)
    return dest


if __name__ == "__main__":
    build()
