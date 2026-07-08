#!/usr/bin/env python3
"""Check public documents for likely personal or sensitive information."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

SENSITIVE_NAMES = [
    # Add names that must never appear in public documents.
    # Example: "홍길동",
]

PATTERNS = {
    "resident_registration_number": re.compile(r"\b\d{6}-[1-4]\d{6}\b"),
    "phone_number": re.compile(r"\b01[016789]-?\d{3,4}-?\d{4}\b|\b0\d{1,2}-\d{3,4}-\d{4}\b"),
    "email": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    "case_number": re.compile(r"\b\d{4}[- ]?(?:행심|구합|두|고단|고약|초기|초재|초심)[- ]?\d+\b"),
    "receipt_number": re.compile(r"(?:접수번호|사건번호|문서번호|관리번호)\s*[:：]?\s*[\w가-힣-]{4,}"),
    "address_keyword": re.compile(r"(?:서울|부산|대구|인천|광주|대전|울산|세종|경기|강원|충북|충남|전북|전남|경북|경남|제주).{0,30}(?:시|군|구|동|읍|면|로|길)\b"),
}

TEXT_EXTENSIONS = {".md", ".txt", ".py", ".yml", ".yaml", ".json", ".toml"}


def iter_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_file() and path.suffix.lower() in TEXT_EXTENSIONS:
            files.append(path)
        elif path.is_dir():
            files.extend(
                child
                for child in path.rglob("*")
                if child.is_file() and child.suffix.lower() in TEXT_EXTENSIONS
            )
    return sorted(files)


def scan_file(path: Path) -> list[tuple[str, int, str]]:
    findings: list[tuple[str, int, str]] = []
    text = path.read_text(encoding="utf-8", errors="replace")

    for line_number, line in enumerate(text.splitlines(), start=1):
        for name in SENSITIVE_NAMES:
            if name and name in line:
                findings.append(("configured_name", line_number, line.strip()))

        for label, pattern in PATTERNS.items():
            if pattern.search(line):
                findings.append((label, line_number, line.strip()))

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Find likely private information before publishing.")
    parser.add_argument("paths", nargs="+", type=Path, help="Files or directories to scan")
    args = parser.parse_args()

    findings_found = False
    for file_path in iter_files(args.paths):
        findings = scan_file(file_path)
        if not findings:
            continue

        findings_found = True
        print(f"\n{file_path}")
        for label, line_number, line in findings:
            print(f"  line {line_number}: {label}: {line}")

    if findings_found:
        print("\nPotential sensitive information found. Review before publishing.")
        return 1

    print("No obvious sensitive information patterns found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
