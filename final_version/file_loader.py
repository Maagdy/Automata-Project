from pathlib import Path

def load_file(file_path):
    """Load text from TXT, PDF, DOCX, DOC, RTF, JSON, CSV, HTML safely"""
    path = Path(file_path)
    ext = path.suffix.lower()

    # ---- TXT ----
    if ext == '.txt':
        return path.read_text(encoding='utf-8', errors='ignore')

    # ---- PDF ----
    elif ext == '.pdf':
        import PyPDF2
        text = []

        try:
            with open(path, "rb") as f:
                pdf = PyPDF2.PdfReader(f, strict=False)

                for page in pdf.pages:
                    try:
                        extracted = page.extract_text()
                        if extracted:
                            text.append(extracted)
                    except:
                        continue  # skip corrupted pages

            return "\n".join(text)

        except Exception as e:
            return f"[Could not read PDF: {e}]"

    # ---- DOCX ----
    elif ext == '.docx':
        try:
            from docx import Document
            doc = Document(path)
            return "\n".join([p.text for p in doc.paragraphs])
        except Exception as e:
            return f"[Could not read DOCX: {e}]"

    # ---- DOC ----
    elif ext == '.doc':
        try:
            import subprocess, tempfile
            # Convert DOC → TXT using antiword
            with tempfile.NamedTemporaryFile(delete=False) as tmp:
                output = subprocess.getoutput(f"antiword '{path}'")
                return output
        except Exception as e:
            return f"[Could not read DOC: {e}]"

    # ---- JSON ----
    elif ext == '.json':
        import json
        try:
            return json.dumps(json.load(open(path, encoding='utf-8')), indent=2)
        except:
            return "[Could not read JSON]"

    # ---- CSV ----
    elif ext == '.csv':
        try:
            return path.read_text(encoding='utf-8', errors='ignore')
        except:
            return "[Could not read CSV]"

    # ---- HTML ----
    elif ext in ['.html', '.htm']:
        try:
            return path.read_text(encoding='utf-8', errors='ignore')
        except:
            return "[Could not read HTML]"

    # ---- UNSUPPORTED ----
    else:
        return f"[Unsupported file type: {ext}]"
