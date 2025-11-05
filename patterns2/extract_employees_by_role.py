import re
import pandas as pd
from pathlib import Path


def extract_employees_by_role(input_path, job_title, output_dir="results"):
    """
    Extracts employees with a specific job title from a plain text file
    and safely overwrites any existing Excel file for that role.

    ✅ Always overwrites old files safely
    ✅ Automatically creates the output directory
    ✅ Handles errors gracefully

    Parameters
    ----------
    input_path : str or Path
        Full path to the input plain text file.
    job_title : str
        The job title to search for (e.g., "Web Developer", "Mobile Developer").
    output_dir : str or Path, optional
        Folder where the Excel file will be saved (default: "results").

    Returns
    -------
    pd.DataFrame
        A DataFrame containing all extracted employees with the given job title.
    """

    input_path = Path(input_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # ✅ Always use static (non-timestamped) filenames
    safe_title = job_title.lower().replace(" ", "_")
    output_file = output_dir / f"{safe_title}.xlsx"

    # 🧹 Always try to safely remove old file first
    if output_file.exists():
        try:
            output_file.unlink()
            print(f"🗑️ Old file removed: {output_file}")
        except Exception as e:
            print(f"⚠️ Warning: Could not delete old file ({output_file}): {e}")

    # 🔍 Regex patterns
    job_pattern = re.compile(rf"\b{re.escape(job_title)}\b", re.IGNORECASE)
    email_pattern = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
    phone_pattern = re.compile(r"(?:\+?\d[\d\s().-]{7,}\d)")

    employees = []

    # 📖 Safely read file
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            for line in f:
                if job_pattern.search(line):
                    email_match = email_pattern.search(line)
                    phone_match = phone_pattern.search(line)

                    parts = line.split()
                    try:
                        emp_index = parts.index("Employee") + 2
                        name = f"{parts[emp_index]} {parts[emp_index + 1]}"
                    except Exception:
                        name = "Unknown"

                    employees.append({
                        "Employee Name": name,
                        "Email": email_match.group(0) if email_match else "N/A",
                        "Phone": phone_match.group(0) if phone_match else "N/A",
                        "Job Title": job_title
                    })
    except FileNotFoundError:
        print(f"❌ Error: Input file not found at {input_path}")
        return pd.DataFrame()
    except Exception as e:
        print(f"⚠️ Error while reading file: {e}")
        return pd.DataFrame()

    # 🧾 Convert to DataFrame and safely save
    df = pd.DataFrame(employees)
    try:
        df.to_excel(output_file, index=False)
        print(f"✅ File saved successfully: {output_file}")
    except Exception as e:
        print(f"❌ Failed to save Excel file: {e}")

    print(f"📊 Total '{job_title}' found: {len(df)}\n")
    return df
