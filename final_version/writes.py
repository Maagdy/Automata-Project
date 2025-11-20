import re


def write_analysis(results, output_file='results_report.txt'):
    """Write analysis results to file"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"{'Word':<40} {'Type':<10} {'Ln':<5} {'Col':<5}\n")
        f.write("="*70 + "\n")
        
        for result in results:
            f.write(f"{result['word']:<40} {result['type']:<10} {result['line']:<5} {result['col']:<5}\n")
    
    print(f"✓ Analysis saved to {output_file}")


def mask_phones(text, phones):
    """Mask last 6 digits of phone numbers with asterisks"""
    masked_text = text
    
    for phone in phones:
        # Get only digits
        digits = re.sub(r'\D', '', phone)
        
        if len(digits) >= 6:
            # Create masked version
            masked = phone
            # Replace last 6 digits with *
            for i in range(6):
                if len(digits) > i:
                    digit = digits[-(i+1)]
                    masked = masked[::-1].replace(digit, '*', 1)[::-1]
            
            masked_text = masked_text.replace(phone, masked)
    
    return masked_text


def write_masked(text, phones, output_file='masked_output.txt'):
    """Write masked version of text"""
    masked = mask_phones(text, phones)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(masked)
    
    print(f"✓ Masked text saved to {output_file}")

