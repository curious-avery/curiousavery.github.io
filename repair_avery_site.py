#!/usr/bin/env python3
"""Repair a downloaded GitHub Pages ZIP for curious-avery.github.io.

Usage:
  python repair_avery_site.py curious-avery.github.io-main.zip

Creates a ready-to-upload folder and ZIP while preserving the existing site,
images, content, styles, and JavaScript. No third-party packages are needed.
"""
import argparse
import re
import shutil
import tempfile
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

REPLACEMENTS = (
    ("assets/css/site.css", "site.css"),
    ("assets/js/site.js", "site.js"),
    ("assets/img/logos/", ""),
    ("assets/img/", ""),
)

def repair_html(file: Path) -> int:
    if not file.exists():
        raise FileNotFoundError(f"Missing required file: {file}")
    content = file.read_text(encoding="utf-8")
    changes = 0
    for old, new in REPLACEMENTS:
        changes += content.count(old)
        content = content.replace(old, new)
    file.write_text(content, encoding="utf-8")
    return changes

def find_missing_local_assets(file: Path, site: Path):
    html = file.read_text(encoding="utf-8")
    refs = re.findall(r"(?:src|href)=[\"']([^\"']+)[\"']", html)
    return sorted({r for r in refs if not (
        r.startswith(("#", "/", "mailto:", "tel:", "http://", "https://", "data:"))
    ) and not (site / r.split("#",1)[0].split("?",1)[0]).is_file()})

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repository_zip", type=Path, help="ZIP downloaded using GitHub's Code > Download ZIP")
    parser.add_argument("--output", type=Path, default=Path.cwd() / "avery-site-fixed")
    args = parser.parse_args()
    if not args.repository_zip.is_file():
        parser.error(f"Input ZIP not found: {args.repository_zip}")
    dest = args.output.resolve()
    if dest.exists():
        parser.error(f"Output directory already exists: {dest}")
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        with ZipFile(args.repository_zip, "r") as z:
            for member in z.infolist():
                p = Path(member.filename)
                if p.is_absolute() or ".." in p.parts:
                    raise ValueError(f"Unsafe ZIP entry: {member.filename}")
            z.extractall(tmp_path)
        sites = [p for p in tmp_path.rglob("index.html") if (p.parent / "site.css").is_file()]
        if len(sites) != 1:
            raise RuntimeError(f"Expected one website root with index.html and site.css, found {len(sites)}")
        root = sites[0].parent
        shutil.copytree(root, dest)
    index_changes = repair_html(dest / "index.html")
    error_changes = repair_html(dest / "404.html") if (dest / "404.html").exists() else 0
    readme = dest / "README.md"
    if readme.is_file():
        text = readme.read_text(encoding="utf-8")
        text = text.replace("curiousavery", "curious-avery")
        readme.write_text(text, encoding="utf-8")

    missing = []
    for page in ("index.html", "404.html"):
        if (dest / page).exists():
            missing.extend(f"{page}: {asset}" for asset in find_missing_local_assets(dest / page, dest))
    archive = dest.with_suffix(".zip")
    with ZipFile(archive, "w", compression=ZIP_DEFLATED) as z:
        for p in sorted(dest.rglob("*")):
            if p.is_file():
                z.write(p, p.relative_to(dest))
    print(f"Repaired index.html references: {index_changes}")
    print(f"Repaired 404.html references: {error_changes}")
    print(f"Missing local resources: {len(missing)}")
    for missing_asset in missing:
        print(f"  WARNING: {missing_asset}")
    print(f"Fixed website folder: {dest}")
    print(f"Ready-to-upload archive: {archive}")
    print("GitHub Pages: owner curious-avery, repository curious-avery.github.io, main / (root)")
    print("Extract the fixed ZIP and upload its contents to the repository root (not the ZIP).")
    if missing:
        raise SystemExit("Some linked assets are missing. Review the warnings above.")

if __name__ == "__main__":
    main()
