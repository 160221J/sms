#!/usr/bin/env python3
"""Build an editable PowerPoint of the Week 15 Day 1 deck (native text, not screenshots)."""

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
OUT = ROOT / "pdf" / "week-15-day-01-slides.pptx"
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
        "WEEK 15  ·  DAY 1",
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
    add_textbox(s, MX, 2.55, 12, 1.0, "Week 15, Day 1", size=48, bold=True, color=WHITE)
    add_textbox(s, MX, 3.7, 11, 1.2, "Auth, frontend wiring, project completion — JWT, Bearer, CORS, React.", size=20, color=RGBColor(0xE7, 0xDD, 0xD0))
    add_textbox(s, MX, 5.3, 11, 0.9, "Umesh Indrajith · BSc Eng (Hons), University of Moratuwa\nSenior Software Engineer / Lecturer", size=16, color=RGBColor(0xD7, 0xCB, 0xB8))
    add_notes(s, "E2E: register → login → Bearer GET students.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Since last week", "Postgres holds students. Now who may call the API?", 22)
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "CRUD hits Postgres with $1 placeholders.",
        "Today: JWT, Bearer middleware, protect student routes.",
        "Wire the provided React app against their API.",
    ], 18)

    s = new_slide(prs, P())
    add_kicker_title(s, "Today", "If Day 1 of week 15 works, you can")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Issue and validate JWT (HS256).",
        "Protect student routes; leave register/login public.",
        "Enable CORS for http://localhost:5173.",
        "Login from React; debug 401 vs CORS vs VITE_API_URL.",
    ], 17)

    s = new_slide(prs, P())
    add_kicker_title(s, "Software engineering", "Application flow", 26)
    add_textbox(s, MX, 2.1, 12, 1.0, "Browser → Vite → Gin → JWT middleware → repository → Postgres", size=18, color=MUTED)
    add_bullets(s, MX, 3.4, 12, 3.0, [
        "Never log passwords. bcrypt hashes; JWT for the client session.",
        "Homework: README runbook + one real bug fix.",
    ], 18)

    s = new_slide(prs, P())
    add_kicker_title(s, "JWT", "HS256 as in internal/utils/jwt.go")
    add_code(s, MX, 2.05, 12, 2.8, """claims := jwt.MapClaims{
  "user_id": userID, "username": username,
  "exp": time.Now().Add(24*time.Hour).Unix(),
}
token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)""", 13)

    s = new_slide(prs, P())
    add_kicker_title(s, "Login", "Register / login stay public")
    add_code(s, MX, 2.05, 12, 2.0, """POST /api/register  → 201
POST /api/login     → { token, user }""", 15)

    s = new_slide(prs, P())
    add_kicker_title(s, "Middleware", "Bearer gate on student routes")
    add_code(s, MX, 2.05, 12, 2.4, """Authorization: Bearer <token>
protected.Use(middleware.AuthMiddleware())
protected.GET("/students", students.List)""", 14)
    add_bullets(s, MX, 4.7, 12, 1.8, ["Missing/invalid token → 401, not 500."], 18)

    s = new_slide(prs, P())
    add_kicker_title(s, "CORS", "Browser rules for localhost:5173")
    add_code(s, MX, 2.05, 12, 2.6, """cors.New(cors.Config{
  AllowOrigins: []string{"http://localhost:5173"},
  AllowHeaders: []string{"Origin","Content-Type","Authorization"},
})""", 13)

    s = new_slide(prs, P())
    add_kicker_title(s, "Frontend", "Provided React app (Vite)")
    add_code(s, MX, 2.05, 12, 2.2, """cd frontend
# VITE_API_URL=http://localhost:8080
npm install && npm run dev""", 15)

    s = new_slide(prs, P())
    add_kicker_title(s, "Debug", "401 · 404 · 500 · CORS · wrong URL")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "401 — missing/expired/invalid token",
        "404 — wrong path or id",
        "500 — server/DB bug (check slog)",
        "CORS — origin not allowed (browser only)",
        "VITE_API_URL — wrong host/port",
    ], 17)

    s = new_slide(prs, P())
    add_kicker_title(s, "SMS milestone", "Feature-complete backend + login UI", 24)
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Protected student CRUD matches the WIP shape.",
        "Frontend login works against their API.",
        "Stretch: flesh out Students.jsx.",
    ], 18)

    s = new_slide(prs, P())
    add_kicker_title(s, "Lab", "E2E: register → login → GET students")
    add_code(s, MX, 2.05, 12, 2.6, """POST /api/register
POST /api/login          # copy token
GET  /api/students       # Authorization: Bearer ...
# React: npm run dev → register → login""", 13)

    s = new_slide(prs, P())
    add_textbox(s, MX, CONTENT_TOP, 3, 0.35, "LIVE DEMO", size=12, bold=True, color=LIVE)
    add_kicker_title(s, "401 then 200", "Protect List live", top=CONTENT_TOP+0.28)
    add_code(s, MX, 2.2, 12, 1.8, """curl /api/students                 # 401
curl -H "Authorization: Bearer $T" /api/students""", 14)

    s = new_slide(prs, P())
    add_textbox(s, MX, CONTENT_TOP, 3, 0.35, "LIVE DEMO", size=12, bold=True, color=LIVE)
    add_kicker_title(s, "React login", "Token in localStorage → interceptor", top=CONTENT_TOP+0.28)
    add_code(s, MX, 2.2, 12, 1.8, """DevTools → localStorage → token
Network → Authorization: Bearer ...""", 14)

    s = new_slide(prs, P())
    add_textbox(s, MX, CONTENT_TOP, 3, 0.35, "LIVE DEMO", size=12, bold=True, color=LIVE)
    add_kicker_title(s, "CORS fail", "Remove origin → browser red; Postman green", top=CONTENT_TOP+0.28)
    add_bullets(s, MX, 2.5, 12, 3.0, ["Temporarily break AllowOrigins", "Reload React → CORS error", "Fix and reload"], 18)

    s = new_slide(prs, P())
    add_kicker_title(s, "Pitfalls", "Common week-15 bugs")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Bearer misspelled / missing space.",
        "JWT secret empty or different between runs.",
        "Student routes left public by mistake.",
        "VITE_API_URL trailing slash issues.",
        "Logging passwords in slog (never).",
    ], 17)

    s = new_slide(prs, P())
    add_kicker_title(s, "Lab · rest of class", "Done when all of this is true")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Register + login return a real JWT",
        "Student routes require Bearer (401 without)",
        "CORS allows Vite; React login path works",
        "Can explain 401 vs CORS vs wrong VITE_API_URL",
    ], 17)

    s = new_slide(prs, P())
    add_kicker_title(s, "Homework", "Runbook + one real bug fix")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "README: Postgres, backend, frontend commands.",
        "Document DB_*, JWT_SECRET, VITE_API_URL.",
        "Fix at least one lab bug; note it in the PR.",
    ], 18)

    s = new_slide(prs, P())
    add_kicker_title(s, "Next session", "Week 16 — review, Go design, demo", 24)
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Code review, refactor, short design pass.",
        "Final demo 8–10 minutes.",
        "Bring a working login → list path.",
    ], 18)

    s = new_slide(prs, P())
    add_kicker_title(s, "Words to keep", "Say these correctly next week")
    add_card(s, MX, 2.1, 5.9, 1.8, "JWT", "Signed claims; client stores token.")
    add_card(s, 7.0, 2.1, 5.7, 1.8, "Bearer", "Authorization header scheme.")
    add_card(s, MX, 4.1, 5.9, 1.8, "CORS", "Browser cross-origin permission.")
    add_card(s, 7.0, 4.1, 5.7, 1.8, "401", "Unauthenticated — fix token, not SQL.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Layout reminder", "Where lab code lives")
    add_code(s, MX, 2.05, 12, 3.0, """docs/week-15-day-01/starter/backend/
  internal/utils/jwt.go
  internal/middleware/auth_middleware.go
frontend/   # repo React app
  src/api/axios.js""", 13)

    s = new_slide(prs, P())
    add_kicker_title(s, "Honest limits", "What this week is not")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Not refresh tokens / OAuth providers.",
        "Not perfect Students UI (stub OK).",
        "Not Docker Compose (week 16 stretch).",
    ], 18)

    s = new_slide(prs, P())
    add_kicker_title(s, "Safety", "Still true")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Example secrets only in git.",
        "bcrypt hashes; never log raw passwords.",
        "gofmt; no binaries in git.",
    ], 18)

    s = new_slide(prs, P())
    add_kicker_title(s, "Review bar", "Instructor merges when")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Student routes protected; register/login public",
        "Login returns JWT; List works with Bearer",
        "CORS allows Vite; React login path works",
        "README runbook present",
    ], 17)

    s = new_slide(prs, P())
    add_kicker_title(s, "Status codes", "Quick map for the lab")
    add_code(s, MX, 2.05, 12, 2.8, """401  no/invalid Bearer
404  missing resource
500  server/DB failure — read logs
CORS browser-only failure (Postman OK)""", 15)

    s = new_slide(prs, P(), dark=True)
    add_textbox(s, MX, 3.0, 12, 1.2, "Questions", size=64, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    add_notes(s, "Then protect List → Postman E2E → React login.")

    if page != TOTAL:
        raise SystemExit(f"expected {TOTAL} slides, built {page}")
    prs.save(str(dest))
    print("Wrote", dest)
    return dest


if __name__ == "__main__":
    build()
