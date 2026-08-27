#!/usr/bin/env python3
"""Render Week 1 Day 1 teaching docs to PDF via headless Chrome."""

from __future__ import annotations

import shutil
import subprocess
import sys
import time
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[1]
SLIDES = REPO / "docs" / "slides"
PDF_DIR = ROOT / "pdf"
TMP = ROOT / ".pdf-html"
CHROME = "google-chrome"

MD_CSS = """
@page { size: A4; margin: 16mm; }
body {
  font-family: "Segoe UI", Calibri, Liberation Sans, sans-serif;
  color: #14202b;
  line-height: 1.45;
  max-width: 820px;
  margin: 0 auto;
  font-size: 12.5pt;
}
h1 { font-size: 22pt; color: #084f4b; margin: 0 0 8pt; }
h2 { font-size: 14pt; color: #0b6e68; margin: 18pt 0 8pt; }
h3 { font-size: 12.5pt; margin: 14pt 0 6pt; }
p, li { margin: 0 0 6pt; }
pre, code {
  font-family: Consolas, "Liberation Mono", monospace;
  font-size: 10pt;
}
pre {
  background: #10212c;
  color: #e8f2ef;
  padding: 10pt 12pt;
  border-radius: 8pt;
  white-space: pre-wrap;
}
code { background: #eef6f5; padding: 0 3pt; border-radius: 3pt; }
pre code { background: none; color: inherit; padding: 0; }
table { border-collapse: collapse; width: 100%; margin: 8pt 0 14pt; font-size: 11pt; }
th, td { border: 1px solid #d8cfc2; padding: 6pt 8pt; text-align: left; vertical-align: top; }
th { background: #eef6f5; }
hr { border: 0; border-top: 1px solid #d8cfc2; margin: 16pt 0; }
a { color: #0b6e68; }
blockquote { border-left: 4px solid #0b6e68; margin: 8pt 0; padding: 4pt 12pt; color: #4d5d6b; }
.kicker { font-size: 10pt; letter-spacing: .12em; text-transform: uppercase; color: #0b6e68; font-weight: 700; }
"""


def md_to_html(src: Path, title: str, kicker: str | None = None) -> Path:
    text = src.read_text(encoding="utf-8")
    body = markdown.markdown(
        text,
        extensions=["tables", "fenced_code", "nl2br"],
    )
    banner = kicker or "Epic Learn · Go Programming Master Course"
    html = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"/>
<title>{title}</title>
<style>{MD_CSS}</style>
</head><body>
<p class="kicker">{banner}</p>
{body}
</body></html>
"""
    TMP.mkdir(parents=True, exist_ok=True)
    out = TMP / (src.stem + ".html")
    out.write_text(html, encoding="utf-8")
    return out


def chrome_pdf(src_url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    profile = Path(f"/tmp/chrome-pdf-profile-{dest.stem}")
    shutil.rmtree(profile, ignore_errors=True)
    profile.mkdir(parents=True, exist_ok=True)
    cmd = [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        f"--user-data-dir={profile}",
        "--remote-debugging-port=0",
        "--no-pdf-header-footer",
        "--hide-scrollbars",
        f"--print-to-pdf={dest}",
        src_url,
    ]
    print("PDF", dest.name, flush=True)
    if dest.exists():
        dest.unlink()
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    deadline = time.time() + 45
    last_size = -1
    stable = 0
    while time.time() < deadline:
        if dest.exists():
            size = dest.stat().st_size
            if size >= 1000 and size == last_size:
                stable += 1
                if stable >= 3:
                    proc.kill()
                    proc.wait(timeout=5)
                    print(f"  {size // 1024} KB", flush=True)
                    return
            else:
                stable = 0
            last_size = size
        elif proc.poll() is not None:
            break
        time.sleep(0.25)
    proc.kill()
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.terminate()
    if dest.exists() and dest.stat().st_size >= 1000:
        print(f"  {dest.stat().st_size // 1024} KB", flush=True)
        return
    log = proc.communicate()[0]
    if log:
        sys.stderr.write(log.decode("utf-8", errors="replace"))
    raise SystemExit(f"chrome failed for {dest.name}")


def main() -> int:
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    jobs: list[tuple[str, Path]] = []

    jobs.append((SLIDES.joinpath("week-01-day-01.html").as_uri(), PDF_DIR / "week-01-day-01-slides.pdf"))
    jobs.append((ROOT.joinpath("student-handout.html").as_uri(), PDF_DIR / "student-handout.pdf"))
    jobs.append((ROOT.joinpath("lab-sheet.html").as_uri(), PDF_DIR / "lab-sheet.pdf"))

    md_jobs = [
        (SLIDES / "week-01-day-01-notes.md", "Presenter notes", "Epic Learn · Week 1, Day 1"),
        (ROOT / "pre-class.md", "Pre-class message", "Epic Learn · Week 1, Day 1"),
        (ROOT / "instructor-checklist.md", "Instructor checklist", "Epic Learn · Week 1, Day 1"),
        (ROOT / "install.md", "Install Go, Git, VS Code", "Epic Learn · Week 1, Day 1"),
        (ROOT / "troubleshooting.md", "Troubleshooting", "Epic Learn · Week 1, Day 1"),
        (ROOT / "homework.md", "Homework", "Epic Learn · Week 1, Day 1"),
        (ROOT / "why-go.template.md", "why-go.md template", "Epic Learn · Week 1, Day 1"),
        (ROOT / "README.md", "Day 1 kit index", "Epic Learn · Week 1, Day 1"),
        (REPO / "COURSE.md", "16-week curriculum", "Epic Learn · Go Programming Master Course"),
        (REPO / "docs" / "sms-project-spec.md", "SMS project spec", "Epic Learn · Go Programming Master Course"),
    ]
    for path, title, kicker in md_jobs:
        html_path = md_to_html(path, title, kicker)
        jobs.append((html_path.as_uri(), PDF_DIR / f"{path.stem}.pdf"))

    for url, dest in jobs:
        chrome_pdf(url, dest)

    print("Wrote", PDF_DIR)
    for p in sorted(PDF_DIR.glob("*.pdf")):
        print(f"  {p.name:40} {p.stat().st_size // 1024:5d} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
