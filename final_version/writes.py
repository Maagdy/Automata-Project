import re


def write_analysis(results, output_file='results_report.txt'):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"{'Word':<40} {'Type':<10} {'Ln':<5} {'Col':<5} {'Word#':<6}\n")
        f.write("=" * 80 + "\n")

        for r in results:
            f.write(
                f"{r['word']:<40} {r['type']:<10} "
                f"{r['line']:<5} {r['col']:<5} {r['word_number']:<6}\n"
            )

    print(f"Analysis saved to {output_file}")

def mask_phones(text, phones):
    masked_text = text
    
    for phone in phones:
        digits = re.sub(r'\D', '', phone)
        
        if len(digits) >= 6:
            masked = phone
            for i in range(6):
                if len(digits) > i:
                    digit = digits[-(i+1)]
                    masked = masked[::-1].replace(digit, '*', 1)[::-1]
            
            masked_text = masked_text.replace(phone, masked)
    
    return masked_text


def write_masked(text, phones, output_file='masked_output.txt'):
    masked = mask_phones(text, phones)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(masked)
    
    print(f"Masked text saved to {output_file}")

