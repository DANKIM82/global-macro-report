"""Copy the current index.html into archive/<AS OF date>.html and rebuild archive/index.html."""
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARCH = ROOT / "archive"


def as_of(path: Path) -> str:
    m = re.search(r"AS OF (\d{4}-\d{2}-\d{2})", path.read_text(encoding="utf-8"))
    if not m:
        raise SystemExit(f"AS OF date not found in {path}")
    return m.group(1)


def rebuild_index() -> None:
    files = sorted((p for p in ARCH.glob("????-??-??.html")), reverse=True)
    rows = "\n".join(f'<li><a href="{p.name}">{p.stem}</a></li>' for p in files)
    html = f"""<!DOCTYPE html>
<html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Archive - Global Macro Intelligence Report</title>
<style>body{{font-family:system-ui,sans-serif;background:#0b0f14;color:#d6dde6;max-width:640px;margin:40px auto;padding:0 16px}}
a{{color:#7fb3ff}}li{{margin:6px 0;font-variant-numeric:tabular-nums}}</style></head>
<body><h1>Archive</h1><p><a href="../">최신판</a></p><ul>
{rows}
</ul></body></html>
"""
    (ARCH / "index.html").write_text(html, encoding="utf-8")


if __name__ == "__main__":
    ARCH.mkdir(exist_ok=True)
    d = as_of(ROOT / "index.html")
    shutil.copyfile(ROOT / "index.html", ARCH / f"{d}.html")
    rebuild_index()
    print(f"archived {d}")
