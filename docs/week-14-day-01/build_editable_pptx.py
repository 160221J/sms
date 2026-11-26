#!/usr/bin/env python3
"""Build an editable PowerPoint of the Week 14 Day 1 deck (native text, not screenshots)."""

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
OUT = ROOT / "pdf" / "week-14-day-01-slides.pptx"
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
        "WEEK 14  ·  DAY 1",
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
    add_textbox(s, MX, 2.55, 12, 1.0, "Week 14, Day 1", size=48, bold=True, color=WHITE)
    add_textbox(s, MX, 3.7, 11, 1.2, "PostgreSQL, SQL, CRUD, transactions, migrations — the map leaves memory.", size=20, color=RGBColor(0xE7, 0xDD, 0xD0))
    add_textbox(s, MX, 5.3, 11, 0.9, "Umesh Indrajith · BSc Eng (Hons), University of Moratuwa\nSenior Software Engineer / Lecturer", size=16, color=RGBColor(0xD7, 0xCB, 0xB8))
    add_notes(s, "Replace in-memory store with Postgres. Injection demo mandatory.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Since last week", "Green tests. Now persist for real.")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Table-driven tests, httptest, fakes, CI habit.",
        "In-memory map becomes optional/fake-only.",
        "context.Context on repos finally matters for DB calls.",
    ], 18)

    s = new_slide(prs, P())
    add_kicker_title(s, "Today", "If Day 1 of week 14 works, you can")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Explain relational tables vs an in-memory map.",
        "Run SELECT/INSERT/UPDATE/DELETE in psql.",
        "Connect with pgx; use only parameterized queries ($1).",
        "Apply a SQL migration; GET /api/students hits Postgres.",
    ], 17)

    s = new_slide(prs, P())
    add_kicker_title(s, "Software engineering", "The database is the source of truth", 24)
    add_textbox(s, MX, 2.1, 12, 1.0, "App restarts must not erase students. Never concatenate user input into SQL.", size=17, color=MUTED)
    add_bullets(s, MX, 3.3, 12, 3.2, [
        "Driver: pgx (internal/database).",
        "Homework: prefer users table + persist register.",
    ], 18)

    s = new_slide(prs, P())
    add_kicker_title(s, "Relational DB", "Tables, rows, keys")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Table ≈ typed collection; row ≈ one student/user.",
        "SERIAL ids; UNIQUE on email/username.",
        "Migration includes users + students.",
    ], 18)

    s = new_slide(prs, P())
    add_kicker_title(s, "SQL", "Four verbs you will live with")
    add_code(s, MX, 2.05, 12, 2.8, """SELECT id, first_name FROM students ORDER BY id;
INSERT INTO students (...) VALUES ($1, ...);
UPDATE students SET course = $1 WHERE id = $2;
DELETE FROM students WHERE id = $1;""", 14)

    s = new_slide(prs, P())
    add_kicker_title(s, "Install", "PostgreSQL on Ubuntu + psql")
    add_code(s, MX, 2.05, 12, 2.2, """sudo apt install postgresql postgresql-contrib
sudo -u postgres createdb sms
psql -U postgres -d sms""", 15)
    add_bullets(s, MX, 4.5, 12, 2.0, ["Or Docker Postgres on :5432 — match .env DB_*.",], 18)

    s = new_slide(prs, P())
    add_kicker_title(s, "Migrations", "Schema as SQL files — not a GUI click", 24)
    add_code(s, MX, 2.05, 12, 1.6, "psql -U postgres -d sms -f migrations/001_init.sql", 15)
    add_bullets(s, MX, 4.0, 12, 2.6, ["Versioned and reviewable.", "Starter: users + students tables."], 18)

    s = new_slide(prs, P())
    add_kicker_title(s, "pgx", "Pool in internal/database")
    add_code(s, MX, 2.05, 12, 2.2, """pool, err := pgxpool.New(ctx, dsn)
err = pool.Ping(ctx)
// Exec / Query / QueryRow with $1, $2""", 15)

    s = new_slide(prs, P())
    add_kicker_title(s, "Danger", "SQL injection — concat, then the fix", 24)
    add_code(s, MX, 2.05, 12, 2.6, """// BAD
q := "SELECT * FROM students WHERE email = '" + email + "'"
// GOOD
q := "SELECT * FROM students WHERE email = $1"
row := pool.QueryRow(ctx, q, email)""", 14)

    s = new_slide(prs, P())
    add_kicker_title(s, "Repository", "Replace the map with SQL")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "StudentRepository uses pgx + $n placeholders.",
        "Keep StudentStore interface — fake for unit tests.",
        "Pass c.Request.Context() into every query.",
    ], 18)

    s = new_slide(prs, P())
    add_kicker_title(s, "Transactions", "All succeed or all roll back")
    add_code(s, MX, 2.05, 12, 2.4, """tx, err := pool.Begin(ctx)
defer tx.Rollback(ctx)
// Exec A, Exec B
return tx.Commit(ctx)""", 15)

    s = new_slide(prs, P())
    add_kicker_title(s, "SMS milestone", "Postman hits Postgres")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "createdb sms → apply 001_init.sql",
        "Wire database.Connect in main",
        "POST /api/students inserts a row",
        "GET /api/students survives restart",
    ], 18)

    s = new_slide(prs, P())
    add_textbox(s, MX, CONTENT_TOP, 3, 0.35, "LIVE DEMO", size=12, bold=True, color=LIVE)
    add_kicker_title(s, "psql", "Create DB, apply migration, SELECT", top=CONTENT_TOP+0.28)
    add_code(s, MX, 2.2, 12, 2.2, """createdb sms
psql -d sms -f migrations/001_init.sql
psql -d sms -c '\\dt'""", 15)

    s = new_slide(prs, P())
    add_textbox(s, MX, CONTENT_TOP, 3, 0.35, "LIVE DEMO", size=12, bold=True, color=LIVE)
    add_kicker_title(s, "Injection", "Concat breaks · $1 holds", top=CONTENT_TOP+0.28)
    add_code(s, MX, 2.2, 12, 1.6, "cd starter/sql-lab && go test -v ./inject/", 15)

    s = new_slide(prs, P())
    add_textbox(s, MX, CONTENT_TOP, 3, 0.35, "LIVE DEMO", size=12, bold=True, color=LIVE)
    add_kicker_title(s, "API + DB", "Create → List survives restart", top=CONTENT_TOP+0.28)
    add_code(s, MX, 2.2, 12, 2.0, """go run ./cmd/server
curl -X POST .../api/students -d '{...}'
curl .../api/students""", 14)

    s = new_slide(prs, P())
    add_kicker_title(s, "Pitfalls", "Common week-14 bugs")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Wrong DB name / password in .env.",
        "Forgot migration → relation does not exist.",
        "String-concat SQL leftover in Create.",
        "NULL date_of_birth scan into time.Time.",
    ], 18)

    s = new_slide(prs, P())
    add_kicker_title(s, "Lab · rest of class", "Done when all of this is true")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Postgres up; sms DB exists",
        "Migration applied; injection understood",
        "Create + List via API hit Postgres",
        "Optional: transaction sketch / users persist",
    ], 17)

    s = new_slide(prs, P())
    add_kicker_title(s, "Homework", "Users in DB (preferred) or note the defer", 24)
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Prefer: persist /api/register into users table.",
        "Or document deferring users to week 15.",
        "PR: migration steps + parameterized queries only.",
    ], 18)

    s = new_slide(prs, P())
    add_kicker_title(s, "Next session", "Week 15 — Auth, frontend wiring", 24)
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "JWT + Bearer middleware; protect student routes.",
        "CORS + React app against their API.",
        "Bring a working Postgres-backed List/Create.",
    ], 18)

    s = new_slide(prs, P())
    add_kicker_title(s, "Words to keep", "Say these correctly next week")
    add_card(s, MX, 2.1, 5.9, 1.8, "Migration", "Versioned SQL that defines schema.")
    add_card(s, 7.0, 2.1, 5.7, 1.8, "Parameterized", "$1 placeholders — never concat input.")
    add_card(s, MX, 4.1, 5.9, 1.8, "pgx pool", "Shared connections to Postgres.")
    add_card(s, 7.0, 4.1, 5.7, 1.8, "Transaction", "Commit all or roll back all.")

    s = new_slide(prs, P())
    add_kicker_title(s, "Layout reminder", "Where lab code lives")
    add_code(s, MX, 2.05, 12, 3.0, """docs/week-14-day-01/starter/
  sql-lab/
  backend/
    migrations/001_init.sql
    internal/database/
    internal/repository/""", 14)

    s = new_slide(prs, P())
    add_kicker_title(s, "Honest limits", "What this week is not")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Not JWT / frontend wiring (week 15).",
        "Not ORMs — raw SQL with pgx.",
        "Not every isolation level or pool tuning.",
    ], 18)

    s = new_slide(prs, P())
    add_kicker_title(s, "Safety", "Still true")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "No real passwords in git — .env is local.",
        "Parameterized queries only after the injection demo.",
        "gofmt; no binaries in git.",
    ], 18)

    s = new_slide(prs, P())
    add_kicker_title(s, "Review bar", "Instructor merges when")
    add_bullets(s, MX, 2.15, 12, 4.5, [
        "Migration file present and documented",
        "Students CRUD uses pgx + $n placeholders",
        "List survives process restart",
        "No string-concat SQL in production paths",
    ], 17)

    s = new_slide(prs, P(), dark=True)
    add_textbox(s, MX, 3.0, 12, 1.2, "Questions", size=64, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    add_notes(s, "Then createdb → migrate → injection → API.")

    if page != TOTAL:
        raise SystemExit(f"expected {TOTAL} slides, built {page}")
    prs.save(str(dest))
    print("Wrote", dest)
    return dest


if __name__ == "__main__":
    build()
