import re

# ========== REGEX DEFINITIONS ==========

EMAIL_RE = re.compile(
    r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
)

PHONE_RE = re.compile(r'''(?x)
    (?<!\w)
    (?:\+?\d{1,3}[\s\-\.]?)?
    (?:\(?\d{2,4}\)?[\s\-\.]?)?
    (?:\d[\s\-\.]?){7,12}
    (?!\w)
''')

DATE_RE = re.compile(
    r'\b\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4}\b|'
    r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2},?\s+\d{4}\b|'
    r'\b\d{4}-\d{2}-\d{2}\b|'
    r'\b\d{1,2}/\d{1,2}/\d{4}\b',
    re.IGNORECASE
)

ADDRESS_RE = re.compile(
    r'\b\d+[A-Z]?\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\s+'
    r'(?:Street|St|Road|Rd|Avenue|Ave|Boulevard|Blvd|Lane|Ln|Drive|Dr|Court|Ct|Parkway|Pkwy|Way)\b'
    r'(?:\s*,\s*[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)*'
)

# ========== HELPERS ==========

def get_line_col(text, index):
    lines = text[:index].split('\n')
    line_num = len(lines)
    col = len(lines[-1]) + 1
    return line_num, col


def find_pattern(pattern, text):
    results = []
    for m in pattern.finditer(text):
        match_text = m.group()
        line, col = get_line_col(text, m.start())
        results.append((match_text, line, col, col + len(match_text)))
    return results
