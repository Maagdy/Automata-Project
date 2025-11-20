# from data_utils_functions import load_employee_data, preprocess_data
# from patterns.pattern1_salary_distribution import analyze_salary_distribution
# from patterns.pattern2_dept_salary import analyze_department_salary_pattern
# from patterns.pattern3_job_role import analyze_job_role_pattern
# from patterns.pattern4_salary_correlation import analyze_tenure_salary_correlation
# from patterns.pattern5_top_performers import analyze_top_performers_pattern
# from patterns.pattern6_analyze_commission import analyze_commission_pattern
# from patterns.pattern7_hiring_trend import analyze_hiring_trend_pattern
# from patterns.pattern8_management_hierarchy import analyze_management_hierarchy_pattern
# from patterns2.extract_employees_by_role import extract_employees_by_role
# from pathlib import Path
# import pandas as pd

# input_file = Path("data/employees_plain_txt.txt")
# job_roles = [
#     "Web Developer",
#     "Mobile Developer",
#     "Data Analyst",
#     "Machine Learning Engineer",
#     "Project Manager",
# ]

# def main():
#     # df = preprocess_data(load_employee_data())
#     # analyze_salary_distribution(df)
#     # analyze_department_salary_pattern(df)
#     # analyze_job_role_pattern(df)
#     # analyze_tenure_salary_correlation(df)
#     # analyze_top_performers_pattern(df)
#     # analyze_commission_pattern(df)
#     # analyze_hiring_trend_pattern(df)
#     # analyze_management_hierarchy_pattern(df)
#     for job in job_roles:
#         extract_employees_by_role(
#             input_path=input_file,
#             job_title=job,
#             output_dir="data/results"
#         )
#         print(f"✅ {job} extraction complete.")

# if __name__ == "__main__":
#     main()# main.py# main.py
from final_version.file_loader import load_file
from final_version.extractors import extract_emails, extract_phones, extract_dates
from final_version.analyzer import analyze_matches
from final_version.writes import write_analysis, write_masked


def main():
    # file_path = "data/test.txt"  
    # file_path = "data/random_data.txt"  
    file_path = "data/employees_plain_txt.txt"  
    # file_path = "final_version/dataset/DOCX_data.docx"        
    # file_path = "final_version/dataset/PDF_data.pdf"        
    # file_path = "final_version/dataset/TXT_data.txt"        

    try:
        # This automatically handles TXT, PDF, and DOCX using its extension
        text = load_file(file_path)
        print("✓ File loaded successfully")

        # Extract data
        emails = extract_emails(text)
        phones = extract_phones(text)
        dates = extract_dates(text)

        print("\nFound:")
        print(f"  - {len(emails)} emails")
        print(f"  - {len(phones)} phones")
        print(f"  - {len(dates)} dates")

        # Analyze positions
        results = analyze_matches(text, emails, phones, dates)

        # Write result files
        write_analysis(results)       # analysis_output.txt
        write_masked(text, phones)    # masked_output.txt

        print("\n✓ All done!")

    except Exception as e:
        print(f"✗ Error: {e}")


if __name__ == "__main__":
    main()
