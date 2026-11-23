"""Pre-push sanity checks for index.html. Exit non-zero on failure."""
import re
import sys
from pathlib import Path

html = (Path(__file__).resolve().parent.parent / "index.html").read_text(encoding="utf-8")
errors = []

if not re.search(r"AS OF \d{4}-\d{2}-\d{2}", html):
    errors.append("AS OF date missing")
if re.search(r'<(script|link|img)[^>]+(src|href)=["\']https?://', html, re.I):
    errors.append("external dependency found (script/link/img with http src)")
if re.search(r"@import\s+url\(['\"]?https?://", html, re.I):
    errors.append("external CSS @import found")
for sec in ["TRADE BLOTTER", "EXECUTIVE SUMMARY", "SCENARIO PROBABILITY MATRIX",
            "TIMELINE", "LIVE VERIFICATION CHECKLIST", "Disclaimer"]:
    if sec.lower() not in html.lower():
        errors.append(f"section missing: {sec}")
if len(html) < 20000:
    errors.append(f"file suspiciously small ({len(html)} bytes)")

if errors:
    print("CHECK FAILED:\n  " + "\n  ".join(errors))
    sys.exit(1)
print("check ok")
