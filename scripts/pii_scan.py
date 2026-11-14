"""Personal-data scanner shared by air-staging and the public air repository.

Usage:
    python scripts/pii_scan.py PATH [PATH ...]

Exit code 1 if any BLOCK finding is present; WARN findings are reported only.
Findings report the kind of data and its location, never the matched text.
Lines containing an entry from a .pii-allow file in the working directory are skipped.
"""
import re
import sys
from pathlib import Path

# Verhoeff tables for Aadhaar check digits.
_D = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 0, 6, 7, 8, 9, 5],
    [2, 3, 4, 0, 1, 7, 8, 9, 5, 6], [3, 4, 0, 1, 2, 8, 9, 5, 6, 7],
    [4, 0, 1, 2, 3, 9, 5, 6, 7, 8], [5, 9, 8, 7, 6, 0, 4, 3, 2, 1],
    [6, 5, 9, 8, 7, 1, 0, 4, 3, 2], [7, 6, 5, 9, 8, 2, 1, 0, 4, 3],
    [8, 7, 6, 5, 9, 3, 2, 1, 0, 4], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
]
_P = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 5, 7, 6, 2, 8, 3, 0, 9, 4],
    [5, 8, 0, 3, 7, 9, 6, 1, 4, 2], [8, 9, 1, 6, 0, 4, 3, 5, 2, 7],
    [9, 4, 5, 3, 1, 2, 6, 8, 7, 0], [4, 2, 8, 6, 5, 7, 3, 9, 0, 1],
    [2, 7, 9, 3, 8, 0, 6, 4, 1, 5], [7, 0, 4, 6, 9, 1, 3, 2, 5, 8],
]


def verhoeff_ok(number: str) -> bool:
    c = 0
    for i, ch in enumerate(reversed(number)):
        c = _D[c][_P[i % 8][int(ch)]]
    return c == 0


def luhn_ok(number: str) -> bool:
    total, alt = 0, False
    for ch in reversed(number):
        d = int(ch)
        if alt:
            d = d * 2 - 9 if d > 4 else d * 2
        total += d
        alt = not alt
    return total % 10 == 0


def _digits(s: str) -> str:
    return re.sub(r"\D", "", s)


# (label, level, regex, optional validator on the matched text)
RULES = [
    ("Aadhaar number", "BLOCK", re.compile(r"\b[2-9]\d{3}[ -]?\d{4}[ -]?\d{4}\b"),
     lambda m: verhoeff_ok(_digits(m))),
    ("PAN", "BLOCK", re.compile(r"\b[A-Z]{3}[ABCFGHLJPT][A-Z]\d{4}[A-Z]\b"), None),
    ("Payment card number", "BLOCK", re.compile(r"\b(?:\d[ -]?){12,18}\d\b"),
     lambda m: 13 <= len(_digits(m)) <= 19 and luhn_ok(_digits(m))),
    ("IFSC code", "BLOCK", re.compile(r"\b[A-Z]{4}0[A-Z0-9]{6}\b"), None),
    ("Bank account number", "BLOCK",
     re.compile(r"(?i)\b(?:a/?c|account)\s*(?:no\.?|number)?\s*[:#-]?\s*\d{9,18}\b"), None),
    ("Indian phone number", "BLOCK",
     re.compile(r"(?<![\d.])(?:\+91[ -]?|0)?[6-9]\d{4}[ -]?\d{5}(?!\d|\.\d)"), None),
    ("Email address", "BLOCK", re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b"), None),
    ("Vehicle registration", "BLOCK",
     re.compile(r"\b[A-Z]{2}[ -]?\d{1,2}[ -]?[A-Z]{1,3}[ -]?\d{4}\b"), None),
    ("Flat or unit number", "WARN",
     re.compile(r"(?i)\b(?:flat|apt\.?|apartment|unit|room)\s*(?:no\.?)?\s*[A-Z]?-?\d{2,5}\b"
                r"|\b[A-F]-\d{3,4}\b"), None),
    ("Personal name after a title", "WARN",
     re.compile(r"\b(?:Mr|Mrs|Ms|Dr|Shri|Smt|Kum)\.?\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?"), None),
    ("PIN code", "WARN", re.compile(r"(?i)\b(?:pin|pincode|pin code)\s*[:-]?\s*\d{6}\b"), None),
]

# Lines containing these are skipped: official identifiers that look like personal data.
ALLOW = [
    re.compile(r"\bP5\d{10}\b"),           # MahaRERA project registration
    re.compile(r"\bCC/\d{4}/\d{2}\b"),      # PMC commencement certificate
    re.compile(r"\bG\.S\.R\.\s*\d+"),       # Gazette notification
    re.compile(r"noreply\.github\.com"),    # GitHub no-reply addresses in credits
]


def _load_allow_file():
    """Literal strings listed in .pii-allow (one per line) mark lines as allowed.

    Use it for published contact details the project chose to show, such as the
    project's own email address. Keep it short and review every entry.
    """
    path = Path(".pii-allow")
    if not path.exists():
        return []
    return [ln.strip() for ln in path.read_text(encoding="utf-8").splitlines()
            if ln.strip() and not ln.startswith("#")]


ALLOW_LITERALS = _load_allow_file()


def scan_text(text: str):
    findings = []
    for lineno, line in enumerate(text.splitlines(), 1):
        if any(a.search(line) for a in ALLOW) or any(s in line for s in ALLOW_LITERALS):
            continue
        for label, level, rx, check in RULES:
            for m in rx.finditer(line):
                if check is None or check(m.group(0)):
                    findings.append((level, label, lineno))
    return findings


def scan_paths(paths):
    results = {}
    for p in paths:
        p = Path(p)
        if not p.exists():
            continue
        files = [p] if p.is_file() else sorted(x for x in p.rglob("*") if x.is_file())
        for f in files:
            try:
                text = f.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                continue
            found = scan_text(text)
            if found:
                results[str(f)] = found
    return results


def has_block(results) -> bool:
    return any(level == "BLOCK" for items in results.values() for level, _, _ in items)


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    results = scan_paths(argv[1:])
    for f, items in results.items():
        for level, label, lineno in items:
            print(f"{level}: {label} in {f}, line {lineno}")
    if not results:
        print("No personal data patterns found.")
    return 1 if has_block(results) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
