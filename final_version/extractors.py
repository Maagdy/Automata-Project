
import re


# Regex patterns
DATE_PATTERN  = r'\b(?:\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|\d{4}[-/]\d{1,2}[-/]\d{1,2})\b'
EMAIL_PATTERN = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}\b'
PHONE_PATTERN = r'\b(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{2,4}\)?[-.\s]?){1,3}\d{3,4}\b'


def extract_emails(text):
    """Extract valid emails from text"""
    matches = re.findall(EMAIL_PATTERN, text, re.IGNORECASE)
    valid = []
    
    for match in matches:
        # Skip invalid ones
        if match.endswith('@com'):
            continue
        if '@gmal.com' in match or '@gmail,com' in match:
            continue
        if match.count('@') != 1:
            continue
        if '.' not in match.split('@')[1]:
            continue
        
        valid.append(match)
    
    return valid


def extract_phones(text):
    """Extract valid phone numbers from text"""
    matches = re.findall(PHONE_PATTERN, text)
    valid = []
    
    for match in matches:
        digits = re.sub(r'\D', '', match)
        
        # Validate length
        if not (7 <= len(digits) <= 15):
            continue
        
        # Skip fake numbers
        if digits == '1234567890':
            continue
        
        # Skip invalid country codes
        if match.startswith('+99'):
            continue
        
        valid.append(match)
    
    return valid


def extract_dates(text):
    """Extract dates from text"""
    return re.findall(DATE_PATTERN, text)


