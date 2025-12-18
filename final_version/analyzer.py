import re
from .extractors import EMAIL_PATTERN, PHONE_PATTERN, DATE_PATTERN


def analyze_matches(text, emails, phones, dates):
    results = []

    allowed = {
        "email": set(emails),
        "phone": set(phones),
        "date":  set(dates),
    }

    patterns = {
        "email": EMAIL_PATTERN,
        "phone": PHONE_PATTERN,
        "date":  DATE_PATTERN,
    }

    BULLETS = {"-", "•", "*", "–", "—"}

    lines = text.splitlines()
    logical_line = 0

    for line in lines:
        if not line.strip():
            continue

        logical_line += 1

        raw_words = line.split()
        words = [w for w in raw_words if w not in BULLETS]

        for typ, pattern in patterns.items():
            for match in re.finditer(pattern, line, re.IGNORECASE):
                value = match.group()

                if value not in allowed[typ]:
                    continue

                char_pos = match.start()
                word_number = 1
                current_index = 0

                for i, word in enumerate(words, start=1):
                    word_start = line.find(word, current_index)
                    word_end = word_start + len(word)

                    if word_start <= char_pos < word_end:
                        word_number = i
                        break

                    current_index = word_end

                results.append({
                    "type": typ,
                    "word": value,
                    "line": logical_line,
                    "col": match.start() + 1,
                    "word_number": word_number
                })

    results.sort(key=lambda r: (r["line"], r["col"]))
    return results
