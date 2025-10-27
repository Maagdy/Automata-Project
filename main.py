from data_utils_functions import load_employee_data, preprocess_data
from patterns.pattern1_salary_distribution import analyze_salary_distribution
from patterns.pattern2_dept_salary import analyze_department_salary_pattern
from patterns.pattern3_job_role import analyze_job_role_pattern
from patterns.pattern4_salary_correlation import analyze_tenure_salary_correlation
from patterns.pattern5_top_performers import analyze_top_performers_pattern
from patterns.pattern6_analyze_commission import analyze_commission_pattern
from patterns.pattern7_hiring_trend import analyze_hiring_trend_pattern
from patterns.pattern8_management_hierarchy import analyze_management_hierarchy_pattern

def main():
    df = preprocess_data(load_employee_data())
    analyze_salary_distribution(df)
    analyze_department_salary_pattern(df)
    analyze_job_role_pattern(df)
    analyze_tenure_salary_correlation(df)
    analyze_top_performers_pattern(df)
    analyze_commission_pattern(df)
    analyze_hiring_trend_pattern(df)
    analyze_management_hierarchy_pattern(df)

if __name__ == "__main__":
    main()
