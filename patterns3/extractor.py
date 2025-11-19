import re
from .patterns import (
    EMAIL_RE,
    PHONE_RE,
    DATE_RE,
    ADDRESS_RE,
    find_pattern,
    get_line_col
)

def find_emails(text):
    return find_pattern(EMAIL_RE, text)


def find_phones(text):
    results = []
    for m in PHONE_RE.finditer(text):
        raw = m.group().strip()

        # filters (avoid false positives)
        if re.match(r'\d{4}-\d{2}-\d{2}', raw): 
            continue
        if re.match(r'\d{1,2}/\d{1,2}/\d{4}', raw):
            continue
        if re.match(r'\d{1,2}\s+[A-Za-z]{3,}\s+\d{4}', raw):
            continue

        line, col = get_line_col(text, m.start())
        results.append((raw, line, col, col + len(raw)))

    return results


def find_dates(text):
    return find_pattern(DATE_RE, text)


def find_addresses(text):
    return find_pattern(ADDRESS_RE, text)
