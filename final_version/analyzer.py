import re
from .extractors import EMAIL_PATTERN, PHONE_PATTERN, DATE_PATTERN


def get_position(text, pattern, match_value):
    """Get line and column number for a match"""
    positions = []
    
    for match in re.finditer(pattern, text, re.IGNORECASE):
        if match.group() == match_value:
            start = match.start()
            
            # Calculate line and column
            lines = text[:start].split('\n')
            line_num = len(lines)
            col_num = len(lines[-1]) + 1
            
            positions.append({
                'word': match_value,
                'line': line_num,
                'col': col_num
            })
    
    return positions


def analyze_matches(text, emails, phones, dates):
    """Analyze all matches and get their positions"""
    results = []
    
    # Analyze emails
    for email in emails:
        positions = get_position(text, EMAIL_PATTERN, email)
        for pos in positions:
            results.append({
                'type': 'email',
                'word': pos['word'],
                'line': pos['line'],
                'col': pos['col']
            })
    
    # Analyze phones
    for phone in phones:
        positions = get_position(text, PHONE_PATTERN, phone)
        for pos in positions:
            results.append({
                'type': 'phone',
                'word': pos['word'],
                'line': pos['line'],
                'col': pos['col']
            })
    
    # Analyze dates
    for date in dates:
        positions = get_position(text, DATE_PATTERN, date)
        for pos in positions:
            results.append({
                'type': 'date',
                'word': pos['word'],
                'line': pos['line'],
                'col': pos['col']
            })
    
    return results

